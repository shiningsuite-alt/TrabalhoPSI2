import json
from GPSI_Module_5_trabalho_1_modified import sales
from pathlib import Path
from tabulate import tabulate

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

def load_state_2(save_file_name):
    if save_file_name.exists():
        with open(save_file_name, "r", encoding="utf-8") as f:
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

state=load_state()

def convert_to_tuple(imported_list):
    imported_list=tuple(imported_list)
    return imported_list

def convert_to_set(imported_list):
    imported_list=set(imported_list)
    return imported_list

def day_time_search(list_name):
    counter = 1
    for i in list_name:
        print(str(counter) + " - " + i)
        counter += 1
    make_choice = validation_check_2(len(list_name))
    day = list_name[make_choice - 1]
    temp_list = []
    for i in state["schedule"]["list_of_days"]:
        for j in state["schedule"]["list_of_time"]:
            if day in state["schedule"][i][j]:
                temp_list.append(state["schedule"][i][j])
    if temp_list:
        print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
        pause()
    else:
        print("Name doesn't exist")

def main():
    convert_to_tuple(state["schedule"]["headers"])
    convert_to_tuple(state["schedule"]["headers_2"])
    convert_to_tuple(state["schedule"]["list_of_days"])
    convert_to_tuple(state["schedule"]["list_of_time"])
    convert_to_set(state["schedule"]["listed_names"])
    while True:
        print("=======Menu=======")
        print("1 - Schedule")
        print("2 - View sellers")
        print("3 - Sales")
        print("4 - Leave")
        make_choice=validation_check_2(4)
        if make_choice==1:
            while True:
                state["schedule"]["print"] = []
                for time in state["schedule"]["list_of_time"]:
                    temp_list = [time]
                    for day in state["schedule"]["list_of_days"]:
                        if len(state["schedule"][day][time]) > 0:
                            temp_list.append("\033[32mFull\033[0m")
                        else:
                            temp_list.append("\033[31mEmpty\033[0m")
                    state["schedule"]["print"].append(temp_list)
                print("=======Schedule=======")
                print("1 - View schedule")
                print("2 - Edit schedule")
                print("3 - Leave")
                make_choice=validation_check_2(3)
                if make_choice==1:
                    print(tabulate(state["schedule"]["print"], headers=state["schedule"]["headers"], tablefmt="grid"))
                    pause()
                elif make_choice==2:
                    print(tabulate(state["schedule"]["print"], headers=state["schedule"]["headers"], tablefmt="grid"))
                    print("Select day")
                    day_select=validation_check_2(5)
                    day=state["schedule"]["list_of_days"][day_select-1]
                    print("Select time")
                    time_select=validation_check_2(9)
                    time=state["schedule"]["list_of_time"][time_select-1]
                    while True:
                        print("========Editing schedule "+day+" "+time+"=======")
                        print("1 - Add event")
                        print("2 - Edit event")
                        print("3 - Remove event")
                        print("4 - Leave")
                        make_choice=validation_check_2(4)
                        if make_choice==1:
                            if len(state["schedule"][day][time])>=1:
                                print("Cannot add more than 1 events per hour")
                                pause()
                            else:
                                counter=1
                                for i in state["schedule"]["list_of_days"]:
                                    for j in state["schedule"]["list_of_time"]:
                                        if state["schedule"][i][j]!=[]:
                                            counter+=1
                                seller_id=counter
                                name=input("Write name of person: ")
                                if name not in state["schedule"]["listed_names"]:
                                    state["schedule"]["listed_names"].add(name)
                                state["schedule"][day][time].append(seller_id)
                                state["schedule"][day][time].append(name.lower())
                                product_type=input("Write type of products: ")
                                state["schedule"][day][time].append(product_type.lower())
                                state["schedule"][day][time].append(time)
                                state["schedule"][day][time].append(day)
                                extra_description=input("Extra description: ")
                                if extra_description=="" or extra_description==" ":
                                    state["schedule"][day][time].append("none")
                                else:
                                    state["schedule"][day][time].append(extra_description.lower())
                                pause()
                        elif make_choice==2:
                            if state["schedule"][day][time]==[]:
                                print("Add an event before editing")
                            else:
                                print("What would you like to change?")
                                print("1 - Day")
                                print("2 - Time")
                                print("3 - Day and time")
                                print("4 - Name")
                                print("5 - Product type")
                                print("6 - Extra description")
                                print("7 - Leave")
                                make_choice=validation_check_2(7)
                                if make_choice==1:
                                    counter=1
                                    for i in state["schedule"]["list_of_days"]:
                                        print(str(counter)+" - "+i)
                                        counter+=1
                                    make_choice=validation_check_2(len(state["schedule"]["list_of_days"]))
                                    new_day=state["schedule"]["list_of_days"][make_choice-1]
                                    state["schedule"][new_day][time]=state["schedule"][day][time]
                                    state["schedule"][day][time]=[]
                                    state["schedule"][new_day][time][4]=new_day
                                    print("Day has been changed from"+ day+" to "+new_day)
                                    pause()
                                elif make_choice==2:
                                    counter=1
                                    for i in state["schedule"]["list_of_time"]:
                                        print(str(counter)+" - "+i)
                                        counter+=1
                                    make_choice=validation_check_2(len(state["schedule"]["list_of_time"]))
                                    new_time=state["schedule"]["list_of_time"][make_choice-1]
                                    state["schedule"][day][new_time]=state["schedule"][day][time]
                                    state["schedule"][day][time]=[]
                                    state["schedule"][day][new_time][3]=new_time
                                    print("Time has been changed from"+ time+" to "+new_time)
                                    pause()
                                elif make_choice==3:
                                    counter = 1
                                    for i in state["schedule"]["list_of_days"]:
                                        print(str(counter) + " - " + i)
                                        counter += 1
                                    make_choice = validation_check_2(len(state["schedule"]["list_of_days"]))
                                    new_day = state["schedule"]["list_of_days"][make_choice - 1]
                                    counter = 1
                                    for i in state["schedule"]["list_of_time"]:
                                        print(str(counter) + " - " + i)
                                        counter += 1
                                    make_choice = validation_check_2(len(state["schedule"]["list_of_time"]))
                                    new_time = state["schedule"]["list_of_time"][make_choice - 1]
                                    state["schedule"][new_day][new_time] = state["schedule"][day][time]
                                    state["schedule"][day][time] = []
                                    print("Time has been changed from" + time + " to " + new_time+" and day has been changed from" + day+" to " + new_day)
                                    state["schedule"][new_day][new_time][4]=new_day
                                    state["schedule"][new_day][new_time][3] = new_time
                                    pause()
                                elif make_choice==4:
                                    new_name=input("Write name of person: ")
                                    if new_name not in state["schedule"]["listed_names"]:
                                        state["schedule"]["listed_names"].add(new_name)
                                    state["schedule"][day][time][1]=new_name
                                    print("Name has been changed")
                                elif make_choice==5:
                                    new_description=input("Write name of person: ")
                                    state["schedule"][day][time][2]=new_description
                                    print("Description has been changed")
                                elif make_choice==6:
                                    new_description=input("Write new description: ")
                                    state["schedule"][day][time][-1]=new_description
                                    print("Description has been changed")
                                else:
                                    print("Leaving...")
                                    pause()
                        elif make_choice==3:
                            if len(state["schedule"][day][time])==0:
                                print("No event at this time")
                                pause()
                            else:
                                for i in state["schedule"]["list_of_days"]:
                                    for j in state["schedule"]["list_of_time"]:
                                        if len(state["schedule"][i][j]) > 0:
                                            if state["schedule"][i][j][0]>state["schedule"][day][time][0]:
                                                state["schedule"][i][j][0]-=1
                                state["schedule"][day][time]=[]
                                print("Removing event...")
                                pause()
                        else:
                            print("Leaving...")
                            pause()
                            break
                        save_state(state)
                else:
                    print("leaving...")
                    pause()
                    break
                save_state(state)
        elif make_choice==2:
            print("========Sellers========")
            print("1 - Search sellers by names")
            print("2 - Search sellers by id")
            print("3 - Search sellers by days")
            print("4 - Search sellers by time")
            print("5 - Search sellers by letters")
            make_choice=validation_check_2(5)
            if make_choice==1:
                name=input("Write name: ")
                name=name.lower()
                if name in state["schedule"]["listed_names"]:
                    for i in state["schedule"]["list_of_days"]:
                        for j in state["schedule"]["list_of_time"]:
                            if name in state["schedule"][i][j]:
                                temp_list=[state["schedule"][i][j]]
                                print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
                                pause()
                else:
                    print("Name doesn't exist")
            elif make_choice==2:
                print("Write student id")
                student_id=validation_check()
                for i in state["schedule"]["list_of_days"]:
                    for j in state["schedule"]["list_of_time"]:
                        if student_id in state["schedule"][i][j]:
                            temp_list=[state["schedule"][i][j]]
                            print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
                            pause()
                            found=True
                            big_break=True
                            break
                        else:
                            found = False
                            big_break = False
                    if big_break:
                        break
                if not found:
                    print("No student found")
            elif make_choice==3:
                day_time_search(state["schedule"]["list_of_days"])
            elif make_choice==4:
                day_time_search(state["schedule"]["list_of_time"])
            elif make_choice==5:
                name = input("Write name: ")
                name=name.lower()
                temp_list=[]
                for i in state["schedule"]["list_of_days"]:
                    for j in state["schedule"]["list_of_time"]:
                        if state["schedule"][i][j]!=[]:
                            if name in state["schedule"][i][j][1]:
                                temp_list.append(state["schedule"][i][j])
                if temp_list:
                    print(tabulate(temp_list, headers=state["schedule"]["headers_2"], tablefmt="grid"))
                    pause()
                else:
                    print("Name doesn't exist")
        elif make_choice==3:
            print("=======Sales=======")
            print("1 - Manage sales of specific store")
            make_choice=validation_check_2(2)
            if make_choice==1:
                if len(state["schedule"]["listed_names"])>0:
                    print("Whose sales would you like to manage?")
                    counter=1
                    for i in state["schedule"]["listed_names"]:
                        print(str(counter)+" - "+i)
                        counter+=1
                    make_choice=validation_check_2(len(state["schedule"]["listed_names"]))
                    temp_list=list(state["schedule"]["listed_names"])
                    file_name=temp_list[make_choice-1]
                    file_name=file_name+".json"
                    sale_save_file = Path("saves") / file_name
                    sales(sale_save_file)
                else:
                    print("No one added to schedule")
        else:
            exit()

main()