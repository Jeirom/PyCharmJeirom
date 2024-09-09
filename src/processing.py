def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
        state соответствует указанному значению."""
    filtered_list = []
    if state != "":
        for d in data:
            if d.get("state") == state:
                filtered_list.append(d)
        return filtered_list
    else:
        return ["Ошибка"]


def sort_by_date(list_of_dicts: list, reverse: bool = True) -> list:
    """Функция должна возвращать новый список,
    отсортированный по дате (date)."""
    sorted_list = []
    for d in sorted(list_of_dicts, key=lambda x: x["date"], reverse=reverse):
        sorted_list.append(d)
    return sorted_list
