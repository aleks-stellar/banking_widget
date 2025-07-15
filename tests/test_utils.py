import json
from json import JSONDecodeError
from pathlib import Path
from unittest.mock import Mock, patch

from src.utils import get_list_operations

PATH_TO_DOWNLOAD = Path(
    Path(__file__).parent.parent, "data", "operations.json"
)


@patch("builtins.open")
def test_get_list_operations_invalid_path(mock_open: Mock) -> None:
    """
    Тест для проверки работы функции, принимающей некорректный путь.
    """
    mock_open.return_value = mock_open(read_data=json.dumps([]))
    json.load = Mock(return_value=[])
    invalid_path = Path(Path(__file__).parent.parent, "py.py")

    result = get_list_operations(invalid_path)

    assert result == []


@patch("builtins.open")
def test_get_list_operations_empty_file(mock_open: Mock) -> None:
    """
    Тест проверяет обработку пустого файла.
    """
    mock_open.return_value = mock_open(read_data="")
    json.load = Mock(return_value=[])

    result = get_list_operations(PATH_TO_DOWNLOAD)

    assert result == []
    mock_open.assert_called_with(PATH_TO_DOWNLOAD, encoding="utf-8")


@patch("builtins.open")
def test_get_list_operations_non_dict_items(mock_open: Mock) -> None:
    """
    Тест для проверки работы функции при неверном типе json-строки
    (когда json-строка не является списком словарей).
    """
    mock_open.return_value = mock_open(
        read_data='[{"id": 1}, ["one", 1], {"id": 2}]'
    )
    json.load = Mock(return_value=[{"id": 1}, "string", {"id": 2}])

    result = get_list_operations(PATH_TO_DOWNLOAD)

    assert result == []
    mock_open.assert_called_with(PATH_TO_DOWNLOAD, encoding="utf-8")


@patch("builtins.open")
def test_get_list_operations_invalid_json_structure(mock_open: Mock) -> None:
    """
    Тест проверяет обработку ситуации, когда JSON-файл содержит данные,
    которые не соответствуют ожидаемой структуре (список словарей).
    """
    mock_open.return_value = mock_open(read_data='{"key": "value"}')
    json.load = Mock(return_value={"key": "value"})
    result = get_list_operations(PATH_TO_DOWNLOAD)
    assert result == []
    mock_open.assert_called_with(PATH_TO_DOWNLOAD, encoding="utf-8")


@patch("builtins.open")
def test_get_list_operations_json_decode_error(mock_open: Mock) -> None:
    """
    Имитируем некорректный json.
    """
    mock_open.return_value = mock_open(read_data="{incorrect json")
    json.load = Mock(side_effect=JSONDecodeError("msg", doc="", pos=0))

    result = get_list_operations(PATH_TO_DOWNLOAD)

    assert result == []
    mock_open.assert_called_with(PATH_TO_DOWNLOAD, encoding="utf-8")
