import pytest

from src.widget import mask_account_card,get_date

def test_mask_account_card(user_number):
    assert mask_account_card(user_number) == 'Счет **7890'

