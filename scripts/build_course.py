import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "app/public"


def main():
    manifest = json.loads((ROOT / "course/manifest.json").read_text(encoding="utf-8"))
    known = {item["path"] for item in manifest}
    other = []
    for path in sorted((ROOT / "course").rglob("*.md")):
        relative = path.relative_to(ROOT / "course").as_posix()
        if relative in known or relative == "index.md":
            continue
        title = path.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
        id = {"setup.md": "setup", "about.md": "about"}.get(relative, relative.removesuffix(".md").replace("/", "-"))
        other.append({"id": id, "path": relative, "title": title, "unit": "reference", "minutes": "At your pace"})
    # Expose the complete reading version of the interactive lesson.
    first = dict(manifest[0]); first["id"] = "first-run-reading"; first["unit"] = "reference"
    catalog = manifest + [first] + other
    for item in catalog:
        item["body"] = (ROOT / "course" / item["path"]).read_text(encoding="utf-8")
    (ROOT / "app/src/catalog.json").write_text(json.dumps(catalog, ensure_ascii=False) + "\n", encoding="utf-8")
    runtime = PUBLIC / "runtime"
    runtime.mkdir(parents=True, exist_ok=True)
    for name in ["pyodide.asm.mjs", "pyodide.asm.wasm", "python_stdlib.zip", "pyodide-lock.json"]:
        shutil.copy2(ROOT / "app/node_modules/pyodide" / name, runtime / name)
    downloads = PUBLIC / "downloads"
    downloads.mkdir(parents=True, exist_ok=True)
    excluded = {".venv", "__pycache__", ".git", ".pytest_cache", ".ruff_cache", "work", "evidence"}
    with zipfile.ZipFile(downloads / "learner-workspace.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted((ROOT / "learner-repo").rglob("*")):
            relative = path.relative_to(ROOT / "learner-repo")
            if path.is_file() and not any(part in excluded for part in relative.parts) and path.name != ".DS_Store":
                if relative.as_posix() == "README.md":
                    archive.writestr("learner-workspace/README.md", path.read_text(encoding="utf-8").replace("../course/index.md", "course/index.md"))
                else:
                    archive.write(path, "learner-workspace/" + relative.as_posix())
        for path in sorted((ROOT / "course").rglob("*.md")):
            archive.write(path, "learner-workspace/course/" + path.relative_to(ROOT / "course").as_posix())
    with zipfile.ZipFile(downloads / "course-reading.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted((ROOT / "course").rglob("*")):
            if path.is_file():
                archive.write(path, "course/" + path.relative_to(ROOT / "course").as_posix())
    print(f"Built {len(catalog)} pages, local Python runtime, and two download archives")


if __name__ == "__main__":
    main()
