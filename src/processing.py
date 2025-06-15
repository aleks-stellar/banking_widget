from typing import Dict, List


def filter_by_state(
    dicts_list: List[Dict[str, str | int]],
    state_key: str = "EXECUTED"
) -> List[Dict[str, str | int]]:
    """
    Функция принимает список словарей и проводит его фильтрацию
    по ключу
    """
    filtered_dicts_list = [
        item_dict
        for item_dict in dicts_list
        if item_dict["state"] == state_key
    ]
    return filtered_dicts_list


# Функция для сортировки даты
def get_date_format(
    dicts_list_date: Dict[str, str | int]
) -> int:
    """
    Функция принимает словарь и извлекает из
    него дату для дальнейшей сортировки
    """
    date_str = str(dicts_list_date["date"])
    date_list = date_str.split("-", 2)
    date_list[2] = date_list[2][:2]
    date_list_reverse = "".join(date_list)
    return int(date_list_reverse)


def sort_by_date(
    dictionaries_list: List[Dict[str, str | int]],
    sorting_direction: bool = True
) -> List[Dict[str, str | int]]:
    """
    Принимает на вход список словарей и сортирует его по дате
    """
    sorted_dictionaries_list = sorted(
        dictionaries_list, key=get_date_format, reverse=sorting_direction
    )
    return sorted_dictionaries_list
