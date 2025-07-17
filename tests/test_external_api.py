from unittest.mock import Mock, patch

from src.external_api import convert_currency


@patch("src.external_api.requests.get")
def test_convert_currency(mock_requests_get: Mock) -> None:

    # Mock requests.get с фейковым JSON-ответом
    mock_response = Mock()
    mock_response.json.return_value = {"result": 123.45}
    mock_requests_get.return_value = mock_response

    # Пример входных данных
    operation = {
        "operationAmount": {
            "amount": 100,
            "currency": {
                "code": "USD"
            }
        }
    }

    # Вызываем тестируемую функцию
    result = convert_currency(operation)

    assert result == 123.45
    mock_requests_get.assert_called_once()
