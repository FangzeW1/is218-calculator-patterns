from calculator.cli import main


def test_cli_add_then_exit(monkeypatch, capsys):
    answers = iter([
        "add 5 3",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    lines = capsys.readouterr().out.splitlines()

    assert "8.0" in lines

def test_cli_history(monkeypatch, capsys):
    answers = iter([
        "add 5 3",
        "history",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    output = capsys.readouterr().out

    assert "8.0" in output
    assert "add 5 3 = 8.0" in output

def test_cli_empty_history(monkeypatch, capsys):
    answers = iter([
        "history",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    output = capsys.readouterr().out

    assert "History is empty" in output

def test_cli_unknown_command(monkeypatch, capsys):
    answers = iter([
        "potato 5 3",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    output = capsys.readouterr().out

    assert "Unknown command" in output

def test_cli_wrong_operand_count(monkeypatch, capsys):
    answers = iter([
        "add 5",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    output = capsys.readouterr().out

    assert "Expected two operands" in output

def test_cli_invalid_number(monkeypatch, capsys):
    answers = iter([
        "add hello 3",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    output = capsys.readouterr().out

    assert "Invalid number" in output

def test_cli_division_by_zero(monkeypatch, capsys):
    answers = iter([
        "divide 5 0",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    output = capsys.readouterr().out

    assert "Cannot divide by zero" in output

def test_cli_continues_after_error(monkeypatch, capsys):
    answers = iter([
        "add hello 3",
        "add 5 3",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    output = capsys.readouterr().out

    assert "Invalid number" in output
    assert "8.0" in output

def test_cli_blank_input(monkeypatch, capsys):
    answers = iter([
        "",
        "add 5 3",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    output = capsys.readouterr().out

    assert "8.0" in output

def test_cli_history_with_operands(monkeypatch, capsys):
    answers = iter([
        "history 5",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt="": next(answers)
    )

    main()

    output = capsys.readouterr().out

    assert "History does not take operands" in output

def test_cli_eof(monkeypatch):
    def end_of_input(prompt=""):
        raise EOFError

    monkeypatch.setattr(
        "builtins.input",
        end_of_input
    )

    main()

def test_main_module_import():
    import calculator.__main__