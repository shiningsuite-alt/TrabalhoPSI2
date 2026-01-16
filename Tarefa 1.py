import random

game1guess=0
random_number=0
menu_pick=0
reset=True
reset_1=True
menu=True
replay=0
chips=0
roulette_guess=0
roulette_bet=0
roulette_number=0
amount_bet=0
winnings=0
double=0
ahead_behind=0
above_below=0
triple1=0
triple2=0
quad1=0
quad2=0
quad3=0
six1=0
six2=0
six3=0
six4=0
six5=0
color_pick=0
half_pick=0
dozen_pick=0
column_pick=0
player_count=0
player_1=False
player_2=False
player_3=False
player_4=False
player_1_chips=0
player_2_chips=0
player_3_chips=0
player_4_chips=0
player_1_winnings=0
player_2_winnings=0
player_3_winnings=0
player_4_winnings=0
player_1_name="player1"
player_2_name="player2"
player_3_name="player3"
player_4_name="player4"
player_1_active=False
player_2_active=False
player_3_active=False
player_4_active=False
rounds=0
rules=0
rules_select=0
rules_view=False
restart = True
menuopen=0

while restart:
    menu=True
    while menu:
        print("1-Play")
        print("2-Roulette")
        print("3-Roulette multiplayer")
        print("4-Rules")
        print("5-Leave")
        menu=False
        menu_pick=int(input("select an option:"))
        while 5<menu_pick<0:
            menu_pick = int(input("select an option between 1 to 5:"))
    if menu_pick==1:
        while reset:
            random_number = random.randint(1, 100)
            print("==================================")
            game1guess = int(input("enter your guess between 1 and 100:"))
            while game1guess!=random_number:
                print("Try again")
                if game1guess < random_number:
                    print("Guess higher")
                elif game1guess > random_number:
                    print("Guess lower")
                game1guess = int(input("enter your guess between 1 and 100:"))
            if game1guess==random_number:
                reset=False
                print("you guessed correctly")
                print("would you like to play again?")
                print("1-Yes")
                print("2-No")
                replay=int(input("select an option:"))
                while replay!=1 and replay!=2:
                    print("invalid option")
                    replay = int(input("select an option:"))
                if replay==1:
                    reset=True
                elif replay==2:
                    restart=True
    elif menu_pick==2:
        print("======================================")
        chips+=30
        print("You have 30 chips")
        while reset_1:
            print("Place your bets")
            print("1-Numero")
            print("2-Split")
            print("3-Street")
            print("4-Corner")
            print("5-Line")
            print("6-Color")
            print("7-Odd")
            print("8-Even")
            print("9-Half")
            print("10-Dozen")
            print("11-Column")
            roulette_bet=int(input("Place your bets:"))
            while roulette_bet<=0 or roulette_bet>11:
                print("Place your bets between 1 to 11")
            roulette_number=random.randint(0,36)
            amount_bet=int(input("Place the amount you want to bet:"))
            while amount_bet>chips:
                mensagem="Cannot bet more than the amount of chips you have, which is:"+str(chips)
                print(mensagem)
                amount_bet = int(input("Place the amount you want to bet, another time:"))
            chips=chips-amount_bet
            if roulette_bet==1:
                roulette_guess=int(input("enter your guess between 0 and 36:"))
                while roulette_guess>36 or roulette_guess<0:
                    roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                print("closing bets")
                mensagem = "You picked " + str(roulette_guess) + "."
                print(mensagem)
                mensagem = "The lucky number is " + str(roulette_number)
                print(mensagem)
                if roulette_guess==roulette_number:
                    print("You win")
                    winnings=amount_bet*40
                    chips=chips+winnings
                    print("you have "+str(chips)+" chips")
                else:
                    print("You lose")
                    print("you have "+str(chips)+" chips, left")
            elif roulette_bet==2:
                roulette_guess = int(input("enter your guess between 1 and 36:"))
                while roulette_guess > 36 or roulette_guess < 0:
                    roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                while roulette_guess==0:
                    roulette_guess= int(input("You can only pick 0 as a single bet, pick a different number:"))
                if roulette_guess==1 or roulette_guess==4 or roulette_guess==7 or roulette_guess==10 or roulette_guess==13 or roulette_guess==16 or roulette_guess==19 or roulette_guess==22 or roulette_guess==25 or roulette_guess==28 or roulette_guess==31 or roulette_guess==34:
                    double=roulette_guess+1
                elif roulette_guess==3 or roulette_guess==6 or roulette_guess==9 or roulette_guess==12 or roulette_guess==15 or roulette_guess==18 or roulette_guess==21 or roulette_guess==24 or roulette_guess==27 or roulette_guess==30 or roulette_guess==33 or roulette_guess==36:
                    double=roulette_guess-1
                elif roulette_guess==2 or roulette_guess==5 or roulette_guess==8 or roulette_guess==11 or roulette_guess==14 or roulette_guess==17 or roulette_guess==20 or roulette_guess==23 or roulette_guess==26 or roulette_guess==29 or roulette_guess==32 or roulette_guess==35:
                    print("1-Ahead")
                    print("2-Behind")
                    ahead_behind=int(input("Would you like to choose one ahead or one behind:"))
                    if ahead_behind==1:
                        roulette_guess=roulette_guess+1
                    elif ahead_behind==2:
                        roulette_guess=roulette_guess-1
                print("closing bets")
                mensagem = "You picked " + str(roulette_guess) + "," + str(double) + "."
                print(mensagem)
                mensagem = "The lucky number is " + str(roulette_number)
                print(mensagem)
                if roulette_guess==roulette_number or double==roulette_number:
                    print("you win")
                    winnings=amount_bet*20
                    chips=chips+winnings
                    print("you have "+str(chips)+" chips")
                else:
                    print("you lose")
                    print("you have "+str(chips)+" chips, left")
            elif roulette_bet==3:
                roulette_guess = int(input("enter your guess between 1 and 36:"))
                while roulette_guess > 36 or roulette_guess < 0:
                    roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                while roulette_guess==0:
                    roulette_guess= int(input("You can only pick 0 as a single bet, pick a different number:"))
                if roulette_guess==1 or roulette_guess==4 or roulette_guess==7 or roulette_guess==10 or roulette_guess==13 or roulette_guess==16 or roulette_guess==19 or roulette_guess==22 or roulette_guess==25 or roulette_guess==28 or roulette_guess==31 or roulette_guess==34:
                    triple1=roulette_guess+1
                    triple2=roulette_guess+2
                elif roulette_guess == 3 or roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33 or roulette_guess == 36:
                    triple1=roulette_guess-1
                    triple2=roulette_guess-2
                elif roulette_guess == 2 or roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32 or roulette_guess == 35:
                    triple1=roulette_guess-1
                    triple2=roulette_guess+1
                print("Closing bets")
                mensagem = "You picked " + str(roulette_guess) + "," + str(triple1) + "," + str(triple2) +  "."
                print(mensagem)
                mensagem = "The lucky number is" + str(roulette_number)
                print(mensagem)
                if roulette_guess==roulette_number or triple1==roulette_number or triple2==roulette_number:
                    print("you win")
                    winnings = amount_bet * 15
                    chips = chips + winnings
                    print("you have " + str(chips) + " chips")
                else:
                    print("you lose")
                    print("you have " + str(chips) + " chips, left")
            elif roulette_bet==4:
                roulette_guess = int(input("enter your guess between 1 and 36:"))
                while roulette_guess > 36 or roulette_guess < 0:
                    roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                while roulette_guess == 0:
                    roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                if roulette_guess == 1:
                    quad1 = roulette_guess + 1
                    quad2 = roulette_guess + 3
                    quad3 = roulette_guess + 4
                elif roulette_guess == 3:
                    quad1 = roulette_guess - 1
                    quad2 = roulette_guess + 2
                    quad3 = roulette_guess + 3
                elif roulette_guess == 2:
                    print("1-Ahead")
                    print("2-Behind")
                    ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                    while ahead_behind!=1 and ahead_behind!=2:
                        ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                    if ahead_behind == 1:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess + 3
                        quad3 = roulette_guess + 4
                    elif ahead_behind == 2:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess + 2
                        quad3 = roulette_guess + 3
                elif roulette_guess == 34:
                    quad1 = roulette_guess + 1
                    quad2 = roulette_guess - 2
                    quad3 = roulette_guess - 3
                elif roulette_guess == 36:
                    quad1 = roulette_guess - 1
                    quad2 = roulette_guess - 3
                    quad3 = roulette_guess - 4
                elif roulette_guess == 35:
                    print("1-Ahead")
                    print("2-Behind")
                    ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                    while ahead_behind!=1 and ahead_behind!=2:
                        ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                    if ahead_behind == 1:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess - 2
                        quad3 = roulette_guess - 3
                    elif ahead_behind == 2:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess - 3
                        quad3 = roulette_guess - 4
                else:
                    print("1-Above")
                    print("2-Below")
                    above_below = int(input("Would you like to choose one above or one below:"))
                    while above_below!=1 and above_below!=2:
                        above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                    if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                        quad1 = roulette_guess - 1
                        if above_below == 1:
                            quad2 = roulette_guess - 3
                            quad3 = roulette_guess - 4
                        elif above_below == 2:
                            quad2 = roulette_guess + 2
                            quad3 = roulette_guess + 3
                    elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                        quad1 = roulette_guess + 1
                        if above_below == 1:
                            quad2 = roulette_guess - 2
                            quad3 = roulette_guess - 3
                        elif above_below == 2:
                            quad2 = roulette_guess + 3
                            quad3 = roulette_guess + 4
                    elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        if above_below == 1 and ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess - 3
                            quad3 = roulette_guess - 2
                        elif above_below == 1 and ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess - 3
                            quad3 = roulette_guess - 4
                        elif above_below == 2 and ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess + 3
                            quad3 = roulette_guess + 4
                        elif above_below == 2 and ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess + 2
                            quad3 = roulette_guess + 3
                print("Closing bets")
                mensagem = "You picked " + str(roulette_guess) + "," + str(quad1) + "," + str(quad2) + "," + str(quad3) + "."
                print(mensagem)
                mensagem = "The lucky number is" + str(roulette_number)
                print(mensagem)
                if roulette_guess == roulette_number or quad1 == roulette_number or quad2 == roulette_number or quad3 == roulette_number:
                    print("You win")
                    winnings = amount_bet * 10
                    chips = chips + winnings
                    print("you have " + str(chips) + " chips")
                else:
                    print("You lose")
                    print("you have " + str(chips) + " chips,left")
            elif roulette_bet==5:
                roulette_guess = int(input("enter your guess between 1 and 36:"))
                print("closing bets")
                while roulette_guess==0:
                    roulette_guess= int(input("You can only pick 0 as a single bet, pick a different number:"))
                while roulette_guess > 36 or roulette_guess < 0:
                    roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                if roulette_guess == 1:
                    six1=roulette_guess + 1
                    six2=roulette_guess + 2
                    six3=roulette_guess + 3
                    six4=roulette_guess + 4
                    six5=roulette_guess + 5
                elif roulette_guess == 2:
                    six1=roulette_guess - 1
                    six2=roulette_guess + 1
                    six3=roulette_guess + 2
                    six4=roulette_guess + 3
                    six5=roulette_guess + 4
                elif roulette_guess == 3:
                    six1=roulette_guess - 1
                    six2=roulette_guess - 2
                    six3=roulette_guess + 1
                    six4=roulette_guess + 2
                    six5=roulette_guess + 3
                elif roulette_guess == 34:
                    six1=roulette_guess - 3
                    six2=roulette_guess - 2
                    six3=roulette_guess - 1
                    six4=roulette_guess + 1
                    six5=roulette_guess + 2
                elif roulette_guess == 35:
                    six1=roulette_guess - 4
                    six2=roulette_guess - 3
                    six3=roulette_guess - 2
                    six4=roulette_guess - 1
                    six5=roulette_guess + 1
                elif roulette_guess == 36:
                    six1=roulette_guess - 5
                    six2=roulette_guess - 4
                    six3=roulette_guess - 3
                    six4=roulette_guess - 2
                    six5=roulette_guess - 1
                else:
                    print("1-Above")
                    print("2-Below")
                    above_below = int(input("Would you like to choose one above or one below:"))
                    if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess - 2
                        while above_below != 1 and above_below != 2:
                            above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                        if above_below == 1:
                            six3 = roulette_guess - 3
                            six4 = roulette_guess - 4
                            six5 = roulette_guess - 5
                        elif above_below == 2:
                            six3 = roulette_guess + 1
                            six4 = roulette_guess + 2
                            six5 = roulette_guess + 3
                    elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                        six1 = roulette_guess + 1
                        six2 = roulette_guess + 2
                        while above_below != 1 and above_below != 2:
                            above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                        if above_below == 1:
                            six3 = roulette_guess - 3
                            six4 = roulette_guess - 2
                            six5 = roulette_guess - 1
                        elif above_below == 2:
                            six3 = roulette_guess + 3
                            six4 = roulette_guess + 4
                            six5 = roulette_guess + 5
                    elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess + 1
                        while above_below != 1 and above_below != 2:
                            above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                        if above_below == 1:
                            six3 = roulette_guess - 2
                            six4 = roulette_guess - 3
                            six5 = roulette_guess - 4
                        elif above_below == 2:
                            six3 = roulette_guess + 2
                            six4 = roulette_guess + 3
                            six5 = roulette_guess + 4
                print("Closing bets")
                mensagem = "You picked " + str(roulette_guess) + "," + str(six1) + "," + str(six2) + "," + str(six3) + ","+ str(six4) + ","+ str(six5) + "."
                print(mensagem)
                mensagem = "The lucky number is" + str(roulette_number)
                print(mensagem)
                if roulette_guess == roulette_number or six1 == roulette_number or six2 == roulette_number or six3 == roulette_number or six4 == roulette_number or six5 == roulette_number:
                    print("You win")
                    winnings = amount_bet * 8
                    chips = chips + winnings
                    print("you have " + str(chips) + " chips")
                else:
                    print("You lose")
                    print("you have " + str(chips) + " chips,left")
            elif roulette_bet==6:
                print("Choose a color")
                print("1-Red (Includes 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)")
                print("2-Black (Includes 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)")
                color_pick = int(input("Make your pick:"))
                while color_pick != 1 and color_pick != 2:
                    color_pick = int(input("Make your pick between red (type 1) or black (type 2):"))
                print("closing bets")
                if color_pick == 1:
                    print("You picked red")
                    mensagem = "The lucky number is" + str(roulette_number)
                    print(mensagem)
                    if roulette_number == 1 or roulette_number == 3  or roulette_number == 5 or roulette_number == 7 or roulette_number == 9 or roulette_number == 12 or roulette_number == 14 or roulette_number == 16 or roulette_number == 18 or roulette_number == 19 or roulette_number == 21 or roulette_number == 23 or roulette_number == 25 or roulette_number == 27 or roulette_number == 30 or roulette_number == 32 or roulette_number == 34 or roulette_number == 36:
                        print("You win")
                        winnings = amount_bet * 2
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
                elif color_pick == 2:
                    print("You picked black")
                    mensagem = "The lucky number is" + str(roulette_number)
                    print(mensagem)
                    if roulette_number == 2 or roulette_number == 4  or roulette_number == 6 or roulette_number == 8 or roulette_number == 10 or roulette_number == 11 or roulette_number == 13 or roulette_number == 15 or roulette_number == 17 or roulette_number == 20 or roulette_number == 22 or roulette_number == 24 or roulette_number == 26 or roulette_number == 28 or roulette_number == 29 or roulette_number == 31 or roulette_number == 33 or roulette_number == 35:
                        print("You win")
                        winnings = amount_bet * 2
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
            elif roulette_bet==7:
                print("You picked odd")
                mensagem = "The lucky number is"+str(roulette_number)
                print(mensagem)
                if roulette_number%2==0:
                    print("You lose")
                    print("you have " + str(chips) + " chips, left")
                else:
                    print("You win")
                    winnings = amount_bet * 2
                    chips = chips + winnings
                    print("you have " + str(chips) + " chips")
            elif roulette_bet==8:
                print("You picked Even")
                mensagem = "The lucky number is" + str(roulette_number)
                print(mensagem)
                if roulette_number%2==0:
                    print("You win")
                    winnings = amount_bet * 2
                    chips = chips + winnings
                    print("you have " + str(chips) + " chips")
                else:
                    print("You lose")
                    print("you have " + str(chips) + " chips, left")
            elif roulette_bet==9:
                print("Choose Half")
                print("1-First Half (Includes 1-18)")
                print("2-Second Half (Includes 19-36)")
                half_pick = int(input("Make your pick:"))
                while half_pick != 1 and half_pick != 2:
                    half_pick = int(input("Make your pick between the first half (type 1) or the second half (type 2):"))
                print("closing bets")
                if half_pick == 1:
                    mensagem = "You picked the first half."
                    print(mensagem)
                    mensagem = "The lucky number is" + str(roulette_number)
                    print(mensagem)
                    if 1<=roulette_number<=18:
                        print("You win")
                        winnings = amount_bet * 2
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
                elif half_pick == 2:
                    mensagem = "You picked the second half."
                    print(mensagem)
                    if 19<=roulette_number<=36:
                        print("You win")
                        winnings = amount_bet * 2
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
            elif roulette_bet==10:
                print("Choose Dozen")
                print("1-First Dozen (Includes 1-12)")
                print("2-Second Dozen (Includes 13-24)")
                print("3-Third Dozen (Includes 25-36)")
                dozen_pick = int(input("Make your pick:"))
                while dozen_pick != 1 and dozen_pick != 2 and dozen_pick != 3:
                    dozen_pick = int(input("Make your pick between the first dozen (type 1) or the second dozen (type 2) or the third dozen (type 3):"))
                print("closing bets")
                if dozen_pick == 1:
                    mensagem = "You picked the first dozen."
                    print(mensagem)
                    mensagem = "The lucky number is" + str(roulette_number)
                    print(mensagem)
                    if 1<=roulette_number<=12:
                        print("You win")
                        winnings = amount_bet * 3
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
                elif dozen_pick == 2:
                    mensagem = "You picked the second dozen."
                    print(mensagem)
                    mensagem = "The lucky number is" + str(roulette_number)
                    print(mensagem)
                    if 13 <= roulette_number <= 24:
                        print("You win")
                        winnings = amount_bet * 3
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
                elif dozen_pick == 3:
                    mensagem = "You picked the third dozen."
                    print(mensagem)
                    mensagem = "The lucky number is" + str(roulette_number)
                    print(mensagem)
                    if 25 <= roulette_number <= 36:
                        print("You win")
                        winnings = amount_bet * 3
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
            elif roulette_bet==11:
                print("Choose Column")
                print("1-First Column (Includes 1,4,7,10,13,16,19,22,25,28,31,34)")
                print("2-Second Column (Includes 2,5,8,11,14,17,20,23,26,29,32,35)")
                print("3-Third Column (Includes 3,6,9,12,15,18,21,24,27,30,33,36)")
                column_pick = int(input("Make your pick:"))
                while column_pick != 1 and column_pick != 2 and column_pick != 3:
                    column_pick = int(input("Make your pick between the first column (type 1) or the second column (type 2) or the third column (type 3):"))
                print("closing bets")
                if column_pick == 1:
                    mensagem = "You picked the first column."
                    print(mensagem)
                    mensagem = "The lucky number is" + str(roulette_number)
                    print(mensagem)
                    if roulette_number == 1 or roulette_number == 4 or roulette_number == 7 or roulette_number == 10 or roulette_number == 13 or roulette_number == 16 or roulette_number == 19 or roulette_number == 22 or roulette_number == 25 or roulette_number == 28 or roulette_number == 31 or roulette_number == 34:
                        print("You win")
                        winnings = amount_bet * 3
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
                elif column_pick == 2:
                    mensagem = "You picked the second column."
                    print(mensagem)
                    mensagem = "The lucky number is" + str(roulette_number)
                    print(mensagem)
                    if roulette_number == 2 or roulette_number == 5 or roulette_number == 8 or roulette_number == 11 or roulette_number == 14 or roulette_number == 17 or roulette_number == 20 or roulette_number == 23 or roulette_number == 26 or roulette_number == 29 or roulette_number == 32 or roulette_number == 35:
                        print("You win")
                        winnings = amount_bet * 3
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
                elif column_pick == 3:
                    mensagem = "You picked the third column."
                    print(mensagem)
                    mensagem = "The lucky number is" + str(roulette_number)
                    print(mensagem)
                    if roulette_number == 3 or roulette_number == 6 or roulette_number == 9 or roulette_number == 12 or roulette_number == 15 or roulette_number == 18 or roulette_number == 21 or roulette_number == 24 or roulette_number == 27 or roulette_number == 30 or roulette_number == 33 or roulette_number == 36:
                        print("You win")
                        winnings = amount_bet * 3
                        chips = chips + winnings
                        print("you have " + str(chips) + " chips")
                    else:
                        print("You lose")
                        print("you have " + str(chips) + " chips, left")
            if chips<=0:
                print("You lose")
                print("you have "+str(chips)+" chips")
                reset=False
            else:
                print("Would you like to continue?")
                print("1-Yes")
                print("2-No")
                replay=int(input("select an option:"))
                if replay == 1:
                    reset_1 = True
                elif replay == 2:
                    restart=True
    elif menu_pick==3:
        print("======================================")
        print("How many players would like to player:")
        print("1-Single player")
        print("2-Double player")
        print("3-Triple player")
        print("4-four player")
        player_count=int(input("select an option:"))
        while 1>player_count>4:
            player_count = int(input("select an option between 1 and 4:"))
        if player_count == 1:
            player_1=True
            player_1_name = input("Write name for player 1:")
            player_1_chips = 30
            player_1_active = True
        elif player_count == 2:
            player_1=True
            player_2=True
            player_1_name = input("Write name for player 1:")
            player_2_name = input("Write name for player 2:")
            player_1_chips = 30
            player_2_chips = 30
            player_1_active = True
            player_2_active = True
        elif player_count == 3:
            player_1=True
            player_2=True
            player_3=True
            player_1_name = input("Write name for player 1:")
            player_2_name = input("Write name for player 2:")
            player_3_name = input("Write name for player 3:")
            player_1_chips = 30
            player_2_chips = 30
            player_3_chips = 30
            player_1_active = True
            player_2_active = True
            player_3_active = True
        elif player_count == 4:
            player_1=True
            player_2=True
            player_3=True
            player_4=True
            player_1_name = input("Write name for player 1:")
            player_2_name = input("Write name for player 2:")
            player_3_name = input("Write name for player 3:")
            player_4_name = input("Write name for player 4:")
            player_1_chips = 30
            player_2_chips = 30
            player_3_chips = 30
            player_4_chips = 30
            player_1_active = True
            player_2_active = True
            player_3_active = True
            player_4_active = True
        rounds=int(input("How many rounds would you like to play:"))
        for i in range(1,rounds+1):
            print("Place your bets")
            print("1-Numero")
            print("2-Split")
            print("3-Street")
            print("4-Corner")
            print("5-Line")
            print("6-Color")
            print("7-Odd")
            print("8-Even")
            print("9-Half")
            print("10-Dozen")
            print("11-Column")
            roulette_number=random.randint(0,36)
            if player_1:
                if player_1_chips <= 0:
                    print("Player 1 is out")
                    print("you have " + str(player_1_chips) + " chips")
                    player_1 = False
                roulette_bet = int(input("Place your bets, player 1:"))
                while roulette_bet <= 0 or roulette_bet > 11:
                    print("Pick a number between 1 and 11")
                amount_bet = int(input("Place the amount you want to bet:"))
                while amount_bet > player_1_chips:
                    mensagem = "Cannot bet more than the amount of chips you have, which is:" + str(player_1_chips)
                    print(mensagem)
                    amount_bet = int(input("Place the amount you want to bet, another time:"))
                player_1_chips = player_1_chips - amount_bet
                if roulette_bet == 1:
                    roulette_guess = int(input("enter your guess between 0 and 36, player 1:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    mensagem = "You picked " + str(roulette_guess) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number:
                        player_1_winnings = amount_bet * 40
                        player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 2:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 1:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1 or roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31 or roulette_guess == 34:
                        double = roulette_guess + 1
                    elif roulette_guess == 3 or roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33 or roulette_guess == 36:
                        double = roulette_guess - 1
                    elif roulette_guess == 2 or roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32 or roulette_guess == 35:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        if ahead_behind == 1:
                            roulette_guess = roulette_guess + 1
                        elif ahead_behind == 2:
                            roulette_guess = roulette_guess - 1
                    mensagem = player_1_name + " picked" + str(roulette_guess) + "," + str(double) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or double == roulette_number:
                        player_1_winnings = amount_bet * 20
                        player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 3:
                    roulette_guess = int(input("enter your guess between 1 and 36 player 1:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1 or roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31 or roulette_guess == 34:
                        triple1 = roulette_guess + 1
                        triple2 = roulette_guess + 2
                    elif roulette_guess == 3 or roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33 or roulette_guess == 36:
                        triple1 = roulette_guess - 1
                        triple2 = roulette_guess - 2
                    elif roulette_guess == 2 or roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32 or roulette_guess == 35:
                        triple1 = roulette_guess - 1
                        triple2 = roulette_guess + 1
                    mensagem = player_1_name + " picked " + str(roulette_guess) + "," + str(triple1) + "," + str(triple2) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or triple1 == roulette_number or triple2 == roulette_number:
                        player_1_winnings = amount_bet * 15
                        player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 4:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 1:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess + 3
                        quad3 = roulette_guess + 4
                    elif roulette_guess == 3:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess + 2
                        quad3 = roulette_guess + 3
                    elif roulette_guess == 2:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        while ahead_behind != 1 and ahead_behind != 2:
                            ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                        if ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess + 3
                            quad3 = roulette_guess + 4
                        elif ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess + 2
                            quad3 = roulette_guess + 3
                    elif roulette_guess == 34:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess - 2
                        quad3 = roulette_guess - 3
                    elif roulette_guess == 36:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess - 3
                        quad3 = roulette_guess - 4
                    elif roulette_guess == 35:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        while ahead_behind != 1 and ahead_behind != 2:
                            ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                        if ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess - 2
                            quad3 = roulette_guess - 3
                        elif ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess - 3
                            quad3 = roulette_guess - 4
                    else:
                        print("1-Above")
                        print("2-Below")
                        above_below = int(input("Would you like to choose one above or one below:"))
                        while above_below != 1 and above_below != 2:
                            above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                        if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                            quad1 = roulette_guess - 1
                            if above_below == 1:
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 4
                            elif above_below == 2:
                                quad2 = roulette_guess + 2
                                quad3 = roulette_guess + 3
                        elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                            quad1 = roulette_guess + 1
                            if above_below == 1:
                                quad2 = roulette_guess - 2
                                quad3 = roulette_guess - 3
                            elif above_below == 2:
                                quad2 = roulette_guess + 3
                                quad3 = roulette_guess + 4
                        elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                            print("1-Ahead")
                            print("2-Behind")
                            ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                            if above_below == 1 and ahead_behind == 1:
                                quad1 = roulette_guess + 1
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 2
                            elif above_below == 1 and ahead_behind == 2:
                                quad1 = roulette_guess - 1
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 4
                            elif above_below == 2 and ahead_behind == 1:
                                quad1 = roulette_guess + 1
                                quad2 = roulette_guess + 3
                                quad3 = roulette_guess + 4
                            elif above_below == 2 and ahead_behind == 2:
                                quad1 = roulette_guess - 1
                                quad2 = roulette_guess + 2
                                quad3 = roulette_guess + 3
                    mensagem = "You picked " + str(roulette_guess) + "," + str(quad1) + "," + str(quad2) + "," + str(quad3) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or quad1 == roulette_number or quad2 == roulette_number or quad3 == roulette_number:
                        player_1_winnings = amount_bet * 10
                        player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 5:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 1:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    if roulette_guess == 1:
                        six1 = roulette_guess + 1
                        six2 = roulette_guess + 2
                        six3 = roulette_guess + 3
                        six4 = roulette_guess + 4
                        six5 = roulette_guess + 5
                    elif roulette_guess == 2:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess + 1
                        six3 = roulette_guess + 2
                        six4 = roulette_guess + 3
                        six5 = roulette_guess + 4
                    elif roulette_guess == 3:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess - 2
                        six3 = roulette_guess + 1
                        six4 = roulette_guess + 2
                        six5 = roulette_guess + 3
                    elif roulette_guess == 34:
                        six1 = roulette_guess - 3
                        six2 = roulette_guess - 2
                        six3 = roulette_guess - 1
                        six4 = roulette_guess + 1
                        six5 = roulette_guess + 2
                    elif roulette_guess == 35:
                        six1 = roulette_guess - 4
                        six2 = roulette_guess - 3
                        six3 = roulette_guess - 2
                        six4 = roulette_guess - 1
                        six5 = roulette_guess + 1
                    elif roulette_guess == 36:
                        six1 = roulette_guess - 5
                        six2 = roulette_guess - 4
                        six3 = roulette_guess - 3
                        six4 = roulette_guess - 2
                        six5 = roulette_guess - 1
                    else:
                        print("1-Above")
                        print("2-Below")
                        above_below = int(input("Would you like to choose one above or one below:"))
                        if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                            six1 = roulette_guess - 1
                            six2 = roulette_guess - 2
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 3
                                six4 = roulette_guess - 4
                                six5 = roulette_guess - 5
                            elif above_below == 2:
                                six3 = roulette_guess + 1
                                six4 = roulette_guess + 2
                                six5 = roulette_guess + 3
                        elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                            six1 = roulette_guess + 1
                            six2 = roulette_guess + 2
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 3
                                six4 = roulette_guess - 2
                                six5 = roulette_guess - 1
                            elif above_below == 2:
                                six3 = roulette_guess + 3
                                six4 = roulette_guess + 4
                                six5 = roulette_guess + 5
                        elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                            six1 = roulette_guess - 1
                            six2 = roulette_guess + 1
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 2
                                six4 = roulette_guess - 3
                                six5 = roulette_guess - 4
                            elif above_below == 2:
                                six3 = roulette_guess + 2
                                six4 = roulette_guess + 3
                                six5 = roulette_guess + 4
                    mensagem = "You picked " + str(roulette_guess) + "," + str(six1) + "," + str(six2) + "," + str(six3) + "," + str(six4) + "," + str(six5) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or six1 == roulette_number or six2 == roulette_number or six3 == roulette_number or six4 == roulette_number or six5 == roulette_number:
                        player_1_winnings = amount_bet * 8
                        player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 6:
                    print("Choose a color")
                    print("1-Red (Includes 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)")
                    print("2-Black (Includes 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)")
                    color_pick = int(input("Make your pick:"))
                    while color_pick != 1 and color_pick != 2:
                        color_pick = int(input("Make your pick between red (type 1) or black (type 2):"))
                    if color_pick == 1:
                        print(player_1_name+" picked red")
                        if roulette_number == 1 or roulette_number == 3 or roulette_number == 5 or roulette_number == 7 or roulette_number == 9 or roulette_number == 12 or roulette_number == 14 or roulette_number == 16 or roulette_number == 18 or roulette_number == 19 or roulette_number == 21 or roulette_number == 23 or roulette_number == 25 or roulette_number == 27 or roulette_number == 30 or roulette_number == 32 or roulette_number == 34 or roulette_number == 36:
                            player_1_winnings = amount_bet * 2
                            player_1_chips = player_1_chips + player_1_winnings
                    elif color_pick == 2:
                        print(player_1_name+" picked black")
                        if roulette_number == 2 or roulette_number == 4 or roulette_number == 6 or roulette_number == 8 or roulette_number == 10 or roulette_number == 11 or roulette_number == 13 or roulette_number == 15 or roulette_number == 17 or roulette_number == 20 or roulette_number == 22 or roulette_number == 24 or roulette_number == 26 or roulette_number == 28 or roulette_number == 29 or roulette_number == 31 or roulette_number == 33 or roulette_number == 35:
                            player_1_winnings = amount_bet * 2
                            player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 7:
                    print(player_1_name+" picked odd")
                    if roulette_number % 2 != 0:
                        player_1_winnings = amount_bet * 2
                        player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 8:
                    print(player_1_name +" picked Even")
                    if roulette_number % 2 == 0:
                        player_1_winnings = amount_bet * 2
                        player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 9:
                    print("Choose Half")
                    print("1-First Half (Includes 1-18)")
                    print("2-Second Half (Includes 19-36)")
                    half_pick = int(input("Make your pick:"))
                    while half_pick != 1 and half_pick != 2:
                        half_pick = int(input("Make your pick between the first half (type 1) or the second half (type 2):"))
                    if half_pick == 1:
                        mensagem = "You picked the first half."
                        print(mensagem)
                        if 1 <= roulette_number <= 18:
                            player_1_winnings = amount_bet * 2
                            player_1_chips = player_1_chips + player_1_winnings
                    elif half_pick == 2:
                        mensagem = "You picked the second half."
                        print(mensagem)
                        if 19 <= roulette_number <= 36:
                            player_1_winnings = amount_bet * 2
                            player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 10:
                    print("Choose Dozen")
                    print("1-First Dozen (Includes 1-12)")
                    print("2-Second Dozen (Includes 13-24)")
                    print("3-Third Dozen (Includes 25-36)")
                    dozen_pick = int(input("Make your pick:"))
                    while dozen_pick != 1 and dozen_pick != 2 and dozen_pick != 3:
                        dozen_pick = int(input("Make your pick between the first dozen (type 1) or the second dozen (type 2) or the third dozen (type 3):"))
                    if dozen_pick == 1:
                        mensagem = "You picked the first dozen."
                        print(mensagem)
                        if 1 <= roulette_number <= 12:
                            player_1_winnings = amount_bet * 3
                            player_1_chips = player_1_chips + player_1_winnings
                    elif dozen_pick == 2:
                        mensagem = "You picked the second dozen."
                        print(mensagem)
                        if 13 <= roulette_number <= 24:
                            player_1_winnings = amount_bet * 3
                            player_1_chips = player_1_chips + player_1_winnings
                    elif dozen_pick == 3:
                        mensagem = "You picked the third dozen."
                        print(mensagem)
                        if 25 <= roulette_number <= 36:
                            player_1_winnings = amount_bet * 3
                            player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 11:
                    print("Choose Column")
                    print("1-First Column (Includes 1,4,7,10,13,16,19,22,25,28,31,34)")
                    print("2-Second Column (Includes 2,5,8,11,14,17,20,23,26,29,32,35)")
                    print("3-Third Column (Includes 3,6,9,12,15,18,21,24,27,30,33,36)")
                    column_pick = int(input("Make your pick:"))
                    while column_pick != 1 and column_pick != 2 and column_pick != 3:
                        column_pick = int(input("Make your pick between the first column (type 1) or the second column (type 2) or the third column (type 3):"))
                    if column_pick == 1:
                        mensagem = player_1_name+ " picked the first column."
                        print(mensagem)
                        if roulette_number == 1 or roulette_number == 4 or roulette_number == 7 or roulette_number == 10 or roulette_number == 13 or roulette_number == 16 or roulette_number == 19 or roulette_number == 22 or roulette_number == 25 or roulette_number == 28 or roulette_number == 31 or roulette_number == 34:
                            player_1_winnings = amount_bet * 3
                            player_1_chips = player_1_chips + player_1_winnings
                    elif column_pick == 2:
                        mensagem = player_1_name +" picked the second column."
                        print(mensagem)
                        if roulette_number == 2 or roulette_number == 5 or roulette_number == 8 or roulette_number == 11 or roulette_number == 14 or roulette_number == 17 or roulette_number == 20 or roulette_number == 23 or roulette_number == 26 or roulette_number == 29 or roulette_number == 32 or roulette_number == 35:
                            player_1_winnings = amount_bet * 3
                            player_1_chips = player_1_chips + player_1_winnings
                    elif column_pick == 3:
                        mensagem = player_1_name+ " picked the third column."
                        print(mensagem)
                        if roulette_number == 3 or roulette_number == 6 or roulette_number == 9 or roulette_number == 12 or roulette_number == 15 or roulette_number == 18 or roulette_number == 21 or roulette_number == 24 or roulette_number == 27 or roulette_number == 30 or roulette_number == 33 or roulette_number == 36:
                            player_1_winnings = amount_bet * 3
                            player_1_chips = player_1_chips + player_1_winnings
            if player_2:
                if player_2_chips <= 0:
                    print("Player 2 is out")
                    print("you have " + str(player_2_chips) + " chips")
                    player_2 = False
                roulette_bet = int(input("Place your bets, player 2:"))
                while roulette_bet <= 0 or roulette_bet > 11:
                    print("Pick a number between 1 and 11")
                amount_bet = int(input("Place the amount you want to bet:"))
                while amount_bet > player_2_chips:
                    mensagem = "Cannot bet more than the amount of chips you have, which is:" + str(player_2_chips)
                    print(mensagem)
                    amount_bet = int(input("Place the amount you want to bet, another time:"))
                player_2_chips = player_2_chips - amount_bet
                if roulette_bet == 1:
                    roulette_guess = int(input("enter your guess between 0 and 36, player 2:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    mensagem = "You picked " + str(roulette_guess) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number:
                        player_2_winnings = amount_bet * 40
                        player_2_chips = player_2_chips + player_2_winnings
                elif roulette_bet == 2:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 1:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1 or roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31 or roulette_guess == 34:
                        double = roulette_guess + 1
                    elif roulette_guess == 3 or roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33 or roulette_guess == 36:
                        double = roulette_guess - 1
                    elif roulette_guess == 2 or roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32 or roulette_guess == 35:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        if ahead_behind == 1:
                            roulette_guess = roulette_guess + 1
                        elif ahead_behind == 2:
                            roulette_guess = roulette_guess - 1
                    mensagem = player_1_name + " picked" + str(roulette_guess) + "," + str(double) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or double == roulette_number:
                        player_1_winnings = amount_bet * 20
                        player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 3:
                    roulette_guess = int(input("enter your guess between 1 and 36 player 2:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1 or roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31 or roulette_guess == 34:
                        triple1 = roulette_guess + 1
                        triple2 = roulette_guess + 2
                    elif roulette_guess == 3 or roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33 or roulette_guess == 36:
                        triple1 = roulette_guess - 1
                        triple2 = roulette_guess - 2
                    elif roulette_guess == 2 or roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32 or roulette_guess == 35:
                        triple1 = roulette_guess - 1
                        triple2 = roulette_guess + 1
                    mensagem = player_2_name + " picked " + str(roulette_guess) + "," + str(triple1) + "," + str(triple2) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or triple1 == roulette_number or triple2 == roulette_number:
                        player_2_winnings = amount_bet * 15
                        player_2_chips = player_2_chips + player_2_winnings
                elif roulette_bet == 4:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 2:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess + 3
                        quad3 = roulette_guess + 4
                    elif roulette_guess == 3:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess + 2
                        quad3 = roulette_guess + 3
                    elif roulette_guess == 2:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        while ahead_behind != 1 and ahead_behind != 2:
                            ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                        if ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess + 3
                            quad3 = roulette_guess + 4
                        elif ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess + 2
                            quad3 = roulette_guess + 3
                    elif roulette_guess == 34:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess - 2
                        quad3 = roulette_guess - 3
                    elif roulette_guess == 36:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess - 3
                        quad3 = roulette_guess - 4
                    elif roulette_guess == 35:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        while ahead_behind != 1 and ahead_behind != 2:
                            ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                        if ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess - 2
                            quad3 = roulette_guess - 3
                        elif ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess - 3
                            quad3 = roulette_guess - 4
                    else:
                        print("1-Above")
                        print("2-Below")
                        above_below = int(input("Would you like to choose one above or one below:"))
                        while above_below != 1 and above_below != 2:
                            above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                        if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                            quad1 = roulette_guess - 1
                            if above_below == 1:
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 4
                            elif above_below == 2:
                                quad2 = roulette_guess + 2
                                quad3 = roulette_guess + 3
                        elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                            quad1 = roulette_guess + 1
                            if above_below == 1:
                                quad2 = roulette_guess - 2
                                quad3 = roulette_guess - 3
                            elif above_below == 2:
                                quad2 = roulette_guess + 3
                                quad3 = roulette_guess + 4
                        elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                            print("1-Ahead")
                            print("2-Behind")
                            ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                            if above_below == 1 and ahead_behind == 1:
                                quad1 = roulette_guess + 1
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 2
                            elif above_below == 1 and ahead_behind == 2:
                                quad1 = roulette_guess - 1
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 4
                            elif above_below == 2 and ahead_behind == 1:
                                quad1 = roulette_guess + 1
                                quad2 = roulette_guess + 3
                                quad3 = roulette_guess + 4
                            elif above_below == 2 and ahead_behind == 2:
                                quad1 = roulette_guess - 1
                                quad2 = roulette_guess + 2
                                quad3 = roulette_guess + 3
                    mensagem = "You picked " + str(roulette_guess) + "," + str(quad1) + "," + str(quad2) + "," + str(quad3) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or quad1 == roulette_number or quad2 == roulette_number or quad3 == roulette_number:
                        player_2_winnings = amount_bet * 10
                        player_2_chips = player_2_chips + player_2_winnings
                elif roulette_bet == 5:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 1:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    if roulette_guess == 1:
                        six1 = roulette_guess + 1
                        six2 = roulette_guess + 2
                        six3 = roulette_guess + 3
                        six4 = roulette_guess + 4
                        six5 = roulette_guess + 5
                    elif roulette_guess == 2:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess + 1
                        six3 = roulette_guess + 2
                        six4 = roulette_guess + 3
                        six5 = roulette_guess + 4
                    elif roulette_guess == 3:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess - 2
                        six3 = roulette_guess + 1
                        six4 = roulette_guess + 2
                        six5 = roulette_guess + 3
                    elif roulette_guess == 34:
                        six1 = roulette_guess - 3
                        six2 = roulette_guess - 2
                        six3 = roulette_guess - 1
                        six4 = roulette_guess + 1
                        six5 = roulette_guess + 2
                    elif roulette_guess == 35:
                        six1 = roulette_guess - 4
                        six2 = roulette_guess - 3
                        six3 = roulette_guess - 2
                        six4 = roulette_guess - 1
                        six5 = roulette_guess + 1
                    elif roulette_guess == 36:
                        six1 = roulette_guess - 5
                        six2 = roulette_guess - 4
                        six3 = roulette_guess - 3
                        six4 = roulette_guess - 2
                        six5 = roulette_guess - 1
                    else:
                        print("1-Above")
                        print("2-Below")
                        above_below = int(input("Would you like to choose one above or one below:"))
                        if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                            six1 = roulette_guess - 1
                            six2 = roulette_guess - 2
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 3
                                six4 = roulette_guess - 4
                                six5 = roulette_guess - 5
                            elif above_below == 2:
                                six3 = roulette_guess + 1
                                six4 = roulette_guess + 2
                                six5 = roulette_guess + 3
                        elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                            six1 = roulette_guess + 1
                            six2 = roulette_guess + 2
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 3
                                six4 = roulette_guess - 2
                                six5 = roulette_guess - 1
                            elif above_below == 2:
                                six3 = roulette_guess + 3
                                six4 = roulette_guess + 4
                                six5 = roulette_guess + 5
                        elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                            six1 = roulette_guess - 1
                            six2 = roulette_guess + 1
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 2
                                six4 = roulette_guess - 3
                                six5 = roulette_guess - 4
                            elif above_below == 2:
                                six3 = roulette_guess + 2
                                six4 = roulette_guess + 3
                                six5 = roulette_guess + 4
                    mensagem = "You picked " + str(roulette_guess) + "," + str(six1) + "," + str(six2) + "," + str(six3) + "," + str(six4) + "," + str(six5) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or six1 == roulette_number or six2 == roulette_number or six3 == roulette_number or six4 == roulette_number or six5 == roulette_number:
                        player_1_winnings = amount_bet * 8
                        player_1_chips = player_1_chips + player_1_winnings
                elif roulette_bet == 6:
                    print("Choose a color")
                    print("1-Red (Includes 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)")
                    print("2-Black (Includes 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)")
                    color_pick = int(input("Make your pick:"))
                    while color_pick != 1 and color_pick != 2:
                        color_pick = int(input("Make your pick between red (type 1) or black (type 2):"))
                    if color_pick == 1:
                        print(player_2_name+" picked red")
                        if roulette_number == 1 or roulette_number == 3 or roulette_number == 5 or roulette_number == 7 or roulette_number == 9 or roulette_number == 12 or roulette_number == 14 or roulette_number == 16 or roulette_number == 18 or roulette_number == 19 or roulette_number == 21 or roulette_number == 23 or roulette_number == 25 or roulette_number == 27 or roulette_number == 30 or roulette_number == 32 or roulette_number == 34 or roulette_number == 36:
                            player_2_winnings = amount_bet * 2
                            player_2_chips = player_2_chips + player_2_winnings
                    elif color_pick == 2:
                        print(player_2_name+" picked black")
                        if roulette_number == 2 or roulette_number == 4 or roulette_number == 6 or roulette_number == 8 or roulette_number == 10 or roulette_number == 11 or roulette_number == 13 or roulette_number == 15 or roulette_number == 17 or roulette_number == 20 or roulette_number == 22 or roulette_number == 24 or roulette_number == 26 or roulette_number == 28 or roulette_number == 29 or roulette_number == 31 or roulette_number == 33 or roulette_number == 35:
                            player_2_winnings = amount_bet * 2
                            player_2_chips = player_2_chips + player_2_winnings
                elif roulette_bet == 7:
                    print(player_2_name+" picked odd")
                    if roulette_number % 2 != 0:
                        player_2_winnings = amount_bet * 2
                        player_2_chips = player_2_chips + player_2_winnings
                elif roulette_bet == 8:
                    print(player_2_name +" picked Even")
                    if roulette_number % 2 == 0:
                        player_2_winnings = amount_bet * 2
                        player_2_chips = player_2_chips + player_2_winnings
                elif roulette_bet == 9:
                    print("Choose Half")
                    print("1-First Half (Includes 1-18)")
                    print("2-Second Half (Includes 19-36)")
                    half_pick = int(input("Make your pick:"))
                    while half_pick != 1 and half_pick != 2:
                        half_pick = int(input("Make your pick between the first half (type 1) or the second half (type 2):"))
                    if half_pick == 1:
                        mensagem = "You picked the first half."
                        print(mensagem)
                        if 1 <= roulette_number <= 18:
                            player_2_winnings = amount_bet * 2
                            player_2_chips = player_2_chips + player_2_winnings
                    elif half_pick == 2:
                        mensagem = "You picked the second half."
                        print(mensagem)
                        if 19 <= roulette_number <= 36:
                            player_2_winnings = amount_bet * 2
                            player_2_chips = player_2_chips + player_2_winnings
                elif roulette_bet == 10:
                    print("Choose Dozen")
                    print("1-First Dozen (Includes 1-12)")
                    print("2-Second Dozen (Includes 13-24)")
                    print("3-Third Dozen (Includes 25-36)")
                    dozen_pick = int(input("Make your pick:"))
                    while dozen_pick != 1 and dozen_pick != 2 and dozen_pick != 3:
                        dozen_pick = int(input("Make your pick between the first dozen (type 1) or the second dozen (type 2) or the third dozen (type 3):"))
                    if dozen_pick == 1:
                        mensagem = "You picked the first dozen."
                        print(mensagem)
                        if 1 <= roulette_number <= 12:
                            player_2_winnings = amount_bet * 3
                            player_2_chips = player_2_chips + player_2_winnings
                    elif dozen_pick == 2:
                        mensagem = "You picked the second dozen."
                        print(mensagem)
                        if 13 <= roulette_number <= 24:
                            player_2_winnings = amount_bet * 3
                            player_2_chips = player_2_chips + player_2_winnings
                    elif dozen_pick == 3:
                        mensagem = "You picked the third dozen."
                        print(mensagem)
                        if 25 <= roulette_number <= 36:
                            player_2_winnings = amount_bet * 3
                            player_2_chips = player_2_chips + player_2_winnings
                elif roulette_bet == 11:
                    print("Choose Column")
                    print("1-First Column (Includes 1,4,7,10,13,16,19,22,25,28,31,34)")
                    print("2-Second Column (Includes 2,5,8,11,14,17,20,23,26,29,32,35)")
                    print("3-Third Column (Includes 3,6,9,12,15,18,21,24,27,30,33,36)")
                    column_pick = int(input("Make your pick:"))
                    while column_pick != 1 and column_pick != 2 and column_pick != 3:
                        column_pick = int(input("Make your pick between the first column (type 1) or the second column (type 2) or the third column (type 3):"))
                    if column_pick == 1:
                        mensagem = player_2_name+ " picked the first column."
                        print(mensagem)
                        if roulette_number == 1 or roulette_number == 4 or roulette_number == 7 or roulette_number == 10 or roulette_number == 13 or roulette_number == 16 or roulette_number == 19 or roulette_number == 22 or roulette_number == 25 or roulette_number == 28 or roulette_number == 31 or roulette_number == 34:
                            player_2_winnings = amount_bet * 3
                            player_2_chips = player_2_chips + player_2_winnings
                    elif column_pick == 2:
                        mensagem = player_2_name +" picked the second column."
                        print(mensagem)
                        if roulette_number == 2 or roulette_number == 5 or roulette_number == 8 or roulette_number == 11 or roulette_number == 14 or roulette_number == 17 or roulette_number == 20 or roulette_number == 23 or roulette_number == 26 or roulette_number == 29 or roulette_number == 32 or roulette_number == 35:
                            player_2_winnings = amount_bet * 3
                            player_2_chips = player_2_chips + player_2_winnings
                    elif column_pick == 3:
                        mensagem = player_2_name+ " picked the third column."
                        print(mensagem)
                        if roulette_number == 3 or roulette_number == 6 or roulette_number == 9 or roulette_number == 12 or roulette_number == 15 or roulette_number == 18 or roulette_number == 21 or roulette_number == 24 or roulette_number == 27 or roulette_number == 30 or roulette_number == 33 or roulette_number == 36:
                            player_2_winnings = amount_bet * 3
                            player_2_chips = player_2_chips + player_2_winnings
            if player_3:
                if player_3_chips <= 0:
                    print("Player 3 is out")
                    print("you have " + str(player_3_chips) + " chips")
                    player_3 = False
                roulette_bet = int(input("Place your bets, player 3:"))
                while roulette_bet <= 0 or roulette_bet > 11:
                    print("Pick a number between 1 and 11")
                amount_bet = int(input("Place the amount you want to bet:"))
                while amount_bet > player_3_chips:
                    mensagem = "Cannot bet more than the amount of chips you have, which is:" + str(player_3_chips)
                    print(mensagem)
                    amount_bet = int(input("Place the amount you want to bet, another time:"))
                player_3_chips = player_3_chips - amount_bet
                if roulette_bet == 1:
                    roulette_guess = int(input("enter your guess between 0 and 36, player 3:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    mensagem = "You picked " + str(roulette_guess) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number:
                        player_3_winnings = amount_bet * 40
                        player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 2:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 3:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1 or roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31 or roulette_guess == 34:
                        double = roulette_guess + 1
                    elif roulette_guess == 3 or roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33 or roulette_guess == 36:
                        double = roulette_guess - 1
                    elif roulette_guess == 2 or roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32 or roulette_guess == 35:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        if ahead_behind == 1:
                            roulette_guess = roulette_guess + 1
                        elif ahead_behind == 2:
                            roulette_guess = roulette_guess - 1
                    mensagem = player_3_name + " picked" + str(roulette_guess) + "," + str(double) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or double == roulette_number:
                        player_3_winnings = amount_bet * 20
                        player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 3:
                    roulette_guess = int(input("enter your guess between 1 and 36 player 3:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1 or roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31 or roulette_guess == 34:
                        triple1 = roulette_guess + 1
                        triple2 = roulette_guess + 2
                    elif roulette_guess == 3 or roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33 or roulette_guess == 36:
                        triple1 = roulette_guess - 1
                        triple2 = roulette_guess - 2
                    elif roulette_guess == 2 or roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32 or roulette_guess == 35:
                        triple1 = roulette_guess - 1
                        triple2 = roulette_guess + 1
                    mensagem = player_3_name + " picked " + str(roulette_guess) + "," + str(triple1) + "," + str(triple2) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or triple1 == roulette_number or triple2 == roulette_number:
                        player_3_winnings = amount_bet * 15
                        player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 4:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 3:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess + 3
                        quad3 = roulette_guess + 4
                    elif roulette_guess == 3:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess + 2
                        quad3 = roulette_guess + 3
                    elif roulette_guess == 2:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        while ahead_behind != 1 and ahead_behind != 2:
                            ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                        if ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess + 3
                            quad3 = roulette_guess + 4
                        elif ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess + 2
                            quad3 = roulette_guess + 3
                    elif roulette_guess == 34:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess - 2
                        quad3 = roulette_guess - 3
                    elif roulette_guess == 36:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess - 3
                        quad3 = roulette_guess - 4
                    elif roulette_guess == 35:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        while ahead_behind != 1 and ahead_behind != 2:
                            ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                        if ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess - 2
                            quad3 = roulette_guess - 3
                        elif ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess - 3
                            quad3 = roulette_guess - 4
                    else:
                        print("1-Above")
                        print("2-Below")
                        above_below = int(input("Would you like to choose one above or one below:"))
                        while above_below != 1 and above_below != 2:
                            above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                        if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                            quad1 = roulette_guess - 1
                            if above_below == 1:
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 4
                            elif above_below == 2:
                                quad2 = roulette_guess + 2
                                quad3 = roulette_guess + 3
                        elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                            quad1 = roulette_guess + 1
                            if above_below == 1:
                                quad2 = roulette_guess - 2
                                quad3 = roulette_guess - 3
                            elif above_below == 2:
                                quad2 = roulette_guess + 3
                                quad3 = roulette_guess + 4
                        elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                            print("1-Ahead")
                            print("2-Behind")
                            ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                            if above_below == 1 and ahead_behind == 1:
                                quad1 = roulette_guess + 1
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 2
                            elif above_below == 1 and ahead_behind == 2:
                                quad1 = roulette_guess - 1
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 4
                            elif above_below == 2 and ahead_behind == 1:
                                quad1 = roulette_guess + 1
                                quad2 = roulette_guess + 3
                                quad3 = roulette_guess + 4
                            elif above_below == 2 and ahead_behind == 2:
                                quad1 = roulette_guess - 1
                                quad2 = roulette_guess + 2
                                quad3 = roulette_guess + 3
                    mensagem = "You picked " + str(roulette_guess) + "," + str(quad1) + "," + str(quad2) + "," + str(quad3) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or quad1 == roulette_number or quad2 == roulette_number or quad3 == roulette_number:
                        player_3_winnings = amount_bet * 10
                        player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 5:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 3:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    if roulette_guess == 1:
                        six1 = roulette_guess + 1
                        six2 = roulette_guess + 2
                        six3 = roulette_guess + 3
                        six4 = roulette_guess + 4
                        six5 = roulette_guess + 5
                    elif roulette_guess == 2:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess + 1
                        six3 = roulette_guess + 2
                        six4 = roulette_guess + 3
                        six5 = roulette_guess + 4
                    elif roulette_guess == 3:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess - 2
                        six3 = roulette_guess + 1
                        six4 = roulette_guess + 2
                        six5 = roulette_guess + 3
                    elif roulette_guess == 34:
                        six1 = roulette_guess - 3
                        six2 = roulette_guess - 2
                        six3 = roulette_guess - 1
                        six4 = roulette_guess + 1
                        six5 = roulette_guess + 2
                    elif roulette_guess == 35:
                        six1 = roulette_guess - 4
                        six2 = roulette_guess - 3
                        six3 = roulette_guess - 2
                        six4 = roulette_guess - 1
                        six5 = roulette_guess + 1
                    elif roulette_guess == 36:
                        six1 = roulette_guess - 5
                        six2 = roulette_guess - 4
                        six3 = roulette_guess - 3
                        six4 = roulette_guess - 2
                        six5 = roulette_guess - 1
                    else:
                        print("1-Above")
                        print("2-Below")
                        above_below = int(input("Would you like to choose one above or one below:"))
                        if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                            six1 = roulette_guess - 1
                            six2 = roulette_guess - 2
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 3
                                six4 = roulette_guess - 4
                                six5 = roulette_guess - 5
                            elif above_below == 2:
                                six3 = roulette_guess + 1
                                six4 = roulette_guess + 2
                                six5 = roulette_guess + 3
                        elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                            six1 = roulette_guess + 1
                            six2 = roulette_guess + 2
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 3
                                six4 = roulette_guess - 2
                                six5 = roulette_guess - 1
                            elif above_below == 2:
                                six3 = roulette_guess + 3
                                six4 = roulette_guess + 4
                                six5 = roulette_guess + 5
                        elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                            six1 = roulette_guess - 1
                            six2 = roulette_guess + 1
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 2
                                six4 = roulette_guess - 3
                                six5 = roulette_guess - 4
                            elif above_below == 2:
                                six3 = roulette_guess + 2
                                six4 = roulette_guess + 3
                                six5 = roulette_guess + 4
                    mensagem = "You picked " + str(roulette_guess) + "," + str(six1) + "," + str(six2) + "," + str(six3) + "," + str(six4) + "," + str(six5) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or six1 == roulette_number or six2 == roulette_number or six3 == roulette_number or six4 == roulette_number or six5 == roulette_number:
                        player_3_winnings = amount_bet * 8
                        player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 6:
                    print("Choose a color")
                    print("1-Red (Includes 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)")
                    print("2-Black (Includes 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)")
                    color_pick = int(input("Make your pick:"))
                    while color_pick != 1 and color_pick != 2:
                        color_pick = int(input("Make your pick between red (type 1) or black (type 2):"))
                    if color_pick == 1:
                        print(player_3_name+" picked red")
                        if roulette_number == 1 or roulette_number == 3 or roulette_number == 5 or roulette_number == 7 or roulette_number == 9 or roulette_number == 12 or roulette_number == 14 or roulette_number == 16 or roulette_number == 18 or roulette_number == 19 or roulette_number == 21 or roulette_number == 23 or roulette_number == 25 or roulette_number == 27 or roulette_number == 30 or roulette_number == 32 or roulette_number == 34 or roulette_number == 36:
                            player_3_winnings = amount_bet * 2
                            player_3_chips = player_3_chips + player_3_winnings
                    elif color_pick == 2:
                        print(player_3_name+" picked black")
                        if roulette_number == 2 or roulette_number == 4 or roulette_number == 6 or roulette_number == 8 or roulette_number == 10 or roulette_number == 11 or roulette_number == 13 or roulette_number == 15 or roulette_number == 17 or roulette_number == 20 or roulette_number == 22 or roulette_number == 24 or roulette_number == 26 or roulette_number == 28 or roulette_number == 29 or roulette_number == 31 or roulette_number == 33 or roulette_number == 35:
                            player_3_winnings = amount_bet * 2
                            player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 7:
                    print(player_3_name+" picked odd")
                    if roulette_number % 2 != 0:
                        player_3_winnings = amount_bet * 2
                        player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 8:
                    print(player_3_name +" picked Even")
                    if roulette_number % 2 == 0:
                        player_3_winnings = amount_bet * 2
                        player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 9:
                    print("Choose Half")
                    print("1-First Half (Includes 1-18)")
                    print("2-Second Half (Includes 19-36)")
                    half_pick = int(input("Make your pick:"))
                    while half_pick != 1 and half_pick != 2:
                        half_pick = int(input("Make your pick between the first half (type 1) or the second half (type 2):"))
                    if half_pick == 1:
                        mensagem = "You picked the first half."
                        print(mensagem)
                        if 1 <= roulette_number <= 18:
                            player_3_winnings = amount_bet * 2
                            player_3_chips = player_3_chips + player_3_winnings
                    elif half_pick == 2:
                        mensagem = "You picked the second half."
                        print(mensagem)
                        if 19 <= roulette_number <= 36:
                            player_3_winnings = amount_bet * 2
                            player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 10:
                    print("Choose Dozen")
                    print("1-First Dozen (Includes 1-12)")
                    print("2-Second Dozen (Includes 13-24)")
                    print("3-Third Dozen (Includes 25-36)")
                    dozen_pick = int(input("Make your pick:"))
                    while dozen_pick != 1 and dozen_pick != 2 and dozen_pick != 3:
                        dozen_pick = int(input("Make your pick between the first dozen (type 1) or the second dozen (type 2) or the third dozen (type 3):"))
                    if dozen_pick == 1:
                        mensagem = "You picked the first dozen."
                        print(mensagem)
                        if 1 <= roulette_number <= 12:
                            player_3_winnings = amount_bet * 3
                            player_3_chips = player_3_chips + player_3_winnings
                    elif dozen_pick == 2:
                        mensagem = "You picked the second dozen."
                        print(mensagem)
                        if 13 <= roulette_number <= 24:
                            player_3_winnings = amount_bet * 3
                            player_3_chips = player_3_chips + player_3_winnings
                    elif dozen_pick == 3:
                        mensagem = "You picked the third dozen."
                        print(mensagem)
                        if 25 <= roulette_number <= 36:
                            player_3_winnings = amount_bet * 3
                            player_3_chips = player_3_chips + player_3_winnings
                elif roulette_bet == 11:
                    print("Choose Column")
                    print("1-First Column (Includes 1,4,7,10,13,16,19,22,25,28,31,34)")
                    print("2-Second Column (Includes 2,5,8,11,14,17,20,23,26,29,32,35)")
                    print("3-Third Column (Includes 3,6,9,12,15,18,21,24,27,30,33,36)")
                    column_pick = int(input("Make your pick:"))
                    while column_pick != 1 and column_pick != 2 and column_pick != 3:
                        column_pick = int(input("Make your pick between the first column (type 1) or the second column (type 2) or the third column (type 3):"))
                    if column_pick == 1:
                        mensagem = player_3_name+ " picked the first column."
                        print(mensagem)
                        if roulette_number == 1 or roulette_number == 4 or roulette_number == 7 or roulette_number == 10 or roulette_number == 13 or roulette_number == 16 or roulette_number == 19 or roulette_number == 22 or roulette_number == 25 or roulette_number == 28 or roulette_number == 31 or roulette_number == 34:
                            player_3_winnings = amount_bet * 3
                            player_3_chips = player_3_chips + player_3_winnings
                    elif column_pick == 2:
                        mensagem = player_3_name +" picked the second column."
                        print(mensagem)
                        if roulette_number == 2 or roulette_number == 5 or roulette_number == 8 or roulette_number == 11 or roulette_number == 14 or roulette_number == 17 or roulette_number == 20 or roulette_number == 23 or roulette_number == 26 or roulette_number == 29 or roulette_number == 32 or roulette_number == 35:
                            player_3_winnings = amount_bet * 3
                            player_3_chips = player_3_chips + player_3_winnings
                    elif column_pick == 3:
                        mensagem = player_3_name+ " picked the third column."
                        print(mensagem)
                        if roulette_number == 3 or roulette_number == 6 or roulette_number == 9 or roulette_number == 12 or roulette_number == 15 or roulette_number == 18 or roulette_number == 21 or roulette_number == 24 or roulette_number == 27 or roulette_number == 30 or roulette_number == 33 or roulette_number == 36:
                            player_3_winnings = amount_bet * 3
                            player_3_chips = player_3_chips + player_3_winnings
            if player_4:
                if player_4_chips <= 0:
                    print("Player 4 is out")
                    print("you have " + str(player_4_chips) + " chips")
                    player_4 = False
                roulette_bet = int(input("Place your bets, player 4:"))
                while roulette_bet <= 0 or roulette_bet > 11:
                    print("Pick a number between 1 and 11")
                amount_bet = int(input("Place the amount you want to bet:"))
                while amount_bet > player_4_chips:
                    mensagem = "Cannot bet more than the amount of chips you have, which is:" + str(player_4_chips)
                    print(mensagem)
                    amount_bet = int(input("Place the amount you want to bet, another time:"))
                player_4_chips = player_4_chips - amount_bet
                if roulette_bet == 1:
                    roulette_guess = int(input("enter your guess between 0 and 36, player 4:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    mensagem = "You picked " + str(roulette_guess) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number:
                        player_4_winnings = amount_bet * 40
                        player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 2:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 4:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1 or roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31 or roulette_guess == 34:
                        double = roulette_guess + 1
                    elif roulette_guess == 3 or roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33 or roulette_guess == 36:
                        double = roulette_guess - 1
                    elif roulette_guess == 2 or roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32 or roulette_guess == 35:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        if ahead_behind == 1:
                            roulette_guess = roulette_guess + 1
                        elif ahead_behind == 2:
                            roulette_guess = roulette_guess - 1
                    mensagem = player_4_name + " picked" + str(roulette_guess) + "," + str(double) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or double == roulette_number:
                        player_4_winnings = amount_bet * 20
                        player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 3:
                    roulette_guess = int(input("enter your guess between 1 and 36 player 4:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1 or roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31 or roulette_guess == 34:
                        triple1 = roulette_guess + 1
                        triple2 = roulette_guess + 2
                    elif roulette_guess == 3 or roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33 or roulette_guess == 36:
                        triple1 = roulette_guess - 1
                        triple2 = roulette_guess - 2
                    elif roulette_guess == 2 or roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32 or roulette_guess == 35:
                        triple1 = roulette_guess - 1
                        triple2 = roulette_guess + 1
                    mensagem = player_4_name + " picked " + str(roulette_guess) + "," + str(triple1) + "," + str(triple2) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or triple1 == roulette_number or triple2 == roulette_number:
                        player_4_winnings = amount_bet * 15
                        player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 4:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 4:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    if roulette_guess == 1:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess + 3
                        quad3 = roulette_guess + 4
                    elif roulette_guess == 3:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess + 2
                        quad3 = roulette_guess + 3
                    elif roulette_guess == 2:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        while ahead_behind != 1 and ahead_behind != 2:
                            ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                        if ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess + 3
                            quad3 = roulette_guess + 4
                        elif ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess + 2
                            quad3 = roulette_guess + 3
                    elif roulette_guess == 34:
                        quad1 = roulette_guess + 1
                        quad2 = roulette_guess - 2
                        quad3 = roulette_guess - 3
                    elif roulette_guess == 36:
                        quad1 = roulette_guess - 1
                        quad2 = roulette_guess - 3
                        quad3 = roulette_guess - 4
                    elif roulette_guess == 35:
                        print("1-Ahead")
                        print("2-Behind")
                        ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                        while ahead_behind != 1 and ahead_behind != 2:
                            ahead_behind = int(input("Would you like to choose one ahead (type 1) or one behind (type 2):"))
                        if ahead_behind == 1:
                            quad1 = roulette_guess + 1
                            quad2 = roulette_guess - 2
                            quad3 = roulette_guess - 3
                        elif ahead_behind == 2:
                            quad1 = roulette_guess - 1
                            quad2 = roulette_guess - 3
                            quad3 = roulette_guess - 4
                    else:
                        print("1-Above")
                        print("2-Below")
                        above_below = int(input("Would you like to choose one above or one below:"))
                        while above_below != 1 and above_below != 2:
                            above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                        if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                            quad1 = roulette_guess - 1
                            if above_below == 1:
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 4
                            elif above_below == 2:
                                quad2 = roulette_guess + 2
                                quad3 = roulette_guess + 3
                        elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                            quad1 = roulette_guess + 1
                            if above_below == 1:
                                quad2 = roulette_guess - 2
                                quad3 = roulette_guess - 3
                            elif above_below == 2:
                                quad2 = roulette_guess + 3
                                quad3 = roulette_guess + 4
                        elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                            print("1-Ahead")
                            print("2-Behind")
                            ahead_behind = int(input("Would you like to choose one ahead or one behind:"))
                            if above_below == 1 and ahead_behind == 1:
                                quad1 = roulette_guess + 1
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 2
                            elif above_below == 1 and ahead_behind == 2:
                                quad1 = roulette_guess - 1
                                quad2 = roulette_guess - 3
                                quad3 = roulette_guess - 4
                            elif above_below == 2 and ahead_behind == 1:
                                quad1 = roulette_guess + 1
                                quad2 = roulette_guess + 3
                                quad3 = roulette_guess + 4
                            elif above_below == 2 and ahead_behind == 2:
                                quad1 = roulette_guess - 1
                                quad2 = roulette_guess + 2
                                quad3 = roulette_guess + 3
                    mensagem = "You picked " + str(roulette_guess) + "," + str(quad1) + "," + str(quad2) + "," + str(quad3) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or quad1 == roulette_number or quad2 == roulette_number or quad3 == roulette_number:
                        player_4_winnings = amount_bet * 10
                        player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 5:
                    roulette_guess = int(input("enter your guess between 1 and 36, player 4:"))
                    while roulette_guess == 0:
                        roulette_guess = int(input("You can only pick 0 as a single bet, pick a different number:"))
                    while roulette_guess > 36 or roulette_guess < 0:
                        roulette_guess = int(input("enter your guess between 0 and 36, Dumbass:"))
                    if roulette_guess == 1:
                        six1 = roulette_guess + 1
                        six2 = roulette_guess + 2
                        six3 = roulette_guess + 3
                        six4 = roulette_guess + 4
                        six5 = roulette_guess + 5
                    elif roulette_guess == 2:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess + 1
                        six3 = roulette_guess + 2
                        six4 = roulette_guess + 3
                        six5 = roulette_guess + 4
                    elif roulette_guess == 3:
                        six1 = roulette_guess - 1
                        six2 = roulette_guess - 2
                        six3 = roulette_guess + 1
                        six4 = roulette_guess + 2
                        six5 = roulette_guess + 3
                    elif roulette_guess == 34:
                        six1 = roulette_guess - 3
                        six2 = roulette_guess - 2
                        six3 = roulette_guess - 1
                        six4 = roulette_guess + 1
                        six5 = roulette_guess + 2
                    elif roulette_guess == 35:
                        six1 = roulette_guess - 4
                        six2 = roulette_guess - 3
                        six3 = roulette_guess - 2
                        six4 = roulette_guess - 1
                        six5 = roulette_guess + 1
                    elif roulette_guess == 36:
                        six1 = roulette_guess - 5
                        six2 = roulette_guess - 4
                        six3 = roulette_guess - 3
                        six4 = roulette_guess - 2
                        six5 = roulette_guess - 1
                    else:
                        print("1-Above")
                        print("2-Below")
                        above_below = int(input("Would you like to choose one above or one below:"))
                        if roulette_guess == 6 or roulette_guess == 9 or roulette_guess == 12 or roulette_guess == 15 or roulette_guess == 18 or roulette_guess == 21 or roulette_guess == 24 or roulette_guess == 27 or roulette_guess == 30 or roulette_guess == 33:
                            six1 = roulette_guess - 1
                            six2 = roulette_guess - 2
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 3
                                six4 = roulette_guess - 4
                                six5 = roulette_guess - 5
                            elif above_below == 2:
                                six3 = roulette_guess + 1
                                six4 = roulette_guess + 2
                                six5 = roulette_guess + 3
                        elif roulette_guess == 4 or roulette_guess == 7 or roulette_guess == 10 or roulette_guess == 13 or roulette_guess == 16 or roulette_guess == 19 or roulette_guess == 22 or roulette_guess == 25 or roulette_guess == 28 or roulette_guess == 31:
                            six1 = roulette_guess + 1
                            six2 = roulette_guess + 2
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 3
                                six4 = roulette_guess - 2
                                six5 = roulette_guess - 1
                            elif above_below == 2:
                                six3 = roulette_guess + 3
                                six4 = roulette_guess + 4
                                six5 = roulette_guess + 5
                        elif roulette_guess == 5 or roulette_guess == 8 or roulette_guess == 11 or roulette_guess == 14 or roulette_guess == 17 or roulette_guess == 20 or roulette_guess == 23 or roulette_guess == 26 or roulette_guess == 29 or roulette_guess == 32:
                            six1 = roulette_guess - 1
                            six2 = roulette_guess + 1
                            while above_below != 1 and above_below != 2:
                                above_below = int(input("Would you like to choose one above (type 1) or one below (type 2):"))
                            if above_below == 1:
                                six3 = roulette_guess - 2
                                six4 = roulette_guess - 3
                                six5 = roulette_guess - 4
                            elif above_below == 2:
                                six3 = roulette_guess + 2
                                six4 = roulette_guess + 3
                                six5 = roulette_guess + 4
                    mensagem = "You picked " + str(roulette_guess) + "," + str(six1) + "," + str(six2) + "," + str(six3) + "," + str(six4) + "," + str(six5) + "."
                    print(mensagem)
                    if roulette_guess == roulette_number or six1 == roulette_number or six2 == roulette_number or six3 == roulette_number or six4 == roulette_number or six5 == roulette_number:
                        player_4_winnings = amount_bet * 8
                        player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 6:
                    print("Choose a color")
                    print("1-Red (Includes 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)")
                    print("2-Black (Includes 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)")
                    color_pick = int(input("Make your pick:"))
                    while color_pick != 1 and color_pick != 2:
                        color_pick = int(input("Make your pick between red (type 1) or black (type 2):"))
                    if color_pick == 1:
                        print(player_4_name+" picked red")
                        if roulette_number == 1 or roulette_number == 3 or roulette_number == 5 or roulette_number == 7 or roulette_number == 9 or roulette_number == 12 or roulette_number == 14 or roulette_number == 16 or roulette_number == 18 or roulette_number == 19 or roulette_number == 21 or roulette_number == 23 or roulette_number == 25 or roulette_number == 27 or roulette_number == 30 or roulette_number == 32 or roulette_number == 34 or roulette_number == 36:
                            player_4_winnings = amount_bet * 2
                            player_4_chips = player_4_chips + player_4_winnings
                    elif color_pick == 2:
                        print(player_4_name+" picked black")
                        if roulette_number == 2 or roulette_number == 4 or roulette_number == 6 or roulette_number == 8 or roulette_number == 10 or roulette_number == 11 or roulette_number == 13 or roulette_number == 15 or roulette_number == 17 or roulette_number == 20 or roulette_number == 22 or roulette_number == 24 or roulette_number == 26 or roulette_number == 28 or roulette_number == 29 or roulette_number == 31 or roulette_number == 33 or roulette_number == 35:
                            player_4_winnings = amount_bet * 2
                            player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 7:
                    print(player_4_name+" picked odd")
                    if roulette_number % 2 != 0:
                        player_4_winnings = amount_bet * 2
                        player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 8:
                    print(player_4_name +" picked Even")
                    if roulette_number % 2 == 0:
                        player_4_winnings = amount_bet * 2
                        player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 9:
                    print("Choose Half")
                    print("1-First Half (Includes 1-18)")
                    print("2-Second Half (Includes 19-36)")
                    half_pick = int(input("Make your pick:"))
                    while half_pick != 1 and half_pick != 2:
                        half_pick = int(input("Make your pick between the first half (type 1) or the second half (type 2):"))
                    if half_pick == 1:
                        mensagem = "You picked the first half."
                        print(mensagem)
                        if 1 <= roulette_number <= 18:
                            player_4_winnings = amount_bet * 2
                            player_4_chips = player_4_chips + player_4_winnings
                    elif half_pick == 2:
                        mensagem = "You picked the second half."
                        print(mensagem)
                        if 19 <= roulette_number <= 36:
                            player_4_winnings = amount_bet * 2
                            player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 10:
                    print("Choose Dozen")
                    print("1-First Dozen (Includes 1-12)")
                    print("2-Second Dozen (Includes 13-24)")
                    print("3-Third Dozen (Includes 25-36)")
                    dozen_pick = int(input("Make your pick:"))
                    while dozen_pick != 1 and dozen_pick != 2 and dozen_pick != 3:
                        dozen_pick = int(input("Make your pick between the first dozen (type 1) or the second dozen (type 2) or the third dozen (type 3):"))
                    if dozen_pick == 1:
                        mensagem = "You picked the first dozen."
                        print(mensagem)
                        if 1 <= roulette_number <= 12:
                            player_4_winnings = amount_bet * 3
                            player_4_chips = player_4_chips + player_4_winnings
                    elif dozen_pick == 2:
                        mensagem = "You picked the second dozen."
                        print(mensagem)
                        if 13 <= roulette_number <= 24:
                            player_4_winnings = amount_bet * 3
                            player_4_chips = player_4_chips + player_4_winnings
                    elif dozen_pick == 3:
                        mensagem = "You picked the third dozen."
                        print(mensagem)
                        if 25 <= roulette_number <= 36:
                            player_4_winnings = amount_bet * 3
                            player_4_chips = player_4_chips + player_4_winnings
                elif roulette_bet == 11:
                    print("Choose Column")
                    print("1-First Column (Includes 1,4,7,10,13,16,19,22,25,28,31,34)")
                    print("2-Second Column (Includes 2,5,8,11,14,17,20,23,26,29,32,35)")
                    print("3-Third Column (Includes 3,6,9,12,15,18,21,24,27,30,33,36)")
                    column_pick = int(input("Make your pick:"))
                    while column_pick != 1 and column_pick != 2 and column_pick != 3:
                        column_pick = int(input("Make your pick between the first column (type 1) or the second column (type 2) or the third column (type 3):"))
                    if column_pick == 1:
                        mensagem = player_4_name+ " picked the first column."
                        print(mensagem)
                        if roulette_number == 1 or roulette_number == 4 or roulette_number == 7 or roulette_number == 10 or roulette_number == 13 or roulette_number == 16 or roulette_number == 19 or roulette_number == 22 or roulette_number == 25 or roulette_number == 28 or roulette_number == 31 or roulette_number == 34:
                            player_4_winnings = amount_bet * 3
                            player_4_chips = player_4_chips + player_4_winnings
                    elif column_pick == 2:
                        mensagem = player_4_name +" picked the second column."
                        print(mensagem)
                        if roulette_number == 2 or roulette_number == 5 or roulette_number == 8 or roulette_number == 11 or roulette_number == 14 or roulette_number == 17 or roulette_number == 20 or roulette_number == 23 or roulette_number == 26 or roulette_number == 29 or roulette_number == 32 or roulette_number == 35:
                            player_4_winnings = amount_bet * 3
                            player_4_chips = player_4_chips + player_4_winnings
                    elif column_pick == 3:
                        mensagem = player_4_name+ " picked the third column."
                        print(mensagem)
                        if roulette_number == 3 or roulette_number == 6 or roulette_number == 9 or roulette_number == 12 or roulette_number == 15 or roulette_number == 18 or roulette_number == 21 or roulette_number == 24 or roulette_number == 27 or roulette_number == 30 or roulette_number == 33 or roulette_number == 36:
                            player_4_winnings = amount_bet * 3
                            player_4_chips = player_4_chips + player_4_winnings
            print("closing bets")
            mensagem = "And The lucky number is " + str(roulette_number)
            print(mensagem)
            if player_1_active:
                if player_1_winnings>0:
                    mensagem = player_1_name + " has won" + str(player_1_winnings)+ "chips, with a grand total of " + str(player_1_chips) + " chips."
                    print(mensagem)
                else:
                    mensagem = player_1_name + " has "+ str(player_1_chips) + "chips left"
                    print(mensagem)
            if player_2_active:
                if player_2_winnings>0:
                    mensagem = player_2_name + " has won" + str(player_2_winnings)+ "chips, with a grand total of " + str(player_2_chips) + " chips."
                    print(mensagem)
                else:
                    mensagem = player_2_name + " has "+ str(player_2_chips) + "chips left"
                    print(mensagem)
            if player_3_active:
                if player_3_winnings>0:
                    mensagem = player_3_name + " has won" + str(player_3_winnings)+ "chips, with a grand total of " + str(player_3_chips) + " chips."
                    print(mensagem)
                else:
                    mensagem = player_3_name + " has "+ str(player_3_chips) + "chips left"
                    print(mensagem)
            if player_4_active:
                if player_4_winnings>0:
                    mensagem = player_4_name + " has won" + str(player_4_winnings)+ "chips, with a grand total of " + str(player_4_chips) + " chips."
                    print(mensagem)
                else:
                    mensagem = player_4_name + " has "+ str(player_4_chips) + "chips left"
                    print(mensagem)
        if player_1_chips>player_2_chips and player_1_chips>player_3_chips and player_1_chips>player_4_chips:
            mensagem= player_1_name + "is the winner with "+ str(player_1_chips) +" chips"
        elif player_2_chips > player_3_chips and player_2_chips > player_4_chips and player_2_chips > player_1_chips:
            mensagem= player_2_name + "is the winner with "+ str(player_2_chips) +" chips"
        elif player_3_chips > player_4_chips and player_3_chips > player_1_chips and player_3_chips > player_2_chips:
            mensagem= player_3_name + "is the winner with "+ str(player_3_chips) +" chips"
        elif player_4_chips > player_1_chips and player_4_chips > player_2_chips and player_4_chips > player_3_chips:
            mensagem= player_4_name + "is the winner with "+ str(player_4_chips) +" chips"
        print("Thank you")
        print("Return to menu")
        print("1-yes")
        print("2-No")
        menuopen = int(input("Make a choice:"))
        while menuopen != 1 and menuopen != 2:
            menuopen = int(input("Make a choice:"))
        if menuopen == 1:
            restart = True
        else:
            print("thanks for playing")
    elif menu_pick==4:
        rules_view=True
        while rules_view:
            print("====What would you like to know====")
            print("1-Jogo de advinhação")
            print("2-Roulette")
            print("3-Roulette multiplayer")
            print("4-Single")
            print("5-Split")
            print("6-Street")
            print("7-Corner")
            print("8-Line")
            print("9-Color")
            print("10-Odd")
            print("11-Even")
            print("12-Half")
            print("13-Dozen")
            print("14-Column")
            rules = int(input("Select:"))
            while 14<rules<1:
                rules = int(input("Select between 1 to 14:"))
            if rules==1:
                print("1-There is a random hidden number between 1 to 100, the player will keep guessing and the game will end when the player gets it right.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==2:
                print("1-The game begins and the player receives 30 chips.")
                print("2-The person selects a type of bet and enters an amount they want to bet.")
                print("3-Depending on the type of bet, the player will enter a specific number.")
                print("4-If the players guess aligns with the roulette number, he/she will earn more chips. Otherwise the player will earn nothing.")
                print("5-The game ends when the player has 0 chips left or they choose to stop.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==3:
                print("1-The game begins and the amount of players is determined.")
                print("2-The players will enter the number of round they would like to play.")
                print("3-Each player will take turns placing they're bets.")
                print("4-After all players have placed they're bets the lucky number is revealed.")
                print("5-Any player whose guess aligns with the number will earn chips.")
                print("6-After all the rounds are played the winner will be the person with the most chips")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==4:
                print("1-Player selects a single number to bet on, 40X the amount bet")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==5:
                print("1-The player places a bet on a number and the adjacent number in the row. 20 times the amount bet.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==6:
                print("1-Player places a bet on an entire row of numbers, 15 times the amount bet.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==7:
                print("1-The player will bet on 4 numbers in the shape of a square, depending on the position of the first number the player will have to choose the direction of the square(left or right) or (up or down). 10 times the amount bet.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==8:
                print("1-The player will choose two rows that are next to each other, 7 times the amount bet.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==9:
                print("1-The player chooses a color, 2 times the amount bet.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==10:
                print("1-The player places they're bets on all odd numbers, 2 times the profit.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==11:
                print("1-The player places they're bets on all even numbers, 2 times the profit.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==12:
                print("1-The player chooses between the first half (1-18) or the second (19-36), 2 times the amount bet.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==13:
                print("1-The player chooses between the first dozen (1-12) or the second (13-24) or the third(25-36), 3 times the amount bet.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            if rules==14:
                print("1-The player chooses between the first column or the second or the third.")
                print("Column 1- 1,4,7,10,13,16,19,22,25,28,31,34")
                print("Column 2- 2,5,8,11,14,17,20,23,26,29,32,35")
                print("Column 3- 3,6,9,12,15,18,21,24,27,30,33,36")
                print("3 times the amount bet.")
                print("Is there anything else you would like to know")
                print("1-Yes")
                print("2-No")
                rules_select = int(input("Select:"))
                while rules_select !=1 and rules_select != 2:
                    rules_select = int(input("Select 1 for yes or 2 for no:"))
                if rules_select == 1:
                    rules_view = True
                elif rules_select == 2:
                    rules_view = False
            print("Thank you")
            print("Return to menu")
            print("1-yes")
            print("2-No")
            menuopen=int(input("Make a choice:"))
            while menuopen !=1 and menuopen!=2:
                menuopen = int(input("Make a choice:"))
            if menuopen==1:
                restart=True
            else:
                print("thanks for playing")
    elif menu_pick==5:
        print("====Thank you for playing=====")
        restart=False