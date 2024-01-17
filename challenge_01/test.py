from multiplication import tabuada


def test_tabuada():
    assert tabuada(2) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert tabuada(3) == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    assert tabuada(7) == [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
