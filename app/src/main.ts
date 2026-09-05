import { python } from "@codemirror/lang-python";
import { EditorState } from "@codemirror/state";
import { EditorView, keymap } from "@codemirror/view";
import { basicSetup } from "codemirror";
import { marked } from "marked";
import DOMPurify from "dompurify";
import catalog from "./catalog.json";
import { canCheck, evaluateWarmup, type Evidence } from "./run-state";
import * as persistence from "./storage";
import "./style.css";

const STARTER =
  'category = "reading"\nminutes = 25\nprint(f"{category}: {minutes} minutes")\n';
const pages = catalog as {
  id: string;
  path: string;
  title: string;
  unit: string;
  minutes: string;
  body: string;
}[];
const root = document.querySelector<HTMLDivElement>("#app")!;
const esc = (text: string) =>
  text.replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ]!,
  );
let saved: persistence.Saved = {
  version: 2,
  code: STARTER,
  quoteError: false,
  completed: [],
  notes: {},
  reviewed: {},
};
let edited = false;
let saveTimer: ReturnType<typeof setTimeout> | null = null;
let editor: EditorView | null = null;
let worker: Worker | null = null;
let ready = false;
let running = false;
let serial = 0;
let active = 0;
let timer: ReturnType<typeof setTimeout> | null = null;
let startupTimer: ReturnType<typeof setTimeout> | null = null;
let evidence: Evidence | null = null;
let runSource = "";
let current = "0.1";
let storageMessage = "Opening local storage…";
let loadEpoch = 0;
const el = (id: string) => document.getElementById(id)!;
const text = (id: string, value: string) => {
  const target = document.getElementById(id);
  if (target) target.textContent = value;
};
function download(name: string, value: string, type = "text/plain") {
  const url = URL.createObjectURL(new Blob([value], { type }));
  const a = document.createElement("a");
  a.href = url;
  a.download = name;
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
async function persist() {
  if (saveTimer) clearTimeout(saveTimer);
  const success = await persistence.save(saved);
  storageMessage = success
    ? "Saved on this device"
    : "Storage unavailable. Export your work before leaving.";
  text("save-state", storageMessage);
}
function queueSave() {
  edited = true;
  text("save-state", "Saving…");
  if (saveTimer) clearTimeout(saveTimer);
  saveTimer = setTimeout(() => void persist(), 300);
}
function shutdown() {
  ++loadEpoch;
  worker?.terminate();
  worker = null;
  ready = false;
  running = false;
  if (timer) clearTimeout(timer);
  if (startupTimer) clearTimeout(startupTimer);
}
function controls() {
  for (const name of ["run", "check", "stop"]) {
    const button = document.getElementById(name) as HTMLButtonElement | null;
    if (button)
      button.disabled =
        name === "stop"
          ? !running
          : name === "check"
            ? running || !ready || !canCheck(saved.code, evidence)
            : running || !ready;
  }
  text(
    "result-state",
    running
      ? "Running current source"
      : evidence
        ? evidence.source === saved.code
          ? "Result for this source"
          : "Code changed. Run again."
        : "No run yet",
  );
}
function runtimeState(label: string, status: string) {
  text("runtime", label);
  const target = document.getElementById("runtime");
  if (target) target.dataset.state = status;
}
function startPython() {
  shutdown();
  const epoch = loadEpoch;
  runtimeState("Loading Python", "loading");
  controls();
  worker = new Worker(new URL("./python.worker.ts", import.meta.url), {
    type: "module",
  });
  const failed = (message: string) => {
    if (epoch !== loadEpoch) return;
    shutdown();
    runtimeState("Python unavailable", "error");
    text(
      "feedback",
      `${message} Retry Python or use the downloadable local workspace. Your editor remains available.`,
    );
    controls();
  };
  startupTimer = setTimeout(
    () => failed("Python did not load within 30 seconds."),
    30000,
  );
  worker.addEventListener("error", () =>
    failed("The Python worker could not start."),
  );
  worker.addEventListener("messageerror", () =>
    failed("Python returned an unreadable response."),
  );
  worker.addEventListener("message", ({ data }) => {
    if (epoch !== loadEpoch) return;
    if (data.type === "ready") {
      if (startupTimer) clearTimeout(startupTimer);
      ready = true;
      runtimeState("Python ready", "ready");
      controls();
      return;
    }
    if (data.type === "startup-error") {
      failed("Runtime files could not be loaded.");
      return;
    }
    if (data.type !== "result" || data.id !== active) return;
    if (timer) clearTimeout(timer);
    running = false;
    evidence = { source: runSource, stdout: data.stdout, error: data.error };
    if (
      data.error &&
      /SyntaxError: unterminated string literal/.test(data.error)
    )
      saved.quoteError = true;
    const error = data.error as string | null;
    const concise = error ? error.split("\n").slice(-4).join("\n") : null;
    text(
      "output",
      concise ||
        [data.stdout, data.stderr].filter(Boolean).join("\n") ||
        "Finished without printed output.",
    );
    text("traceback", error || "");
    (el("error-detail") as HTMLDetailsElement).hidden = !error;
    if (error)
      text(
        "feedback",
        "Python could not finish this run. Inspect the marked source line, repair it, and run again.",
      );
    else {
      const prediction = (
        document.querySelector(
          'input[name="prediction"]:checked',
        ) as HTMLInputElement | null
      )?.value;
      if (runSource === STARTER)
        text(
          "feedback",
          prediction === "reading: 25 minutes"
            ? "Your prediction matches. The names contribute their values, not their spellings."
            : `You predicted ${prediction}. The run printed reading: 25 minutes. Braces insert each name's current value.`,
        );
      else
        text(
          "feedback",
          evidence.source === saved.code
            ? "Compare the result with your intended change. When ready, check this version."
            : "You edited during this run. Run the current version before checking.",
        );
    }
    text(
      "repair-status",
      saved.quoteError
        ? "Quote error observed"
        : "Quote error not yet observed",
    );
    controls();
    void persist();
  });
}
async function run() {
  if (!ready || running || !worker) return;
  const prediction = document.querySelector('input[name="prediction"]:checked');
  if (!prediction) {
    text(
      "feedback",
      "Choose a prediction first. A wrong prediction is useful too.",
    );
    (
      document.querySelector('input[name="prediction"]') as HTMLInputElement
    ).focus();
    return;
  }
  runSource = saved.code;
  evidence = null;
  active = ++serial;
  running = true;
  text("output", "Running…");
  text("feedback", "");
  controls();
  void persist();
  worker.postMessage({ type: "run", id: active, code: runSource });
  timer = setTimeout(
    () =>
      stop("Stopped after three seconds. Check whether your loop can finish."),
    3000,
  );
}
function stop(message = "Stopped by you. Your source is unchanged.") {
  evidence = { source: runSource, stdout: "", error: message };
  text("output", message);
  text("feedback", "Python is restarting. The last result stays visible.");
  startPython();
}
function warmup() {
  el("reading").innerHTML = `
    <div class="warmup-grid">
      <section class="task-panel" aria-labelledby="task-title">
        <p class="kicker">Start here · 10 to 15 minutes</p><h1 id="task-title">Your first Python run</h1>
        <p>Read three lines. Predict their result. Then make the program yours.</p>
        <div class="mobile-code" aria-label="Starter source preview"><pre>${esc(STARTER)}</pre><a href="#editor">Edit the program below</a></div>
        <fieldset><legend>What will the starter print?</legend>
        ${["reading: 25 minutes", "category: minutes", "no output"].map((x) => `<label class="choice"><input type="radio" name="prediction" value="${esc(x)}"> ${esc(x)}</label>`).join("")}</fieldset>
        <details open class="activity"><summary>1. Run and understand</summary><p><code>category</code> names text; <code>minutes</code> names a number. The braces insert their values. <code>print</code> displays the result.</p></details>
        <details class="activity"><summary>2. Change and repair</summary><p>Change the category to <code>walking</code> and minutes to <code>40</code>. Run. Remove the closing quote after walking, run the error, then restore it and run again.</p><p id="repair-status">${saved.quoteError ? "Quote error observed" : "Quote error not yet observed"}</p><label for="explanation">What did you repair, and why did it help?</label><textarea id="explanation" rows="3" placeholder="The missing quote…">${esc(saved.notes["0.1"] || "")}</textarea></details>
        <details class="activity"><summary>3. Verify and continue</summary><p>Required output: <code>walking: 40 minutes</code>. Check your current code after the repair and explanation. Your explanation is retained for reflection, not automatically graded.</p><a class="next-link" href="#0.2">Open your local workspace →</a></details>
        <a class="quiet-link" href="#first-run-reading">Read the complete explanation</a>
      </section>
      <section class="workspace" aria-label="Python workspace">
        <div class="panel-bar"><strong>main.py</strong><span id="runtime" role="status" data-state="loading">Loading Python</span></div>
        <div id="editor"></div>
        <div class="controls"><button id="run" class="primary" disabled>Run code</button><button id="stop" disabled>Stop</button><button id="check" disabled>Check this change</button></div>
        <div class="output-bar"><strong>Output</strong><span id="result-state">No run yet</span></div>
        <pre id="output" tabindex="0">Choose a prediction, then run. You can edit while Python loads.</pre>
        <details id="error-detail" hidden><summary>Full Python error</summary><pre id="traceback"></pre></details>
        <p id="feedback" role="status">Each run starts fresh, just like a Python file.</p>
        <details class="utilities"><summary>Reset, download and recovery</summary><div class="controls"><button id="reset">Restore starter</button><button id="download-code">Download main.py</button><button id="retry">Retry Python</button></div><p>Reset restores source only. Your historical progress and notes remain. If the runtime is unavailable, <a href="./downloads/learner-workspace.zip" download>download the workspace</a> and follow <a href="#0.2">local setup</a>.</p></details>
      </section>
    </div>`;
  editor = new EditorView({
    parent: el("editor"),
    state: EditorState.create({
      doc: saved.code,
      extensions: [
        basicSetup,
        python(),
        EditorView.lineWrapping,
        EditorView.contentAttributes.of({ "aria-label": "Python source code" }),
        keymap.of([
          {
            key: "Mod-Enter",
            run: () => {
              void run();
              return true;
            },
          },
        ]),
        EditorView.updateListener.of((update) => {
          if (update.docChanged) {
            saved.code = update.state.doc.toString();
            controls();
            queueSave();
          }
        }),
      ],
    }),
  });
  el("run").onclick = () => void run();
  el("stop").onclick = () => stop();
  el("retry").onclick = startPython;
  el("explanation").oninput = (event) => {
    saved.notes["0.1"] = (event.target as HTMLTextAreaElement).value;
    queueSave();
  };
  el("check").onclick = () => {
    const failure = evaluateWarmup(
      saved.code,
      evidence,
      saved.quoteError,
      saved.notes["0.1"] || "",
    );
    if (failure) {
      text("feedback", failure);
      if (!saved.notes["0.1"])
        (el("explanation").closest("details") as HTMLDetailsElement).open =
          true;
      return;
    }
    if (!saved.completed.includes("0.1")) saved.completed.push("0.1");
    text(
      "feedback",
      "Check passed for this source. Your first lesson is complete. Continue to your local workspace.",
    );
    updateProgress();
    void persist();
  };
  el("reset").onclick = () => {
    if (
      confirm(
        "Restore the three starter lines? Download your current source first if you want to keep it.",
      )
    ) {
      shutdown();
      evidence = null;
      editor!.dispatch({
        changes: { from: 0, to: editor!.state.doc.length, insert: STARTER },
      });
      text("output", "Starter restored. Choose a prediction and run.");
      startPython();
    }
  };
  el("download-code").onclick = () => download("main.py", saved.code);
  startPython();
}
function updateProgress() {
  const core = pages.filter((x) => /^\d+\.\d+$/.test(x.id));
  const done = core.filter((x) => saved.completed.includes(x.id)).length;
  text("progress", `${done} / ${core.length} milestones recorded`);
  document.querySelectorAll<HTMLAnchorElement>("[data-lesson]").forEach((a) => {
    a.dataset.done = String(saved.completed.includes(a.dataset.lesson!));
    a.setAttribute(
      "aria-current",
      a.dataset.lesson === current ? "page" : "false",
    );
  });
}
function render() {
  current = decodeURIComponent(location.hash.slice(1) || "0.1");
  const page = pages.find((x) => x.id === current);
  shutdown();
  editor?.destroy();
  editor = null;
  evidence = null;
  if (current === "0.1") warmup();
  else if (page) {
    const html = DOMPurify.sanitize(marked.parse(page.body) as string);
    el("reading").innerHTML = `<article class="prose">${html}</article>`;
    el("reading")
      .querySelectorAll<HTMLAnchorElement>("a[href]")
      .forEach((a) => {
        const href = a.getAttribute("href")!;
        if (href.endsWith(".md") && !href.startsWith("http")) {
          const resolved = new URL(
            href,
            `https://course.invalid/${page.path}`,
          ).pathname.slice(1);
          const destination = pages.find((x) => x.path === resolved);
          if (destination) a.href = `#${destination.id}`;
        }
      });
    if (/^\d+\.\d+$/.test(page.id)) {
      const index = pages.indexOf(page);
      const next = pages.slice(index + 1).find((x) => /^\d+\.\d+$/.test(x.id));
      const due = pages
        .filter(
          (x) =>
            /^\d+\.\d+$/.test(x.id) &&
            saved.completed.includes(x.id) &&
            x.id !== page.id &&
            !saved.reviewed[`${page.id}:${x.id}`],
        )
        .slice(-1)[0];
      el("reading").insertAdjacentHTML(
        "beforeend",
        `<section class="reflection"><h2>Record your evidence</h2><p>The checks run in your local project. This is your learning record, not an automatic certificate.</p><label for="lesson-note">What passed, what did you observe, and how would you explain it?</label><textarea id="lesson-note" rows="4">${esc(saved.notes[page.id] || "")}</textarea><label class="choice"><input id="evidence-confirm" type="checkbox"> I ran the required checks and completed the explanation and recovery or review activity.</label><button id="record" class="primary">Record this milestone</button><p id="record-feedback" role="status"></p>${due ? `<details><summary>Bring back an earlier idea: ${esc(due.title)}</summary><p>Without reopening the lesson, explain one rule, predict a new input, then run it locally to check your explanation.</p><label for="retrieval">Your prediction and observed result</label><textarea id="retrieval" rows="3"></textarea><button id="record-retrieval">Save retrieval observation</button><p id="retrieval-state" role="status"></p></details>` : ""}${next ? `<a class="next-link" href="#${next.id}">Next: ${esc(next.title)} →</a>` : ""}</section>`,
      );
      el("lesson-note").oninput = (e) => {
        saved.notes[page.id] = (e.target as HTMLTextAreaElement).value;
        queueSave();
      };
      el("record").onclick = () => {
        if (
          !(el("evidence-confirm") as HTMLInputElement).checked ||
          (saved.notes[page.id] || "").trim().length < 40
        ) {
          text(
            "record-feedback",
            "Confirm the activities and write at least one specific observation before recording.",
          );
          return;
        }
        if (!saved.completed.includes(page.id)) saved.completed.push(page.id);
        text(
          "record-feedback",
          "Milestone recorded on this device. Keep your local check results and files.",
        );
        updateProgress();
        void persist();
      };
      if (due)
        el("record-retrieval").onclick = () => {
          const value = (el("retrieval") as HTMLTextAreaElement).value.trim();
          if (value.length < 20) {
            text(
              "retrieval-state",
              "Add your prediction and what you observed.",
            );
            return;
          }
          saved.reviewed[`${page.id}:${due.id}`] = value;
          void persist();
          text("retrieval-state", "Retrieval observation saved.");
        };
    }
  } else
    el("reading").innerHTML =
      '<article class="prose"><h1>Page not found</h1><p>Choose a lesson from the course contents.</p><a href="#0.1">Start the course</a></article>';
  updateProgress();
  document.title = `${page?.title || "First Run"} · Modern Python`;
  (el("contents") as HTMLDetailsElement).open = false;
  window.scrollTo(0, 0);
  if (page && current !== "0.1") {
    const heading = el("reading").querySelector("h1");
    heading?.setAttribute("tabindex", "-1");
    heading?.focus({ preventScroll: true });
  }
}
root.innerHTML = `<header class="site-header"><a class="brand" href="#0.1"><span class="brand-mark">py</span><span>Modern Python<small>From first run to reviewed change</small></span></a><div class="header-actions"><span id="progress"></span><a class="download" href="./downloads/learner-workspace.zip" download>Get the workspace ↓</a></div></header><div class="course-shell"><aside><details id="contents"><summary>Course contents</summary><nav aria-label="Course contents"><label for="search">Find a lesson or reference</label><input id="search" type="search" placeholder="Functions, Git, setup…">${pages.map((p) => `<a data-lesson="${p.id}" href="#${p.id}">${/^\d+\.\d+$/.test(p.id) ? `<span>${esc(p.id)}</span>` : ""}${esc(p.title)}</a>`).join("")}<p id="search-state" role="status"></p></nav></details><div class="saved-tools"><p id="save-state" role="status">${storageMessage}</p><button id="export-progress">Export progress</button><label class="import-label">Import progress<input id="import-progress" type="file" accept="application/json"></label><p id="import-status" role="status"></p></div></aside><main id="lesson"><div id="reading"></div></main></div><footer><span>Modern Python · By Denis Ostapenko · Edition 1.0</span><a href="#about">About, sources and course limits</a><a href="./downloads/course-reading.zip" download>Offline lesson text</a></footer>`;
el("search").oninput = (e) => {
  const value = (e.target as HTMLInputElement).value.toLowerCase();
  let count = 0;
  document.querySelectorAll<HTMLAnchorElement>("[data-lesson]").forEach((a) => {
    a.hidden = !a.textContent!.toLowerCase().includes(value);
    if (!a.hidden) count++;
  });
  text("search-state", `${count} pages found`);
};
el("export-progress").onclick = () => {
  void persist();
  download(
    "modern-python-progress.json",
    JSON.stringify(saved, null, 2),
    "application/json",
  );
};
el("import-progress").onchange = async (e) => {
  const file = (e.target as HTMLInputElement).files?.[0];
  if (!file) return;
  try {
    if (file.size > 500000) throw new Error("File is too large");
    const incoming: unknown = JSON.parse(await file.text());
    if (!persistence.valid(incoming))
      throw new Error("Not a supported Modern Python progress file");
    if (!confirm("Replace the current draft and progress with this export?"))
      return;
    saved = incoming;
    edited = true;
    await persist();
    render();
    text(
      "import-status",
      "Progress restored. Run imported source before checking.",
    );
  } catch (error) {
    text("import-status", String(error));
  }
};
window.addEventListener("hashchange", render);
window.addEventListener("pagehide", () => {
  void persist();
  shutdown();
});
render();
void (async () => {
  await persistence.connect();
  const loaded = await persistence.read();
  if (loaded && !edited) {
    saved = loaded;
    render();
  }
  storageMessage = (await persistence.save(saved))
    ? "Saved on this device"
    : "Storage unavailable. Export your work before leaving.";
  text("save-state", storageMessage);
})();
