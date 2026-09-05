from answer import subtotal


def test_empty_subtotal():
    assert subtotal([]) == 0


def test_two_prices():
    assert subtotal([3, 4]) == 7
