from typing import List, Dict

def filter_by_state(
    dicts_list: List[Dict[str, str | int]],
    state_key:str="CANCELED"
) -> List[Dict[str, str | int]]:
    """
    Функция принимает список словарей и проводит его фильтрацию
    по ключу
    """
    filtered_dicts_list = [
        item_dict
        for item_dict in dicts_list
        if item_dict["state"] == state_key
    ]
    return filtered_dicts_list


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
