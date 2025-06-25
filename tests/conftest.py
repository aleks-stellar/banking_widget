import pytest


# Фикстура, возвращающая корректный номер карты
@pytest.fixture
def card_number_int() -> int:
    return 7000792289606361


# Фикстура, возвращающая номер карты строкового типа
@pytest.fixture
def card_number_incorrect_type() -> str:
    return "7000792289606361"


# Фикстура, возвращающая номер карты некорректной длины
@pytest.fixture
def card_number_incorrect_length() -> int:
    return 7000


# Фикстура, возвращающая корректный номер счета
@pytest.fixture
def account_number_int() -> int:
    return 73654108430135874305


# Фикстура, возвращающая номер счета строкового типа
@pytest.fixture
def account_number_incorrect_type() -> str:
    return "73654108430135874305"


# Фикстура, возвращающая номер счета некорректной длины
@pytest.fixture
def account_number_incorrect_length() -> int:
    return 7365


# Фикстура для корректного аккаунта карты
@pytest.fixture
def account_card_card() -> str:
    return "Visa Platinum 7000792289606361"


# Фикстура для корректного аккаунта счета
@pytest.fixture
def account_card_account() -> str:
    return "Счет 73654108430135874305"


# Фикстура для корректной входной даты
@pytest.fixture
def date_correct() -> str:
    return "2024-03-11T02:26:18.671407"


# Фикстура для некорректной входной даты
@pytest.fixture
def date_incorrect() -> str:
    return "03-11-2024T02:26:18.671407"


# Фикстура для корректного списка транзакций
@pytest.fixture
def transactions_list_correct() -> list[dict[str, int | str]]:
    return [
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'}
    ]


# Фикстура для корректного списка транзакций без необходимого state
@pytest.fixture
def transactions_list_without_state() -> list[dict[str, int | str]]:
    return [
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'}
    ]
