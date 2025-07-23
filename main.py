from pathlib import Path
from pprint import pprint

from src.utils import get_list_operations
from src.transactions_parser import (read_csv_transactions,
                                     read_excel_transactions)
from src.processing import (
    filter_by_state, sort_by_date, filter_transactions_by_pattern)
from src.generators import filter_by_currency
from src.widget import mask_account_card


def main() -> None:
    """
    Отвечает за основную логику проекта и связывает
    функциональности между собой.
    """
    file_types = [
        {
            1: "Для обработки выбран JSON-файл.",
            "file_type": "JSON",
            "func_to_read": get_list_operations,
            "path_to_file": Path("data", "operations.json")
        },
        {
            2: "Для обработки выбран CSV-файл.",
            "file_type": "CSV",
            "func_to_read": read_csv_transactions,
            "path_to_file": Path("data", "transactions.csv")
        },
        {
            3: "Для обработки выбран XLSX-файл.",
            "file_type": "XLSX",
            "func_to_read": read_excel_transactions,
            "path_to_file": Path("data", "transactions_excel.xlsx")
        }
    ]

    print(
        """\nПривет! Добро пожаловать в программу
работы с банковскими транзакциями.\n"""
    )
    print(
        """Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла\n"""
    )

    file_type_choice = None
    is_file_type_choice_correct = False
    for i in range(3):
        file_type_choice = int(input("Введите число здесь: "))

        if file_type_choice not in [1, 2, 3]:
            print("Введите число, соответствующее"
                  " номеру варианта (1, 2 или 3): ")
        else:
            is_file_type_choice_correct = True
            break

    # Создаем словарь с данными о файле выбранного типа
    if is_file_type_choice_correct:
        file_type_dict = file_types[file_type_choice - 1]

        # Вызов функции, читающей файл с выбранным расширением
        read_transactions_list = (
            file_type_dict["func_to_read"](file_type_dict["path_to_file"])
        )
        print(f"{file_type_dict[file_type_choice]}\n")
    else:
        print("Вы не выбрали вариант ответа. Завершение работы программы.")
        return

    print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

    operations_status_choice = None
    is_status_choice_correct = False

    for i in range(3):
        operations_status_choice = input("Введите статус здесь: ").lower()

        if (operations_status_choice not in
                ["executed", "canceled", "pending"]):
            print(f"\nСтатус операции {operations_status_choice} недоступен. \n"
                  f"Введите статус, по которому необходимо"
                  f" выполнить фильтрацию. \nДоступные для фильтровки статусы: "
                  f"EXECUTED, CANCELED, PENDING.")
        else:
            is_status_choice_correct = True
            break

    if is_status_choice_correct:
        print(f"\nВыбран статус операции {operations_status_choice.upper()}.")

        # Вызов функции, производящей фильтрацию по статусу
        filtered_transactions_list = filter_by_state(
            read_transactions_list, operations_status_choice.upper()
        )
        print(f"Транзакции отфильтрованы по статусу "
              f"{operations_status_choice.upper()}.")
    else:
        print("\nВы не выбрали вариант ответа. Завершение работы программы.")
        return

    print("\nОтсортировать операции по дате? Да/Нет")

    sort_date_choice = None
    is_sort_date_choice_correct = False

    for i in range(3):
        sort_date_choice = input("Введите ответ здесь: ").lower()

        if sort_date_choice not in ["да", "нет"]:
            print("Введите один из двух вариантов ответа (да/нет): ")
        else:
            is_sort_date_choice_correct = True
            break

    if not is_sort_date_choice_correct:
            print(
            "\nВы не выбрали вариант ответа. Завершение работы программы."
            )
            return

    if sort_date_choice == "да":

        print("\nОтсортировать по возрастанию или по убыванию?"
            " (по возрастанию/по убыванию)")

        sort_asc_desc = None
        is_sort_asc_desc_correct = False
        for i in range(3):
            sort_asc_desc = input("Введите Ваш ответ: ").lower()
            if sort_asc_desc not in ["по возрастанию", "по убыванию"]:
                print(
                    "Введите один из двух вариантов ответа "
                    "(по возрастанию/по убыванию): "
                )
            else:
                is_sort_asc_desc_correct = True
                break

            if not is_sort_asc_desc_correct:
                print(
                    "\nВы не выбрали вариант ответа. "
                    "Завершение работы программы."
                )
                return

        # Значение аргумента по умолчанию
        if sort_asc_desc == "по убыванию":
            # Вызов функции, производящей сортировку по дате по убыванию
            sorted_transactions_list = sort_by_date(
                filtered_transactions_list
            )
            print(f"\nТранзакции отсортированы по убыванию.")

        # Значение направления сортировки по возрастанию
        else:
            sorted_transactions_list = sort_by_date(
                filtered_transactions_list,
                sorting_direction=False
            )
            print(f"\nТранзакции отсортированы по возрастанию.")

    else:
        sorted_transactions_list = filtered_transactions_list

    filter_by_rub_choice = None
    is_filter_by_rub_choice_correct = False
    for i in range(3):
        filter_by_rub_choice = input(
            "\nВыводить только рублевые транзакции? (Да/Нет): "
        ).lower()

        if filter_by_rub_choice not in ["да", "нет"]:
            print("Введите один из двух вариантов ответа (да/нет): ")
        else:
            is_filter_by_rub_choice_correct = True
            break

    if not is_filter_by_rub_choice_correct:
        print(
            "\nВы не выбрали вариант ответа. Завершение работы программы."
        )
        return

    # Фильтрация транзакций по рублю
    if filter_by_rub_choice == "да":
        filtered_by_rub_transactions_list = []

        # Инициализация генератора
        filtered_by_rub_transactions_gen = filter_by_currency(
            sorted_transactions_list, "RUB"
        )
        for transaction in filtered_by_rub_transactions_gen:
            filtered_by_rub_transactions_list.append(transaction)

    # Нет фильтрации по рублю - возвращаем предыдущий результат
    else:
        filtered_by_rub_transactions_list = sorted_transactions_list

    filter_by_description_choice = None
    is_filter_by_description_choice_correct = False
    for i in range(3):
        filter_by_description_choice = input(
            "\nОтфильтровать список транзакций по "
            "определенному слову в описании? (Да/Нет): "
        ).lower()

        if filter_by_description_choice not in ["да", "нет"]:
            print("Введите один из двух вариантов ответа (да/нет): ")
        else:
            is_filter_by_description_choice_correct = True
            break

    if not is_filter_by_description_choice_correct:
        print(
            "\nВы не выбрали вариант ответа. Завершение работы программы."
        )
        return

    # Фильтрация транзакций по слову в описании транзакции
    if filter_by_description_choice == "да":
        search_description_string = input(
            "Введите строку для поиска: "
        ).lower()
        filtered_by_description_list = filter_transactions_by_pattern(
            filtered_by_rub_transactions_list,
            search_string=search_description_string
        )
    else:
        filtered_by_description_list = filtered_by_rub_transactions_list

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(filtered_by_description_list)}\n")

    if len(filtered_by_description_list) == 0:
        print("Не найдено ни одной транзакции, "
              "подходящей под ваши условия фильтрации.")
        return

    for my_transaction in filtered_by_description_list:
        print(f"{my_transaction["date"]}", end=" ")
        print(f"{my_transaction["description"]}")

        if "from" in my_transaction and "to" in my_transaction:
            masked_acc_or_card_from = mask_account_card(my_transaction["from"])
            masked_acc_or_card_to = mask_account_card(my_transaction["to"])
            print(f"{masked_acc_or_card_from} -> {masked_acc_or_card_to}")

        elif "from" in my_transaction and "to" not in my_transaction:
            masked_acc_or_card_from = mask_account_card(my_transaction["from"])
            print(f"{masked_acc_or_card_from}")

        elif "from" not in my_transaction and "to" in my_transaction:
            masked_acc_or_card_to = mask_account_card(my_transaction["to"])
            print(f"{masked_acc_or_card_to}")

        else:
            print(f"...")


        print(
            f"Сумма: {my_transaction["operationAmount"]["amount"]}", end=" "
        )
        print(
            f"{my_transaction["operationAmount"]["currency"]["name"]}"
        )
        print("\n")


if __name__ == '__main__':
    main()
