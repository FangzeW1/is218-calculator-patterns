from calculator.calculation import Calculation


class CalculateCommand:
    def __init__(
        self,
        calculation: Calculation,
        history: list[str],
        label: str = "calculation"
    ):
        # The command receives its pieces instead of building them.
        self.calculation = calculation
        self.history = history
        self.label = label

    def execute(self) -> float:
        # Run the calculation first.
        # If this raises an error, history is never changed.
        result = self.calculation.execute()

        # Only successful calculations are recorded.
        self.history.append(f"{self.label} = {result}")

        return result


class HistoryCommand:
    def __init__(self, history: list[str]):
        self.history = history

    def execute(self) -> list[str]:
        # Return a copy so outside code cannot modify stored history.
        return self.history.copy()