from hello import add


def test_add():
    assert add(2, 2) == 4
    assert add(2, 3) != 4
