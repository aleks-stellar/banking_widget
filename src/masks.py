"""В модуле реализованы:
Функция маскировки номера банковской карты {get_mask_card_number},
Функция маскировки номера банковского счета {get_mask_account}."""


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    card_number_list = [str(card_number)[i: i + 4] for i in range(0, len(str(card_number)), 4)]
    card_number_list[1] = card_number_list[1][:2] + "**"
    card_number_list[2] = "****"
    modified_card_number = " ".join(card_number_list)
    return modified_card_number


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    modified_account_number = "**" + str(account_number)[-4:]
    return modified_account_number