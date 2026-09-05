import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEARNER = ROOT / "learner-repo"


def main():
    cases = 0
    for folder in sorted((LEARNER / "exercises").iterdir()):
        if not folder.is_dir():
            continue
        result = subprocess.run([sys.executable, str(LEARNER / "tools/check_exercise.py"), folder.name, "--extended", "--solution"], capture_output=True, text=True, timeout=45, check=False)
        if result.returncode:
            raise RuntimeError(f"Solution {folder.name}: {result.stdout}\n{result.stderr}")
        cases += len(json.loads((folder / "cases.json").read_text(encoding="utf-8")))
    checkpoints = 0
    for folder in sorted((LEARNER / "checkpoints").iterdir()):
        if not folder.is_dir():
            continue
        with tempfile.TemporaryDirectory() as temporary:
            copied = Path(temporary) / "checkpoint"
            shutil.copytree(folder, copied)
            code = (copied / "main.py").read_text(encoding="utf-8")
            args = ["--help"] if "argparse" in code else []
            result = subprocess.run([sys.executable, str(copied / "main.py"), *args], input="reading\n25\n", cwd=copied, capture_output=True, text=True, timeout=5, check=False)
            if result.returncode:
                raise RuntimeError(f"Checkpoint {folder.name}: {result.stderr}")
            checkpoints += 1
    print(f"PASS: {cases} exercise solution cases and {checkpoints} isolated checkpoint runs")


if __name__ == "__main__":
    main()
