import json
import subprocess
import sys
from pathlib import Path

import pytest

DAYBOOK = Path(__file__).resolve().parents[1] / "daybook"
sys.path.insert(0, str(DAYBOOK))
from model import make_entry  # noqa: E402
from reporting import totals_by_category  # noqa: E402
from storage import load_entries, save_entries  # noqa: E402


def test_repeated_category_and_empty():
    assert totals_by_category([]) == {}
    assert totals_by_category([make_entry("walk", 2), make_entry("walk", 3)]) == {
        "walk": 5
    }


@pytest.mark.parametrize(
    "category,minutes",
    [("", 1), (" ", 1), ("walk", 0), ("walk", -1), ("walk", True), ("walk", "3")],
)
def test_invalid_entry(category, minutes):
    with pytest.raises(ValueError):
        make_entry(category, minutes)


def test_unicode_round_trip_and_missing(tmp_path):
    path = tmp_path / "nested" / "data.json"
    assert load_entries(path) == []
    entries = [make_entry(" São Bento ", 3)]
    save_entries(path, entries)
    assert load_entries(path) == entries
    assert json.loads(path.read_text(encoding="utf-8"))[0]["category"] == "São Bento"


@pytest.mark.parametrize(
    "raw",
    ["broken", "{}", '[{"category":"walk","minutes":false}]', '[{"category":"walk"}]'],
)
def test_bad_data_preserved(tmp_path, raw):
    path = tmp_path / "data.json"
    path.write_text(raw, encoding="utf-8")
    with pytest.raises(ValueError):
        load_entries(path)
    assert path.read_text(encoding="utf-8") == raw


def test_failed_replace_preserves_original(tmp_path, monkeypatch):
    path = tmp_path / "data.json"
    path.write_text("original", encoding="utf-8")

    def fail(*args):
        raise OSError("simulated replacement failure")

    monkeypatch.setattr("storage.os.replace", fail)
    with pytest.raises(OSError):
        save_entries(path, [make_entry("walk", 3)])
    assert path.read_text(encoding="utf-8") == "original"
    assert list(tmp_path.iterdir()) == [path]


def test_cli_journey_and_failure(tmp_path):
    path = tmp_path / "data.json"

    def cli(*args):
        return subprocess.run(
            [sys.executable, str(DAYBOOK / "main.py"), "--data", str(path), *args],
            cwd=tmp_path,
            capture_output=True,
            text=True,
            check=False,
            timeout=5,
        )

    assert cli("--help").returncode == 0
    assert cli("summary").stdout == ""
    assert cli("add", "reading", "25").returncode == 0
    assert cli("add", "reading", "15").returncode == 0
    assert cli("summary").stdout == "reading: 40 minutes\n"
    assert cli("list").stdout == "reading: 25 minutes\nreading: 15 minutes\n"
    before = path.read_bytes()
    result = cli("add", "reading", "0")
    assert result.returncode == 1
    assert "positive whole" in result.stderr
    assert path.read_bytes() == before
    assert cli("add", "reading", "bad").returncode == 2
