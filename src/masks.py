import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/masks.log",
    # filename='masks.log',
    filemode="w",
)
auth_logger = logging.getLogger("app.auth")
# logging.basicConfig(
#     logger = logging.getLogger(__name__)
#     file_handler = logging.FileHandler('masks.log')
#     file_formatter = "%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
#     file_handler.setFormatter(file_formatter)
#     logger.addHandler(file_handler)
#     logger.setLevel(logging.INFO)
# )


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты."""
    auth_logger.info(f"Маска карты{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(macc_number: str) -> str:
    """Функция маскировки номера счета."""
    mask_account = "**" + macc_number[-4:]
    auth_logger.info(f"Маска счета{mask_account}")
    return mask_account
