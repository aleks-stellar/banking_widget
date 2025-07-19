from pathlib import Path
from typing import Callable
from unittest.mock import Mock, patch

import pandas as pd

from src.transactions_parser import (read_csv_transactions,
                                     read_excel_transactions)

PATH_TO_FILE = Path(
    Path(__file__).parent.parent, "data", "transactions.csv"
)
PATH_TO_EXCEL_FILE = Path(
    Path(__file__).parent.parent, "data", "transactions_excel.xlsx"
)
INVALID_PATH_TO_FILE = Path(
    Path(__file__).parent.parent, "data", "operations.csv"
)


@patch("src.transactions_parser.csv.DictReader")
@patch("builtins.open")
def test_read_csv_transactions_valid(
        mock_open: Mock,
        mock_dict_reader: Mock,
        rows_in_reader: Callable,
        opened_and_formatted_transactions: Callable
) -> None:
    """
    Тест для проверки работы функции, принимающей корректные данные.
    """
    mock_dict_reader.return_value = rows_in_reader
    mock_file = Mock()
    mock_open.return_value.__enter__.return_value = mock_file
    result = read_csv_transactions(PATH_TO_FILE)
    assert result == opened_and_formatted_transactions
    mock_open.assert_called_once_with(PATH_TO_FILE, encoding="utf-8")
    mock_dict_reader.assert_called_once_with(mock_file, delimiter=";")


@patch("src.transactions_parser.csv.DictReader")
@patch("builtins.open")
def test_read_csv_transactions_empty(
        mock_open: Mock,
        mock_dict_reader: Mock,
) -> None:
    """
    Тест для проверки работы функции, принимающей пустой список транзакций.
    """
    mock_dict_reader.return_value = []
    mock_file = Mock()
    mock_open.return_value.__enter__.return_value = mock_file
    result = read_csv_transactions(PATH_TO_FILE)
    assert result == []
    mock_open.assert_called_once_with(PATH_TO_FILE, encoding="utf-8")
    mock_dict_reader.assert_called_once_with(mock_file, delimiter=";")


@patch("src.transactions_parser.csv.DictReader")
@patch("builtins.open")
def test_read_csv_transactions_invalid_nesting(
        mock_open: Mock,
        mock_dict_reader: Mock,
) -> None:
    """
    Тест для проверки работы функции, принимающей некорректные данные.
    """
    mock_dict_reader.return_value = [{"0ne": 1}, "Two", 2]
    mock_file = Mock()
    mock_open.return_value.__enter__.return_value = mock_file
    result = read_csv_transactions(PATH_TO_FILE)
    assert result == []
    mock_open.assert_called_once_with(PATH_TO_FILE, encoding="utf-8")
    mock_dict_reader.assert_called_once_with(mock_file, delimiter=";")


@patch("src.transactions_parser.csv.DictReader")
@patch("builtins.open")
def test_read_csv_transactions_without_keys(
        mock_open: Mock,
        mock_dict_reader: Mock,
) -> None:
    """
    Тест для проверки работы функции, принимающей
    данные без необходимых ключей.
    """
    mock_dict_reader.return_value = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        }
    ]
    mock_file = Mock()
    mock_open.return_value.__enter__.return_value = mock_file
    result = read_csv_transactions(PATH_TO_FILE)
    assert result == []
    mock_open.assert_called_once_with(PATH_TO_FILE, encoding="utf-8")
    mock_dict_reader.assert_called_once_with(mock_file, delimiter=";")


@patch("src.transactions_parser.csv.DictReader")
@patch("builtins.open")
def test_read_csv_transactions_invalid_path(
        mock_open: Mock,
        mock_dict_reader: Mock,
        rows_in_reader: Callable
) -> None:
    """
    Тест для проверки работы функции, принимающей некорректный путь.
    """
    mock_dict_reader.return_value = rows_in_reader
    mock_file = Mock()
    mock_open.return_value.__enter__.return_value = mock_file
    result = read_csv_transactions(INVALID_PATH_TO_FILE)
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_transactions_valid(
        mock_read_excel: Mock,
        df_data: Callable,
        opened_and_formatted_transactions: Callable
) -> None:
    """
    Тест для проверки работы функции, принимающей корректные данные.
    """
    mock_read_excel.return_value = df_data
    result = read_excel_transactions(PATH_TO_EXCEL_FILE)
    assert result == opened_and_formatted_transactions
    mock_read_excel.assert_called_once_with(PATH_TO_EXCEL_FILE)


@patch("pandas.read_excel")
def test_read_excel_transactions_invalid_path(
        mock_read_excel: Mock,
        df_data: Callable,
        opened_and_formatted_transactions: Callable
) -> None:
    """
    Тест для проверки работы функции, принимающей некорректный путь.
    """
    mock_read_excel.return_value = df_data
    result = read_excel_transactions(INVALID_PATH_TO_FILE)
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_transactions_missing_keys(
    mock_read_excel: Mock
) -> None:
    """
    Тест для проверки работы функции, принимающей некорректный формат данных.
    """
    mock_read_excel.return_value = pd.DataFrame(
        {
            "id": ["123"],
            "state": ["EXECUTED"]
        }
    )
    result = read_excel_transactions(PATH_TO_EXCEL_FILE)
    assert result == []
    mock_read_excel.assert_called_once_with(PATH_TO_EXCEL_FILE)


@patch("pandas.read_excel")
def test_read_excel_transactions_empty(
    mock_read_excel: Mock
) -> None:
    """
    Тест для проверки работы функции, принимающей пустой датафрейм.
    """
    mock_read_excel.return_value = pd.DataFrame()
    result = read_excel_transactions(PATH_TO_EXCEL_FILE)
    assert result == []
    mock_read_excel.assert_called_once_with(PATH_TO_EXCEL_FILE)


@patch("pandas.read_excel", side_effect=Exception)
def test_read_excel_transactions_exception(mock_read_excel: Mock) -> None:
    """
    Тест проверяет обработку непредвиденных ошибок при чтении Excel-файла.
    """
    result = read_excel_transactions(PATH_TO_EXCEL_FILE)
    assert result == []
    mock_read_excel.assert_called_once_with(PATH_TO_EXCEL_FILE)
