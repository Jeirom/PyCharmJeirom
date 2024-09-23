import logging
from typing import Union


#Основная конфигурация logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='../logs/application.log',  # Запись логов в файл
                    filemode='w')  # Перезапись файла при каждом запуске

card_logger = logging.getLogger('app.mask.card')
mask_account_logger = logging.getLogger('app.mask.account')


def get_mask_card_number(number_card: Union[str]) -> str:
    """Функция маскирует средние числа номера карты, выводит результат"""
    try:

        if len(number_card) >= 16:
            card_logger.info(f'The function worked without data problems: {number_card}')
            return f"{number_card[:4]} {number_card[4:6]}{'*' * 2} {'*' * 4} {number_card[12:]}"

        else:

            card_logger.warning('Not enough numbers')
            return 'Неверное количество цифр'

    except Exception as e:
        card_logger.critical(f'{e} error')
        return []


def get_mask_account(account_number: Union[str]) -> str:
    """Функция маскрирует цифры номера счета, оставляя последние 4. Выводит резулат."""
    mask_account_logger.info(f'The function has accepted the data: {account_number}')
    if len(account_number) < 20:
        mask_account_logger.error('Not enough numbers')
        return "Мало цифр"
    else:
        mask_account_logger.info(f'The function worked without data problems: {account_number}')
        return f"{'*' * 2}{account_number[-4:]}"


user_input = input('Напишите ваш формат: КАРТА \ СЧЕТ : ').lower()
if user_input == 'карта':
    card = input('Введите 16-значный номер карты: ')
    result = get_mask_card_number(card)
    print(result)
else:
    print('Лень')


