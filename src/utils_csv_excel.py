import csv
import logging
from typing import Any
import pandas as pd
from utils import financial_transactions

# Основная конфигурация logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/transaction.log",  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске

transaction_log = logging.getLogger("DISTRIBUTOR logs")


def distributor_file(file_path: str) -> Any:
    """Функция принимает на вход файл формата CSV, JSON, XLSX, обрабатывает и открывает"""
    # time_start = datetime.datetime.now()
    # transaction_log.info("Func start")

    try:

        if file_path.endswith(".json"):
            financial_transactions(file_path)
            transaction_log.warning("The function has been transferred to another module")

        elif file_path.endswith(".csv"):
            with open(file_path) as file:
                transactions = csv.reader(file, delimiter=";")
                return list(transactions)

        elif file_path.endswith(".xlsx"):
            excel_data = pd.read_excel(file_path)
            return excel_data

    except Exception as e:
        transaction_log.error(f"Error : {e}")
        return []

    # finally:
    # time_stop = datetime.datetime.now()
    # transaction_log.debug(f"The function worked in {time_stop-time_start} second")


# print(distributor_file("../data/operations.json"))
