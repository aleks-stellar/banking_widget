"""
В модуле реализованы две функции:
Функция {mask_account_card}, которая умеет обрабатывать информацию как
о картах, так и о счетах;
Функция {get_date}, которая принимает на вход строку с датой в формате
'2024-03-11T02:26:18.671407' и возвращает строку с датой в формате
'ДД.ММ.ГГГГ' ('11.03.2024').
"""

from masks import get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Функция принимает информацию о карте и маскирует ее номер"""
    card_type_list = []
    card_info_list = card_info.split()

    for string in card_info_list:
        if string.isalpha():
            card_type_list.append(string)
    card_type = " ".join(card_type_list)

    card_number = int(card_info_list[-1])
    return f"{card_type} {get_mask_card_number(card_number)}"


if __name__ == "__main__":

    print(mask_account_card("Visa Gold 5999414228426353"))
