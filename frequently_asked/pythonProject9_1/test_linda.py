import pytest

@pytest.mark.method1
def test_execute():
    a = 5
    b = 6
    assert a == b, "test failed"


def test_method_linda():
    a = 5
    b = 5
    assert a == b, "test failed"
