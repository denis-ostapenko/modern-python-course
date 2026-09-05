import argparse
import ast
import json
import runpy
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def execute(folder, answer, case):
    source = answer.read_text(encoding="utf-8")
    if "inputs" in case:
        tree = ast.parse(source)
        found = set()
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1:
                target = node.targets[0]
                if isinstance(target, ast.Name) and target.id in case["inputs"]:
                    node.value = ast.parse(
                        repr(case["inputs"][target.id]), mode="eval"
                    ).body
                    found.add(target.id)
        if found != set(case["inputs"]):
            raise ValueError("Keep the named input assignments from the starter")
        source = ast.unparse(ast.fix_missing_locations(tree))
    script = folder / "candidate.py"
    script.write_text(source, encoding="utf-8")
    if "argv" in case or "inputs" in case:
        result = subprocess.run(
            [sys.executable, str(script), *case.get("argv", [])],
            cwd=folder,
            text=True,
            capture_output=True,
            timeout=3,
        )
        assert result.returncode == case.get("exit", 0), result.stderr[-1500:]
        if "output" in case:
            assert result.stdout.rstrip("\n") == case["output"], (
                f"Expected {case['output']!r}, observed {result.stdout!r}"
            )
        for stream in ("stdout", "stderr"):
            key = stream + "_contains"
            if key in case:
                assert case[key] in getattr(result, stream)
        return
    namespace = runpy.run_path(str(script))
    if "file" in case:
        data = folder / "books.json"
        if case["file"] is not None:
            data.write_text(case["file"], encoding="utf-8")
        try:
            value = namespace["load_books"](data)
        except ValueError:
            assert case.get("error") == "ValueError", "Unexpected ValueError"
        else:
            assert "error" not in case, "Expected ValueError"
            assert value == case["result"], (
                f"Expected {case['result']!r}, observed {value!r}"
            )
        if case["file"] is not None:
            assert data.read_text(encoding="utf-8") == case["file"], (
                "Do not modify input files"
            )
    else:
        value = namespace[case["function"]](*case["args"])
        assert value == case["result"], (
            f"Expected {case['result']!r}, observed {value!r}"
        )
        assert set(p.name for p in folder.iterdir()) <= {"candidate.py"}, (
            "Calculation created an unexpected file"
        )


def main():
    parser = argparse.ArgumentParser(description="Check a course exercise")
    parser.add_argument(
        "lesson",
        choices=sorted(p.name for p in (ROOT / "exercises").iterdir() if p.is_dir()),
    )
    parser.add_argument("--extended", action="store_true")
    parser.add_argument(
        "--solution",
        action="store_true",
        help="Instructor verification of the supplied solution",
    )
    parser.add_argument("--case", type=int, help=argparse.SUPPRESS)
    args = parser.parse_args()
    directory = ROOT / "exercises" / args.lesson
    cases = json.loads((directory / "cases.json").read_text(encoding="utf-8"))
    answer = directory / ("solution.py" if args.solution else "answer.py")
    if args.case is not None:
        with tempfile.TemporaryDirectory() as temporary:
            folder = Path(temporary)
            import os

            previous = Path.cwd()
            try:
                os.chdir(folder)
                execute(folder, answer, cases[args.case])
            finally:
                os.chdir(previous)
        return 0
    chosen = range(len(cases)) if args.extended else range(1)
    failures = 0
    for i in chosen:
        command = [
            sys.executable,
            str(Path(__file__).resolve()),
            args.lesson,
            "--case",
            str(i),
        ]
        if args.solution:
            command.append("--solution")
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=5)
            if result.returncode:
                failures += 1
                print(f"FAIL case {i + 1}: {result.stderr.strip().splitlines()[-1]}")
            else:
                print(f"PASS case {i + 1}")
        except subprocess.TimeoutExpired:
            failures += 1
            print(f"FAIL case {i + 1}: execution exceeded five seconds")
    print(
        "READY: behavior checks passed"
        if not failures
        else "RETRY: use a lesson hint, then rerun"
    )
    return int(failures > 0)


if __name__ == "__main__":
    raise SystemExit(main())
