import json
from pathlib import Path

save_file= Path("save_state_5_2.json")

default_state = {
    "schedule": {
        "headers": [
            "Time",
            "1 - Monday",
            "2 - Tuesday",
            "3 - Wednesday",
            "4 - Thursday",
            "5 - Friday"
        ],
        "headers_2": [
            "Id",
            "Name",
            "Product type",
            "Time",
            "Day",
            "Description"
        ],
        "list_of_days": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        ],
        "list_of_time": [
            "8:00",
            "9:05",
            "10:15",
            "11:25",
            "12:35",
            "13:45",
            "14:50",
            "16:00",
            "17:10"
        ],
        "Monday": {
            "8:00": [],
            "9:05": [],
            "10:15": [],
            "11:25": [],
            "12:35": [],
            "13:45": [],
            "14:50": [],
            "16:00": [],
            "17:10": []
        },
        "Tuesday": {
            "8:00": [],
            "9:05": [],
            "10:15": [],
            "11:25": [],
            "12:35": [],
            "13:45": [],
            "14:50": [],
            "16:00": [],
            "17:10": []
        },
        "Wednesday": {
            "8:00": [],
            "9:05": [],
            "10:15": [],
            "11:25": [],
            "12:35": [],
            "13:45": [],
            "14:50": [],
            "16:00": [],
            "17:10": []
        },
        "Thursday": {
            "8:00": [],
            "9:05": [],
            "10:15": [],
            "11:25": [],
            "12:35": [],
            "13:45": [],
            "14:50": [],
            "16:00": [],
            "17:10": []
        },
        "Friday": {
            "8:00": [],
            "9:05": [],
            "10:15": [],
            "11:25": [],
            "12:35": [],
            "13:45": [],
            "14:50": [],
            "16:00": [],
            "17:10": []
        },
        "listed_names": set(),
        "print": []
    },
    "sales": {}
}

def load_state():
    if save_file.exists():
        with open(save_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return default_state.copy()

def save_state(estado):
    estado["schedule"]["listed_names"]=list(estado["schedule"]["listed_names"])
    with open(save_file, "w", encoding="utf-8") as f:
        json.dump(estado, f, indent=4)
    estado["schedule"]["listed_names"]=set(estado["schedule"]["listed_names"])

def pause():
    wait=input("Press enter to continue...")

def validation_check():
    while True:
        try:
            choice = int(input("Choice: "))
            break
        except ValueError:
            print("Write a number")
    return choice

def validation_check_2(x):
    while True:
        try:
            choice = int(input("Choice: "))
            while choice>x:
                try:
                    choice = int(input("Make a choice that is in range: "))
                except ValueError:
                    print("Write a number")
            break
        except ValueError:
            print("Write a number")
    return choice

def validation_check_3(x,y):
    while True:
        try:
            choice = int(input("Choice: "))
            while y<choice or choice<x:
                try:
                    choice = int(input("Make a choice that is in range: "))
                except ValueError:
                    print("Write a number")
            break
        except ValueError:
            print("Write a number")
    return choice

def convert_to_tuple(imported_list):
    imported_list=tuple(imported_list)
    return imported_list

def convert_to_set(imported_list):
    imported_list=set(imported_list)
    return imported_list
