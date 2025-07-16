# Проект banking_widget

## Описание

Проект banking_widget позволяет
работать с данными банковских карт.

### Модули
- masks - в модуле реализованы:
Функция маскировки номера банковской карты {get_mask_card_number},
Функция маскировки номера банковского счета {get_mask_account}.
- widget - в модуле реализованы две функции:
Функция {mask_account_card}, которая умеет обрабатывать информацию как
о картах, так и о счетах.
Функция {get_date}, которая принимает на вход строку с датой в формате
'2024-03-11T02:26:18.671407' и возвращает строку с датой в формате
'ДД.ММ.ГГГГ' ('11.03.2024').
- processing - в модуле реализованы функции для обработки транзакций
по дате и статусу операции
- generators - в модуле реализованы функции для работы с массивами
транзакций
- decorators - в модуле реализован декоратор log, который регистрирует
детали выполнения функции
- external_api - в модуле реализована функция convert_currency
для конвертации валют в RUB с помощью Exchange Rates Data API
- utils - в модуле реализована функция get_list_operations, возвращающая
список словарей с данными о финансовых транзакциях из json-файла.


## Установка

Клонируйте репозиторий
```
https://github.com/aleks-stellar/banking_widget.git
```

## Использование

1. Откройте модуль src/processing
2. Вызовите функцию filter_by_state для проверки
ее работоспособности, указав вместо аргумента state_key нужный вам параметр фильтрации:
```
print(filter_by_state(
[
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], state_key
)
)
```

Примечание. Аргумент state_key отвечает за параметр фильтрации state.
По умолчанию "EXECUTED"

3. Вызовите функцию sort_by_date для проверки
ее работоспособности, указав значение параметра reverse_arg True или False:
```
print(sort_by_date(
[
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
], reverse_arg
)
)
```

Примечание. Аргумент reverse_arg отвечает за направление сортировки:
- True: по убыванию (стоит по умолчанию)
- False: по возрастанию

4. Создайте файл .env из копии файла .env.example и замените
значения переменных реальными данными
5. Создайте файл config.py из копии файла config.py.example и замените
значения переменных реальными данными

## Примеры использования

1. При вызове filter_by_state для проверки работоспособности выводится список:

*[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]*

2. При вызове filter_by_state c state_key "CANCELED" выводится

*[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]*

3. При вызове sort_by_date для проверки работоспособности выводится список:

*[{'id': 41428829, 'state': 'EXECUTED','date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]*

2. При вызове sort_by_date c reverse_arg False выводится

*[{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]*

3. Пример использования функции filter_by_currency

```transactions_list = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

usd_transactions = filter_by_currency(transactions_list, "USD")

for i in range(2):
    print(next(usd_transactions))
```

4. Пример использования функции transaction_descriptions

```
descriptions = transaction_descriptions(transactions_list)

for i in range(5):
    print(next(descriptions))
```

5. Пример использования функции card_number_generator

```
for card_number in card_number_generator(1, 5):
    print(card_number)
```

## Тестирование

1. Запуск всех тестов

`pytest`

2. Запуск отчета о покрытии кода тестами

`pytest --cov`

3. Проверка src линтерами

```
flake8 src
mypy src
isort src
```

4. Проверка tests линтерами

```
flake8 tests
mypy tests
isort tests
```