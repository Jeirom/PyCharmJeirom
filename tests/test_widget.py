from src.widget import get_date, mask_account_card


def test_mask_account_card(user_number):
    assert mask_account_card(user_number) == "Счет **7890"

def test_get_date(input_time):
    assert get_date(input_time) == "31.12.2023"

