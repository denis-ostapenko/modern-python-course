import subprocess
import sys
from pathlib import Path


def test_command_journeys(tmp_path):
    source = Path(__file__).with_name("cli.py")
    data = tmp_path / "records.json"

    def command(*args):
        return subprocess.run([sys.executable, str(source), "--data", str(data), *args], capture_output=True, text=True, check=False, timeout=5)

    assert command("--help").returncode == 0
    assert command("summary").stdout == ""
    assert command("add", "2026-09-05", "A book", "12").returncode == 0
    assert command("add", "2026-09-06", "A book", "8").returncode == 0
    assert command("summary").stdout == "A book: 20 pages\n"
    assert command("list", "--title", "Absent").stdout == ""
    assert "A book | 12 pages" in command("list").stdout
    before = data.read_bytes()
    result = command("add", "2026-09-05", "A book", "0")
    assert result.returncode == 1
    assert result.stderr
    assert data.read_bytes() == before
    assert command("add", "2026-09-05", "A book", "not-a-number").returncode == 2
