import general_functions
from items import items
from orders import orders
from schedule import schedule_editer
from pathlib import Path

save_file = Path("sellers.json")

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
            "8:00": {},
            "9:05": {},
            "10:15": {},
            "11:25": {},
            "12:35": {},
            "13:45": {},
            "14:50": {},
            "16:00": {},
            "17:10": {}
        },
        "Tuesday": {
            "8:00": {},
            "9:05": {},
            "10:15": {},
            "11:25": {},
            "12:35": {},
            "13:45": {},
            "14:50": {},
            "16:00": {},
            "17:10": {}
        },
        "Wednesday": {
            "8:00": {},
            "9:05": {},
            "10:15": {},
            "11:25": {},
            "12:35": {},
            "13:45": {},
            "14:50": {},
            "16:00": {},
            "17:10": {}
        },
        "Thursday": {
            "8:00": {},
            "9:05": {},
            "10:15": {},
            "11:25": {},
            "12:35": {},
            "13:45": {},
            "14:50": {},
            "16:00": {},
            "17:10": {}
        },
        "Friday": {
            "8:00": {},
            "9:05": {},
            "10:15": {},
            "11:25": {},
            "12:35": {},
            "13:45": {},
            "14:50": {},
            "16:00": {},
            "17:10": {}
        },
        "listed_names": [
        ],
        "print": [
            [
                "8:00",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m"
            ],
            [
                "9:05",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m"
            ],
            [
                "10:15",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m"
            ],
            [
                "11:25",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[32mFull\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m"
            ],
            [
                "12:35",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m"
            ],
            [
                "13:45",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m"
            ],
            [
                "14:50",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m"
            ],
            [
                "16:00",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m"
            ],
            [
                "17:10",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m",
                "\u001b[31mEmpty\u001b[0m"
            ]
        ]
    }
}

default_state_2 = {
    "items":{
        "quantities":{}
    },
    "lists":{},
    "sales":{}
}

state=general_functions.load_state(save_file,default_state)

def main():
    while True:
        print("======Menu======")
        print("1 - Select seller")
        print("2 - Edit seller")
        print("3 - Leave")
        make_choice=general_functions.validation_check_2(3)
        if make_choice == 1:
            name=input("Enter seller's name: ")
            name=name.lower()
            if name in state["schedule"]["listed_names"]:
                file_name=name+".json"
                sale_save_file_name = Path("saves") / file_name
                state_sale=general_functions.load_state(sale_save_file_name,default_state_2)
                while True:
                    print("======= Sales =======")
                    print("1 - Manage stock")
                    print("2 - Manage orders")
                    print("3 - Leave")
                    make_choice=general_functions.validation_check_2(3)
                    if make_choice == 1:
                        items(state_sale, sale_save_file_name)
                    elif make_choice == 2:
                        orders(state_sale,sale_save_file_name)
            else:
                print("Seller does not exist")
        elif make_choice == 2:
            schedule_editer(state,save_file)
        else:
            exit()

main()