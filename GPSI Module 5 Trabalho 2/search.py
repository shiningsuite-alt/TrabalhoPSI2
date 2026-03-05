import functions
from tabulate import tabulate

def day_time_search(list_name,state):
    counter = 1
    for i in list_name:
        print(str(counter) + " - " + i)
        counter += 1
    make_choice = functions.validation_check_2(len(list_name))
    day = list_name[make_choice - 1]
    temp_list = []
    for i in state["schedule"]["list_of_days"]:
        for j in state["schedule"]["list_of_time"]:
            if day in state["schedule"][i][j]:
                temp_list.append(state["schedule"][i][j])
    if temp_list:
        print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
        functions.pause()
    else:
        print("Name doesn't exist")

def search_sellers(state):
    print("========Sellers========")
    print("1 - Search sellers by names")
    print("2 - Search sellers by id")
    print("3 - Search sellers by days")
    print("4 - Search sellers by time")
    print("5 - Search sellers by letters")
    make_choice = functions.validation_check_2(5)
    if make_choice == 1:
        name = input("Write name: ")
        name = name.lower()
        if name in state["schedule"]["listed_names"]:
            for i in state["schedule"]["list_of_days"]:
                for j in state["schedule"]["list_of_time"]:
                    if name in state["schedule"][i][j]:
                        temp_list = [state["schedule"][i][j]]
                        print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
                        functions.pause()
        else:
            print("Name doesn't exist")
    elif make_choice == 2:
        print("Write student id")
        student_id = functions.validation_check()
        for i in state["schedule"]["list_of_days"]:
            for j in state["schedule"]["list_of_time"]:
                if student_id in state["schedule"][i][j]:
                    temp_list = [state["schedule"][i][j]]
                    print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
                    functions.pause()
                    found = True
                    big_break = True
                    break
                else:
                    found = False
                    big_break = False
            if big_break:
                break
        if not found:
            print("No student found")
    elif make_choice == 3:
        day_time_search(state["schedule"]["list_of_days"],state)
    elif make_choice == 4:
        day_time_search(state["schedule"]["list_of_time"],state)
    elif make_choice == 5:
        name = input("Write name: ")
        name = name.lower()
        temp_list = []
        for i in state["schedule"]["list_of_days"]:
            for j in state["schedule"]["list_of_time"]:
                if state["schedule"][i][j]:
                    if name in state["schedule"][i][j][1]:
                        temp_list.append(state["schedule"][i][j])
        if temp_list:
            print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
            functions.pause()
        else:
            print("Name doesn't exist")