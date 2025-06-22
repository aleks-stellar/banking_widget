"""
В модуле реализованы две функции:
Функция {mask_account_card}, которая умеет обрабатывать информацию как
о картах, так и о счетах.
Функция {get_date}, которая принимает на вход строку с датой в формате
'2024-03-11T02:26:18.671407' и возвращает строку с датой в формате
'ДД.ММ.ГГГГ' ('11.03.2024').
"""

from src import masks


def mask_account_card(card_info: str) -> str:
    """Функция принимает информацию о карте и маскирует номер карты
    или счета"""

    card_type_list = []
    card_info_list = card_info.split()

    if len(card_info_list) < 2:
        raise TypeError

    if card_info_list[0].isdigit():
        raise TypeError

    for string in card_info_list:
        if string.isalpha():
            card_type_list.append(string)
    card_type = " ".join(card_type_list)

    card_number = int(card_info_list[-1])

    if card_type_list[0] == "Счет":
        return f"{card_type} {masks.get_mask_account(card_number)}"
    else:
        return f"{card_type} {masks.get_mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """Функция реформатирует дату"""
    date_list = date_str.split("-", 2)

    if not date_list[0].isdigit() or not date_list[1].isdigit() or not date_list[2][:2].isdigit():
        raise TypeError

    if not len(date_list[0]) == 4 or not len(date_list[1]) == 2:
        raise TypeError

    date_list[2] = date_list[2][:2]
    date_list_reverse = ".".join(date_list[::-1])
    return date_list_reverse
