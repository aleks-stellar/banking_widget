import logging
from pathlib import Path

PATH_TO_LOG_FILE = Path(Path(__file__).parent.parent, "logs", "masks.log")

card_logger = logging.getLogger("app.card_mask")
card_logger.setLevel(logging.INFO)
card_file_handler = logging.FileHandler(
    PATH_TO_LOG_FILE,
    mode="w", encoding="utf-8"
)
card_file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
)
card_file_handler.setFormatter(card_file_formatter)
card_logger.addHandler(card_file_handler)

account_logger = logging.getLogger("app.account_mask")
account_logger.setLevel(logging.INFO)
account_file_handler = logging.FileHandler(
    PATH_TO_LOG_FILE,
    mode="w", encoding="utf-8"
)
account_file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
)
account_file_handler.setFormatter(account_file_formatter)
account_logger.addHandler(account_file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    card_logger.info("The function has started...")
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

        card_logger.info("Function has successfully completed its work...")
        return modified_card_number

    except TypeError as e:
        card_logger.error("Incorrect input data...")
        print(f"Ошибка: {e}")
        return ""

    except Exception as e:
        card_logger.error("Unexpected error...")
        print(f"Непредвиденная ошибка: {e}")
        return ""


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    account_logger.info("The function has started...")
    try:
        if not isinstance(account_number, int):
            raise TypeError("Полученное значение не является числом")

        if len(str(account_number)) != 20:
            raise TypeError("Не верная длина номера счета")

        modified_account_number = "**" + str(account_number)[-4:]

        account_logger.info("Function has successfully completed its work...")
        return modified_account_number

    except TypeError as e:
        account_logger.error("Incorrect input data...")
        print(f"Ошибка: {e}")
        return ""

    except Exception as e:
        account_logger.error("Unexpected error...")
        print(f"Непредвиденная ошибка: {e}")
        return ""
