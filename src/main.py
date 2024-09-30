from typing import Any

from src.generators import filter_by_currency
from src.masks import *
from src.processing import filter_by_state, sort_by_date
from src.sorted_trans import sorted_trans
from src.utils import financial_transactions
from src.utils_csv_excel import distributor_file

# PATH_TO_FILE_JSON = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
# PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
# PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def customer_support_chat(file: Any) -> None:
    """Основная программа папки SRC. В ней работают остальные модули этой папки. Принимает на вход файл
    фильтрует его, выдает пользователю результат по его запросам"""

    while True:
        menu_item = input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
        )
        if menu_item == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = financial_transactions(file)
            break
        elif menu_item == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = distributor_file(file)
            break
        elif menu_item == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = distributor_file(file)
            break
        else:
            print("Такого ответа нет. Программа перезагружается..")

    state_list = ["EXECUTED", "CANCELED", "PENDING"]
    print(transactions)
    while True:
        state = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
            """
        ).upper()

        if state not in state_list:
            print(f'Статус операции "{state}" недоступен.')
        else:
            break

    try:
        ask_sorted_words = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        if ask_sorted_words.upper() == "ДА":
            sorted_words = input("Введите слово")
            filtered_transactions = filter_by_state(transactions, sorted_words)
    except Exception as e:
        print(f"error {e}")

    try:
        sorted_date = input("Отсортировать операции по дате? Да/Нет ")
        if sorted_date.upper() == "ДА":
            if input("Отсортировать по убыванию? ").upper() == "ДА":
                mode_flag = True
        else:
            print("Сортировка по возрастанию включено по умолчанию.")
            mode_flag = False
        filtered_transactions = sort_by_date(filtered_transactions, mode_flag)
    except Exception as er:
        print(f"error {er}")

    try:
        if input("Выводить только рублевые транзакции? Да/Нет").upper() == "ДА":
            rub_transactions = filter_by_currency(filtered_transactions, "RUB")
            filtered_transactions = list(rub_transactions)[:-1]
    except Exception as err:
        print(f"error {err}")
    ask_sorted_words = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет").upper()

    try:
        if ask_sorted_words == "ДА":
            sorted_words = input("Введите слово:     ")
            filtered_transactions = sorted_trans(filtered_transactions, sorted_words)
    except Exception as erro:
        print(f"error {erro}")

    print("Распечатываю итоговый список транзакций...")
    if len(filtered_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for tr in filtered_transactions:
            tr_date = get_mask_account(tr["date"])
            currency = tr["operationAmount"]["currency"]["name"]
            if tr["description"] == "Открытие вклада":
                from_to = get_mask_card_number(tr["to"])
            else:
                from_to = get_mask_card_number(tr["from"]) + " -> " + get_mask_card_number(tr["to"])

            amount = tr["operationAmount"]["amount"]
            print(
                f"""{tr_date} {tr['description']}
    {from_to}
    Сумма: {round(float(amount))} {currency}
    """
            )


if __name__ == "__main__":
    customer_support_chat("transactions.csv")

# print(customer_support_chat('transactions.csv'))
