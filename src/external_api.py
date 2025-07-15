import os

import requests
from dotenv import load_dotenv


def convert_currency(operations_dict: dict) -> float:
    """
    Функция для конвертации валют в RUB.
    :param operations_dict: Сумма транзакции
    :return: Конвертированная сумма транзакции.
    """
    amount = operations_dict["operationAmount"]["amount"]
    from_currency = operations_dict["operationAmount"]["currency"]["code"]
    to_currency = "RUB"

    # Загружаем переменные окружения
    load_dotenv()

    # Получаем ключ
    api_key = os.getenv("API_KEY_CONVERT")

    api_url = "https://api.apilayer.com/exchangerates_data/convert"

    # Задаем параметры запроса
    query_params = {
        "to": to_currency,
        "from": from_currency,
        "amount": amount
    }
    headers = {
        "apikey": api_key
    }

    # Делаем запрос
    response = requests.get(
        api_url, params=query_params, headers=headers)

    # Записываем в переменную результаты запроса
    data = response.json()
    result = data["result"]

    return float(result)
