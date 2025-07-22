import re
from collections import Counter
from typing import Dict, List


def filter_by_state(
    transactions_list: List[Dict[str, str | int]],
    state: str = "EXECUTED"
) -> List[Dict[str, str | int]]:
    """
    Принимает список словарей с банковскими операциями
    и проводит его фильтрацию по ключу.
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
    Принимает словарь с информацией о банковской операции
    и извлекает из него дату для дальнейшей сортировки.
    """
    date_str = str(transaction_dict["date"])
    date_list = date_str.split("-", 2)

    if (not date_list[0].isdigit() or
            not date_list[1].isdigit() or
            not date_list[2][:2].isdigit()):
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
    Принимает список словарей с информацией о банковской операции
    и сортирует его по дате.
    """
    sorted_transactions_list = sorted(
        unsorted_transactions_list,
        key=get_date_format,
        reverse=sorting_direction
    )
    return sorted_transactions_list


def filter_transactions_by_pattern(
        transactions_data: list[dict], search_string: str
) -> list[dict]:
    """
    Выбирает из списка словарей с банковскими операциями те,
    у которых в описании есть данная строка.
    :param transactions_data: Список словарей с банковскими операциями.
    :param search_string: Строка, которая должна быть в описании операции.
    :return: Отфильтрованный список словарей.
    """
    try:
        # Шаблон строки поиска с учетом регистра
        pattern = re.compile(search_string, re.IGNORECASE)
        result = []

        for transaction in transactions_data:
            if "description" in transaction:
                if pattern.search(transaction["description"]):
                    result.append(transaction)
            else:
                raise KeyError("В словаре нет ключа \"description\"")

        return result

    except KeyError as e:
        print(f"Ошибка: {e}")
        return []


def count_transactions_by_description(
        operations_list: list[dict],
        categories_list: list[str]
) -> dict[str, int]:
    """
    Подсчитывает в словарь транзакции по категориям.
    :param operations_list: Список словарей с банковскими операциями.
    :param categories_list: Список категорий для подсчета.
    :return: Словарь {название категории: кол-во операций}.
    """
    descriptions_list = []

    # Создает циклом список категорий из списка транзакций
    for item in operations_list:
        if item["description"] in categories_list:
            descriptions_list.append(item["description"])

    # Создаем словарь из объекта Counter
    result = dict(Counter(descriptions_list))

    # Добавляем в этот словарь отсутствующие категории со значениями 0
    for category in categories_list:
        if category not in descriptions_list:
            result[category] = 0

    return dict(result)
