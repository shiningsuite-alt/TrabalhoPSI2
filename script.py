import random

def history_adder(sigla_type_history_1,sigla_type_history_2,sigla_type_history_3,sigla_type_history_4,sigla_type_history_5,sigla_type_history_6,sigla_type_history_7,sigla_type_history_8,sigla_type_history_9,sigla_type_history_10,sigla_type):
    if sigla_type_history_1 == "":
        sigla_type_history_1 = sigla_type
    elif sigla_type_history_2 == "":
        sigla_type_history_2 = sigla_type
    elif sigla_type_history_3 == "":
        sigla_type_history_3 = sigla_type
    elif sigla_type_history_4 == "":
        sigla_type_history_4 = sigla_type
    elif sigla_type_history_5 == "":
        sigla_type_history_5 = sigla_type
    elif sigla_type_history_6 == "":
        sigla_type_history_6 = sigla_type
    elif sigla_type_history_7 == "":
        sigla_type_history_7 = sigla_type
    elif sigla_type_history_8 == "":
        sigla_type_history_8 = sigla_type
    elif sigla_type_history_9 == "":
        sigla_type_history_9 = sigla_type
    elif sigla_type_history_10 == "":
        sigla_type_history_10 = sigla_type
    else:
        sigla_type_history_1 = sigla_type_history_2
        sigla_type_history_2 = sigla_type_history_3
        sigla_type_history_3 = sigla_type_history_4
        sigla_type_history_4 = sigla_type_history_5
        sigla_type_history_5 = sigla_type_history_6
        sigla_type_history_6 = sigla_type_history_7
        sigla_type_history_7 = sigla_type_history_8
        sigla_type_history_8 = sigla_type_history_9
        sigla_type_history_9 = sigla_type_history_10
        sigla_type_history_10 = sigla_type
    return sigla_type_history_1,sigla_type_history_2,sigla_type_history_3,sigla_type_history_4,sigla_type_history_5,sigla_type_history_6,sigla_type_history_7,sigla_type_history_8,sigla_type_history_9,sigla_type_history_10

exempt_words=["o", "a", "os", "as", "um", "uma", "de", "da", "do", "em", "para", "com", "e", "ou", "mas","the","but","or","and","with","for","in","a","an","of"]
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","á","ã","â","à","ä","ó","õ","ô","ò","ö","í","ì","î","ï","é","ê","è","ë","ú","û","ù","ü","Á","Ã","Â","À","Ä","Ó","Õ","Ô","Ò","Ö","Í","Ì","Î","Ï","É","Ê","È","Ë","Ú","Û","Ù","Ü",",",";",".",":","-","_","<",">","|","\\","!","\"","@","£","€","#","$","§","%","&","/","{","(","[","]",")","}","=","?","'","»","«","ç","Ç","º","ª","+","*"]
upper_case=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Á","Ã","Â","À","Ä","Ó","Õ","Ô","Ò","Ö","Í","Ì","Î","Ï","É","Ê","È","Ë","Ú","Û","Ù","Ü","Ç"]
lower_case=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","á","ã","â","à","ä","ó","õ","ô","ò","ö","í","ì","î","ï","é","ê","è","ë","ú","û","ù","ü","ç"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=[",",";",".",":","-","_","<",">","|","\\","!","\"","@","£","€","#","$","§","%","&","/","{","(","[","]",")","}","=","?","'","»","«","º","ª","+","*"]
list_a=["A","Á","À","Â","Ã","Ä","a","á","à","â","ã","ä","@","ª"]
list_b=["B","b","[","6","p","q","d","(","P"]
list_c=["C","c","<","(","ç","Ç","{","["]
list_d=["D","d","b","q","p","P",]
list_e=["E","e","3","é","ê","è","ë","É","Ê","È","Ë","£","€"]
list_f=["F","f","£"]
list_g=["G","g","q","9","Q",")"]
list_h=["H","h","#"]
list_i=["I","i","!",":","í","ì","î","ï","Í","Ì","Î","Ï"]
list_j=["J","j",";","7",",","]",")"]
list_k=["K","k","+","*","<","&"]
list_l=["L","l","/","{","(","[","\\"]
list_m=["M","m","w","W","3","n","N"]
list_n=["N","n","V","v","U","u","»",">"]
list_o=["O","o","0","ó","õ","ô","ò","ö","Ó","Õ","Ô","Ò","Ö","§","º","%"]
list_p=["P","p","q","b","d","{","(","["]
list_q=["Q","p","q","b","d","G","g","9"]
list_r=["R","r",]
list_s=["S","s","5","$","§"]
list_t=["t","T","#","+"]
list_u=["U","u","n","«","<","ú","û","ù","ü","Ú","Û","Ù","Ü"]
list_v=["U","u","V","v","<"]
list_w=["M","m","w","W","3","V","v"]
list_x=["x","X","+","*"]
list_y=["Y","y",")","v","%"]
list_z=["Z","z","2"]
big_loop=True
upper_case_letter_counter=0
lower_case_letter_counter=0
number_counter=0
symbol_counter=0
make_choice=0
make_choice_random=0
make_choice_enter=0
password=""
frase=""
frase_edited=""
frase_split=""
frase_enter_loop=True
error_loop=True
number_of_letters=0
password_history_1=""
password_history_2=""
password_history_3=""
password_history_4=""
password_history_5=""
password_history_6=""
password_history_7=""
password_history_8=""
password_history_9=""
password_history_10=""
random_history_1=""
random_history_2=""
random_history_3=""
random_history_4=""
random_history_5=""
random_history_6=""
random_history_7=""
random_history_8=""
random_history_9=""
random_history_10=""
code_history_1=""
code_history_2=""
code_history_3=""
code_history_4=""
code_history_5=""
code_history_6=""
code_history_7=""
code_history_8=""
code_history_9=""
code_history_10=""
redo=True
letter_adder=""
random_loop=True
basic_check=True
sigla_type_1=""
sigla_type_2=""
sigla_type_3=""
sigla_type_4=""
sigla_type_5=""
sigla_type_6=""
sigla_type_7=""
sigla_type_1_history_1=""
sigla_type_1_history_2=""
sigla_type_1_history_3=""
sigla_type_1_history_4=""
sigla_type_1_history_5=""
sigla_type_1_history_6=""
sigla_type_1_history_7=""
sigla_type_1_history_8=""
sigla_type_1_history_9=""
sigla_type_1_history_10=""
sigla_type_2_history_1=""
sigla_type_2_history_2=""
sigla_type_2_history_3=""
sigla_type_2_history_4=""
sigla_type_2_history_5=""
sigla_type_2_history_6=""
sigla_type_2_history_7=""
sigla_type_2_history_8=""
sigla_type_2_history_9=""
sigla_type_2_history_10=""
sigla_type_3_history_1=""
sigla_type_3_history_2=""
sigla_type_3_history_3=""
sigla_type_3_history_4=""
sigla_type_3_history_5=""
sigla_type_3_history_6=""
sigla_type_3_history_7=""
sigla_type_3_history_8=""
sigla_type_3_history_9=""
sigla_type_3_history_10=""
sigla_type_4_history_1=""
sigla_type_4_history_2=""
sigla_type_4_history_3=""
sigla_type_4_history_4=""
sigla_type_4_history_5=""
sigla_type_4_history_6=""
sigla_type_4_history_7=""
sigla_type_4_history_8=""
sigla_type_4_history_9=""
sigla_type_4_history_10=""
sigla_type_5_history_1=""
sigla_type_5_history_2=""
sigla_type_5_history_3=""
sigla_type_5_history_4=""
sigla_type_5_history_5=""
sigla_type_5_history_6=""
sigla_type_5_history_7=""
sigla_type_5_history_8=""
sigla_type_5_history_9=""
sigla_type_5_history_10=""
sigla_type_6_history_1=""
sigla_type_6_history_2=""
sigla_type_6_history_3=""
sigla_type_6_history_4=""
sigla_type_6_history_5=""
sigla_type_6_history_6=""
sigla_type_6_history_7=""
sigla_type_6_history_8=""
sigla_type_6_history_9=""
sigla_type_6_history_10=""
sigla_type_7_history_1=""
sigla_type_7_history_2=""
sigla_type_7_history_3=""
sigla_type_7_history_4=""
sigla_type_7_history_5=""
sigla_type_7_history_6=""
sigla_type_7_history_7=""
sigla_type_7_history_8=""
sigla_type_7_history_9=""
sigla_type_7_history_10=""
morse_history_1=""
morse_history_2=""
morse_history_3=""
morse_history_4=""
morse_history_5=""
morse_history_6=""
morse_history_7=""
morse_history_8=""
morse_history_9=""
morse_history_10=""
history_loop=True
morse_loop=True
morse_edited = ""
morse = ""

