import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


def test_filter_by_currency_usd(list_transactions: list[dict]) -> None:
    generator = filter_by_currency(list_transactions, "USD")
    usd_transactions_list = list(generator)
    assert len(usd_transactions_list) == 3
    assert all(
        transaction["operationAmount"]["currency"]["code"] == "USD"
        for transaction in usd_transactions_list
    )


def test_filter_by_currency_usd_without_usd(
        list_transactions: list[dict]
) -> None:
    del list_transactions[0]
    del list_transactions[0]
    del list_transactions[1]
    print(list_transactions)
    generator = filter_by_currency(list_transactions, "USD")
    with pytest.raises(ValueError):
        next(generator)


def test_transaction_descriptions(
        list_transactions: list[dict]
) -> None:
    generator = transaction_descriptions(list_transactions)
    list_transaction_descriptions = list(generator)
    assert len(list_transaction_descriptions) == 5
    with pytest.raises(ValueError):
        next(transaction_descriptions([]))


def test_transaction_descriptions_without_transactions(
        list_transactions: list[dict]
) -> None:
    for transaction in list_transactions:
        del transaction["description"]
    generator = transaction_descriptions(list_transactions)
    with pytest.raises(ValueError):
        next(generator)


@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
    ]),
    (9999999999999998, 9999999999999999,
     ['9999 9999 9999 9998', '9999 9999 9999 9999']),
    (3, 1, [])
])
def test_card_number_generator(
        start: int, stop: int, expected: str
) -> None:
    card_numbers = list(card_number_generator(start, stop))
    assert card_numbers == expected


def test_card_number_generator_invalid_range() -> None:
    with pytest.raises(ValueError):
        list(card_number_generator(99999999999999990, 1))
