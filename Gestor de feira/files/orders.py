import general_functions

def orders(sale_state,sale_save_file_name):
    while True:
        if "sales" not in sale_state:
            sale_state["sales"] = {}
        if "lists" not in sale_state:
            sale_state["lists"] = {}
        if "items" not in sale_state:
            sale_state["items"] = {}
        if "temp_order" not in sale_state["sales"]:
            sale_state["sales"]["temp_order"] = {}
        if "quantities" not in sale_state["sales"]["temp_order"]:
            sale_state["sales"]["temp_order"]["quantities"] = {}
        if "items" not in sale_state["sales"]["temp_order"]:
            sale_state["sales"]["temp_order"]["items"] = {}
        if "orders" not in sale_state["sales"]:
            sale_state["sales"]["orders"] = {}
        if "order_names" not in sale_state["sales"]:
            sale_state["sales"]["order_names"] = []
        print("======Order manager======")
        if sale_state["sales"]["temp_order"]["items"] == {}:
            print("1 - Create order")
        else:
            print("1 - Continue order")
        print("2 - View orders")
        print("3 - Edit order")
        print("4 - Delete order")
        print("3 - Leave")
        make_choice= general_functions.validation_check_2(5)
        if make_choice == 1:
            while True:
                print("========Manage sales========")
                print("1 - Sell")
                print("2 - leave")
                make_choice = general_functions.validation_check_2(2)
                if make_choice == 1:
                    if len(sale_state["items"]) > 0:
                        while True:
                            print("========Sales========")
                            print("1 - Add item to order")
                            print("2 - Remove item from order")
                            print("3 - Edit item")
                            print("4 - View order")
                            print("5 - Finalize order")
                            if len(sale_state["sales"]["temp_order"]["quantities"]) > 0:
                                print("6 - Cancel order")
                            else:
                                print("6 - Leave")
                            make_choice = general_functions.validation_check_2(6)
                            if make_choice == 1:
                                while True:
                                    print("========Item select to Add========")
                                    print("1 - Select item by name")
                                    print("2 - Select item by class")
                                    print("3 - Select item by id")
                                    print("4 - stop")
                                    make_choice = general_functions.validation_check_2(4)
                                    if make_choice == 1 or make_choice == 2 or make_choice == 3:
                                        continue_path=False
                                        if make_choice == 1:
                                            item_name = input("Write item name:")
                                            if item_name in sale_state["items"]:
                                                continue_path = True
                                            else:
                                                continue_path = False
                                        elif make_choice == 2:
                                            if "items_class" not in sale_state["lists"]:
                                                sale_state["lists"]["items_class"] = []
                                            if len(sale_state["lists"]["items_class"]) > 0:
                                                print("========Select class========")
                                                for i in range(len(sale_state["lists"]["items_class"])):
                                                    print(str(i + 1) + " - " + sale_state["lists"]["items_class"][i])
                                                make_choice = general_functions.validation_check_2(len(sale_state["lists"]["items_class"]))
                                                item_class = sale_state["lists"]["items_class"][make_choice - 1]
                                                sale_state["lists"]["items_class_temp"] = []
                                                for i in sale_state["items"].keys():
                                                    if "item_class" in sale_state["items"][i]:
                                                        if item_class==sale_state["items"][i]["item_class"]:
                                                            sale_state["lists"]["items_class_temp"].append(sale_state["items"][i]["item_name"])
                                                for i in range(len(sale_state["lists"]["items_class_temp"])):
                                                    print(str(i + 1) + " - " + sale_state["lists"]["items_class_temp"][i])
                                                make_choice = general_functions.validation_check_2(len(sale_state["lists"]["items_class_temp"]))
                                                item_name = sale_state["lists"]["items_class_temp"][make_choice - 1]
                                                continue_path = True
                                            else:
                                                continue_path = False
                                        elif make_choice == 3:
                                            print("Write item id")
                                            item_id = general_functions.validation_check()
                                            for i in sale_state["items"].keys():
                                                if "item_id" in sale_state["items"][i]:
                                                    if item_id == sale_state["items"][i]["item_id"]:
                                                        item_name = i
                                                        continue_path = True
                                                        break
                                                    else:
                                                        continue_path = False
                                        if continue_path:
                                            print("Write item quantity")
                                            item_quantity = general_functions.validation_check_2(sale_state["items"]["quantities"][item_name])
                                            item_price = sale_state["items"][item_name]["item_price"] * item_quantity
                                            if item_name not in sale_state["sales"]["temp_order"]["items"]:
                                                sale_state["sales"]["temp_order"]["items"][item_name]={}
                                                sale_state["sales"]["temp_order"]["items"][item_name]["item_name"] = item_name
                                                sale_state["sales"]["temp_order"]["items"][item_name]["item_price"] = item_price
                                                sale_state["sales"]["temp_order"]["quantities"][item_name]=item_quantity
                                                print(item_name + " has been added")
                                                sale_state["items"]["quantities"][item_name] -= item_quantity
                                            else:
                                                sale_state["sales"]["temp_order"]["items"][item_name]["item_price"]+= item_price
                                                sale_state["sales"]["temp_order"]["quantities"][item_name]+= item_quantity
                                                sale_state["items"]["quantities"][item_name] -= item_quantity
                                                print(str(item_quantity) + item_name + "(s) has(have) been added")
                                            general_functions.pause()
                                        else:
                                            print("Item not found or no classes exist")
                                            general_functions.pause()
                                    else:
                                        print("Cancelling")
                                        general_functions.pause()
                                        break
                                    general_functions.save_state(sale_state, sale_save_file_name)
                            elif make_choice == 2:
                                if len(sale_state["sales"]["temp_order"]["items"]) > 0:
                                    print("========Remove from order========")
                                    counter = 1
                                    for i in sale_state["sales"]["temp_order"]["items"].keys():
                                        print(str(counter) + " - " + str(sale_state["sales"]["temp_order"]["items"][i]))
                                        counter += 1
                                    make_choice = general_functions.validation_check_2(len(sale_state["sales"]["temp_order"]))
                                    item_name = list(sale_state["sales"]["temp_order"]["items"])[make_choice - 1]
                                    sale_state["items"]["quantities"][item_name] += sale_state["sales"]["temp_order"]["quantities"][item_name]
                                    del sale_state["sales"]["temp_order"]["items"][item_name]
                                    del sale_state["sales"]["temp_order"]["quantities"][item_name]
                                    print("Order has been removed")
                                    general_functions.pause()
                                else:
                                    print("Add something to remove")
                                    general_functions.pause()
                            elif make_choice == 3:
                                if len(sale_state["sales"]["temp_order"]["items"]) > 0:
                                    counter = 1
                                    for i in sale_state["sales"]["temp_order"]["items"].keys():
                                        print(str(counter) + " - " + str(sale_state["sales"]["temp_order"]["items"][i]))
                                        counter = counter+1
                                    make_choice = general_functions.validation_check_2(counter-1)
                                    item_name = list(sale_state["sales"]["temp_order"]["items"])[make_choice - 1]
                                    while True:
                                        print("======Edit item======")
                                        print("1 - Edit quantity")
                                        print("2 - Leave")
                                        make_choice=general_functions.validation_check_2(2)
                                        if make_choice == 1:
                                            sale_state["items"]["quantities"][item_name]+=sale_state["sales"]["temp_order"]["quantities"][item_name]
                                            sale_state["sales"]["temp_order"]["quantities"][item_name]=0
                                            print("Write new quantity")
                                            sale_state["sales"]["temp_order"]["quantities"][item_name]=general_functions.validation_check_2(sale_state["items"]["quantities"][item_name])
                                            sale_state["items"]["quantities"][item_name]-=sale_state["sales"]["temp_order"]["quantities"][item_name]
                                            sale_state["sales"]["temp_order"]["items"][item_name]["item_price"]=sale_state["items"][item_name]["item_price"]*sale_state["sales"]["temp_order"]["quantities"][item_name]
                                            print("Quantity has been changed")
                                        else:
                                            print("leaving...")
                                            general_functions.pause()
                                            break
                                    general_functions.pause()
                                else:
                                    print("Add something to view")
                                    general_functions.pause()
                            elif make_choice == 4:
                                if len(sale_state["sales"]["temp_order"]["items"]) > 0:
                                    counter = 1
                                    for i in sale_state["sales"]["temp_order"]["items"].keys():
                                        print(str(counter) + " - " + str(sale_state["sales"]["temp_order"]["items"][i]))
                                        counter += 1
                                    general_functions.pause()
                                else:
                                    print("Add something to view")
                                    general_functions.pause()
                            elif make_choice == 5:
                                if len(sale_state["sales"]["temp_order"]["items"]) > 0:
                                    order_name = "order" + str(len(sale_state["sales"]["orders"]) + 1)
                                    sale_state["sales"]["orders"][order_name] = sale_state["sales"]["temp_order"]
                                    sale_state["sales"]["order_names"].append(order_name)
                                    sale_state["sales"]["temp_order"] = {}
                                    sale_state["sales"]["temp_order"]["quantities"] = {}
                                    sale_state["sales"]["temp_order"]["items"] = {}
                                    print("Order has been added")
                                    general_functions.pause()
                                else:
                                    print("Add something to finalize order")
                                    general_functions.pause()
                            else:
                                if len(sale_state["sales"]["temp_order"]["items"]) > 0:
                                    for i in sale_state["sales"]["temp_order"]["items"].keys():
                                        sale_state["items"]["quantities"][i] += sale_state["sales"]["temp_order"]["quantities"][i]
                                    sale_state["sales"]["temp_order"] = {}
                                    print("order cancelled")
                                    general_functions.pause()
                                    break
                                else:
                                    print("leaving...")
                                    general_functions.pause()
                                    break
                            general_functions.save_state(sale_state, sale_save_file_name)
                    else:
                        print("Add items to store before you can access this feature")
                else:
                    print("Leaving...")
                    general_functions.pause()
                    break
        elif make_choice == 2:
            if "sales" not in sale_state:
                sale_state["sales"] = {}
            if "lists" not in sale_state:
                sale_state["lists"] = {}
            if "items" not in sale_state:
                sale_state["items"] = {}
            if "temp_order" not in sale_state["sales"]:
                sale_state["sales"]["temp_order"] = {}
            if "orders" not in sale_state["sales"]:
                sale_state["sales"]["orders"] = {}
            if "order_names" not in sale_state["sales"]:
                sale_state["sales"]["order_names"] = []
            while True:
                if len(sale_state["sales"]["orders"]) > 0:
                    order_print_list = []
                    if len(sale_state["sales"]["orders"]) > 9:
                        counter = 1
                        for i in list(reversed(sale_state["sales"]["orders"].keys()))[:10]:
                            print(str(counter) + " - " + i)
                            counter += 1
                            order_print_list.append(i)
                        print("apple")
                    else:
                        counter = 1
                        for i in reversed(sale_state["sales"]["orders"].keys()):
                            print(str(counter) + " - " + i)
                            counter += 1
                            order_print_list.append(i)
                    make_choice = general_functions.validation_check_2(len(order_print_list))
                    order_select = order_print_list[make_choice - 1]
                    print("========" + order_select + "========")
                    print(" quantity | name | price")
                    for i in sale_state["sales"]["orders"][order_select].keys():
                        print(sale_state["sales"]["orders"][order_select][i])
                    print("Would you like to continue? (y/n)")
                    print("1 - Yes")
                    print("2 - No")
                    make_choice = general_functions.validation_check_2(2)
                    if make_choice == 2:
                        print("leaving")
                        general_functions.pause()
                        break
                    else:
                        print("continuing")
                        general_functions.pause()
                else:
                    print("leaving, no orders inside")
                    break
        elif make_choice == 3:
            print("Write order number")
            order_number=general_functions.validation_check()
            order_name="order"+str(order_number)
            if order_name in sale_state["sales"]["order_names"]:
                sale_state["sales"]["temp_order"]["quantities"]=sale_state["sales"]["orders"][order_name]["quantities"]
                sale_state["sales"]["temp_order"]["items"]=sale_state["sales"]["orders"][order_name]["items"]
                general_functions.save_state(sale_state, sale_save_file_name)
                while True:
                    print("========Sales========")
                    print("1 - Add item to order")
                    print("2 - Remove item from order")
                    print("3 - Edit item")
                    print("4 - View order")
                    print("5 - Save and quit")
                    make_choice = general_functions.validation_check_2(5)
                    if make_choice == 1:
                        while True:
                            print("========Item select to Add========")
                            print("1 - Select item by name")
                            print("2 - Select item by class")
                            print("3 - Select item by id")
                            print("4 - stop")
                            make_choice = general_functions.validation_check_2(4)
                            if make_choice == 1 or make_choice == 2 or make_choice == 3:
                                if make_choice == 1:
                                    item_name = input("Write item name:")
                                    if item_name in sale_state["items"]:
                                        continue_path = True
                                    else:
                                        continue_path = False
                                elif make_choice == 2:
                                    if "items_class" not in sale_state["lists"]:
                                        sale_state["lists"]["items_class"] = []
                                    if len(sale_state["lists"]["items_class"]) > 0:
                                        print("========Select class========")
                                        for i in range(len(sale_state["lists"]["items_class"])):
                                            print(str(i + 1) + " - " + sale_state["lists"]["items_class"][i])
                                        make_choice = general_functions.validation_check_2(len(sale_state["lists"]["items_class"]))
                                        item_class = sale_state["lists"]["items_class"][make_choice - 1]
                                        sale_state["lists"]["items_class_temp"] = []
                                        for i in sale_state["items"].keys():
                                            if item_class == sale_state["items"][i]["item_class"]:
                                                sale_state["lists"]["items_class_temp"].append(sale_state["items"][i]["item_name"])
                                        for i in range(len(sale_state["lists"]["items_class_temp"])):
                                            print(str(i + 1) + " - " + sale_state["lists"]["items_class_temp"][i])
                                        make_choice = general_functions.validation_check_2(len(sale_state["lists"]["items_class_temp"]))
                                        item_name = sale_state["lists"]["items_class_temp"][make_choice - 1]
                                        continue_path = True
                                    else:
                                        continue_path = False
                                elif make_choice == 3:
                                    print("Write item id")
                                    item_id = general_functions.validation_check()
                                    for i in sale_state["items"].keys():
                                        if item_id == sale_state["items"][i]["item_id"]:
                                            item_name = i
                                            continue_path = True
                                            break
                                        else:
                                            continue_path = False
                                if continue_path:
                                    print("Write item quantity")
                                    item_quantity = general_functions.validation_check_2(sale_state["items"]["quantities"][item_name])
                                    item_price = sale_state["items"][item_name]["item_price"] * item_quantity
                                    if item_name not in sale_state["sales"]["temp_order"]["items"]:
                                        sale_state["sales"]["temp_order"]["items"][item_name]["item_name"] = item_name
                                        sale_state["sales"]["temp_order"]["items"][item_name]["item_price"] = item_price
                                        sale_state["sales"]["temp_order"]["quantities"][item_name] = item_quantity
                                        print(item_name + " has been added")
                                        sale_state["items"]["quantities"][item_name] -= item_quantity
                                    else:
                                        sale_state["sales"]["temp_order"]["items"][item_name]["item_price"] += item_price
                                        sale_state["sales"]["temp_order"]["quantities"][item_name] += item_quantity
                                        sale_state["items"]["quantities"][item_name] -= item_quantity
                                        print(str(item_quantity) + item_name + "(s) has(have) been added")
                                    general_functions.pause()
                                else:
                                    print("Item not found or no classes exist")
                                    general_functions.pause()
                            else:
                                print("Cancelling")
                                general_functions.pause()
                                break
                            general_functions.save_state(sale_state, sale_save_file_name)
                    elif make_choice == 2:
                        if len(sale_state["sales"]["temp_order"]["items"]) > 0:
                            print("========Remove from order========")
                            counter = 1
                            for i in sale_state["sales"]["temp_order"]["items"].keys():
                                print(str(counter) + " - " + str(sale_state["sales"]["temp_order"]["items"][i]))
                                counter += 1
                            make_choice = general_functions.validation_check_2(len(sale_state["sales"]["temp_order"]))
                            item_name = list(sale_state["sales"]["temp_order"]["items"])[make_choice - 1]
                            sale_state["items"]["quantities"][item_name] += sale_state["sales"]["temp_order"]["quantities"][item_name]
                            del sale_state["sales"]["temp_order"]["items"][item_name]
                            print("Order has been removed")
                            general_functions.pause()
                        else:
                            print("Add something to remove")
                            general_functions.pause()
                    elif make_choice == 3:
                        if len(sale_state["sales"]["temp_order"]["items"]) > 0:
                            counter = 1
                            for i in sale_state["sales"]["temp_order"]["items"].keys():
                                print(str(counter) + " - " + str(sale_state["sales"]["temp_order"]["items"][i]))
                                counter = counter+1
                            make_choice = general_functions.validation_check_2(counter-1)
                            item_name = list(sale_state["sales"]["temp_order"]["items"])[make_choice - 1]
                            while True:
                                print("======Edit item======")
                                print("1 - Edit quantity")
                                print("2 - Leave")
                                make_choice=general_functions.validation_check_2(2)
                                if make_choice == 1:
                                    sale_state["items"]["quantities"][item_name]+=sale_state["sales"]["temp_order"]["quantities"][item_name]
                                    sale_state["sales"]["temp_order"]["quantities"][item_name]=0
                                    print("Write new quantity")
                                    sale_state["sales"]["temp_order"]["quantities"][item_name]=general_functions.validation_check_2(sale_state["items"]["quantities"][item_name])
                                    sale_state["items"]["quantities"][item_name]-=sale_state["sales"]["temp_order"]["quantities"][item_name]
                                    sale_state["sales"]["temp_order"]["items"][item_name]["item_price"]=sale_state["items"][item_name]["item_price"]*sale_state["sales"]["temp_order"]["quantities"][item_name]
                                    print("Quantity has been changed")
                                else:
                                    print("leaving...")
                                    general_functions.pause()
                                    break
                            general_functions.pause()
                        else:
                            print("Add something to view")
                            general_functions.pause()
                    elif make_choice == 4:
                        if len(sale_state["sales"]["temp_order"]["items"]) > 0:
                            counter = 1
                            for i in sale_state["sales"]["temp_order"]["items"].keys():
                                print(str(counter) + " - " + str(sale_state["sales"]["temp_order"]["items"][i]))
                                counter += 1
                            general_functions.pause()
                        else:
                            print("Add something to view")
                            general_functions.pause()
                    else:
                        if len(sale_state["sales"]["temp_order"]["items"]) > 0:
                            sale_state["sales"]["orders"][order_name] = sale_state["sales"]["temp_order"]
                            sale_state["sales"]["order_names"].append(order_name)
                            sale_state["sales"]["temp_order"] = {}
                            print("Order has been added")
                            general_functions.pause()
                        else:
                            print("Add something to finalize order")
                            general_functions.pause()
                    general_functions.save_state(sale_state, sale_save_file_name)
            else:
                print("order not found...")
                general_functions.pause()
        elif make_choice == 4:
            print("Add order number")
            order_number=general_functions.validation_check_2(len(sale_state["sales"]["orders"]))
            order_name="order"+str(order_number)
            if order_name in sale_state["sales"]["order_names"]:
                del sale_state["sales"]["orders"][order_name]
                sale_state["sales"]["orders"].remove(order_name)
                print("order deleted successfully")
            else:
                print("order not found...")
                general_functions.pause()
        else:
            print("leaving...")
            general_functions.pause()
            break
        general_functions.save_state(sale_state, sale_save_file_name)