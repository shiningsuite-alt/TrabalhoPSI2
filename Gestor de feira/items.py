import general_functions

def items(sale_state,sale_save_file_name):
    if "items" not in sale_state:
        sale_state["items" ] ={}
    if "lists" not in sale_state:
        sale_state["lists" ] ={}
    if "items_class" not in sale_state["lists"]:
        sale_state["lists"]["items_class" ] =[]
    while True:
        print("============Stock manager============")
        print("1 - Add product")
        print("2 - Update product")
        print("3 - Delete product")
        print("4 - search product")
        print("5 - Leave")
        make_choice = general_functions.validation_check_2(5)
        if make_choice == 1:
            print("========Add product========")
            item_name = input("Write item Name:")
            item_name = item_name.lower()
            if item_name not in sale_state["items"]:
                sale_state["items"][item_name] = {}
                sale_state["items"][item_name]["item_name"] = item_name
                item_id = 1
                for i in sale_state["items"].keys():
                    if "item_id" in sale_state["items"][i]:
                        if item_id == sale_state["items"][i]["item_id"]:
                            item_id += 1
                sale_state["items"][item_name]["item_id"] = item_id
                print("Write item price")
                item_price = general_functions.validation_check_float()
                sale_state["items"][item_name]["item_price"] = item_price
                print("Write item quantity")
                item_quantity = general_functions.validation_check()
                sale_state["items"]["quantities"][item_name] = item_quantity
                while True:
                    print("Item class")
                    print("1 - Write a new item class")
                    print("2 - Select a preexisting item class")
                    make_choice = general_functions.validation_check_2(2)
                    if make_choice == 1:
                        item_class = input("Write item Class:")
                        item_class = item_class.lower()
                        if item_class not in sale_state["lists"]["items_class"]:
                            sale_state["lists"]["items_class"].append(item_class)
                        break
                    else:
                        if len(sale_state["lists"]["items_class"]) > 0:
                            counter = 1
                            for i in sale_state["lists"]["items_class"]:
                                print(str(counter) + " -  " + i)
                                counter += 1
                            make_choice = general_functions.validation_check_2(len(sale_state["lists"]["items_class"]))
                            item_class = sale_state["lists"]["items_class"][make_choice - 1]
                            break
                        else:
                            print("No preexisting item classes")
                            general_functions.pause()
                sale_state["items"][item_name]["item_class"] = item_class
                print("Added  " + item_name)
                general_functions.pause()
            else:
                print("Item already exists")
                general_functions.pause()
        elif make_choice == 2:
            item_name = input("Write item name:")
            while True:
                if item_name in sale_state["items"]:
                    print("========Update product========")
                    print("1 - Change id")
                    print("2 - Change name")
                    print("3 - Change class")
                    print("4 - Change price")
                    print("5 - Change quantity")
                    print("6 - Leave")
                    make_choice = general_functions.validation_check_2(6)
                    if make_choice == 1:
                        print("IDs are automatically assigned and cannot be changed")
                        general_functions.pause()
                    elif make_choice == 2:
                        new_name = input("Write new item name:")
                        sale_state["items"][new_name] = sale_state["items"][item_name]
                        del sale_state["items"][item_name]
                        sale_state["items"]["quantities"][new_name] = sale_state["items"]["quantities"][item_name]
                        del sale_state["items"]["quantities"][item_name]
                        sale_state["items"][new_name]["item_name"] = new_name
                        item_name = new_name
                        print("Item name has been changed")
                        general_functions.pause()
                    elif make_choice == 3:
                        print("=======Select class=======")
                        for i in range(len(sale_state["lists"]["items_class"])):
                            print(str(i + 1) + " -  " + sale_state["lists"]["items_class"][i])
                        class_select = general_functions.validation_check_2(len(sale_state["lists"]["items_class"]))
                        class_new = sale_state["lists"]["items_class"][class_select - 1]
                        sale_state["items"][item_name]["item_class"] = class_new
                        print("Class has been changed")
                        general_functions.pause()
                    elif make_choice == 4:
                        print("=======Select Price=======")
                        new_price = general_functions.validation_check_float()
                        sale_state["items"][item_name]["item_price"] = new_price
                        print("Price has been changed")
                        general_functions.pause()
                    elif make_choice == 5:
                        print("=======Select Quantity=======")
                        new_quantity = general_functions.validation_check()
                        sale_state["items"]["quantities"][item_name] = new_quantity
                        print("Quantity has been changed")
                        general_functions.pause()
                    else:
                        print("leaving...")
                        general_functions.pause()
                        break
                else:
                    print("Item doesn't exist")
                    general_functions.pause()
                    break
                general_functions.save_state(sale_state, sale_save_file_name)
        elif make_choice == 3:
            while True:
                print("========Remove product========")
                print("1 - Remove by name")
                print("2 - Remove by class")
                print("3 - Remove by id")
                print("4 - Leave")
                make_choice = general_functions.validation_check_2(4)
                if make_choice == 1:
                    item_name = input("Write item Name:")
                    item_name = item_name.lower()
                    if item_name in sale_state["items"]:
                        del sale_state["items"][item_name]
                        del sale_state["items"]["quantities"][item_name]
                        print("Removed " + item_name)
                        general_functions.pause()
                    else:
                        print("Item does not exist")
                        general_functions.pause()
                elif make_choice == 2:
                    if len(sale_state["lists"]["items_class"]) > 0:
                        counter = 1
                        for i in sale_state["lists"]["items_class"]:
                            print(str(counter) + " - " + i)
                            counter += 1
                        make_choice = general_functions.validation_check_2(len(sale_state["lists"]["items_class"]))
                        item_class = sale_state["lists"]["items_class"][make_choice - 1]
                        print("Item Class - " + item_class)
                        sale_state["lists"]["items_class_temp"] = []
                        counter = 1
                        for i in sale_state["items"].keys():
                            if "item_class" in sale_state["items"][i]:
                                if item_class==sale_state["items"][i]["item_class"]:
                                    print(str(counter) + " - " + i)
                                    counter += 1
                                    sale_state["lists"]["items_class_temp"].append(i)
                        if len(sale_state["lists"]["items_class_temp"]) > 0:
                            make_choice = general_functions.validation_check_2(len(sale_state["lists"]["items_class_temp"]))
                            item_name = sale_state["lists"]["items_class_temp"][make_choice - 1]
                            del sale_state["items"][item_name]
                            del sale_state["items"]["quantities"][item_name]
                            print("Removed " + item_name)
                        else:
                            print("No item in this class to remove")
                            print("going back....")
                        general_functions.pause()
                    else:
                        print("No preexisting classes, add class to access this feature")
                        general_functions.pause()
                elif make_choice == 3:
                    item_id = int(input("Write item id:"))
                    failure = True
                    for i in sale_state["items"].keys():
                        if "item_id" in sale_state["items"][i]:
                            if item_id == sale_state["items"][i]["item_id"]:
                                print("Removed " + i)
                                del sale_state["items"][i]
                                del sale_state["items"]["quantities"][i]
                                failure = False
                                general_functions.pause()
                                break
                            else:
                                failure = True
                    if failure:
                        print("Item doesn't exist")
                        general_functions.pause()
                else:
                    print("leaving")
                    general_functions.pause()
                    break
                general_functions.save_state(sale_state, sale_save_file_name)
        elif make_choice == 4:
            while True:
                print("========Search product========")
                print("1 - Search by name")
                print("2 - Search by class")
                print("3 - Search by id")
                print("4 - Leave")
                make_choice = general_functions.validation_check_2(4)
                if make_choice == 1:
                    item_name = input("Write item Name:")
                    item_name = item_name.lower()
                    if item_name in sale_state["items"]:
                        for i in sale_state["items"][item_name].items():
                            print(i)
                        print(sale_state["items"]["quantities"][item_name])
                        general_functions.pause()
                    else:
                        print("Item does not exist")
                        general_functions.pause()
                elif make_choice == 2:
                    if len(sale_state["lists"]["items_class"]) > 0:
                        counter = 1
                        for i in sale_state["lists"]["items_class"]:
                            print(str(counter) + " - " + i)
                            counter += 1
                        make_choice = general_functions.validation_check_2(len(sale_state["lists"]["items_class"]))
                        item_class = sale_state["lists"]["items_class"][make_choice - 1]
                        print("Item Class - " + item_class)
                        sale_state["lists"]["items_class_temp"] = []
                        counter = 1
                        for i in sale_state["items"].keys():
                            if "item_class" in sale_state["items"][i]:
                                if item_class == sale_state["items"][i]["item_class"]:
                                    print(str(counter) + " - " + str(sale_state["items"][i]) + str(sale_state["items"]["quantities"][i]))
                                    counter += 1
                        general_functions.pause()
                    else:
                        print("No preexisting classes, add class to access this feature")
                elif make_choice == 3:
                    print("Write item id")
                    item_id = general_functions.validation_check()
                    failure = True
                    for i in sale_state["items"].keys():
                        if "item_id" in sale_state["items"][i]:
                            if item_id == sale_state["items"][i]["item_id"]:
                                for j in sale_state["items"][i].items():
                                    print(j)
                                print(sale_state["items"]["quantities"][i])
                                failure = False
                                general_functions.pause()
                                break
                            else:
                                failure = True
                    if failure:
                        print("Item doesn't exist")
                        general_functions.pause()
                else:
                    print("leaving")
                    general_functions.pause()
                    break
                general_functions.save_state(sale_state, sale_save_file_name)
        else:
            print("leaving...")
            general_functions.pause()
            break
        general_functions.save_state(sale_state, sale_save_file_name)