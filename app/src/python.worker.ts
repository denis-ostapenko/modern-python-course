/// <reference lib="webworker" />
import { loadPyodide } from "pyodide";

const runtime = loadPyodide({
  indexURL: new URL("../runtime/", self.location.href).href,
});
runtime
  .then(() => self.postMessage({ type: "ready" }))
  .catch((error) =>
    self.postMessage({ type: "startup-error", error: String(error) }),
  );
self.addEventListener("message", async ({ data }) => {
  if (data.type !== "run") return;
  const stdout: string[] = [];
  const stderr: string[] = [];
  let size = 0;
  const capture = (target: string[], line: string) => {
    size += line.length;
    if (size > 32000)
      throw new Error(
        "Output limit reached (32,000 characters). Reduce the amount you print.",
      );
    target.push(line);
  };
  try {
    const py = await runtime;
    py.setStdout({ batched: (line) => capture(stdout, line) });
    py.setStderr({ batched: (line) => capture(stderr, line) });
    const scope = py.toPy({ __name__: "__main__" });
    try {
      const result = await py.runPythonAsync(data.code, {
        globals: scope,
        filename: "main.py",
      });
      if (result && typeof result.destroy === "function") result.destroy();
    } finally {
      scope.destroy();
    }
    self.postMessage({
      type: "result",
      id: data.id,
      stdout: stdout.join("\n"),
      stderr: stderr.join("\n"),
      error: null,
    });
  } catch (error) {
    self.postMessage({
      type: "result",
      id: data.id,
      stdout: stdout.join("\n"),
      stderr: stderr.join("\n"),
      error: String(error),
    });
  }
});
