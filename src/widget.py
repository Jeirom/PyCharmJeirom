from typing import Union
def mask_account_card(user_number: Union[str]) -> str:
    """Функция скрывает данные пользователя, выводит их"""
    word = []
    number = []
    #bank_card = "MasterCard Visa Classic Visa Platinum Visa Gold Maestro"
    if "счет" in user_number.lower():
        for i in user_number:
            if i.isalpha():
                word.append(i)
            else:
                number.append(i)
        return f"{''.join(word)} {'*' * 2}{''.join(number)[-4:]}"
    else:
        for i in user_number.replace(' ', ''):
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


print(mask_account_card("Visa 8532456712345678"))
def get_date(time):
    return f"{time[8:10]}.{time[5:7]}.{time[0:4]}"

print(get_date("2024-03-11T02:26:18.671407"))