import logging
from pathlib import Path

PATH_TO_LOG_FILE = Path("..", "logs", "masks.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    filename="masks.log",
    filemode="w",
    encoding="utf-8"
)
card_logger = logging.getLogger("app.card_mask")
account_logger = logging.getLogger("app.account_mask")


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    # card_logger.info("The function has started...")
    try:
        if not isinstance(card_number, int):
            raise TypeError("Полученное значение не является числом")

        if len(str(card_number)) != 16:
            raise TypeError("Не верная длина номера карты")

        card_number_list = [
            str(card_number)[i: i + 4]
            for i in range(0, len(str(card_number)), 4)
        ]
        card_number_list[1] = card_number_list[1][:2] + "**"
        card_number_list[2] = "****"
        modified_card_number = " ".join(card_number_list)

        return modified_card_number

    except TypeError as e:
        print(f"Ошибка: {e}")
        return ""

    except Exception as e:
        print(f"Непредвиденная ошибка {e}")
        return ""


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""

    if not isinstance(account_number, int):
        raise TypeError("Полученное значение не является числом")

    if len(str(account_number)) != 20:
        raise TypeError("Не верная длина номера счета")

    modified_account_number = "**" + str(account_number)[-4:]
    return modified_account_number
