import json
import logging
from json import JSONDecodeError
from external_api import currency_conversion
from typing import Any
#Основная конфигурация logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='../logs/application.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске

file_transaction_logger = logging.getLogger('app.decode.file')
transaction_amount_logger = logging.getLogger('app.transaction.amount')


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:

        with open(path, encoding="utf-8") as financial_file:
            file_transaction_logger.info(f'open file {path}')
            try:

                file_transaction_logger.info('Func ok')
                transactions = json.load(financial_file)

            except json.JSONDecodeError:

                file_transaction_logger.critical('JSONDecodeError')
                return []

        if not isinstance(transactions, list):

            return []

        return transactions

    except FileNotFoundError as e:

        file_transaction_logger.critical(f'Error {e}')
        return []



def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        transaction_amount_logger.info('Func ok!')
        amount = trans["operationAmount"]["amount"]

    else:

        amount = currency_conversion(trans)
        transaction_amount_logger.info('API request sent')
    return amount

