import pytest

from calculator.operations import Operations


def test_subtract():
    assert Operations.subtract(5, 3) == 2
    assert Operations.subtract(-5, 3) == -8


def test_multiply():
    assert Operations.multiply(4, 3) == 12
    assert Operations.multiply(2.5, 2) == pytest.approx(5.0)
    assert Operations.multiply(4, 0) == 0


def test_divide():
    assert Operations.divide(6, 3) == pytest.approx(2.0)
    assert Operations.divide(5, 2) == pytest.approx(2.5)


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operations.divide(5, 0)