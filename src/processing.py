from typing import Union


def filter_by_state(data: Union[list], state="EXECUTED") -> list:
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
        state соответствует указанному значению."""
    return [d for d in data if d.get("state") == state]


def sort_by_date(list_of_dicts: Union[list], reverse=True) -> list:
    """Функция должна возвращать новый список,
    отсортированный по дате (date)."""
    return sorted(list_of_dicts, key=lambda x: x["date"], reverse=reverse)
