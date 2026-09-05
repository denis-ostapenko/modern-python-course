import json

import pytest

from reading import filter_records, load_records, make_record, save_records, summarize


def test_record_normalizes_title():
    assert make_record("2026-09-05", " A book ", 12) == {"date": "2026-09-05", "title": "A book", "pages": 12}


@pytest.mark.parametrize("date,title,pages", [("bad", "A", 1), ("2026-02-30", "A", 1), ("2026-09-05", " ", 1), ("2026-09-05", "A", 0), ("2026-09-05", "A", True)])
def test_invalid_records(date, title, pages):
    with pytest.raises(ValueError):
        make_record(date, title, pages)


def test_summary_and_filter():
    records = [make_record("2026-09-05", "A", 12), make_record("2026-09-06", "A", 8), make_record("2026-09-06", "B", 5)]
    assert summarize(records) == {"A": 20, "B": 5}
    assert summarize([]) == {}
    assert filter_records(records, "B") == [records[2]]
    assert len(records) == 3


def test_round_trip(tmp_path):
    path = tmp_path / "records.json"
    records = [make_record("2026-09-05", "Água", 12)]
    save_records(path, records)
    assert load_records(path) == records
    assert json.loads(path.read_text(encoding="utf-8")) == records


def test_missing_and_malformed(tmp_path):
    path = tmp_path / "records.json"
    assert load_records(path) == []
    path.write_text("broken", encoding="utf-8")
    with pytest.raises(ValueError):
        load_records(path)
    assert path.read_text(encoding="utf-8") == "broken"


def test_invalid_shape(tmp_path):
    path = tmp_path / "records.json"
    path.write_text('{}', encoding="utf-8")
    with pytest.raises(ValueError):
        load_records(path)
