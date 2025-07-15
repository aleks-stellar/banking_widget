import json
from json import JSONDecodeError
from pathlib import Path


def get_list_operations(path_to_json: Path) -> list[dict | None]:
    """
    Функция возвращает список словарей с данными о финансовых транзакциях
    из json-файла.
    :param path_to_json: Путь к json-файлу.
    :return: Список словарей с операцией или пустой список.
    """
    try:
        # Проверка существования файла
        if not path_to_json.exists():
            raise FileNotFoundError(f"Файл не найден по пути: {path_to_json}")

        # Открываем файл и загружаем json
        with open(path_to_json, encoding="utf-8") as json_file:
            json_data = json.load(json_file)

        # Проверяем, что данные представляют собой список
        if not isinstance(json_data, list):
            raise TypeError("Данные должны быть списком словарей")

        # Проверяем, что каждый элемент списка - это словарь
        for item in json_data:
            if not isinstance(item, dict):
                raise TypeError("Элементы списка должны быть словарями")

        return json_data

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return []

    except JSONDecodeError as e:
        print(f"Ошибка: неверное JSON-форматирование - {e}")
        return []

    except TypeError as e:
        print(f"Ошибка: {e}")
        return []
