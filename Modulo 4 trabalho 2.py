def edit_name_function(list_names,name_edit_select,name_edit,name_list):
    if len(list_names) > 0:
        if name_edit_select.lower() in list_names:
            undo_save_1 = name_edit_select.lower()
            undo_save_2 = name_edit.lower()
            name_index = list_names.index(name_edit_select.lower())
            list_names[name_index] = name_edit.lower()
            undo_index = name_index
            print(name_list+": Name Changed successfully")
            value_undo=4
            return list_names, name_edit_select, name_edit, undo_save_1, undo_save_2, undo_index, value_undo
        else:
            undo_save_1 = ""
            undo_save_2 = ""
            undo_index = 0
            value_undo = 0
            print(name_list+":Name not found")
            return list_names, name_edit_select, name_edit, undo_save_1, undo_save_2, undo_index, value_undo
    else:
        undo_save_1=""
        undo_save_2=""
        undo_index=0
        value_undo=0
        print(name_list+":No names to change")
        return list_names, name_edit_select, name_edit, undo_save_1, undo_save_2, undo_index, value_undo

def undo_edit_name_function(list_names,name_edit_selected,name_edited):
    name_index = list_names.index(name_edit_selected.lower())
    list_names[name_index] = name_edited.lower()
    return list_names, name_edit_selected, name_edited

list_name=""
first_names_cleared = []
middle_names_cleared = []
last_names_cleared = []
all_names_cleared = []
first_names=[]
middle_names=[]
last_names=[]
all_names=[]
big_loop=True
make_choice=0
yes_no_choice=0
name_temp=""
letters=["A","Á","À","Â","Ã","Ä","B","C","Ç","D","E","É","È","Ê","Ë","F","G","H","I","Í","Ì","Î","Ï","J","K","L","M","N","O","Ó","Ò","Õ","Ô","Ö","P","Q","R","S","T","U","Ü","Ú","Ù","Û","V","W","X","Y","Z","a","á","à","â","ã","ä","b","c","ç","d","e","é","è","ê","ë","f","g","h","i","í","ì","î","ï","j","k","l","m","n","o","ó","ò","õ","ô","ö","p","q","r","s","t","u","ü","ú","ù","û","v","w","x","y","z"]
undo_value=0
undo_name=""
undo_list=0
list_select=0
name_search=""
add_loop=True
edit_name_loop=True
remove_name_loop=True
edit_name=""
edit_name_select=""
undo_edit_index=0
undo_edit_index_first=0
undo_edit_index_middle=0
undo_edit_index_last=0
undo_edit_index_all=0
undo_edit=""
undo_edited=""
undo_edit_1=""
undo_edited_1=""
undo_edit_2=""
undo_edited_2=""
undo_edit_3=""
undo_edited_3=""
undo_edit_value=0
relevent_names=False
validation_loop=True

