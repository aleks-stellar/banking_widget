from typing import Dict, List


def filter_by_state(
    transactions_list: List[Dict[str, str | int]],
    state: str = "EXECUTED"
) -> List[Dict[str, str | int]]:
    """
    Функция принимает список словарей и проводит его фильтрацию
    по ключу
    """

    for transaction in transactions_list:
        if "state" not in transaction:
            raise KeyError

    filtered_transactions_list = [
        transaction
        for transaction in transactions_list
        if transaction["state"] == state
    ]
    return filtered_transactions_list


# Функция для сортировки даты
def get_date_format(
    transaction_dict: Dict[str, str | int]
) -> int:
    """
    Функция принимает словарь и извлекает из
    него дату для дальнейшей сортировки
    """
    date_str = str(transaction_dict["date"])
    date_list = date_str.split("-", 2)

    if not date_list[0].isdigit() or not date_list[1].isdigit() or not date_list[2][:2].isdigit():
        raise TypeError

    if not len(date_list[0]) == 4 or not len(date_list[1]) == 2:
        raise TypeError

    date_list[2] = date_list[2][:2]
    date_str = "".join(date_list)
    return int(date_str)


def sort_by_date(
    unsorted_transactions_list: List[Dict[str, str | int]],
    sorting_direction: bool = True
) -> List[Dict[str, str | int]]:
    """
    Принимает на вход список словарей и сортирует его по дате
    """
    sorted_transactions_list = sorted(
        unsorted_transactions_list,
        key=get_date_format,
        reverse=sorting_direction
    )
    return sorted_transactions_list
