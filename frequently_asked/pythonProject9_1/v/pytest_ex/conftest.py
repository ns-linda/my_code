import pytest

@pytest.fixture(scope='session', autouse=True)
def test_call():
    print("Session fixture")
    