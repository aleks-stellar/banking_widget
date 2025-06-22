import pytest

from src.processing import filter_by_state, get_date_format, sort_by_date

# Тестирование функции filter_by_state при корректных входных данных
def test_filter_by_state_correct(transactions_list_correct):
    assert filter_by_state(transactions_list_correct) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


# Тестирование функции filter_by_state при корректных входных данных без необходимого state
def test_filter_by_state_without_necessary_state(transactions_list_without_state):
    assert filter_by_state(transactions_list_without_state) == []


# Обработка случая отсутствия значения статуса по умолчанию в словаре
@pytest.mark.parametrize("transactions_list, state, expected", [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}], "Exe", []),
    ([{'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'}], "Exe", [])
])
def test_filter_by_state_different_state(transactions_list, state, expected):
    assert filter_by_state(transactions_list, state) == expected


# Тест для обработки случая, когда ключа state нет в словаре
def test_filter_by_state_without_state_key():
    with pytest.raises(KeyError):
        filter_by_state([{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}])
    with pytest.raises(KeyError):
        filter_by_state([{}])


# Тестирование функции sort_by_date с корректными входными данными и разным ключом сортировки
def test_sort_by_date():
    assert sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ], True) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    assert sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ], False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


# Проверка корректности сортировки при одинаковых датах
def test_sort_by_identical_date():
    assert sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T02:08:58.425572'},
    ], False) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T02:08:58.425572'}
    ]


# Тесты на работу функции с некорректными или нестандартными форматами дат
def test_get_date_incorrect_format(date_incorrect):
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
