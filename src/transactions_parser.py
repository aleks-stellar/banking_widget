import csv
from pathlib import Path

import pandas as pd


def read_csv_transactions(path_to_csv_file: Path) -> list[dict] | None:
    """
    Считывает финансовые операции из CSV-файла
    и преобразует их в список словарей.
    :param path_to_csv_file: Путь к CSV-файлу с транзакциями.
    :return: Список словарей с транзакциями.
    """
    result = []

    try:
        if not path_to_csv_file.exists():
            raise FileNotFoundError(
                f"Файл не найден по пути \"{path_to_csv_file}\""
            )

        with open(path_to_csv_file, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=";")
            for row in reader:
                result.append(
                    {
                        "id": row["id"],
                        "state": row["state"],
                        "date": row["date"],
                        "operationAmount": {
                            "amount": row["amount"],
                            "currency": {
                                "name": row["currency_name"],
                                "code": row["currency_code"]
                            }
                        },
                        "description": row["description"],
                        "from": row["from"],
                        "to": row["to"]
                    }
                )

        return result

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return []

    except KeyError as e:
        print(f"Не найден ключ {e}")
        return []

    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        return []


def read_excel_transactions(path_to_excel_file: Path) -> list[dict] | None:
    """
    Считывает финансовые операции из EXCEL-файла
    и преобразует их в список словарей.
    :param path_to_excel_file: Путь к EXCEL-файлу с транзакциями.
    :return: Список словарей с транзакциями.
    """
    result = []

    try:
        if not path_to_excel_file.exists():
            raise FileNotFoundError(
                f"Файл не найден по пути \"{path_to_excel_file}\""
            )
        excel_transactions = pd.read_excel(path_to_excel_file)
        for _, row in excel_transactions.iterrows():
            result.append(
                {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {
                            "name": row["currency_name"],
                            "code": row["currency_code"]
                        }
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"]
                }
            )

        return result

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return []

    except KeyError as e:
        print(f"Не найден ключ {e}")
        return []

    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        return []
