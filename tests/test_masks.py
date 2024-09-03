import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_masks_len(my_number, problem_number):
    assert get_mask_card_number(my_number) == "1234 56** **** 3456"



def test_len_account_card(my_number):
    assert get_mask_account(my_number) == "Мало цифр"



def test_get_mask_card_number_bad(bad_card_number):
    assert get_mask_card_number(bad_card_number) == "Неверное количество цифр"


def test_get_mask_account_good(good_account_number):
    assert get_mask_account(good_account_number) == "**1234"


def test_get_mask_account_bad(bad_account_number):
    assert get_mask_account(bad_account_number) == "Мало цифр"


@pytest.mark.parametrize(
    "number_card, expected",
    [
        ("123456781234567", "Неверное количество цифр"),
        ("1234", "Неверное количество цифр"),
    ],
)
def test_get_mask_card_number(number_card, expected):
    assert get_mask_card_number(number_card) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("1234567890", "Мало цифр"),
        ("123456789012345678", "Мало цифр"),
        ("123456789012345678901234567890", "**7890"),  # Тест с длинным номером счета
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
