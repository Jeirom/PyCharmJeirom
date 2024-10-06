from src.masks import get_mask_account
from src.processing import date_sort_func, state_func
from src.read_from_csv import read_from_csv
from src.sorting_transactions import sorting_transactions_by_description
from src.utils import get_transactions_data
from src.widget import *


def main() -> None:
    """Функция, определяющая работу с конечным пользователем разработанной программы.
    Задаёт вопросы и в соответствии с полученными ответами работает с разработанными модулями."""
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями!
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла;
    2. Получить информацию о транзакциях из CSV-файла;
    3. Получить информацию о транзакциях из XLSX-файла."""
    )
    while True:
        users_menu_choise = input("Введите свой выбор сюда: ")
        if users_menu_choise in ("1", "2", "3"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    menu = {
        "1": "Для обработки выбран JSON-файл.",
        "2": "Для обработки выбран CSV-файл.",
        "3": "Для обработки выбран XLSX-файл.",
    }
    print(f"{menu[users_menu_choise]}")
    if users_menu_choise == "1":
        transaction_data_list = get_transactions_data("../data/operations.json")
    elif users_menu_choise == "2":
        transaction_data_list = read_from_csv("../garbage/transactions.csv")
    elif users_menu_choise == "3":
        transaction_data_list = read_from_csv("../garbage/transactions.csv")
    # Фильтрация по статусу
    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы:  EXECUTED, CANCELED, PENDING"""
        )
        users_status = input("Введите выбранный статус сюда: ").upper()
        if users_status in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    filtred_transaction_data = state_func(transaction_data_list, users_status)
    print(f"Операции отфильтрованы по статусу {users_status}.")
    # Фильтрация по дате

    while True:
        print("Отфильтровать операции по дате?")
        users_choise_date_sort = input("Введите да/нет сюда: ").lower()
        if users_choise_date_sort in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    if users_choise_date_sort == "да":

        while True:
            print("Отфильтровать по возрастанию или убыванию?")
            users_choise_sort_direction = input("Введите по возрастанию/по убыванию сюда: ").lower()
            if users_choise_sort_direction in ("по возрастанию", "по убыванию"):
                break
            print("Введён некорректный ответ. Повторите ввод ответа.")
        if users_choise_sort_direction == "по возрастанию":
            direction = False
        elif users_choise_sort_direction == "по убыванию":
            direction = True
        date_sorted_transactions = date_sort_func(filtred_transaction_data, direction)
    elif users_choise_date_sort == "нет":
        date_sorted_transactions = filtred_transaction_data
    # Фильтрация по рублёвым транзакциям

    while True:
        print("Выводить только рублёвые транзакции?")
        users_choise_rub = input("Введите да/нет сюда: ").lower()
        if users_choise_rub in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    if users_choise_rub == "да":
        rub_transactions = [
            transaction
            for transaction in date_sorted_transactions
            if transaction["operationAmount"]["currency"]["code"] == "RUB"
        ]
    elif users_choise_rub == "нет":
        rub_transactions = date_sorted_transactions
    # Фильтрация по определённому слову в описании

    while True:
        print("Отфильтровать список по определённому слову в описании?")
        users_choise_description = input("Введите да/нет сюда: ").lower()
        if users_choise_description in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    if users_choise_description == "да":
        users_word_to_filter = input("Введите слово для сортировки сюда: ").lower()
        sorted_by_description = sorting_transactions_by_description(rub_transactions, users_word_to_filter)
        result_transactions = sorted_by_description
    elif users_choise_description == "нет":
        result_transactions = rub_transactions
    # Работа с итоговым списком
    count_of_transactions = len(result_transactions)
    # Вывод результатов, если список не пустой
    print("Распечатываю итоговый список транзакций...")
    if count_of_transactions == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(result_transactions)}")
        for tr in result_transactions:
            tr_date = get_mask_account(tr["date"])
            currency = tr["operationAmount"]["currency"]["name"]
            if tr["description"] == "Открытие вклада":
                from_to = mask_account_card(tr["to"])
            else:
                from_to = mask_account_card(tr["from"]) + " -> " + mask_account_card(tr["to"])

            amount = tr["operationAmount"]["amount"]
            print(
                f"""{tr_date} {tr['description']}
    {from_to}
    Сумма: {round(float(amount))} {currency}
    """
            )

    # if count_of_transactions > 0:


#         print("Распечатываю итоговый список транзакций...\n")
#         print(f"Всего банковских операций в выборке {count_of_transactions}.\n")
#         for item in result_transactions:
#             if item["description"] == "Открытие вклада":
#                 date_str = date_formatting(item["date"])
#                 descr_str = item["description"]
#                 summa_str = item["operationAmount"]
#                 currency_str = item["operationAmount"]["currency"]["code"]
#                 print(
#                     f"""{date_str} {descr_str}
# Сумма: {summa_str} {currency_str}\n"""
#                 )
#             else:
#                 date_str = date_formatting(item["date"])
#                 descr_str = item["description"]
#                 from_str = masking_with_info(item["from"])
#                 to_str = masking_with_info(item["to"])
#                 summa_str = item["operationAmount"]
#                 currency_str = item["operationAmount"]["currency"]["code"]
#                 print(
#                     f"""{date_str} {descr_str}
# {from_str} -> {to_str}
# Сумма: {summa_str} {currency_str}\n"""
#                 )
#     # Вывод результата с пустым списком
#     else:
#         print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
#

if __name__ == "__main__":
    main()
