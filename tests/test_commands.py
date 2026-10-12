import pytest

from calculator.calculation import ArithmeticCalculation
from calculator.commands import CalculateCommand, HistoryCommand
from calculator.operations import Operations


def test_calculate_command_returns_result_and_adds_history():
    history = []

    calculation = ArithmeticCalculation.create(
        5,
        3,
        Operations.add
    )

    command = CalculateCommand(
        calculation,
        history,
        "add 5 3"
    )

    result = command.execute()

    assert result == 8
    assert history == ["add 5 3 = 8"]


def test_failed_calculation_does_not_add_history():
    history = []

    calculation = ArithmeticCalculation.create(
        5,
        0,
        Operations.divide
    )

    command = CalculateCommand(
        calculation,
        history,
        "divide 5 0"
    )

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()

    assert history == []


def test_history_command_returns_copy():
    history = ["add 5 3 = 8"]

    command = HistoryCommand(history)
    returned_history = command.execute()

    returned_history.append("fake entry")

    assert history == ["add 5 3 = 8"]


def test_history_command_empty():
    history = []

    command = HistoryCommand(history)

    assert command.execute() == []