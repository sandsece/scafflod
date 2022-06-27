from hello import add
from hello import subtract


def test_add():
    assert add(2, 2) == 4
    assert add(2, 3) != 4


def test_subtract():
    assert subtract(5, 4) == 1
