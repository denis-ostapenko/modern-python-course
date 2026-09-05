import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / "course/manifest.json").read_text(encoding="utf-8"))
    assert len(manifest) == 17
    assert len({page["id"] for page in manifest}) == len(manifest)
    failures = []
    examples = 0
    files = list((ROOT / "course").rglob("*.md"))
    for page in manifest:
        if not (ROOT / "course" / page["path"]).is_file():
            failures.append(f"Missing lesson: {page['path']}")
        if page.get("exercise"):
            for asset in ("answer.py", "solution.py", "cases.json", "README.md"):
                if not (ROOT / "learner-repo/exercises" / page["id"] / asset).is_file():
                    failures.append(f"Missing {page['id']} exercise {asset}")
            for phase in ("start", "complete"):
                if not (ROOT / f"learner-repo/checkpoints/lesson-{page['id']}-{phase}/main.py").is_file():
                    failures.append(f"Missing checkpoint {page['id']}-{phase}")
    for path in files:
        source = path.read_text(encoding="utf-8")
        if any(s in source for s in ("\u2013", "\u2014", "AUTHOR_PEN_NAME", "/Users/", "Status: lesson specification", "Status: optional lab specification")):
            failures.append(f"Editorial/private placeholder in {path.relative_to(ROOT)}")
        for href in re.findall(r'\]\(([^)]+)\)', source):
            if href.startswith(("https://", "http://", "#")):
                continue
            target = (path.parent / href.split("#")[0]).resolve()
            if not target.is_file():
                failures.append(f"Broken link: {path.relative_to(ROOT)} -> {href}")
        for code, expected in re.findall(r'```python\n(.*?)\n```\n\nExpected output:\n\n```text\n(.*?)\n```', source, re.S):
            try:
                result = subprocess.run([sys.executable, "-c", code], input="", capture_output=True, text=True, timeout=5, check=False)
                assert result.returncode == 0, result.stderr
                assert result.stdout.rstrip("\n") == expected, repr(result.stdout)
                examples += 1
            except (AssertionError, subprocess.TimeoutExpired) as error:
                failures.append(f"Example failed in {path.relative_to(ROOT)}: {error}")
    if failures:
        print("\n".join(failures))
        return 1
    print(f"PASS: {len(manifest)} milestones, {len(files)} reading pages, links and assets, {examples} exact-output examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
