import pytest

from src.widget import mask_account_card

# Тестирование функции при корректных входных данных
def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361",\
        "Маскировка виджета карты не соответствует ожидаемой"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305", \
        "Маскировка виджета счета не соответствует ожидаемой"


@pytest.mark.parametrize("info, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")
])
def test_mask_account_card_parameterized(info, expected):
    assert mask_account_card(info) == expected


# Тестирование функции при некорректных входных данных
def test_mask_account_card_incorrect():
    with pytest.raises(TypeError):
        mask_account_card("Счет")
    with pytest.raises(TypeError):
        mask_account_card("Счет 6924")
    with pytest.raises(TypeError):
        mask_account_card("5768374894856730")
    with pytest.raises(TypeError):
        mask_account_card("5768374894856730 Maestro")
