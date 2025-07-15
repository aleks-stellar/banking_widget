from unittest.mock import Mock, patch

from src.external_api import convert_currency


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv")
@patch("src.external_api.load_dotenv")
def test_convert_currency(
        mock_load_dotenv: Mock,
        mock_getenv: Mock,
        mock_requests_get: Mock
) -> None:
    mock_load_dotenv.return_value = None

    # Мок os.getenv для возврата фейкового ключа
    mock_getenv.return_value = "fake_api_key"

    # mock requests.get с фейковым JSON-ответом
    mock_response = Mock()
    mock_response.json.return_value = {"result": 123.45}
    mock_requests_get.return_value = mock_response

    # пример входных данных
    operation = {
        "operationAmount": {
            "amount": 100,
            "currency": {
                "code": "USD"
            }
        }
    }

    # вызываем тестируемую функцию
    result = convert_currency(operation)

    assert result == 123.45
    mock_load_dotenv.assert_called_once()
    mock_getenv.assert_called_with("API_KEY_CONVERT")
    mock_requests_get.assert_called_once()
