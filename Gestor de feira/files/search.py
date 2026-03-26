import general_functions
from tabulate import tabulate

def search_sellers(state):
    print("========Sellers========")
    print("1 - Search sellers by names")
    print("2 - Search sellers by id")
    print("3 - Search sellers by letters")
    print("4 - Leave")
    make_choice = general_functions.validation_check_2(4)
    temp_list = []
    if make_choice == 1:
        name = input("Write name: ")
        name = name.lower()
        if name in state["schedule"]["listed_names"]:
            for i in state["schedule"]["list_of_days"]:
                for j in state["schedule"]["list_of_time"]:
                    if name in state["schedule"][i][j]:
                        temp_list.append(list(state["schedule"][i][j][name].values()))
                        print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
                        general_functions.pause()
        else:
            print("Name doesn't exist")
    elif make_choice == 2:
        print("Write student id")
        student_id = general_functions.validation_check()
        temp_list = []
        for day in state["schedule"]["list_of_days"]:
            for time in state["schedule"]["list_of_time"]:
                for name in state["schedule"]["listed_names"]:
                    if name in state["schedule"][day][time]:
                        if state["schedule"][day][time][name]["ID"] == student_id:
                            temp_list.append(list(state["schedule"][day][time][name].values()))
        if temp_list:
            print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
        else:
            print("No ID found")
        general_functions.pause()
    elif make_choice == 3:
        name = input("Write name: ")
        name = name.lower()
        temp_list = []
        for day in state["schedule"]["list_of_days"]:
            for time in state["schedule"]["list_of_time"]:
                for name in state["schedule"]["listed_names"]:
                    if name in state["schedule"][day][time]:
                        if name==state["schedule"][day][time][name]["name"]:
                            temp_list.append(state["schedule"][day][time][name].values())
        if temp_list:
            print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
        else:
            print("Name doesn't exist")
        general_functions.pause()
    elif make_choice == 4:
        print("Leaving...")
        general_functions.pause()