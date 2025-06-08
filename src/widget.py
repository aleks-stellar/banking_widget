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
    date_list[2] = date_list[2][:2]
    date_list_reverse = ".".join(date_list[::-1])
    return date_list_reverse


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))