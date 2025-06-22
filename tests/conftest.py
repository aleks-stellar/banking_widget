import pytest

# Фикстура, возвращающая корректный номер карты
@pytest.fixture
def card_number_int():
    return 7000792289606361

# Фикстура, возвращающая номер карты строкового типа
@pytest.fixture
def card_number_incorrect_type():
    return "7000792289606361"

# Фикстура, возвращающая номер карты некорректной длины
@pytest.fixture
def card_number_incorrect_length():
    return 7000

# Фикстура, возвращающая корректный номер счета
@pytest.fixture
def account_number_int():
    return 73654108430135874305

# Фикстура, возвращающая номер счета строкового типа
@pytest.fixture
def account_number_incorrect_type():
    return "73654108430135874305"

# Фикстура, возвращающая номер счета некорректной длины
@pytest.fixture
def account_number_incorrect_length():
    return 7365


# Фикстура для корректного аккаунта карты
@pytest.fixture
def account_card_card():
    return "Visa Platinum 7000792289606361"

# Фикстура для корректного аккаунта счета
@pytest.fixture
def account_card_account():
    return "Счет 73654108430135874305"

# Фикстура для корректной входной даты
@pytest.fixture
def date_correct():
    return "2024-03-11T02:26:18.671407"