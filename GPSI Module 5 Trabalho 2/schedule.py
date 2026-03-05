import functions
from tabulate import tabulate

def schedule_editer(state):
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
        make_choice = functions.validation_check_2(3)
        if make_choice == 1:
            print(tabulate(state["schedule"]["print"], headers=state["schedule"]["headers"], tablefmt="grid"))
            functions.pause()
        elif make_choice == 2:
            print(tabulate(state["schedule"]["print"], headers=state["schedule"]["headers"], tablefmt="grid"))
            print("Select day")
            day_select = functions.validation_check_2(5)
            day = state["schedule"]["list_of_days"][day_select - 1]
            print("Select time")
            time_select = functions.validation_check_2(9)
            time = state["schedule"]["list_of_time"][time_select - 1]
            while True:
                print("========Editing schedule " + day + " " + time + "=======")
                print("1 - Add event")
                print("2 - Edit event")
                print("3 - Remove event")
                print("4 - Leave")
                make_choice = functions.validation_check_2(4)
                if make_choice == 1:
                    if len(state["schedule"][day][time]) >= 1:
                        print("Cannot add more than 1 events per hour")
                        functions.pause()
                    else:
                        counter = 1
                        for i in state["schedule"]["list_of_days"]:
                            for j in state["schedule"]["list_of_time"]:
                                if state["schedule"][i][j]:
                                    counter += 1
                        seller_id = counter
                        name = input("Write name of person: ")
                        if name not in state["schedule"]["listed_names"]:
                            state["schedule"]["listed_names"].add(name)
                        state["schedule"][day][time].append(seller_id)
                        state["schedule"][day][time].append(name.lower())
                        product_type = input("Write type of products: ")
                        state["schedule"][day][time].append(product_type.lower())
                        state["schedule"][day][time].append(time)
                        state["schedule"][day][time].append(day)
                        extra_description = input("Extra description: ")
                        if extra_description == "" or extra_description == " ":
                            state["schedule"][day][time].append("none")
                        else:
                            state["schedule"][day][time].append(extra_description.lower())
                        functions.pause()
                elif make_choice == 2:
                    if not state["schedule"][day][time]:
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
                        make_choice = functions.validation_check_2(7)
                        if make_choice == 1:
                            counter = 1
                            for i in state["schedule"]["list_of_days"]:
                                print(str(counter) + " - " + i)
                                counter += 1
                            make_choice = functions.validation_check_2(len(state["schedule"]["list_of_days"]))
                            new_day = state["schedule"]["list_of_days"][make_choice - 1]
                            if not state["schedule"][new_day][time]:
                                state["schedule"][new_day][time] = state["schedule"][day][time]
                                state["schedule"][day][time] = []
                                state["schedule"][new_day][time][4] = new_day
                                print("Day has been changed from" + day + " to " + new_day)
                            else:
                                print("Day has event already")
                            functions.pause()
                        elif make_choice == 2:
                            counter = 1
                            for i in state["schedule"]["list_of_time"]:
                                print(str(counter) + " - " + i)
                                counter += 1
                            make_choice = functions.validation_check_2(len(state["schedule"]["list_of_time"]))
                            new_time = state["schedule"]["list_of_time"][make_choice - 1]
                            if not state["schedule"][day][new_time]:
                                state["schedule"][day][new_time] = state["schedule"][day][time]
                                state["schedule"][day][time] = []
                                state["schedule"][day][new_time][3] = new_time
                                print("Time has been changed from" + time + " to " + new_time)
                            else:
                                print("Day already has events")
                            functions.pause()
                        elif make_choice == 3:
                            counter = 1
                            for i in state["schedule"]["list_of_days"]:
                                print(str(counter) + " - " + i)
                                counter += 1
                            make_choice = functions.validation_check_2(len(state["schedule"]["list_of_days"]))
                            new_day = state["schedule"]["list_of_days"][make_choice - 1]
                            counter = 1
                            for i in state["schedule"]["list_of_time"]:
                                print(str(counter) + " - " + i)
                                counter += 1
                            make_choice = functions.validation_check_2(len(state["schedule"]["list_of_time"]))
                            new_time = state["schedule"]["list_of_time"][make_choice - 1]
                            if not state["schedule"][new_day][new_time]:
                                state["schedule"][new_day][new_time] = state["schedule"][day][time]
                                state["schedule"][day][time] = []
                                print("Time has been changed from " + time + " to " + new_time + " and day has been changed from" + day + " to " + new_day)
                                state["schedule"][new_day][new_time][4] = new_day
                                state["schedule"][new_day][new_time][3] = new_time
                            else:
                                print("Event in this slot")
                            functions.pause()
                        elif make_choice == 4:
                            new_name = input("Write name of person: ")
                            if new_name not in state["schedule"]["listed_names"]:
                                state["schedule"]["listed_names"].add(new_name)
                            state["schedule"][day][time][1] = new_name
                            print("Name has been changed")
                        elif make_choice == 5:
                            new_description = input("Write name of person: ")
                            state["schedule"][day][time][2] = new_description
                            print("Description has been changed")
                        elif make_choice == 6:
                            new_description = input("Write new description: ")
                            state["schedule"][day][time][-1] = new_description
                            print("Description has been changed")
                        else:
                            print("Leaving...")
                            functions.pause()
                elif make_choice == 3:
                    if len(state["schedule"][day][time]) == 0:
                        print("No event at this time")
                        functions.pause()
                    else:
                        for i in state["schedule"]["list_of_days"]:
                            for j in state["schedule"]["list_of_time"]:
                                if len(state["schedule"][i][j]) > 0:
                                    if state["schedule"][i][j][0] > state["schedule"][day][time][0]:
                                        state["schedule"][i][j][0] -= 1
                        state["schedule"][day][time] = []
                        print("Removing event...")
                        functions.pause()
                else:
                    print("Leaving...")
                    functions.pause()
                    break
                functions.save_state(state)
        else:
            print("leaving...")
            functions.pause()
            break
        functions.save_state(state)