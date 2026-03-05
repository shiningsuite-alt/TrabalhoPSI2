import functions
from schedule import schedule_editer
from seller import sales
from search import search_sellers
from pathlib import Path

state=functions.load_state()

def main():
    functions.convert_to_tuple(state["schedule"]["headers"])
    functions.convert_to_tuple(state["schedule"]["headers_2"])
    functions.convert_to_tuple(state["schedule"]["list_of_days"])
    functions.convert_to_tuple(state["schedule"]["list_of_time"])
    functions.convert_to_set(state["schedule"]["listed_names"])
    while True:
        print("=======Menu=======")
        print("1 - Schedule")
        print("2 - View sellers")
        print("3 - Sales")
        print("4 - Leave")
        make_choice=functions.validation_check_2(4)
        if make_choice==1:
            schedule_editer(state)
        elif make_choice==2:
            search_sellers(state)
        elif make_choice==3:
            print("=======Sales=======")
            if len(state["schedule"]["listed_names"])>0:
                print("Whose sales would you like to manage?")
                counter=1
                for i in state["schedule"]["listed_names"]:
                    print(str(counter)+" - "+i)
                    counter+=1
                make_choice=functions.validation_check_2(len(state["schedule"]["listed_names"]))
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