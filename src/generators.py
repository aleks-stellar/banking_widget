"""Этот модуль содержит функции,
реализующие генераторы для обработки массивов транзакций."""
from typing import Iterator


def filter_by_currency(
        transactions: list[dict],
        currency: str
) -> Iterator[dict]:
    """Функция по списку транзакций возвращает итератор
    с транзакциями в определенной валюте"""
    usd_transactions_count = 0
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
            usd_transactions_count += 1
        if usd_transactions_count == 0:
            raise ValueError("Не найдено транзакции в заданной валюте")


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция генерирует описание операций по очереди"""
    if len(transactions) == 0:
        raise ValueError("Список транзакций пуст")
    descriptions_key_count = 0
    for transaction in transactions:
        if "description" not in transaction:
            raise ValueError("У данной транзакции отсутствует описание")
        yield transaction["description"]
        descriptions_key_count += 1


def card_number_generator(
        start: int = 1, stop: int = 9999999999999999
) -> Iterator[str]:
    """Функция генерирует номер карты в формате XXXX XXXX XXXX XXXX"""
    if (start not in range(1, 10000000000000000)
            or stop not in range(1, 10000000000000000)):
        raise ValueError(
            "Некорректные начальное или конечное значение диапазона"
        )
    for num in range(start, stop + 1):
        card_number_str = ("0" * (16 - len(str(num)))
                           + str(num))
        card_number_str = " ".join(
            [
                card_number_str[n: n + 4]
                for n in range(0, len(card_number_str), 4)
            ]
        )
        yield card_number_str
