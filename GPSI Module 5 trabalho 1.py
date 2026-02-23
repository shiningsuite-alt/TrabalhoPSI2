import json
from pathlib import Path

save_file= Path("save_state_5_1.json")

default_state = {
    "items":{},
    "lists":{},
    "sales":{}
}

def load_state():
    if save_file.exists():
        with open(save_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return default_state.copy()

def save_state(estado):
    with open(save_file, "w", encoding="utf-8") as f:
        json.dump(estado, f, indent=4)

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

def main():
    while True:
        print("========Menu========")
        print("1 - Manage stock")
        print("2 - Manage sales")
        print("3 - Exit")
        make_choice = validation_check_2(3)
        if make_choice == 1:
            if "items" not in state:
                state["items"]={}
            if "lists" not in state:
                state["lists"]={}
            if "items_class" not in state["lists"]:
                state["lists"]["items_class"]=[]
            while True:
                print("============Stock manager============")
                print("1 - Add product")
                print("2 - Update product")
                print("3 - Delete product")
                print("4 - search product")
                print("5 - Leave")
                make_choice = validation_check_2(5)
                if make_choice == 1:
                    print("========Add product========")
                    item_name = input("Write item Name:")
                    item_name=item_name.lower()
                    if item_name not in state["items"]:
                        item_id = 1
                        for i in state["items"].keys():
                            if item_id==state["items"][i][0]:
                                item_id +=1
                        item_price = float(input("Write item price: "))
                        print("Write item quantity")
                        item_quantity = validation_check()
                        while True:
                            print("Item class")
                            print("1 - Write a new item class")
                            print("2 - Select a preexisting item class")
                            make_choice = validation_check_2(2)
                            if make_choice == 1:
                                item_class = input("Write item Class:")
                                item_class=item_class.lower()
                                state["lists"]["items_class"].append(item_class)
                                break
                            else:
                                if len(state["lists"]["items_class"])>0:
                                    counter=1
                                    for i in state["lists"]["items_class"]:
                                        print(str(counter)+" - "+i)
                                        counter+=1
                                    make_choice = validation_check_2(len(state["lists"]["items_class"]))
                                    item_class=state["lists"]["items_class"][make_choice-1]
                                    break
                                else:
                                    print("No preexisting item classes")
                                    pause()
                        state["items"][item_name]=(item_id, item_name, item_class, item_price, item_quantity)
                        print("Added "+ item_name)
                        pause()
                    else:
                        print("Item already exists")
                        pause()
                elif make_choice == 2:
                    item_name=input("Write item name:")
                    while True:
                        if item_name in state["items"]:
                            print("========Update product========")
                            print("1 - Change id")
                            print("2 - Change name")
                            print("3 - Change class")
                            print("4 - Change price")
                            print("5 - Change quantity")
                            print("6 - Leave")
                            make_choice = validation_check_2(6)
                            if make_choice == 1:
                                print("IDs are automatically assigned and cannot be changed")
                                pause()
                            elif make_choice == 2:
                                temp_list=list(state["items"][item_name])
                                new_name=input("Write new item name:")
                                new_name=new_name.lower()
                                temp_list[1]=new_name
                                state["items"][new_name]=tuple(temp_list)
                                del state["items"][item_name]
                                print("Item name has been changed")
                                pause()
                                item_name=new_name
                            elif make_choice == 3:
                                temp_list = list(state["items"][item_name])
                                print("=======Select class=======")
                                for i in range(len(state["lists"]["items_class"])):
                                    print(str(i+1)+" - "+state["lists"]["items_class"][i])
                                class_select=validation_check_2(len(state["lists"]["items_class"]))
                                class_new=state["lists"]["items_class"][class_select-1]
                                temp_list[2]=class_new
                                state["items"][item_name]=tuple(temp_list)
                                print("Class has been changed")
                                pause()
                            elif make_choice == 4:
                                temp_list = list(state["items"][item_name])
                                print("=======Select Price=======")
                                new_price = float(input("Write new price: "))
                                temp_list[3] = new_price
                                state["items"][item_name] = tuple(temp_list)
                                print("Price has been changed")
                                pause()
                            elif make_choice == 5:
                                temp_list = list(state["items"][item_name])
                                print("=======Select Quantity=======")
                                new_quantity = int(input("Write new quantity: "))
                                temp_list[4] = new_quantity
                                state["items"][item_name] = tuple(temp_list)
                                print("Quantity has been changed")
                                pause()
                            else:
                                print("leaving...")
                                pause()
                                break
                        else:
                            print("Item doesn't exist")
                            pause()
                            break
                        save_state(state)
                elif make_choice == 3:
                    while True:
                        print("========Remove product========")
                        print("1 - Remove by name")
                        print("2 - Remove by class")
                        print("3 - Remove by id")
                        print("4 - Leave")
                        make_choice = validation_check_2(4)
                        if make_choice == 1:
                            item_name = input("Write item Name:")
                            item_name = item_name.lower()
                            if item_name in state["items"]:
                                del state["items"][item_name]
                                print("Removed " + item_name)
                                pause()
                            else:
                                print("Item does not exist")
                                pause()
                        elif make_choice == 2:
                            if len(state["lists"]["items_class"])>0:
                                counter=1
                                for i in state["lists"]["items_class"]:
                                    print(str(counter)+ " - " +i)
                                    counter+=1
                                make_choice = validation_check_2(len(state["lists"]["items_class"]))
                                item_class=state["lists"]["items_class"][make_choice-1]
                                print("Item Class - " +item_class)
                                state["lists"]["items_class_temp"]=[]
                                counter=1
                                for i in state["items"].keys():
                                    if item_class in state["items"][i]:
                                        print(str(counter)+" - "+i)
                                        counter+=1
                                        state["lists"]["items_class_temp"].append(i)
                                make_choice = validation_check_2(len(state["lists"]["items_class_temp"]))
                                item_name=state["lists"]["items_class_temp"][make_choice-1]
                                del state["items"][item_name]
                                print("Removed " + item_name)
                                pause()
                            else:
                                print("No preexisting classes, add class to access this feature")
                                pause()
                        elif make_choice == 3:
                            item_id = int(input("Write item id:"))
                            failure=True
                            for i in state["items"].keys():
                                if item_id==state["items"][i][0]:
                                    print("Removed "+i)
                                    del state["items"][i]
                                    failure=False
                                    pause()
                                    break
                                else:
                                    failure=True
                            if failure:
                                print("Item doesn't exist")
                                pause()
                        else:
                            print("leaving")
                            pause()
                            break
                        save_state(state)
                elif make_choice == 4:
                    while True:
                        print("========Search product========")
                        print("1 - Search by name")
                        print("2 - Search by class")
                        print("3 - Search by id")
                        print("4 - Leave")
                        make_choice = validation_check_2(4)
                        if make_choice == 1:
                            item_name = input("Write item Name:")
                            item_name = item_name.lower()
                            if item_name in state["items"]:
                                print("id   name   class   price   quantity")
                                print(state["items"][item_name])
                                pause()
                            else:
                                print("Item does not exist")
                                pause()
                        elif make_choice == 2:
                            if len(state["lists"]["items_class"])>0:
                                counter=1
                                for i in state["lists"]["items_class"]:
                                    print(str(counter)+ " - " +i)
                                    counter+=1
                                make_choice = validation_check_2(len(state["lists"]["items_class"]))
                                item_class=state["lists"]["items_class"][make_choice-1]
                                print("Item Class - " +item_class)
                                state["lists"]["items_class_temp"]=[]
                                counter=1
                                print("      id   name   class   price   quantity")
                                for i in state["items"].keys():
                                    if item_class in state["items"][i]:
                                        print(str(counter)+" - "+ str(state["items"][i]))
                                        counter+=1
                                pause()
                            else:
                                print("No preexisting classes, add class to access this feature")
                        elif make_choice == 3:
                            print("Write item id")
                            item_id = validation_check()
                            failure=True
                            print("id   name   class   price   quantity")
                            for i in state["items"].keys():
                                if item_id==state["items"][i][0]:
                                    print(str(state["items"][i]))
                                    failure=False
                                    pause()
                                    break
                                else:
                                    failure=True
                            if failure:
                                print("Item doesn't exist")
                                pause()
                        else:
                            print("leaving")
                            pause()
                            break
                        save_state(state)
                else:
                    print("leaving...")
                    pause()
                    break
                save_state(state)
        elif make_choice == 2:
            while True:
                print("========Manage sales========")
                print("1 - Sell")
                print("2 - leave")
                make_choice = validation_check_2(2)
                if make_choice == 1:
                    if len(state["items"])>0:
                        while True:
                            if "sales" not in state:
                                state["sales"]={}
                            if "lists" not in state:
                                state["lists"]={}
                            if "items" not in state:
                                state["items"]={}
                            if "temp_order" not in state["sales"]:
                                state["sales"]["temp_order"]= {}
                            if "orders" not in state["sales"]:
                                state["sales"]["orders"]={}
                            print("========Sales========")
                            print("1 - Add item to order")
                            print("2 - Remove item from order")
                            print("3 - View order")
                            print("4 - Finalize order")
                            print("5 - Cancel order")
                            make_choice = validation_check_2(5)
                            if make_choice == 1:
                                while True:
                                    print("========Item select to Add========")
                                    print("1 - Select item by name")
                                    print("2 - Select item by class")
                                    print("3 - Select item by id")
                                    print("4 - stop")
                                    make_choice = validation_check_2(4)
                                    if make_choice == 1 or make_choice==2 or make_choice==3:
                                        if make_choice==1:
                                            item_name = input("Write item name:")
                                            if item_name in state["items"]:
                                                continue_path=True
                                            else:
                                                continue_path=False
                                        elif make_choice==2:
                                            if "items_class" not in state["lists"]:
                                                state["lists"]["items_class"]=[]
                                            if len(state["lists"]["items_class"])>0:
                                                print("========Select class========")
                                                for i in range(len(state["lists"]["items_class"])):
                                                    print(str(i+1)+ " - " +state["lists"]["items_class"][i])
                                                make_choice = validation_check_2(len(state["lists"]["items_class"]))
                                                item_class = state["lists"]["items_class"][make_choice-1]
                                                state["lists"]["items_class_temp"]=[]
                                                for i in state["items"].keys():
                                                    if item_class in state["items"][i]:
                                                        state["lists"]["items_class_temp"].append(state["items"][i][1])
                                                for i in range(len(state["lists"]["items_class_temp"])):
                                                    print(str(i+1)+" - "+ state["lists"]["items_class_temp"][i])
                                                make_choice = validation_check_2(len(state["lists"]["items_class_temp"]))
                                                item_name = state["lists"]["items_class_temp"][make_choice-1]
                                                continue_path=True
                                            else:
                                                continue_path=False
                                        elif make_choice==3:
                                            print("Write item id")
                                            item_id = validation_check()
                                            for i in state["items"].keys():
                                                if item_id == state["items"][i][0]:
                                                    item_name=i
                                                    continue_path=True
                                                    break
                                                else:
                                                    continue_path=False
                                        if continue_path:
                                            print("Write item quantity")
                                            item_quantity=validation_check_2(state["items"][item_name][4])
                                            item_price=state["items"][item_name][3]*item_quantity
                                            state["sales"]["temp_order"][item_name]=(item_quantity,item_name,item_price)
                                            print(item_name+" has been added")
                                            temp_list = list(state["items"][item_name])
                                            temp_list[4] -= item_quantity
                                            state["items"][item_name] = tuple(temp_list)
                                            pause()
                                        else:
                                            print("Item not found or no classes exist")
                                            pause()
                                    else:
                                        print("Cancelling")
                                        pause()
                                        break
                                    save_state(state)
                            elif make_choice==2:
                                if len(state["sales"]["temp_order"])>0:
                                    print("========Remove from order========")
                                    counter=1
                                    for i in state["sales"]["temp_order"].keys():
                                        print(str(counter)+ " - " + str(state["sales"]["temp_order"][i]))
                                        counter+=1
                                    make_choice = validation_check_2(len(state["sales"]["temp_order"]))
                                    item_name=list(state["sales"]["temp_order"])[make_choice-1]
                                    temp_list = list(state["items"][item_name])
                                    temp_list[4] += state["sales"]["temp_order"][item_name][0]
                                    state["items"][item_name]=tuple(temp_list)
                                    del state["sales"]["temp_order"][item_name]
                                    print("Order has been removed")
                                    pause()
                                else:
                                    print("Add something to remove")
                                    pause()
                            elif make_choice==3:
                                if len(state["sales"]["temp_order"])>0:
                                    counter=1
                                    for i in state["sales"]["temp_order"].keys():
                                        print(str(counter)+ " - " + str(state["sales"]["temp_order"][i]))
                                        counter+=1
                                    pause()
                                else:
                                    print("Add something to view")
                                    pause()
                            elif make_choice==4:
                                if len(state["sales"]["temp_order"])>0:
                                    order_name="order"+str(len(state["sales"]["orders"])+1)
                                    state["sales"]["orders"][order_name]=state["sales"]["temp_order"]
                                    state["sales"]["temp_order"]={}
                                    print("Order has been added")
                                    pause()
                                else:
                                    print("Add something to finalize order")
                                    pause()
                            else:
                                for i in state["sales"]["temp_order"].keys():
                                    state["items"][i][4]+=state["sales"]["temp_order"][i][0]
                                state["sales"]["temp_order"]={}
                                print("order cancelled")
                                pause()
                                break
                            save_state(state)
                    else:
                        print("Add items to store before you can access this feature")
                else:
                    print("Leaving...")
                    pause()
                    break
        else:
            exit()

main()