import pytest

@pytest.fixture
def my_number():
    return '1234567890123456'
@pytest.fixture
def problem_number():
    return '123456'
@pytest.fixture
def notstr_num():
    return 1234567890123456

@pytest.fixture
def number():
    return '12345678901234567890'

@pytest.fixture
def mock_list_of_dicts():
    return [
{"date": "2022-01-01"},
{"date": "2021-12-31"},
{"date": "2022-01-03"},
{"date": "2022-01-02"}
]

@pytest.fixture
def user_number():
    return "счет 12345678901234567890"

@pytest.fixture
def good_card_number():
    return '1234567812345678'

@pytest.fixture
def bad_card_number():
    return '12345'

@pytest.fixture
def good_account_number():
    return '12345678123456781234'

@pytest.fixture
def bad_account_number():
    return '123'

@pytest.fixture
def amazing_date():
    return '12345678910'

@pytest.fixture
def input_time():
    return "2023-12-31"