import pytest


@pytest.fixture
def my_number():
    return "1234567890123456"


@pytest.fixture
def problem_number():
    return "123456"


@pytest.fixture
def notstr_num():
    return 1234567890123456


@pytest.fixture
def number():
    return "12345678901234567890"


@pytest.fixture
def mock_list_of_dicts():
    return [{"date": "2022-01-01"}, {"date": "2021-12-31"}, {"date": "2022-01-03"}, {"date": "2022-01-02"}]


@pytest.fixture
def user_number():
    return "счет 12345678901234567890"


@pytest.fixture
def good_card_number():
    return "1234567812345678"


@pytest.fixture
def bad_card_number():
    return "12345"


@pytest.fixture
def good_account_number():
    return "12345678123456781234"


@pytest.fixture
def bad_account_number():
    return "123"


@pytest.fixture
def amazing_date():
    return "12345678910"


@pytest.fixture
def input_time():
    return "2023-12-31"


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


# @pytest.fixture
# def card_numbers_() -> list[str]:
#     return [
#         "0000 0000 0000 0001",
#         "0000 0000 0000 0002",
#         "0000 0000 0000 0003",
#         "0000 0000 0000 0004",
#         "0000 0000 0000 0005"
#     ]


@pytest.fixture
def card_numbers() -> list[str]:
    return ["1596837868705199", "7158300734726758", "6831982476737658"]


@pytest.fixture
def account_numbers() -> list[str]:
    return ["64686473678894779589", "35383033474447895560", "73654108430135874305"]


@pytest.fixture
def customer_details() -> list[str]:
    return [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]


@pytest.fixture
def enter_data() -> list[str]:
    return ["2024-03-11T02:26:18.671407", "2018-06-30T02:08:58.425572", "2018-09-12T21:27:25.241689"]


@pytest.fixture
def file_error():
    return 123
