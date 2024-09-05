import random

from tests.conftest import number

transactions = [
{
"id": 939719570,
"state": "EXECUTED",
"date": "2018-06-30T02:08:58.425572",
"operationAmount": {
"amount": "9824.07",
"currency": {
"name": "USD",
"code": "USD"
}
},
"description": "Перевод организации",
"from": "Счет 75106830613657916952",
"to": "Счет 11776614605963066702"
},
{
"id": 123456789,
"state": "PENDING",
"date": "2019-07-15T10:30:45.123456",
"operationAmount": {
"amount": "5000.00",
"currency": {
"name": "EUR",
"code": "EUR"
}
},
"description": "Оплата услуг",
"from": "Счет 12345678901234567890",
"to": "Счет 09876543210987654321"
}
]





def filter_by_currency(transactions:list, currency:str) -> dict:
    """Функция фильтрует входной список словарей, проходит до нужных данных, выводит только те словари, которые
    проходят под условия задачи"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction




filtered_transactions = filter_by_currency(transactions, "USD")
for transaction in filtered_transactions:
    print(transaction)


def transaction_descriptions(transactions:list) -> dict:
    """функция выводит данные пользователя о платежах"""
    for transaction in transactions:
        yield transaction["description"]


descriptions = transaction_descriptions(transactions)
for _ in range(1):
    print(next(descriptions))


transactions = [
{
"id": 939719570,
"state": "EXECUTED",
"date": "2018-06-30T02:08:58.425572",
"operationAmount": {
"amount": "9824.07",
"currency": {
"name": "USD",
"code": "USD"
}
},
"description": "Перевод организации",
"from": "Счет 75106830613657916952",
"to": "Счет 11776614605963066702"
},
{
"id": 123456789,
"state": "PENDING",
"date": "2019-07-15T10:30:45.123456",
"operationAmount": {
"amount": "5000.00",
"currency": {
"name": "EUR",
"code": "EUR"
}
},
"description": "Оплата услуг",
"from": "Счет 12345678901234567890",
"to": "Счет 09876543210987654321"
}
]



