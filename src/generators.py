"""Этот модуль содержит все новые функции,
реализующие генераторы для обработки данных."""
from typing import Iterator


def filter_by_currency(
        transactions: list[dict],
        currency: str
) -> Iterator[dict]:
    """Функция по списку транзакций возвращает итератор
    с транзакциями в определенной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Функция генерирует описание операций по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(
        start: int = 1, stop: int = 9999999999999999
) -> Iterator[str]:
    """Функция генерирует номер карты в формате XXXX XXXX XXXX XXXX"""
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
