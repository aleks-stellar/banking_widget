from unittest.mock import mock_open, patch

from src.decorators import log


@log()
def my_function(x, y):
    return x / y


def test_log_to_console_correct_value(capsys):
    my_function(1, 1)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_to_console_invalid_value(capsys):
    my_function(1, 0)
    captured = capsys.readouterr()
    assert captured.out == ("my_function error: "
                            "ZeroDivisionError. Inputs: (1, 0), {}\n"
                            )


@patch("builtins.open", new_callable=mock_open)
def test_log_to_file_correct(mock_file):
    @log(filename="test.log")
    def test_function(a, b):
        return a // b

    test_function(1, 1)
    mock_file.assert_called_once_with("test.log", "a", encoding="utf-8")
    mock_file().write.assert_any_call("test_function ok")
    mock_file().write.assert_any_call("\n")
