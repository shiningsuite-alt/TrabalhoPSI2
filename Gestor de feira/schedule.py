import general_functions
from search import search_sellers
from tabulate import tabulate

def schedule_editer(state,save_file_name):
    while True:
        state["schedule"]["print"] = []
        for time in state["schedule"]["list_of_time"]:
            temp_list = [time]
            for day in state["schedule"]["list_of_days"]:
                if len(state["schedule"][day][time]) == 10:
                    temp_list.append("\033[32mFull\033[0m")
                elif 10 > len(state["schedule"][day][time]) > 0:
                    temp_list.append("\033[93mPartially filled\033[0m")
                else:
                    temp_list.append("\033[31mEmpty\033[0m")
            state["schedule"]["print"].append(temp_list)
        print("=======Schedule=======")
        print("1 - View schedule")
        print("2 - Edit schedule")
        print("3 - Leave")
        make_choice = general_functions.validation_check_2(3)
        if make_choice == 1:
            print(tabulate(state["schedule"]["print"], headers=state["schedule"]["headers"], tablefmt="grid"))
            general_functions.pause()
        elif make_choice == 2:
            print(tabulate(state["schedule"]["print"], headers=state["schedule"]["headers"], tablefmt="grid"))
            print("Select day")
            day_select = general_functions.validation_check_2(5)
            day = state["schedule"]["list_of_days"][day_select - 1]
            print("Select time")
            time_select = general_functions.validation_check_2(9)
            time = state["schedule"]["list_of_time"][time_select - 1]
            while True:
                print("========Editing schedule " + day + " " + time + "=======")
                print("1 - Add seller")
                print("2 - View seller")
                print("3 - Edit seller")
                print("4 - Remove seller")
                print("5 - Leave")
                make_choice = general_functions.validation_check_2(5)
                if make_choice == 1:
                    if len(state["schedule"][day][time]) >= 10:
                        print("Cannot add more than 10 events per hour")
                        general_functions.pause()
                    else:
                        name = input("Write name of person: ")
                        name=name.lower()
                        state["schedule"][day][time][name]={}
                        counter = 1
                        state["schedule"][day][time][name]["ID"] = len(state["schedule"][day][time])
                        state["schedule"][day][time][name]["name"] = name
                        if name not in state["schedule"]["listed_names"]:
                            state["schedule"]["listed_names"].append(name)
                        state["schedule"][day][time][name]["type_of_product"] = input("Write type of products: ")
                        state["schedule"][day][time][name]["time"]=time
                        state["schedule"][day][time][name]["day"]=day
                        extra_description = input("Extra description: ")
                        if extra_description == "" or extra_description == " ":
                            state["schedule"][day][time][name]["extra_description"]="none"
                        else:
                            state["schedule"][day][time][name]["extra_description"]=extra_description
                        general_functions.pause()
                elif make_choice==2:
                    search_sellers(state)
                elif make_choice == 3:
                    name=input("Select seller: ")
                    name=name.lower()
                    if name not in state["schedule"][day][time]:
                        print("Add an event before editing")
                    else:
                        print("What would you like to change?")
                        print("1 - Day")
                        print("2 - Time")
                        print("3 - Name")
                        print("4 - Product type")
                        print("5 - Extra description")
                        print("6 - Leave")
                        make_choice = general_functions.validation_check_2(7)
                        if make_choice == 1:
                            counter = 1
                            for i in state["schedule"]["list_of_days"]:
                                print(str(counter) + " - " + i)
                                counter += 1
                            make_choice = general_functions.validation_check_2(len(state["schedule"]["list_of_days"]))
                            new_day = state["schedule"]["list_of_days"][make_choice - 1]
                            if len(state["schedule"][new_day][time])<10:
                                state["schedule"][new_day][time][name] = state["schedule"][day][time][name]
                                del state["schedule"][day][time][name]
                                state["schedule"][new_day][time][name]["day"] = new_day
                                print("Day has been changed from" + day + " to " + new_day)
                            else:
                                print("this section has 10 events already")
                            general_functions.pause()
                        elif make_choice == 2:
                            counter = 1
                            for i in state["schedule"]["list_of_time"]:
                                print(str(counter) + " - " + i)
                                counter += 1
                            make_choice = general_functions.validation_check_2(len(state["schedule"]["list_of_time"]))
                            new_time = state["schedule"]["list_of_time"][make_choice - 1]
                            if len(state["schedule"][day][new_time])<10:
                                state["schedule"][day][new_time][name] = state["schedule"][day][time][name]
                                del state["schedule"][day][time][name]
                                state["schedule"][day][new_time][name]["time"] = new_time
                                print("Time has been changed from" + time + " to " + new_time)
                            else:
                                print("Time has 10 events already")
                            general_functions.pause()
                        elif make_choice == 3:
                            new_name = input("Write new name of person: ")
                            if new_name not in state["schedule"]["listed_names"]:
                                state["schedule"]["listed_names"].append(new_name)
                            state["schedule"][day][time][new_name] = state["schedule"][day][time][name]
                            del state["schedule"][day][time][name]
                            state["schedule"][day][time][new_name]["name"]=new_name
                            print("Name has been changed")
                        elif make_choice == 4:
                            new_description = input("Write name of person: ")
                            state["schedule"][day][time][name]["type_of_product"] = new_description
                            print("Description has been changed")
                        elif make_choice == 5:
                            new_description = input("Write new description: ")
                            state["schedule"][day][time][name]["extra_description"] = new_description
                            print("Description has been changed")
                        else:
                            print("Leaving...")
                            general_functions.pause()
                elif make_choice == 4:
                    if len(state["schedule"][day][time]) == 0:
                        print("No event at this time")
                        general_functions.pause()
                    else:
                        print("========Remove seller========")
                        print("1 - Remove by ID")
                        print("2 - Remove by Name")
                        print("3 - Leave")
                        make_choice = general_functions.validation_check_2(3)
                        if make_choice == 1:
                            print("Enter ID")
                            id_select = general_functions.validation_check_2(len(state["schedule"][day][time]))
                            for i in state["schedule"][day][time]:
                                if state["schedule"][day][time][i]["ID"] == id_select:
                                    del state["schedule"][day][time][i]
                                    print("Seller has been removed")
                                    found_id=True
                                    break
                                else:
                                    found_id = False
                            if not found_id:
                                print("Id not found")
                            general_functions.pause()
                        elif make_choice == 2:
                            name_select = input("Enter Name: ")
                            name_select=name_select.lower()
                            if name_select in state["schedule"][day][time]:
                                del state["schedule"][day][time][name_select]
                                print("Seller has been removed")
                            else:
                                print("Id not found")
                            general_functions.pause()
                        elif make_choice == 3:
                            print("Leaving...")
                            general_functions.pause()
                            break
                else:
                    print("Leaving...")
                    general_functions.pause()
                    break
                general_functions.save_state(state,save_file_name)
        else:
            print("leaving...")
            general_functions.pause()
            break
        general_functions.save_state(state,save_file_name)