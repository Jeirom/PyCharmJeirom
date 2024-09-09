from typing import Union


def get_mask_card_number(number_card: Union[str]) -> str:
    """Функция маскирует средние числа номера карты, выводит результат"""
    if len(number_card) >= 16:
        return f"{number_card[:4]} {number_card[4:6]}{'*' * 2} {'*' * 4} {number_card[12:]}"
    else:
        return 'Неверное количество цифр'

def get_mask_account(account_number: Union[str]) -> str:
    """Функция маскрирует цифры номера счета, оставляя последние 4. Выводит резулат."""
    if len(account_number) < 20:
        return "Мало цифр"
    else:
        return f"{'*' * 2}{account_number[-4:]}"

    # Тест для гита
