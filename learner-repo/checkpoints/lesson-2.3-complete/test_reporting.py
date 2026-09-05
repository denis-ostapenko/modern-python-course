from main import totals_by_category


def test_empty_summary():
    assert totals_by_category([]) == {}


def test_repeated_category():
    entries = [{"category": "walk", "minutes": 2}, {"category": "walk", "minutes": 3}]
    assert totals_by_category(entries) == {"walk": 5}
