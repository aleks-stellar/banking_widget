import json
import logging
from json import JSONDecodeError
from pathlib import Path


PATH_TO_LOG_FILE = Path(Path(__file__).parent.parent, "logs", "utils.log")

logger = logging.getLogger("app.utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(
    PATH_TO_LOG_FILE,
    mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_list_operations(path_to_json: Path) -> list[dict | None]:
    """
    Функция возвращает список словарей с данными о финансовых транзакциях
    из json-файла.
    :param path_to_json: Путь к json-файлу.
    :return: Список словарей с операцией или пустой список.
    """
    logger.info("The function has started...")
    try:
        # Проверка существования файла
        if not path_to_json.exists():
            raise FileNotFoundError(
                f"Файл не найден по пути \"{path_to_json}\""
            )

        # Открываем файл и загружаем json
        logger.info("Downloading transaction data from a file...")
        with open(path_to_json, encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        # Проверяем, что данные представляют собой список
        if not isinstance(json_data, list):
            raise TypeError("Данные должны быть списком словарей")

        # Проверяем, что каждый элемент списка - это словарь
        for item in json_data:
            if not isinstance(item, dict):
                raise TypeError("Элементы списка должны быть словарями")

        logger.info("Function has successfully completed its work...")
        return json_data

    except FileNotFoundError as e:
        logger.error("File not found...")
        print(f"Ошибка: {e}")
        return []

    except JSONDecodeError as e:
        logger.error("Formatting error of JSON-file...")
        print(f"Ошибка: неверное JSON-форматирование - {e}")
        return []

    except TypeError as e:
        logger.error("Unexpected error...")
        print(f"Ошибка: {e}")
        return []
