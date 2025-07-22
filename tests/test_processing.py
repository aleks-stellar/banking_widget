import pytest

from src.processing import (
    filter_by_state,
    get_date_format, sort_by_date,
    filter_transactions_by_pattern
)


# Тестирование функции filter_by_state при корректных входных данных
def test_filter_by_state_correct(
        transactions_list_correct: list[dict[str, str | int]]
) -> None:
    assert filter_by_state(transactions_list_correct) == [
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]


# Тестирование функции filter_by_state при корректных
# входных данных без необходимого state
def test_filter_by_state_without_necessary_state(
        transactions_list_without_state: list[dict[str, str | int]]
) -> None:
    assert filter_by_state(transactions_list_without_state) == []


# Обработка случая отсутствия значения статуса по умолчанию в словаре
@pytest.mark.parametrize("transactions_list, state, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED',
       'date': '2019-07-03T18:35:29.512364'}], "Exe", []),
    ([{'id': 41428829, 'state': '',
       'date': '2019-07-03T18:35:29.512364'}], "Exe", [])
])
def test_filter_by_state_different_state(
        transactions_list: list[dict[str, str | int]],
        state: str, expected: list[dict[str, str | int]]
) -> None:
    assert filter_by_state(transactions_list, state) == expected


# Тест для обработки случая, когда ключа state нет в словаре
def test_filter_by_state_without_state_key() -> None:
    with pytest.raises(KeyError):
        filter_by_state([
            {'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}
        ])
    with pytest.raises(KeyError):
        filter_by_state([{}])


# Тестирование функции sort_by_date с корректными
# входными данными и разным ключом сортировки
def test_sort_by_date() -> None:
    assert sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'}
    ], True) == [
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'}
    ]
    assert sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'}
    ], False) == [
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'}
    ]


# Проверка корректности сортировки при одинаковых датах
def test_sort_by_identical_date() -> None:
    assert sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2019-07-03T02:08:58.425572'},
    ], False) == [
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2019-07-03T02:08:58.425572'}
    ]


# Тесты на работу функции с некорректными или нестандартными форматами дат
def test_get_date_incorrect_format(
        date_incorrect: str
) -> None:
    with pytest.raises(TypeError):
        get_date_format(
            {'id': 41428829, 'state': 'EXECUTED', 'date': date_incorrect}
        )
    with pytest.raises(TypeError):
        get_date_format(
            {'id': 41428829, 'state': 'EXECUTED', 'date': "T02:26:18.671407"}
        )
    with pytest.raises(TypeError):
        get_date_format(
            {'id': 41428829, 'state': 'EXECUTED', 'date': ""}
        )


def test_filter_transactions_by_pattern_valid(
        opened_and_formatted_transactions
) -> None:
    """
    Тестирует функцию filter_transactions_by_pattern_valid,
    вызванную в корректными параметрами.
    """
    expected_result = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "operationAmount": {
                    "amount": "16210",
                    "currency": {
                        "name": "Sol",
                        "code": "PEN"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397"
            }
    ]
    actual_result_valid = filter_transactions_by_pattern(
        opened_and_formatted_transactions,
        search_string="перевод"
    )
    actual_result_empty = filter_transactions_by_pattern(
        opened_and_formatted_transactions,
        search_string="возмещение"
    )
    assert actual_result_valid == expected_result
    assert len(actual_result_valid) == 1
    assert actual_result_empty == []


def test_filter_transactions_by_pattern_key_error(
        opened_and_formatted_transactions
) -> None:
    """
    Тестирует работу функцию filter_transactions_by_pattern_valid
    с списком транзакций с отсутствующим ключом "description".
    """
    data_transactions = [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
            },
            {
                "id": "564764",
                "state": "EXECUTED",
                "date": "2021-06-07T12:36:31Z",
            }
        ]

    actual_result = filter_transactions_by_pattern(
        data_transactions, "перевод"
    )

    assert actual_result == []
    assert len(actual_result) == 0
