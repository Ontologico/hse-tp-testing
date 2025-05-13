import pytest

from .basic_funcs import add, divide, multiply


def test_add():
    assert add(2, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 3) == -3
    assert multiply(0, 5) == 0


def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.fixture
def example_numbers():
    return (3.0, 2.0)


def test_add_fixture(example_numbers):
    assert add(*example_numbers) == 5


def test_multiply_fixture(example_numbers):
    assert multiply(*example_numbers) == 6