while big_loop:
    print("==========Menu==========")
    print("1 - Add names")
    print("2 - Remove names")
    print("3 - Edit names")
    print("4 - List all name")
    print("5 - Search names")
    print("6 - Undo")
    print("7 - Clear")
    print("8 - Leave")
    while validation_loop:
        try:
            make_choice = int(input("Choice: "))
            break
        except ValueError:
            print("Write a number")
    if make_choice==1:
        while add_loop:
            print("======== Add Names ========")
            print("1 - Add first name")
            print("2 - Add middle name")
            print("3 - Add last name")
            while validation_loop:
                try:
                    make_choice = int(input("Choice: "))
                    break
                except ValueError:
                    print("Write a number")
            name_temp=input("Add name: ")
            while name_temp=="" or not all(char in letters for char in name_temp):
                name_temp = input("Name cannot be blank, contain numbers or symbols, try again: ")
            if make_choice==1:
                if name_temp.lower() in first_names:
                    print("Name already added")
                else:
                    first_names.append(name_temp.lower())
                    print("Name added successfully")
                    undo_value=1
                    undo_name=name_temp.lower()
                    undo_list=1
            elif make_choice==2:
                if name_temp.lower() in middle_names:
                    print("Name already added")
                else:
                    middle_names.append(name_temp.lower())
                    print("Name added successfully")
                    undo_value=1
                    undo_name=name_temp.lower()
                    undo_list=2
            elif make_choice==3:
                if name_temp.lower() in last_names:
                    print("Name already added")
                else:
                    last_names.append(name_temp.lower())
                    print("Name added successfully")
                    undo_value=1
                    undo_name=name_temp.lower()
                    undo_list=3
            print("Would you like to continue:")
            print("1 - Yes")
            print("2 - No")
            yes_no_choice = int(input("Choice: "))
            if yes_no_choice == 1:
                print("OK")
            elif yes_no_choice == 2:
                break
    elif make_choice==2:
        while remove_name_loop:
            print("1 - Remove specific name")
            print("2 - Remove the last name on the list")
            while validation_loop:
                try:
                    make_choice = int(input("Choice: "))
                    break
                except ValueError:
                    print("Write a number")
            print("1 - First names")
            print("2 - Middle names")
            print("2 - Last names")
            while validation_loop:
                try:
                    list_select = int(input("Choice: "))
                    break
                except ValueError:
                    print("Write a number")
            if make_choice==1:
                name_temp=input("Select name: ")
                if list_select==1:
                    if name_temp.lower() in first_names:
                        first_names.remove(name_temp.lower())
                        print("Name Removed successfully")
                        undo_value=2
                        undo_list=3
                    else:
                        print("Name not found")
                elif list_select==2:
                    if name_temp.lower() in middle_names:
                        middle_names.remove(name_temp.lower())
                        print("Name Removed successfully")
                        undo_value=2
                        undo_list=2
                    else:
                        print("Name not found")
                elif list_select==3:
                    if name_temp.lower() in last_names:
                        last_names.remove(name_temp.lower())
                        print("Name Removed successfully")
                        undo_value=2
                        undo_list=3
                    else:
                        print("Name not found")
            elif make_choice==2:
                if list_select==1:
                    if len(first_names)>0:
                        undo_name=first_names.pop()
                        print("Name Removed successfully")
                        undo_value=2
                        undo_list=1
                    else:
                        print("No names to remove")
                if list_select==2:
                    if len(middle_names)>0:
                        undo_name=middle_names.pop()
                        print("Name Removed successfully")
                        undo_value=2
                        undo_list=2
                    else:
                        print("No names to remove")
                if list_select==3:
                    if len(last_names)>0:
                        undo_name=last_names.pop()
                        print("Name Removed successfully")
                        undo_value=2
                        undo_list=3
                    else:
                        print("No names to remove")
            print("Would you like to continue:")
            print("1 - Yes")
            print("2 - No")
            while validation_loop:
                try:
                    yes_no_choice = int(input("Choice: "))
                    break
                except ValueError:
                    print("Write a number")
            if yes_no_choice == 1:
                print("OK")
            elif yes_no_choice == 2:
                break
    elif make_choice==3:
        while edit_name_loop:
            print("===========Edit names===========")
            edit_name_select=input("Select a name you want to change: ")
            edit_name=input("Select what you would like to change the name to: ")
            edit_name_select = edit_name_select.lower()
            edit_name = edit_name.lower()
            print("Which list would you like to change this name from?")
            print("1 - First names")
            print("2 - Middle names")
            print("3 - Last names")
            print("4 - All names")
            make_choice = int(input("Choice: "))
            if make_choice == 1:
                list_name="First names"
                if len(first_names)>0:
                    first_names, edit_name_select, edit_name, undo_edit, undo_edited, undo_edit_index, undo_value= edit_name_function(first_names,edit_name_select,edit_name,list_name)
                    undo_edit_value = 1
                else:
                    print(list_name+": No names to edit")
            elif make_choice == 2:
                list_name="Middle names"
                if len(middle_names)>0:
                    middle_names, edit_name_select, edit_name, undo_edit, undo_edited, undo_edit_index, undo_value= edit_name_function(middle_names,edit_name_select,edit_name,list_name)
                    undo_edit_value = 2
                else:
                    print(list_name+":No names to edit")
            elif make_choice == 3:
                list_name="Last names"
                if len(last_names)>0:
                    last_names, edit_name_select, edit_name, undo_edit, undo_edited, undo_edit_index, undo_value= edit_name_function(last_names,edit_name_select,edit_name,list_name)
                    undo_edit_value = 3
                else:
                    print(list_name+":No names to edit")
            elif make_choice == 4:
                all_names = all_names + first_names
                for i in range(len(middle_names)):
                    if i not in all_names:
                        all_names.append(i)
                for i in range(len(last_names)):
                    if i not in all_names:
                        all_names.append(i)
                if len(first_names)>0:
                    list_name="First names"
                    first_names, edit_name_select, edit_name, undo_edit, undo_edited, undo_edit_index_first,undo_value= edit_name_function(first_names,edit_name_select,edit_name,list_name)
                    # noinspection PyRedeclaration
                    undo_edit_value = 4
                else:
                    list_name="First names"
                    print(list_name+":No names to edit")
                if len(middle_names) > 0:
                    list_name="Middle names"
                    middle_names, edit_name_select, edit_name, undo_edit_1, undo_edited_1, undo_edit_index_middle,undo_value= edit_name_function(middle_names,edit_name_select,edit_name,list_name)
                    # noinspection PyRedeclaration
                    undo_edit_value = 4
                else:
                    list_name="Middle names"
                    print(list_name+":No names to edit")
                if len(last_names) > 0:
                    list_name="Last names"
                    last_names, edit_name_select, edit_name, undo_edit_2, undo_edited_2, undo_edit_index_last,undo_value= edit_name_function(last_names,edit_name_select,edit_name,list_name)
                    # noinspection PyRedeclaration
                    undo_edit_value = 4
                else:
                    list_name="Last names"
                    print(list_name+":No names to edit")
                if len(all_names) > 0:
                    list_name="All names"
                    all_names, edit_name_select, edit_name, undo_edit_3, undo_edited_3, undo_edit_index_last,undo_value= edit_name_function(all_names,edit_name_select,edit_name,list_name)
                    undo_edit_value = 4
                else:
                    list_name="All names"
                    print(list_name+":No names to edit")
            print("Would you like to continue:")
            print("1 - Yes")
            print("2 - No")
            yes_no_choice = int(input("Choice: "))
            if yes_no_choice == 1:
                print("OK")
            elif yes_no_choice == 2:
                break
    elif make_choice==4:
        print("1 - List first names")
        print("2 - List middle names")
        print("3 - List last names")
        print("4 - List all names")
        while validation_loop:
            try:
                make_choice = int(input("Choice: "))
                break
            except ValueError:
                print("Write a number")
        if make_choice == 1:
            first_names.sort()
            print("==========First Name==========")
            for i in range(len(first_names)):
                # noinspection PyTypeHints
                print(first_names[i].capitalize())
        elif make_choice == 2:
            middle_names.sort()
            print("==========Middle Name==========")
            for i in range(len(middle_names)):
                # noinspection PyTypeHints
                print(middle_names[i].capitalize())
        elif make_choice == 3:
            last_names.sort()
            print("==========Last Name==========")
            for i in range(len(last_names)):
                # noinspection PyTypeHints
                print(last_names[i].capitalize())
        elif make_choice == 4:
            all_names = []
            for i in range(len(first_names)):
                all_names.append(first_names[i].lower())
            for i in range(len(middle_names)):
                if middle_names[i].lower() not in all_names:
                    all_names.append(middle_names[i].lower())
            for i in range(len(last_names)):
                if last_names[i].lower() not in all_names:
                    all_names.append(last_names[i].lower())
            print("==========All Names==========")
            for i in range(len(all_names)):
                # noinspection PyTypeHints
                print(str(all_names[i]).capitalize())
            print("Total number of names: " + str(len(all_names)))
    elif make_choice==5:
        print("========Name search========")
        name_search=input("Search name: ")
        while name_search=="" or not all(char in letters for char in name_temp):
            name_search = input("Name cannot be blank, contain numbers or symbols, try again: ")
        all_names = []
        for i in range(len(first_names)):
            all_names.append(first_names[i].lower())
        for i in range(len(middle_names)):
            if middle_names[i].lower() not in all_names:
                all_names.append(middle_names[i].lower())
                #all_names.append(i)
        for i in range(len(last_names)):
            if last_names[i].lower() not in all_names:
                all_names.append(last_names[i].lower())
        all_names.sort()
        relevent_names=False
        for names in range(len(all_names)):
            # noinspection PyTypeHints
            if name_search.lower() in all_names[names].lower():
                # noinspection PyTypeHints
                print(all_names[names].capitalize())
                relevent_names=True
        if relevent_names:
            print("These are all relevent names")
        else:
            print("No names")
    elif make_choice==6:
        if undo_value==1:
            if undo_list==1:
                first_names.pop()
            elif undo_list == 2:
                middle_names.pop()
            elif undo_list == 3:
                last_names.pop()
            print(undo_name.capitalize()+" has been removed")
            undo_value=0
        elif undo_value==2:
            if undo_list==1:
                first_names.append(undo_name)
            elif undo_list == 2:
                middle_names.append(undo_name)
            elif undo_list == 3:
                last_names.append(undo_name)
            print(undo_name.capitalize()+"has been readded")
            undo_value=0
        elif undo_value==3:
            first_names = first_names_cleared
            middle_names = middle_names_cleared
            last_names = last_names_cleared
            all_names = all_names_cleared
            print("Undid clear")
            undo_value=0
        elif undo_value==4:
            if undo_edit_value==1:
                first_names,undo_edit,undo_edited = undo_edit_name_function(first_names,undo_edit,undo_edited)
            elif undo_edit_value==2:
                middle_names,undo_edit,undo_edited = undo_edit_name_function(middle_names,undo_edit,undo_edited)
            elif undo_edit_value==3:
                last_names,undo_edit,undo_edited = undo_edit_name_function(last_names,undo_edit,undo_edited)
            elif undo_edit_value==4:
                if undo_edited!="":
                    first_names,undo_edited,undo_edit = undo_edit_name_function(first_names,undo_edited,undo_edit)
                if undo_edited_1!="":
                    middle_names,undo_edited_1,undo_edit_1 = undo_edit_name_function(middle_names,undo_edited_1,undo_edit_1)
                if undo_edited_2!="":
                    last_names,undo_edited_2,undo_edit_2 = undo_edit_name_function(last_names,undo_edited_2,undo_edit_2)
                if undo_edited_3!="":
                    all_names,undo_edited_3,undo_edit_3 = undo_edit_name_function(all_names,undo_edited_3,undo_edit_3)
            print("Action undone successfully")
            undo_value=0
        elif undo_value==0:
            print("No action to be undone")
    elif make_choice==7:
        print("Are you sure?(Y/n)")
        yes_no=input("Choice: ")
        while yes_no.lower()!="n" and yes_no.lower()!="y" and yes_no.lower()!="" and yes_no.lower()!="no" and yes_no.lower()!="yes":
            yes_no = input("Choose (Y/n): ")
        if yes_no.lower()=="y" or yes_no.lower()=="yes" or yes_no.lower()=="":
            first_names_cleared = first_names
            middle_names_cleared = middle_names
            last_names_cleared = last_names
            all_names_cleared = all_names
            first_names = []
            middle_names = []
            last_names = []
            all_names = []
            undo_value=3
            print("Names cleared")
        else:
            print("Returning...............")
    elif make_choice==8:
        exit()