while big_loop:
    print("========Menu========")
    print("1 - Random")
    print("2 - Codification")
    print("3 - Siglas")
    print("4 - Morse Code")
    print("5 - Add password")
    print("6 - History")
    print("7 - Leave")
    while basic_check:
        try:
            make_choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("That's not a number! Try again.")
    while make_choice < 1 or make_choice > 7:
        try:
            make_choice_enter = int(input("Enter your choice: "))
            break
        except ValueError:
            print("That's not a number! Try again.")
    if make_choice==1:
        random_loop=True
        while random_loop:
            letter_adder=""
            redo=True
            number_of_letters=random.randint(5,16)
            for i in range(number_of_letters):
                letter_adder+=random.choice(letters)
            random_history_1, random_history_2, random_history_3, random_history_4, random_history_5, random_history_6, random_history_7, random_history_8, random_history_9, random_history_10 = history_adder(random_history_1, random_history_2, random_history_3, random_history_4, random_history_5, random_history_6, random_history_7, random_history_8, random_history_9, random_history_10,letter_adder)
            print(letter_adder+" - Would you like this as your password?")
            print("1 - Keep as password")
            print("2 - Retry")
            print("3 - Choose process")
            print("4 - Exit")
            while basic_check:
                try:
                    make_choice_random = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            while make_choice_random>4 or make_choice_random<1:
                try:
                    make_choice_random = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            if make_choice_random == 1:
                password=letter_adder
                random_loop=False
                big_loop=False
            elif make_choice_random == 2:
                random_loop=True
                big_loop=True
            elif make_choice_random == 3:
                random_loop=False
                big_loop=True
            elif make_choice_random == 4:
                random_loop=False
                big_loop=False
    elif make_choice==2:
        frase_enter_loop=True
        while frase_enter_loop:
            frase_edited=""
            frase=input("Digite uma sentence ou palavra: ")
            while len(frase)>16 or len(frase)<5:
                print("Has to be longer than 5 characters and less than 16")
                frase = input("Try again: ")
            for char in frase.lower():
                if char=="a":
                    frase_edited+=random.choice(list_a)
                elif char=="b":
                    frase_edited+=random.choice(list_b)
                elif char=="c":
                    frase_edited+=random.choice(list_c)
                elif char=="d":
                    frase_edited+=random.choice(list_d)
                elif char=="e":
                    frase_edited+=random.choice(list_e)
                elif char=="f":
                    frase_edited+=random.choice(list_f)
                elif char=="g":
                    frase_edited+=random.choice(list_g)
                elif char=="h":
                    frase_edited+=random.choice(list_h)
                elif char=="i":
                    frase_edited+=random.choice(list_i)
                elif char=="j":
                    frase_edited+=random.choice(list_j)
                elif char=="k":
                    frase_edited+=random.choice(list_k)
                elif char=="l":
                    frase_edited+=random.choice(list_l)
                elif char=="m":
                    frase_edited+=random.choice(list_m)
                elif char=="n":
                    frase_edited+=random.choice(list_n)
                elif char=="o":
                    frase_edited+=random.choice(list_o)
                elif char=="p":
                    frase_edited+=random.choice(list_p)
                elif char=="q":
                    frase_edited+=random.choice(list_q)
                elif char=="r":
                    frase_edited+=random.choice(list_r)
                elif char=="s":
                    frase_edited+=random.choice(list_s)
                elif char=="t":
                    frase_edited+=random.choice(list_t)
                elif char=="u":
                    frase_edited+=random.choice(list_u)
                elif char=="v":
                    frase_edited+=random.choice(list_v)
                elif char=="w":
                    frase_edited+=random.choice(list_w)
                elif char=="x":
                    frase_edited+=random.choice(list_x)
                elif char=="y":
                    frase_edited+=random.choice(list_y)
                elif char=="z":
                    frase_edited+=random.choice(list_z)
                elif char==" ":
                    frase_edited+=" "
                else:
                    frase_edited+=random.choice(letters)
            code_history_1, code_history_2, code_history_3, code_history_4, code_history_5, code_history_6, code_history_7, code_history_8, code_history_9, code_history_10 = history_adder(code_history_1, code_history_2, code_history_3, code_history_4, code_history_5, code_history_6, code_history_7, code_history_8, code_history_9, code_history_10, frase_edited)
            print(frase_edited + " - Would you like this as your password?")
            print("1 - Keep as password")
            print("2 - Retry")
            print("3 - Choose process")
            print("4 - Exit")
            while basic_check:
                try:
                    make_choice_enter = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            while make_choice_enter>4 or make_choice_enter<1:
                try:
                    make_choice_enter = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            if make_choice_enter == 1:
                password = frase_edited
                frase_enter_loop = False
                big_loop = False
            elif make_choice_enter == 2:
                frase_enter_loop = True
                big_loop = True
            elif make_choice_enter == 3:
                frase_enter_loop = False
                big_loop = True
            elif make_choice_enter == 4:
                frase_enter_loop = False
                big_loop = False
    elif make_choice==3:
        frase_enter_loop = True
        while frase_enter_loop:
            sigla_type_1=""
            sigla_type_2=""
            sigla_type_3=""
            sigla_type_4=""
            sigla_type_5=""
            sigla_type_6=""
            sigla_type_7=""
            frase_edited = ""
            frase = input("Digite uma sentence ou palavra: ")
            while len(frase) > 99 or len(frase) < 5:
                print("Has to be longer than 5 characters and less than 16")
                frase = input("Try again: ")
            frase_split = frase.split()
            for word in frase_split:
                if word.lower() not in exempt_words:
                    sigla_type_1+= word[0].upper()
                    sigla_type_3 += word[0].upper()
                    sigla_type_3 += word[1].lower()
                    sigla_type_4 += word[0].upper()
                    sigla_type_4 += word[-1].lower()
                    sigla_type_5 += word[0].upper()
                    sigla_type_6 += word[0].lower()
                    sigla_type_7 += word[0].lower()
                sigla_type_2 += word[0].upper()
            sigla_type_5 += "_"
            sigla_type_7 += "_"
            for i in range(random.randint(1, 10)):
                sigla_type_5 += str(random.randint(0, 10))
                sigla_type_7 += str(random.randint(0, 10))
            sigla_type_1_history_1, sigla_type_1_history_2, sigla_type_1_history_3, sigla_type_1_history_4, sigla_type_1_history_5, sigla_type_1_history_6, sigla_type_1_history_7, sigla_type_1_history_8, sigla_type_1_history_9, sigla_type_1_history_10 = history_adder(sigla_type_1_history_1, sigla_type_1_history_2, sigla_type_1_history_3, sigla_type_1_history_4, sigla_type_1_history_5, sigla_type_1_history_6, sigla_type_1_history_7, sigla_type_1_history_8, sigla_type_1_history_9, sigla_type_1_history_10, sigla_type_1)
            sigla_type_2_history_1, sigla_type_2_history_2, sigla_type_2_history_3, sigla_type_2_history_4, sigla_type_2_history_5, sigla_type_2_history_6, sigla_type_2_history_7, sigla_type_2_history_8, sigla_type_2_history_9, sigla_type_2_history_10 = history_adder(sigla_type_2_history_1, sigla_type_2_history_2, sigla_type_2_history_3, sigla_type_2_history_4, sigla_type_2_history_5, sigla_type_2_history_6, sigla_type_2_history_7, sigla_type_2_history_8, sigla_type_2_history_9, sigla_type_2_history_10, sigla_type_2)
            sigla_type_3_history_1, sigla_type_3_history_2, sigla_type_3_history_3, sigla_type_3_history_4, sigla_type_3_history_5, sigla_type_3_history_6, sigla_type_3_history_7, sigla_type_3_history_8, sigla_type_3_history_9, sigla_type_3_history_10 = history_adder(sigla_type_3_history_1, sigla_type_3_history_2, sigla_type_3_history_3, sigla_type_3_history_4, sigla_type_3_history_5, sigla_type_3_history_6, sigla_type_3_history_7, sigla_type_3_history_8, sigla_type_3_history_9, sigla_type_3_history_10, sigla_type_3)
            sigla_type_4_history_1, sigla_type_4_history_2, sigla_type_4_history_3, sigla_type_4_history_4, sigla_type_4_history_5, sigla_type_4_history_6, sigla_type_4_history_7, sigla_type_4_history_8, sigla_type_4_history_9, sigla_type_4_history_10 = history_adder(sigla_type_4_history_1, sigla_type_4_history_2, sigla_type_4_history_3, sigla_type_4_history_4, sigla_type_4_history_5, sigla_type_4_history_6, sigla_type_4_history_7, sigla_type_4_history_8, sigla_type_4_history_9, sigla_type_4_history_10, sigla_type_4)
            sigla_type_5_history_1, sigla_type_5_history_2, sigla_type_5_history_3, sigla_type_5_history_4, sigla_type_5_history_5, sigla_type_5_history_6, sigla_type_5_history_7, sigla_type_5_history_8, sigla_type_5_history_9, sigla_type_5_history_10 = history_adder(sigla_type_5_history_1, sigla_type_5_history_2, sigla_type_5_history_3, sigla_type_5_history_4, sigla_type_5_history_5, sigla_type_5_history_6, sigla_type_5_history_7, sigla_type_5_history_8, sigla_type_5_history_9, sigla_type_5_history_10, sigla_type_5)
            sigla_type_6_history_1, sigla_type_6_history_2, sigla_type_6_history_3, sigla_type_6_history_4, sigla_type_6_history_5, sigla_type_6_history_6, sigla_type_6_history_7, sigla_type_6_history_8, sigla_type_6_history_9, sigla_type_6_history_10 = history_adder(sigla_type_6_history_1, sigla_type_6_history_2, sigla_type_6_history_3, sigla_type_6_history_4, sigla_type_6_history_5, sigla_type_6_history_6, sigla_type_6_history_7, sigla_type_6_history_8, sigla_type_6_history_9, sigla_type_6_history_10, sigla_type_6)
            sigla_type_7_history_1, sigla_type_7_history_2, sigla_type_7_history_3, sigla_type_7_history_4, sigla_type_7_history_5, sigla_type_7_history_6, sigla_type_7_history_7, sigla_type_7_history_8, sigla_type_7_history_9, sigla_type_7_history_10 = history_adder(sigla_type_7_history_1, sigla_type_7_history_2, sigla_type_7_history_3, sigla_type_7_history_4, sigla_type_7_history_5, sigla_type_7_history_6, sigla_type_7_history_7, sigla_type_7_history_8, sigla_type_7_history_9, sigla_type_7_history_10, sigla_type_7)
            print(frase_edited + " - Would you like one of these as your password?")
            print("1 - Keep "+sigla_type_1+" as your password?")
            print("2 - Keep "+sigla_type_2+" as your password?")
            print("3 - Keep "+sigla_type_3+" as your password?")
            print("4 - Keep "+sigla_type_4+" as your password?")
            print("5 - Keep "+sigla_type_5+" as your password?")
            print("6 - Keep "+sigla_type_6+" as your password?")
            print("7 - Keep "+sigla_type_7+" as your password?")
            print("8 - Retry")
            print("9 - Choose process")
            print("10 - Exit")
            while basic_check:
                try:
                    make_choice_enter = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            while make_choice_enter>10 or make_choice_enter<1:
                try:
                    make_choice_enter = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            if make_choice_enter == 1:
                password = sigla_type_1
                frase_enter_loop = False
                big_loop = False
            elif make_choice_enter == 2:
                password = sigla_type_2
                frase_enter_loop = False
                big_loop = False
            elif make_choice_enter == 3:
                password = sigla_type_3
                frase_enter_loop = False
                big_loop = False
            elif make_choice_enter == 4:
                password = sigla_type_4
                frase_enter_loop = False
                big_loop = False
            elif make_choice_enter == 5:
                password = sigla_type_5
                frase_enter_loop = False
                big_loop = False
            elif make_choice_enter == 6:
                password = sigla_type_6
                frase_enter_loop = False
                big_loop = False
            elif make_choice_enter == 7:
                password = sigla_type_7
                frase_enter_loop = False
                big_loop = False
            elif make_choice_enter == 8:
                frase_enter_loop = True
                big_loop = True
            elif make_choice_enter == 9:
                frase_enter_loop = False
                big_loop = True
            elif make_choice_enter == 10:
                frase_enter_loop = False
                big_loop = False
    elif make_choice==4:
        morse_loop = True
        while morse_loop:
            morse_edited = ""
            morse = input("Digite uma sentence ou palavra: ")
            for char in morse.lower():
                if char=="a":
                    morse_edited += ".-"
                elif char=="b":
                    morse_edited += "-..."
                elif char=="c":
                    morse_edited += "-.-."
                elif char=="d":
                    morse_edited += "-.."
                elif char=="e":
                    morse_edited += "."
                elif char=="f":
                    morse_edited += "..-."
                elif char=="g":
                    morse_edited += "--."
                elif char=="h":
                    morse_edited += "...."
                elif char=="i":
                    morse_edited += ".."
                elif char=="j":
                    morse_edited += ".---"
                elif char=="k":
                    morse_edited += "-.-"
                elif char=="l":
                    morse_edited += ".-.."
                elif char=="m":
                    morse_edited += "--"
                elif char=="n":
                    morse_edited += "-."
                elif char=="o":
                    morse_edited += "---"
                elif char=="p":
                    morse_edited += ".--."
                elif char=="q":
                    morse_edited += "--.-"
                elif char=="r":
                    morse_edited += ".-."
                elif char=="s":
                    morse_edited += "..."
                elif char=="t":
                    morse_edited += "-"
                elif char=="u":
                    morse_edited += "..-"
                elif char=="v":
                    morse_edited += "...-"
                elif char=="w":
                    morse_edited += ".--"
                elif char=="x":
                    morse_edited += "-..-"
                elif char=="y":
                    morse_edited += "-.--"
                elif char=="z":
                    morse_edited += "--.."
                elif char=="1":
                    morse_edited += ".----"
                elif char=="2":
                    morse_edited += "..---"
                elif char=="3":
                    morse_edited += "...--"
                elif char=="4":
                    morse_edited += "....-"
                elif char=="5":
                    morse_edited += "....."
                elif char=="6":
                    morse_edited += "-...."
                elif char=="7":
                    morse_edited += "--..."
                elif char=="8":
                    morse_edited += "---.."
                elif char=="9":
                    morse_edited += "----."
                elif char=="0":
                    morse_edited += "-----"
                elif char==".":
                    morse_edited += ".-.-.-"
                elif char==",":
                    morse_edited += "--..--"
                elif char=="?":
                    morse_edited += "..--.."
                elif char==" ":
                    morse_edited += " "
                else:
                    morse_edited += ""
                morse_edited += " "
            morse_history_1, morse_history_2, morse_history_3, morse_history_4, morse_history_5, morse_history_6, morse_history_7, morse_history_8, morse_history_9, morse_history_10 = history_adder(morse_history_1, morse_history_2, morse_history_3, morse_history_4, morse_history_5, morse_history_6, morse_history_7, morse_history_8, morse_history_9, morse_history_10, morse_edited)
            print(morse_edited + "Would you like to set this as your password?")
            print("1 - Keep as password")
            print("2 - Retry")
            print("3 - Choose process")
            print("4 - Exit")
            while basic_check:
                try:
                    make_choice_enter = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            while make_choice_enter > 4 or make_choice_enter < 1:
                try:
                    make_choice_enter = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            if make_choice_enter == 1:
                password = morse_edited
                morse_loop = False
                big_loop = False
            elif make_choice_enter == 2:
                morse_loop = True
                big_loop = True
            elif make_choice_enter == 3:
                morse_loop = False
                big_loop = True
            elif make_choice_enter == 4:
                morse_loop = False
                big_loop = False
    elif make_choice==5:
        password=input("Enter your password: ")
    elif make_choice==6:
        history_loop = True
        while history_loop:
            print("========History========")
            print("Which history would you like to see")
            print("1 - Type 1")
            print("2 - Type 2")
            print("3 - Type 3")
            print("4 - Type 4")
            print("5 - Type 5")
            print("6 - Type 6")
            print("7 - Type 7")
            print("8 - Random history")
            print("9 - Code history")
            print("10 - Morse history")
            print("11 - Password history")
            print("12 - Clear history")
            print("13 - Leave history")
            while basic_check:
                try:
                    make_choice = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            while make_choice>13 or make_choice<0:
                try:
                    make_choice = int(input("Enter your choice: "))
                    break
                except ValueError:
                    print("That's not a number! Try again.")
            if make_choice == 1:
                if sigla_type_1_history_1!="":
                    print("1 -" + sigla_type_1_history_1)
                if sigla_type_1_history_2!="":
                    print("2 -" + sigla_type_1_history_2)
                if sigla_type_1_history_3!="":
                    print("3 -" + sigla_type_1_history_3)
                if sigla_type_1_history_4!="":
                    print("4 -" + sigla_type_1_history_4)
                if sigla_type_1_history_5!="":
                    print("5 -" + sigla_type_1_history_5)
                if sigla_type_1_history_6!="":
                    print("6 -" + sigla_type_1_history_6)
                if sigla_type_1_history_7!="":
                    print("7 -" + sigla_type_1_history_7)
                if sigla_type_1_history_8!="":
                    print("8 -" + sigla_type_1_history_8)
                if sigla_type_1_history_9!="":
                    print("9 -" + sigla_type_1_history_9)
                if sigla_type_1_history_10!="":
                    print("10 -" + sigla_type_1_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = sigla_type_1_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = sigla_type_1_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = sigla_type_1_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = sigla_type_1_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = sigla_type_1_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = sigla_type_1_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = sigla_type_1_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = sigla_type_1_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = sigla_type_1_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = sigla_type_1_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 2:
                if sigla_type_2_history_1 != "":
                    print("1 -" + sigla_type_2_history_1)
                if sigla_type_2_history_2 != "":
                    print("2 -" + sigla_type_2_history_2)
                if sigla_type_2_history_3 != "":
                    print("3 -" + sigla_type_2_history_3)
                if sigla_type_2_history_4 != "":
                    print("4 -" + sigla_type_2_history_4)
                if sigla_type_2_history_5 != "":
                    print("5 -" + sigla_type_2_history_5)
                if sigla_type_2_history_6 != "":
                    print("6 -" + sigla_type_2_history_6)
                if sigla_type_2_history_7 != "":
                    print("7 -" + sigla_type_2_history_7)
                if sigla_type_2_history_8 != "":
                    print("8 -" + sigla_type_2_history_8)
                if sigla_type_2_history_9 != "":
                    print("9 -" + sigla_type_2_history_9)
                if sigla_type_2_history_10 != "":
                    print("10 -" + sigla_type_2_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = sigla_type_2_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = sigla_type_2_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = sigla_type_2_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = sigla_type_2_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = sigla_type_2_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = sigla_type_2_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = sigla_type_2_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = sigla_type_2_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = sigla_type_2_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = sigla_type_2_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 3:
                if sigla_type_3_history_1 != "":
                    print("1 -" + sigla_type_3_history_1)
                if sigla_type_3_history_2 != "":
                    print("2 -" + sigla_type_3_history_2)
                if sigla_type_3_history_3 != "":
                    print("3 -" + sigla_type_3_history_3)
                if sigla_type_3_history_4 != "":
                    print("4 -" + sigla_type_3_history_4)
                if sigla_type_3_history_5 != "":
                    print("5 -" + sigla_type_3_history_5)
                if sigla_type_3_history_6 != "":
                    print("6 -" + sigla_type_3_history_6)
                if sigla_type_3_history_7 != "":
                    print("7 -" + sigla_type_3_history_7)
                if sigla_type_3_history_8 != "":
                    print("8 -" + sigla_type_3_history_8)
                if sigla_type_3_history_9 != "":
                    print("9 -" + sigla_type_3_history_9)
                if sigla_type_3_history_10 != "":
                    print("10 -" + sigla_type_3_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = sigla_type_3_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = sigla_type_3_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = sigla_type_3_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = sigla_type_3_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = sigla_type_3_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = sigla_type_3_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = sigla_type_3_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = sigla_type_3_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = sigla_type_3_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = sigla_type_3_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 4:
                if sigla_type_4_history_1 != "":
                    print("1 -" + sigla_type_4_history_1)
                if sigla_type_4_history_2 != "":
                    print("2 -" + sigla_type_4_history_2)
                if sigla_type_4_history_3 != "":
                    print("3 -" + sigla_type_4_history_3)
                if sigla_type_4_history_4 != "":
                    print("4 -" + sigla_type_4_history_4)
                if sigla_type_4_history_5 != "":
                    print("5 -" + sigla_type_4_history_5)
                if sigla_type_4_history_6 != "":
                    print("6 -" + sigla_type_4_history_6)
                if sigla_type_4_history_7 != "":
                    print("7 -" + sigla_type_4_history_7)
                if sigla_type_4_history_8 != "":
                    print("8 -" + sigla_type_4_history_8)
                if sigla_type_4_history_9 != "":
                    print("9 -" + sigla_type_4_history_9)
                if sigla_type_4_history_10 != "":
                    print("10 -" + sigla_type_4_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = sigla_type_4_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = sigla_type_4_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = sigla_type_4_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = sigla_type_4_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = sigla_type_4_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = sigla_type_4_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = sigla_type_4_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = sigla_type_4_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = sigla_type_4_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = sigla_type_4_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 5:
                if sigla_type_5_history_1 != "":
                    print("1 -" + sigla_type_5_history_1)
                if sigla_type_5_history_2 != "":
                    print("2 -" + sigla_type_5_history_2)
                if sigla_type_5_history_3 != "":
                    print("3 -" + sigla_type_5_history_3)
                if sigla_type_5_history_4 != "":
                    print("4 -" + sigla_type_5_history_4)
                if sigla_type_5_history_5 != "":
                    print("5 -" + sigla_type_5_history_5)
                if sigla_type_5_history_6 != "":
                    print("6 -" + sigla_type_5_history_6)
                if sigla_type_5_history_7 != "":
                    print("7 -" + sigla_type_5_history_7)
                if sigla_type_5_history_8 != "":
                    print("8 -" + sigla_type_5_history_8)
                if sigla_type_5_history_9 != "":
                    print("9 -" + sigla_type_5_history_9)
                if sigla_type_5_history_10 != "":
                    print("10 -" + sigla_type_5_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = sigla_type_5_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = sigla_type_5_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = sigla_type_5_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = sigla_type_5_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = sigla_type_5_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = sigla_type_5_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = sigla_type_5_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = sigla_type_5_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = sigla_type_5_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = sigla_type_5_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 6:
                if sigla_type_6_history_1 != "":
                    print("1 -" + sigla_type_6_history_1)
                if sigla_type_6_history_2 != "":
                    print("2 -" + sigla_type_6_history_2)
                if sigla_type_6_history_3 != "":
                    print("3 -" + sigla_type_6_history_3)
                if sigla_type_6_history_4 != "":
                    print("4 -" + sigla_type_6_history_4)
                if sigla_type_6_history_5 != "":
                    print("5 -" + sigla_type_6_history_5)
                if sigla_type_6_history_6 != "":
                    print("6 -" + sigla_type_6_history_6)
                if sigla_type_6_history_7 != "":
                    print("7 -" + sigla_type_6_history_7)
                if sigla_type_6_history_8 != "":
                    print("8 -" + sigla_type_6_history_8)
                if sigla_type_6_history_9 != "":
                    print("9 -" + sigla_type_6_history_9)
                if sigla_type_6_history_10 != "":
                    print("10 -" + sigla_type_6_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = sigla_type_6_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = sigla_type_6_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = sigla_type_6_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = sigla_type_6_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = sigla_type_6_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = sigla_type_6_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = sigla_type_6_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = sigla_type_6_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = sigla_type_6_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = sigla_type_6_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 7:
                if sigla_type_7_history_1 != "":
                    print("1 -" + sigla_type_7_history_1)
                if sigla_type_7_history_2 != "":
                    print("2 -" + sigla_type_7_history_2)
                if sigla_type_7_history_3 != "":
                    print("3 -" + sigla_type_7_history_3)
                if sigla_type_7_history_4 != "":
                    print("4 -" + sigla_type_7_history_4)
                if sigla_type_7_history_5 != "":
                    print("5 -" + sigla_type_7_history_5)
                if sigla_type_7_history_6 != "":
                    print("6 -" + sigla_type_7_history_6)
                if sigla_type_7_history_7 != "":
                    print("7 -" + sigla_type_7_history_7)
                if sigla_type_7_history_8 != "":
                    print("8 -" + sigla_type_7_history_8)
                if sigla_type_7_history_9 != "":
                    print("9 -" + sigla_type_7_history_9)
                if sigla_type_7_history_10 != "":
                    print("10 -" + sigla_type_7_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = sigla_type_7_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = sigla_type_7_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = sigla_type_7_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = sigla_type_7_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = sigla_type_7_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = sigla_type_7_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = sigla_type_7_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = sigla_type_7_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = sigla_type_7_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = sigla_type_7_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 8:
                if random_history_1 != "":
                    print("1 - " + random_history_1)
                if random_history_2 != "":
                    print("2 - " + random_history_2)
                if random_history_3 != "":
                    print("3 - " + random_history_3)
                if random_history_4 != "":
                    print("4 - " + random_history_4)
                if random_history_5 != "":
                    print("5 - " + random_history_5)
                if random_history_6 != "":
                    print("6 - " + random_history_6)
                if random_history_7 != "":
                    print("7 - " + random_history_7)
                if random_history_8 != "":
                    print("8 - " + random_history_8)
                if random_history_9 != "":
                    print("9 - " + random_history_9)
                if random_history_10 != "":
                    print("10 - " + random_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = random_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = random_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = random_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = random_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = random_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = random_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = random_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = random_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = random_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = random_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 9:
                if code_history_1 != "":
                    print("1 -" + code_history_1)
                if code_history_2 != "":
                    print("2 -" + code_history_2)
                if code_history_3 != "":
                    print("3 -" + code_history_3)
                if code_history_4 != "":
                    print("4 -" + code_history_4)
                if code_history_5 != "":
                    print("5 -" + code_history_5)
                if code_history_6 != "":
                    print("6 -" + code_history_6)
                if code_history_7 != "":
                    print("7 -" + code_history_7)
                if code_history_8 != "":
                    print("8 -" + code_history_8)
                if code_history_9 != "":
                    print("9 -" + code_history_9)
                if code_history_10 != "":
                    print("10 -" + code_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = code_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = code_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = code_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = code_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = code_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = code_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = code_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = code_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = code_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = code_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 10:
                if morse_history_1 != "":
                    print("1 - " + morse_history_1)
                if morse_history_2 != "":
                    print("2 - " + morse_history_2)
                if morse_history_3 != "":
                    print("3 - " + morse_history_3)
                if morse_history_4 != "":
                    print("4 - " + morse_history_4)
                if morse_history_5 != "":
                    print("5 - " + morse_history_5)
                if morse_history_6 != "":
                    print("6 - " + morse_history_6)
                if morse_history_7 != "":
                    print("7 - " + morse_history_7)
                if morse_history_8 != "":
                    print("8 - " + morse_history_8)
                if morse_history_9 != "":
                    print("9 - " + morse_history_9)
                if morse_history_10 != "":
                    print("10 - " + morse_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = morse_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = morse_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = morse_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = morse_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = morse_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = morse_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = morse_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = morse_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = morse_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = morse_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 11:
                if password_history_1 != "":
                    print("1 - " + password_history_1)
                if password_history_2 != "":
                    print("2 - " + password_history_2)
                if password_history_3 != "":
                    print("3 - " + password_history_3)
                if password_history_4 != "":
                    print("4 - " + password_history_4)
                if password_history_5 != "":
                    print("5 - " + password_history_5)
                if password_history_6 != "":
                    print("6 - " + password_history_6)
                if password_history_7 != "":
                    print("7 - " + password_history_7)
                if password_history_8 != "":
                    print("8 - " + password_history_8)
                if password_history_9 != "":
                    print("9 - " + password_history_9)
                if password_history_10 != "":
                    print("10 - " + password_history_10)
                print("Would you like to set one of these as your password?")
                print("1 - Keep 1 as password")
                print("2 - Keep 2 as password")
                print("3 - Keep 3 as password")
                print("4 - Keep 4 as password")
                print("5 - Keep 5 as password")
                print("6 - Keep 6 as password")
                print("7 - Keep 7 as password")
                print("8 - Keep 8 as password")
                print("9 - Keep 9 as password")
                print("10 - Keep 10 as password")
                print("11 - Leave")
                make_choice = int(input("Enter your choice: "))
                if make_choice == 1:
                    password = password_history_1
                    print("Set as password")
                elif make_choice == 2:
                    password = password_history_2
                    print("Set as password")
                elif make_choice == 3:
                    password = password_history_3
                    print("Set as password")
                elif make_choice == 4:
                    password = password_history_4
                    print("Set as password")
                elif make_choice == 5:
                    password = password_history_5
                    print("Set as password")
                elif make_choice == 6:
                    password = password_history_6
                    print("Set as password")
                elif make_choice == 7:
                    password = password_history_7
                    print("Set as password")
                elif make_choice == 8:
                    password = password_history_8
                    print("Set as password")
                elif make_choice == 9:
                    password = password_history_9
                    print("Set as password")
                elif make_choice == 10:
                    password = password_history_10
                    print("Set as password")
                elif make_choice == 11:
                    history_loop = False
                    print("Leaving")
            elif make_choice == 12:
                sigla_type_1_history_1 = ""
                sigla_type_1_history_2 = ""
                sigla_type_1_history_3 = ""
                sigla_type_1_history_4 = ""
                sigla_type_1_history_5 = ""
                sigla_type_1_history_6 = ""
                sigla_type_1_history_7 = ""
                sigla_type_1_history_8 = ""
                sigla_type_1_history_9 = ""
                sigla_type_1_history_10 = ""
                sigla_type_2_history_1 = ""
                sigla_type_2_history_2 = ""
                sigla_type_2_history_3 = ""
                sigla_type_2_history_4 = ""
                sigla_type_2_history_5 = ""
                sigla_type_2_history_6 = ""
                sigla_type_2_history_7 = ""
                sigla_type_2_history_8 = ""
                sigla_type_2_history_9 = ""
                sigla_type_2_history_10 = ""
                sigla_type_3_history_1 = ""
                sigla_type_3_history_2 = ""
                sigla_type_3_history_3 = ""
                sigla_type_3_history_4 = ""
                sigla_type_3_history_5 = ""
                sigla_type_3_history_6 = ""
                sigla_type_3_history_7 = ""
                sigla_type_3_history_8 = ""
                sigla_type_3_history_9 = ""
                sigla_type_3_history_10 = ""
                sigla_type_4_history_1 = ""
                sigla_type_4_history_2 = ""
                sigla_type_4_history_3 = ""
                sigla_type_4_history_4 = ""
                sigla_type_4_history_5 = ""
                sigla_type_4_history_6 = ""
                sigla_type_4_history_7 = ""
                sigla_type_4_history_8 = ""
                sigla_type_4_history_9 = ""
                sigla_type_4_history_10 = ""
                sigla_type_5_history_1 = ""
                sigla_type_5_history_2 = ""
                sigla_type_5_history_3 = ""
                sigla_type_5_history_4 = ""
                sigla_type_5_history_5 = ""
                sigla_type_5_history_6 = ""
                sigla_type_5_history_7 = ""
                sigla_type_5_history_8 = ""
                sigla_type_5_history_9 = ""
                sigla_type_5_history_10 = ""
                sigla_type_6_history_1 = ""
                sigla_type_6_history_2 = ""
                sigla_type_6_history_3 = ""
                sigla_type_6_history_4 = ""
                sigla_type_6_history_5 = ""
                sigla_type_6_history_6 = ""
                sigla_type_6_history_7 = ""
                sigla_type_6_history_8 = ""
                sigla_type_6_history_9 = ""
                sigla_type_6_history_10 = ""
                sigla_type_7_history_1 = ""
                sigla_type_7_history_2 = ""
                sigla_type_7_history_3 = ""
                sigla_type_7_history_4 = ""
                sigla_type_7_history_5 = ""
                sigla_type_7_history_6 = ""
                sigla_type_7_history_7 = ""
                sigla_type_7_history_8 = ""
                sigla_type_7_history_9 = ""
                sigla_type_7_history_10 = ""
                morse_history_1 = ""
                morse_history_2 = ""
                morse_history_3 = ""
                morse_history_4 = ""
                morse_history_5 = ""
                morse_history_6 = ""
                morse_history_7 = ""
                morse_history_8 = ""
                morse_history_9 = ""
                morse_history_10 = ""
                random_history_1 = ""
                random_history_2 = ""
                random_history_3 = ""
                random_history_4 = ""
                random_history_5 = ""
                random_history_6 = ""
                random_history_7 = ""
                random_history_8 = ""
                random_history_9 = ""
                random_history_10 = ""
            elif make_choice == 13:
                history_loop=False
                print("Leaving history....")
    elif make_choice == 7:
        print("Bye")
        big_loop=False
    if password!="":
        password_history_1, password_history_2, password_history_3, password_history_4, password_history_5, password_history_6, password_history_7, password_history_8, password_history_9, password_history_10 = history_adder(password_history_1, password_history_2, password_history_3, password_history_4, password_history_5, password_history_6, password_history_7, password_history_8, password_history_9, password_history_10, password)
        for char in password:
            if char in upper_case:
                upper_case_letter_counter+=1
            elif char in lower_case:
                lower_case_letter_counter+=1
            elif char in numbers:
                number_counter+=1
            elif char in symbols:
                symbol_counter+=1
        if symbol_counter>=2 and number_counter>=2 and upper_case_letter_counter>=2 and lower_case_letter_counter>=2:
            print("Password strength: Strong")
            big_loop=False
        elif symbol_counter<=0 and number_counter<=0:
            print("Password strength: Weak")
            print("Add numbers and symbols")
            big_loop=True
        else:
            print("Password strength: Medium")
            print("It is recommended to change the password")
            print("Would you like to change the password?")
            print("1 - Yes")
            print("2 - No")
            make_choice=input("Make your choice")
            if make_choice == 1:
                big_loop=True
            elif make_choice == 2:
                big_loop=False
if password!="":
    print("Password set to " + password)