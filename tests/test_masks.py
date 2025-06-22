import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестирование функции get_mask_card_number при корректных входных данных
def test_get_mask_card_number_correct_format(
        card_number_int: int
) -> None:
    assert get_mask_card_number(card_number_int) == (
        "7000 79** **** 6361"
    ), "Маска карты не соответствует ожидаемой"


# Тестирование функции get_mask_card_number при некорректных входных данных
def test_get_mask_card_number_type_error(
        card_number_incorrect_type: int, card_number_incorrect_length: int
) -> None:
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(card_number_incorrect_type)
    assert str(exc_info.value) == "Полученное значение не является числом"

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(card_number_incorrect_length)
    assert str(exc_info.value) == "Не верная длина номера карты"


# Тестирование функции get_mask_account при корректных входных данных
def test_get_mask_account_number_correct_format(
        account_number_int: int
) -> None:
    assert get_mask_account(account_number_int) == "**4305"


# Тестирование функции get_mask_account при некорректных входных данных
def test_get_account_number_type_error(
        account_number_incorrect_type: int,
        account_number_incorrect_length: int
) -> None:
    with pytest.raises(TypeError) as exc_info:
        get_mask_account(account_number_incorrect_type)
    assert str(exc_info.value) == "Полученное значение не является числом"

    with pytest.raises(TypeError) as exc_info:
        get_mask_account(account_number_incorrect_length)
    assert str(exc_info.value) == "Не верная длина номера счета"
