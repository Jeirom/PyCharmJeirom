from typing import Union

from masks import get_mask_account, get_mask_card_number


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
        finaly_result_number = "".join(number).title()
        return f"{''.join(word).title()} {get_mask_account(finaly_result_number)}"
    else:
        for i in user_number.replace(" ", ""):
            if i.isalpha():
                word.append(i)
            else:
                number.append(i)
        finaly_result_card = "".join(number)
        return f"{''.join(word) + ' '} " f"{get_mask_card_number(finaly_result_card)}"


def get_date(time: Union[str]) -> str:
    """Функция сортирует полученную дату и время, выводит в хх.хх.хххх формате"""
    return f"{time[8:10]}.{time[5:7]}.{time[0:4]}"



#Тест для PR