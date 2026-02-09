import json
from pathlib import Path

save_file= Path("save_state.json")

default_state = {
    "classes":{
    },
    "grades" :{
    },
    "faltas":{
    }
}

def validation_check(x):
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

def validation_check_2(x,y):
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

class_name=""
subjects=["Ingles","Fisico-quimica","Matematica","Programação de sitemas informaticas","Arc-compra","Area de integração","Portuguêse","TIC","Educação Fisica","Ciencias-Naturais","Espanhol","Arte","CEDarte","Historia","Geografia","Cidadania","Redes","Sistema operativo","ExpCorDraMus","ExpPlastica","GA/A","GA/I","HCArtes","LEFinceira","Markting","PsicoSoc","Saudeinf","Sociolgia","TCRL","TPIEduc","ComunicarFr","OTEturistica","Psicologica","TeCATur","Turis-IAT","Bio-geo","Filosofia","Apl.inform.1","Biologica","Fisica","Economica","Frances","MACS"]

state=load_state()

while True:
    print("=========Menu=========")
    print("What would you like to do?")
    print("1 - Select class")
    print("2 - Edit classes")
    print("3 - Leave")
    make_choice=validation_check(3)
    if make_choice==1:
        if save_file.exists() and len(state["classes"].keys())>0:
            print("==========Classes==========")
            counter=0
            for i in state["classes"]:
                print(str(counter+1) + " - " + i)
                counter+=1
            list_of_classes=list(state["classes"].keys())
            classes_choice=validation_check(len(state["classes"]))
            while True:
                print("=============="+list_of_classes[classes_choice-1]+"==============")
                class_name=list_of_classes[classes_choice-1]
                print("1 - Add student")
                print("2 - Remove student")
                print("3 - view all students")
                print("4 - Edit student")
                print("5 - Leave")
                make_choice=validation_check(5)
                if make_choice==1:
                    print("=========Add student=========")
                    student_name=input("Write a students name: ")
                    student_name=student_name.lower()
                    if student_name.lower() not in state["classes"][class_name]:
                        print("Adding "+ student_name)
                        state["classes"][class_name].append(student_name)
                        state["grades"][class_name][student_name] = {}
                        state["faltas"][class_name][student_name] = {}
                        pause()
                    else:
                        print("Student already exists")
                        pause()
                elif make_choice==2:
                    print("=========Remove student=========")
                    student_name=input("Write a students name: ")
                    student_name.lower()
                    if student_name in state["classes"][class_name]:
                        print("Removing "+ student_name)
                        state["classes"][class_name].remove(student_name)
                        title=class_name+" , "+student_name
                        del state["grades"][class_name][student_name]
                        del state["faltas"][class_name][student_name]
                        pause()
                    else:
                        print("Student doesn't exist")
                        pause()
                elif make_choice==3:
                    print("========="+class_name+" students=========")
                    counter=0
                    state["classes"][class_name].sort()
                    for i in state["classes"][class_name]:
                        print(str(counter+1)+" - "+i.capitalize())
                        counter+=1
                    pause()
                elif make_choice==4:
                    print("=========Student select=========")
                    student_name=input("Write a students name: ")
                    student_name=student_name.lower()
                    if student_name in state["classes"][class_name]:
                        while True:
                            print("============="+student_name.capitalize()+"=============")
                            print("1 - Evaluations")
                            print("2 - Absences")
                            print("3 - Grades")
                            print("4 - Leave")
                            make_choice=validation_check(4)
                            counter = 0
                            select=[]
                            subjects_selected=[]
                            if make_choice!=4:
                                if "1-A (GPSI)" in class_name:
                                    select=[0,1,2,3,4,5,6,7,8]
                                    for i in [subjects[i] for i in select]:
                                        subjects_selected.append(i)
                                elif "2-A (GPSI)" in class_name or "3-A (GPSI)" in class_name:
                                    select=[0,1,2,3,17,5,6,16,8]
                                    for i in [subjects[i] for i in select]:
                                        subjects_selected.append(i)
                                elif "CT" in class_name:
                                    if "12" in class_name:
                                        if "CTA" in class_name:
                                            select=[2,6,32,39,37,8]
                                            for i in [subjects[i] for i in select]:
                                                subjects_selected.append(i)
                                        else:
                                            select=[2,6,32,38,37,8]
                                            for i in [subjects[i] for i in select]:
                                                subjects_selected.append(i)
                                    elif "CTE" in class_name:
                                        select = [35, 40, 8,36,1,14,0,2,6]
                                        for i in [subjects[i] for i in select]:
                                            subjects_selected.append(i)
                                    else:
                                        select = [35, 8,36,1,14,0,2,6]
                                        for i in [subjects[i] for i in select]:
                                            subjects_selected.append(i)
                                elif "LH" in class_name:
                                    if "12" in class_name:
                                        select=[6,32,27,13,8]
                                        for i in [subjects[i] for i in select]:
                                                subjects_selected.append(i)
                                    elif "11" in class_name:
                                        select=[6,42,0,13,14,36,8]
                                        for i in [subjects[i] for i in select]:
                                                subjects_selected.append(i)
                                    else:
                                        select=[6,42,0,13,41,36,8]
                                        for i in [subjects[i] for i in select]:
                                                subjects_selected.append(i)
                                elif "CSE" in class_name:
                                    if "12" in class_name:
                                        select=[6,8,2,40,27]
                                        for i in [subjects[i] for i in select]:
                                                subjects_selected.append(i)
                                    elif "11" in class_name:
                                        select=[6,8,2,36,0,40,13]
                                        for i in [subjects[i] for i in select]:
                                                subjects_selected.append(i)
                                    else:
                                        select=[6,8,2,36,14,0,40,13]
                                        for i in [subjects[i] for i in select]:
                                                subjects_selected.append(i)
                                elif "TAE" in class_name:
                                    if "12" in class_name:
                                        select = [5,30,8,18,19,14,0,31,6,32,26,33,29,34]
                                        for i in [subjects[i] for i in select]:
                                            subjects_selected.append(i)
                                    elif "11" in class_name:
                                        select = [5,30,8,18,19,14,22,0,31,6,32,26,27,33,29,34]
                                        for i in [subjects[i] for i in select]:
                                            subjects_selected.append(i)
                                    else:
                                        select = [5,8,18,19,20,21,22,0,23,24,2,6,25,26,27,28,29,]
                                        for i in [subjects[i] for i in select]:
                                            subjects_selected.append(i)
                                else:
                                    select=[15,14,13,12,11,10,9,8,7,6,3,1,0]
                                    for i in [subjects[i] for i in select]:
                                        subjects_selected.append(i)
                                for i in range(len(subjects_selected)):
                                    print(str(counter + 1) + " - " + str(subjects_selected[i]))
                                    counter += 1
                                subject_number = validation_check(len(subjects_selected))
                                subject=subjects_selected[subject_number-1]
                                if subject not in state["grades"][class_name][student_name]:
                                    state["grades"][class_name][student_name][subject]= {}
                            if make_choice==1:
                                while True:
                                    if "evaluations" not in state["grades"][class_name][student_name][subject]:
                                        state["grades"][class_name][student_name][subject]["evaluations"]= []
                                    print("=============" + student_name.capitalize() + " "+ subject+ " Evaluations=============")
                                    print("1 - Add evaluation")
                                    print("2 - Remove evaluation")
                                    print("3 - Edit evaluation")
                                    print("4 - View evaluation")
                                    print("5 - Leave")
                                    make_choice=validation_check(5)
                                    if make_choice==1:
                                        print("Type in the grade you want to add")
                                        evaluation=validation_check_2(0,100)
                                        state["grades"][class_name][student_name][subject]["evaluations"].append(evaluation)
                                        print("Evaluation has been added")
                                    elif make_choice==2:
                                        if len(state["grades"][class_name][student_name][subject]["evaluations"])>0:
                                            counter=0
                                            for i in state["grades"][class_name][student_name][subject]["evaluations"]:
                                                print(str(counter+1) + " - " + str(i))
                                                counter+=1
                                            make_choice=validation_check(len(state["grades"][class_name][student_name][subject]["evaluations"]))
                                            del state["grades"][class_name][student_name][subject]["evaluations"][make_choice-1]
                                            print("Evaluation has been removed")
                                        else:
                                            print("Add a grade to remove")
                                    elif make_choice==3:
                                        if len(state["grades"][class_name][student_name][subject]["evaluations"]) > 0:
                                            counter = 0
                                            for i in state["grades"][class_name][student_name][subject]["evaluations"]:
                                                print(str(counter + 1) + " - " + str(i))
                                                counter += 1
                                            make_choice = validation_check(len(state["grades"][class_name][student_name][subject]["evaluations"]))
                                            state["grades"][class_name][student_name][subject]["evaluations"].pop(make_choice-1)
                                            print("Evaluation has been removed, add new evaluation")
                                            evaluation=validation_check_2(0,100)
                                            state["grades"][class_name][student_name][subject]["evaluations"].append(evaluation)
                                            print("Evaluation has been added")
                                        else:
                                            print("Add a grade to remove")
                                    elif make_choice==4:
                                        if len(state["grades"][class_name][student_name][subject]["evaluations"])>0:
                                            counter=0
                                            for i in state["grades"][class_name][student_name][subject]["evaluations"]:
                                                print(str(counter+1) + " - " + str(i))
                                                counter+=1
                                        else:
                                            print("Add a grade to View")
                                    else:
                                        save_state(state)
                                        break
                                    save_state(state)
                            elif make_choice==2:
                                while True:
                                    if subject not in state["faltas"][class_name][student_name]:
                                        state["faltas"][class_name][student_name][subject] = {}
                                    if "material_absence" not in state["faltas"][class_name][student_name][subject]:
                                        state["faltas"][class_name][student_name][subject]["material_absence"] = 0
                                    if "unjustified_absence" not in state["faltas"][class_name][student_name][subject]:
                                        state["faltas"][class_name][student_name][subject]["unjustified_absence"] = []
                                    if "justified_absence" not in state["faltas"][class_name][student_name][subject]:
                                        state["faltas"][class_name][student_name][subject]["justified_absence"] = []
                                    if "disciplinary_absence" not in state["faltas"][class_name][student_name][subject]:
                                        state["faltas"][class_name][student_name][subject]["disciplinary_absence"] = []
                                    save_state(state)
                                    print("=============="+student_name+" "+subject+" Absences============")
                                    print("1 - Absences of material")
                                    print("2 - Unjustified absence")
                                    print("3 - disciplinary absence")
                                    print("4 - Justified absence")
                                    print("5 - View absences")
                                    print("6 - Leave")
                                    make_choice=validation_check(6)
                                    if make_choice==1:
                                        while True:
                                            if "material_absence" in state["faltas"][class_name][student_name][subject]:
                                                state["faltas"][class_name][student_name][subject]["material_absence"] += 1
                                                print("Absence of material:"+ str(state["faltas"][class_name][student_name][subject]["material_absence"]))
                                                pause()
                                                break
                                            else:
                                                state["faltas"][class_name][student_name][subject]["material_absence"] = 0
                                    elif make_choice==2:
                                        print("Enter the date (DD/mm/yyyy)")
                                        day=validation_check_2(0,30)
                                        print("Enter the month (dd/MM/yyyy)")
                                        month=validation_check_2(0,12)
                                        print("Enter the year (dd/mm/YYYY)")
                                        year=validation_check_2(2025,2026)
                                        date=str(day)+"/"+str(month)+"/"+str(year)
                                        state["faltas"][class_name][student_name][subject]["unjustified_absence"].append(date)
                                        print("Absences has been added")
                                    elif make_choice==3:
                                        disciplinary_absence=input("Enter the reason of the absence:")
                                        state["faltas"][class_name][student_name][subject]["disciplinary_absence"].append(disciplinary_absence)
                                    elif make_choice==4:
                                        print("Enter the date (DD/mm/yyyy)")
                                        day=validation_check_2(0,30)
                                        print("Enter the month (dd/MM/yyyy)")
                                        month=validation_check_2(0,12)
                                        print("Enter the month (dd/mm/YYYY)")
                                        year=validation_check_2(2025,2026)
                                        date=str(day)+"/"+str(month)+"/"+str(year)
                                        if date in state["faltas"][class_name][student_name][subject]["unjustified_absence"]:
                                            state["faltas"][class_name][student_name][subject]["unjustified_absence"].remove(date)
                                            state["faltas"][class_name][student_name][subject]["justified_absence"].append(date)
                                            print("Absence justified")
                                        else:
                                            print("No absence to justify")
                                    elif make_choice==5:
                                        while True:
                                            print("============================================")
                                            print("1 - Absences of material")
                                            print("2 - Unjustified absence")
                                            print("3 - disciplinary absence")
                                            print("4 - Justified absence")
                                            print("5 - View all absences")
                                            print("6 - Leave")
                                            make_choice=validation_check(6)
                                            if make_choice==1:
                                                if "material_absence" in state["faltas"][class_name][student_name][subject]:
                                                    print("Absences of materials: " + str(state["faltas"][class_name][student_name][subject]["material_absence"]))
                                                    pause()
                                            elif make_choice==2:
                                                if len(state["faltas"][class_name][student_name][subject]["unjustified_absence"])>0:
                                                    print("Unjustified absences")
                                                    for i in state["faltas"][class_name][student_name][subject]["unjustified_absence"]:
                                                        print(i)
                                                    pause()
                                                else:
                                                    print("No Unjustified absences")
                                                    pause()
                                            elif make_choice==3:
                                                if len(state["faltas"][class_name][student_name][subject]["disciplinary_absence"])>0:
                                                    print("disciplinary absences")
                                                    for i in state["faltas"][class_name][student_name][subject]["disciplinary_absence"]:
                                                        print(i)
                                                    pause()
                                                else:
                                                    print("No disciplinary absences")
                                                    pause()
                                            elif make_choice==4:
                                                if len(state["faltas"][class_name][student_name][subject]["justified_absence"])>0:
                                                    print("justified absences")
                                                    for i in state["faltas"][class_name][student_name][subject]["justified_absence"]:
                                                        print(i)
                                                    pause()
                                                else:
                                                    print("No Justified absences")
                                                    pause()
                                            elif make_choice==5:
                                                print("Absences of materials: "+ str(state["faltas"][class_name][student_name][subject]["material_absence"]))
                                                print("Unjustified absence: " + str(len(state["faltas"][class_name][student_name][subject]["unjustified_absence"])))
                                                print("disciplinary absence: " + str(len(state["faltas"][class_name][student_name][subject]["disciplinary_absence"])))
                                                print("Justified absence: " + str(len(state["faltas"][class_name][student_name][subject]["justified_absence"])))
                                                pause()
                                            elif make_choice==6:
                                                print("Leaving.......")
                                                break
                                    else:
                                        break
                                    save_state(state)
                            elif make_choice==3:
                                media=0
                                if subject not in state["grades"][class_name][student_name]:
                                    state["grades"][class_name][student_name][subject]={}
                                    state["grades"][class_name][student_name][subject]["Grades"] = 0
                                if "evaluations" in state["grades"][class_name][student_name][subject]:
                                    for i in state["grades"][class_name][student_name][subject]["evaluations"]:
                                        media+=i
                                    media=media/len(state["grades"][class_name][student_name][subject]["evaluations"])
                                    print("Média: " + str(media))
                                    state["grades"][class_name][student_name][subject]["Grades"] = media
                                else:
                                    print("No evaluations")
                                save_state(state)
                            else:
                                break
                            save_state(state)
                    else:
                        print("No student with this name in this class")
                        pause()
                elif make_choice==5:
                    print("leaving....")
                    break
                save_state(state)
        else:
            print("No classes")
            pause()
    elif make_choice==2:
        while True:
            print("========Class edit========")
            print("What would you like to do?")
            print("1 - Add class")
            print("2 - list classes")
            print("3 - Remove class")
            print("4 - Clear all classes")
            print("5 - Leave class")
            make_choice=validation_check(5)
            if make_choice==1:
                print("======Add class======")
                print("Write the class number")
                class_number=validation_check_2(5,12)
                if class_number==10:
                    print("1 - Professional course")
                    print("2 - Regular course")
                    course_type=validation_check(2)
                    if course_type==1:
                        print("Which course")
                        print("1 - GPSI")
                        print("2 - TAE/CMRPP")
                        course_choice=validation_check(2)
                        if course_choice==1:
                            class_name="10 (1-A (GPSI))"
                        elif course_choice==2:
                            class_name="10 (1-B (TAE/CMRPP))"
                            if class_name in state["classes"]:
                                class_name="10 (1-C (TAE/CMRPP))"
                    else:
                        print("Which course")
                        print("1 - Ciências e tecnologias")
                        print("2 - Linguas e Humanidades")
                        print("3 - Ciências socioeconomicas")
                        course_choice=validation_check(3)
                        if course_choice==1:
                            course_name="(CT)"
                        elif course_choice==2:
                            course_name="(LH)"
                        else:
                            course_name="(CSE)"
                        class_section = input("Write your class section: ")
                        while len(class_section)>1:
                            class_section = input("single letter please: ")
                        class_name=str(class_number)+" - "+ class_section.upper() + course_name
                elif class_number==11:
                    print("1 - Professional course")
                    print("2 - Regular course")
                    course_type=validation_check(2)
                    if course_type==1:
                        print("Which course")
                        print("1 - GPSI")
                        print("2 - TAE/TUR")
                        course_choice=validation_check(2)
                        if course_choice==1:
                            class_name="11 (2-A (GPSI))"
                        elif course_choice==2:
                            class_name="11 (2-B (TAE/TUR))"
                            if class_name in state["classes"]:
                                class_name="11 (2-C (TAE/TUR))"
                    else:
                        print("Which course")
                        print("1 - Ciências e tecnologias")
                        print("2 - Ciências e tecnologias e Economicas")
                        print("3 - Linguas e Humanidades")
                        print("4 - Ciências socioeconomicas")
                        course_choice=validation_check(4)
                        if course_choice==1:
                            course_name="(CT)"
                        elif course_choice==2:
                            course_name="(CTE)"
                        elif course_choice==3:
                            course_name="(LH)"
                        else:
                            course_name="(CSE)"
                        class_section = input("Write your class section: ")
                        while len(class_section)>1:
                            class_section = input("single letter please: ")
                        class_name=str(class_number)+" - "+ class_section.upper() + course_name
                elif class_number==12:
                    print("1 - Professional course")
                    print("2 - Regular course")
                    course_type=validation_check(2)
                    if course_type==1:
                        print("Which course")
                        print("1 - GPSI")
                        print("2 - TAE/TUR")
                        course_choice=validation_check(2)
                        if course_choice==1:
                            class_name="12 (3-A (GPSI))"
                        elif course_choice==2:
                            class_name="12 (3-B (TAE/TUR))"
                            if class_name in state["classes"]:
                                class_name="12 (3-C (TAE/TUR))"
                    else:
                        print("Which course")
                        print("1 - Ciências e tecnologias")
                        print("2 - Ciências e tecnologias Articulado")
                        print("3 - Linguas e Humanidades")
                        print("4 - Linguas e Humanidades Articulado")
                        print("5 - Ciências Socio-Económicas")
                        course_choice=validation_check(5)
                        if course_choice==1:
                            course_name="(CT)"
                        elif course_choice==2:
                            course_name="(CTA)"
                        elif course_choice==3:
                            course_name="(LH)"
                        elif course_choice==4:
                            course_name="(LHA)"
                        else:
                            course_name="(CSE)"
                        class_section = input("Write your class section: ")
                        while len(class_section)>1:
                            class_section = input("single letter please: ")
                        class_name=str(class_number)+" - "+ class_section.upper() + course_name
                else:
                    class_section = input("Write your class section: ")
                    while len(class_section)>1:
                        class_section = input("single letter please: ")
                    class_name=str(class_number)+" - "+ class_section.upper()
                if class_name not in state["classes"]:
                    print("Adding class " + class_name)
                    state["classes"][class_name]=[]
                    state["grades"][class_name]= {}
                    state["faltas"][class_name]= {}
                    save_state(state)
                    pause()
                else:
                    print("Class already exists")
                    pause()
            elif make_choice==2:
                if len(state["classes"])<=0:
                    print("No classes to list")
                    pause()
                else:
                    for i in state["classes"]:
                        print(i)
                    pause()
            elif make_choice==3:
                print("======Remove class======")
                print("Write the class number")
                class_number=validation_check(12)
                if class_number==10:
                    print("1 - Professional course")
                    print("2 - Regular course")
                    course_type=validation_check(2)
                    if course_type==1:
                        print("Which course")
                        print("1 - GPSI")
                        print("2 - TAE/CMRPP")
                        course_choice=validation_check(2)
                        if course_choice==1:
                            class_name="10 (1-A (GPSI))"
                        elif course_choice==2:
                            class_name="10 (1-B (TAE/CMRPP))"
                            if class_name in state["classes"]:
                                class_name="10 (1-C (TAE/CMRPP))"
                    else:
                        print("Which course")
                        print("1 - Ciências e tecnologias")
                        print("2 - Linguas e Humanidades")
                        print("3 - Ciências socioeconomicas")
                        course_choice=validation_check(3)
                        if course_choice==1:
                            course_name="(CT)"
                        elif course_choice==2:
                            course_name="(LH)"
                        else:
                            course_name="(CSE)"
                        class_section = input("Write your class section: ")
                        while len(class_section)>1:
                            class_section = input("single letter please: ")
                        class_name=str(class_number)+" - "+ class_section.upper() + course_name
                elif class_number==11:
                    print("1 - Professional course")
                    print("2 - Regular course")
                    course_type=validation_check(2)
                    if course_type==1:
                        print("Which course")
                        print("1 - GPSI")
                        print("2 - TAE/TUR")
                        course_choice=validation_check(2)
                        if course_choice==1:
                            class_name="10 (1-A (GPSI))"
                        elif course_choice==2:
                            class_name="10 (1-B (TAE/TUR))"
                            if class_name in state["classes"]:
                                class_name="10 (1-C (TAE/TUR))"
                    else:
                        print("Which course")
                        print("1 - Ciências e tecnologias")
                        print("2 - Ciências e tecnologias e Economicas")
                        print("3 - Linguas e Humanidades")
                        print("4 - Ciências socioeconomicas")
                        course_choice=validation_check(4)
                        if course_choice==1:
                            course_name="(CT)"
                        elif course_choice==2:
                            course_name="(CTE)"
                        elif course_choice==3:
                            course_name="(LH)"
                        else:
                            course_name="(CSE)"
                        class_section = input("Write your class section: ")
                        while len(class_section)>1:
                            class_section = input("single letter please: ")
                        class_name=str(class_number)+" - "+ class_section.upper() + course_name
                elif class_number==12:
                    print("1 - Professional course")
                    print("2 - Regular course")
                    course_type=validation_check(2)
                    if course_type==1:
                        print("Which course")
                        print("1 - GPSI")
                        print("2 - TAE/TUR")
                        course_choice=validation_check(2)
                        if course_choice==1:
                            class_name="12 (3-A (GPSI))"
                        elif course_choice==2:
                            class_name="12 (3-B (TAE/TUR))"
                            if class_name in state["classes"]:
                                class_name="12 (3-C (TAE/TUR))"
                    else:
                        print("Which course")
                        print("1 - Ciências e tecnologias")
                        print("2 - Ciências e tecnologias Articulado")
                        print("3 - Linguas e Humanidades")
                        print("4 - Linguas e Humanidades Articulado")
                        print("5 - Ciências Socio-Económicas")
                        course_choice=validation_check(5)
                        if course_choice==1:
                            course_name="(CT)"
                        elif course_choice==2:
                            course_name="(CTA)"
                        elif course_choice==3:
                            course_name="(LH)"
                        elif course_choice==4:
                            course_name="(LHA)"
                        else:
                            course_name="(CSE)"
                        class_section = input("Write your class section: ")
                        while len(class_section)>1:
                            class_section = input("single letter please: ")
                        class_name=str(class_number)+" - "+ class_section.upper() + course_name
                else:
                    class_section = input("Write your class section: ")
                    while len(class_section)>1:
                        class_section = input("single letter please: ")
                    class_name=str(class_number)+" - "+ class_section.upper()
                if class_name in state["classes"]:
                    print("Removing class " + class_name)
                    del state["classes"][class_name]
                    del state["grades"][class_name]
                    del state["faltas"][class_name]
                    save_state(state)
                    pause()
                else:
                    print("Class doesnt exist")
                    pause()
            elif make_choice==4:
                print("Are you sure")
                yes_no=input("Y/n: ")
                while yes_no.upper()=="Y" and yes_no.upper()=="" and yes_no.upper()==" " and yes_no.upper()=="YES" and yes_no.upper()=="N" and yes_no.upper()=="NO":
                    yes_no=input("Y/n: ")
                if yes_no.upper()=="Y" or yes_no.upper()=="" or yes_no.upper()==" " or yes_no.upper()=="YES":
                    state["classes"]={}
                    state["faltas"]={}
                    state["grades"]= {}
                    save_state(state)
                elif yes_no.upper()=="N" or yes_no.upper()=="NO":
                    print("Going back")
            else:
                print("leaving....")
                save_state(state)
                break
            save_state(state)
    else:
        exit()