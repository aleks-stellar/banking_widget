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


# Фикстура для корректного списка транзакций
# в котором представлено описание транзакции
@pytest.fixture
def transactions_description_list() -> list[dict]:
    transactions_list = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
    return transactions_list


