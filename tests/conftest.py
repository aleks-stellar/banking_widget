import pytest

@pytest.fixture
def card_number_int():
    return 7000792289606361

@pytest.fixture
def card_number_incorrect_type():
    return "7000792289606361"

@pytest.fixture
def card_number_incorrect_length():
    return 7000

@pytest.fixture
def account_number_int():
    return 73654108430135874305

@pytest.fixture
def account_number_incorrect_type():
    return "73654108430135874305"

@pytest.fixture
def account_number_incorrect_length():
    return 7365

