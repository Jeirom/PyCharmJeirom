from typing import Union


def mask_account_card(user_number: Union[str]) -> str:
    """Функция скрывает данные пользователя, выводит их"""
    word = []
    number = []
    if "счет" in user_number.lower():
        for i in user_number:
            if i.isalpha():
                word.append(i)
            else:
                number.append(i)
        return f"{''.join(word).title()} {'*' * 2}{''.join(number)[-4:]}"
    else:
        for i in user_number.replace(" ", ""):
            if i.isalpha():
                word.append(i)
            else:
                number.append(i)
        return (
            f"{''.join(word) + ' '} "
            f"{''.join(number)[:4]} "
            f"{''.join(number)[4:6]}{'*' * 2} "
            f"{'*' * 4} "
            f"{''.join(number)[12:]}"
        )


def get_date(time: Union[str]) -> str:
    """Функция сортирует полученную дату и время, выводит в хх.хх.хххх формате"""
    return f"{time[8:10]}.{time[5:7]}.{time[0:4]}"
