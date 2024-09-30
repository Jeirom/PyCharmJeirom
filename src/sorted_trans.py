import re
from collections import defaultdict

def sorted_trans(transactions: list[dict], words: str) -> list[dict]:

    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращает список словарей, у которых в описании есть данная строка"""

    transactions = defaultdict(int)
    operations_new = []
    for trans in transactions:
        if re.search(words, trans.get("description", "")):
            operations_new.append(trans)
            transactions = operations_new
        return transactions


def count_operations_by_category(transactions_list: list[dict], categories: list[str]) -> dict[str, int]:

    """Функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""

    category_count = defaultdict(int)


    for transaction in transactions_list:
        description = transaction.get("description", "").lower()

        for ctg in categories:
            if re.search(re.escape(ctg.lower()), description):
                category_count[ctg] += 1

    return dict(category_count)