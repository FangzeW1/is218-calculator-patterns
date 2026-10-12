# My calculator submission

## Setup, run, and test

Create and activate a virtual environment, then install the requirements:

##```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

Run the calculator with:
python -m calculator

Run the full test suite with coverage using:
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100

## Example conversation

```text
> add 5 3
8.0
> subtract 10 4
6.0
...
> exit
```

Static, class, and instance methods:
The methods in Operations, such as Operations.add(), are static methods because they only use the values passed into them and do not need self or cls.

Calculation.create() is a class method because it uses cls to create an object of the concrete class that called it.

ArithmeticCalculation.execute() is an instance method because it uses the calculation object's stored operands and operation through self.
Factory, Command, and Strategy

For add 5 3, the CLI reads the command and selects Operations.add from the operations dictionary. ArithmeticCalculation.create(5, 3, Operations.add) acts as the factory and creates the calculation.

The selected operation function is the Strategy because the same calculation code can use addition, subtraction, multiplication, or division. 

CalculateCommand is the Command because it runs the calculation, stores a successful history entry, and returns the result.
OOP

Encapsulation: Calculation keeps its operands and operation together inside one object. HistoryCommand returns a copy of the history list so outside code cannot modify the stored history directly.

Abstraction: Calculation is an abstract base class that requires an execute() method. Concrete calculation classes must provide that behavior.

Inheritance: ArithmeticCalculation inherits from Calculation and reuses its constructor and create() class method.

Polymorphism: Code can call execute() on a calculation without needing to know the exact implementation. CalculateCommand can work with any calculation that follows the Calculation contract.

Composition: CalculateCommand contains a calculation object, and the calculation contains an operation function. Larger behavior is built by combining these smaller parts.

SOLID

Single Responsibility Principle: Each part has one main job. Operations performs arithmetic, calculations hold calculation data, commands coordinate actions and history, and the CLI handles user input and output.

Open/Closed Principle: A new operation can be added by creating another operation function and registering it in the CLI dictionary without changing ArithmeticCalculation.execute() or CalculateCommand.execute().

Liskov Substitution Principle: Any replacement for Calculation should still follow the same execute() contract by returning a numeric result or raising an appropriate error.

Interface Segregation Principle: The calculation interface is small and only requires execute() instead of unrelated methods.

Dependency Inversion Principle: CalculateCommand receives a Calculation object instead of creating a specific calculation itself. The calculation also receives an operation function rather than hard-coding addition or another operation.

Adding subtraction, multiplication, and division did not require changing calculation execution because `ArithmeticCalculation.execute()` always runs:

```python
return self.operation(self.a, self.b)
```

Only the operation function changes.

Tests and GitHub Actions

The project reaches 100% line coverage using:
python -m pytest --cov=calculator --cov-report=term-missing --cov-fail-under=100

Successful GitHub Actions run:
https://github.com/FangzeW1/is218-calculator-patterns/actions/runs/38187995782/job/114614432925

Coverage exclusions
The abstract Calculation.execute() placeholder is excluded with # pragma: no cover because it only defines the required contract and contains no real implementation to test.
The if __name__ == "__main__": entry point is also excluded because it only starts main(). The behavior of main() itself is tested directly.