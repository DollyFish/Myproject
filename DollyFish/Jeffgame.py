import random, Menu, pickle
from time import sleep

def maingame():
    username = "Guess"
    stamp = ["NOT HAVE", "NOT HAVE", "NOT HAVE"]

    with open('stamprally.txt', 'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            data = {}

    with open('stamprally.txt', 'wb') as file:
        data[username] = stamp
        pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
        file.close()

    main(username)


def main(username):
    print("═════ ♡♡♡♡ Welcome to Taboo Count (/≧▽≦)/  ♡♡♡♡ ═════")
    choice = input("""      
      ---------- Press Enter To Start ----------- """)
    print()
    menugame(username)


def menugame(username):
    print("          ════════════════════════════════════")
    print("          Ready for Taboo Count ? ٩(ˊ ˋ*)و ~✧ ")
    print("          ════════════════════════════════════")

    choice = input("""
                  -> 1. Start Game
                  -> 2. Tutorial
                  -> S. CheckStamp
                  -> R. Return to Menu

                Please enter your choice: """)
    if choice == "1":
        game(username)
    elif choice == "2":
        Tutorial(username)
    elif choice == "S" or choice == "s":
        stamp(username)
    elif choice == "R" or choice == "r":
        print()
        print("Jeff the computer said goodbye へ[ •́ ‸ •̀ ]ʋ")
        sleep(1)
        print()
        Menu.displaygame(username)
    else:
        print()
        print("You must only select from the given choice")
        print("Please try again... (｡•́︿•̀｡)")
        print()
        menugame(username)


def Tutorial(username):
    instruction = ["In Taboo Count ...",
                   "Player must compete against Jeff the computer ٩(ˊ  ˋ*)و ~✧",
                   "",
                   "1. A Taboo number will be generated",
                   "",
                   "2. Choose to play first or second, as well as how many number you wish to enter ...",
                   "",
                   "* BUT for each turn, you can only enter between one to three numbers at a time *",
                   "* The numbers that you enter must be integers and they must be in a consecutive order (one after another) *",
                   "* If you are entering more than one number, enter one number at a time and press enter after you've finished entering each value *",
                   "",
                   "3. Enter your values",
                   "",
                   "4. Wait for Jeff the computer to count its values and players will then take turns",
                   "",
                   "The player who counts the Taboo number loses and the player who can avoid it wins !",
                   "",
                   "〚 ! WARNING ! 〛",
                   "If you enter numbers that are... ",
                   "! NOT integers",
                   "! NOT in a consecutive order",
                   "! Enter MORE THAN one to three numbers at a time",
                   "! Enter INVALID numbers",
                   "YOU WILL AUTOMATICALLY BE ELIMINATED FROM THE GAME ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃",
                   "",
                   ]

    for s in instruction:
        print(s);
        sleep(1.3)

    choice = input("""  
    ------------ Press Enter To Return -------------- """)
    print()
    menugame(username)


def stamp(username):
    with open('stamprally.txt', 'rb') as file:
        display = pickle.load(file)
        for row in display:
            if row == username:
                print()
                print("          ══════════════════════════════════")
                print("                  ✧ %s 's stamps' ✧ :" % row,
                      "\n                      ①", display[row][0],
                      "\n                      ②", display[row][1],
                      "\n                      ③", display[row][2])
                print("          ═══════════════════════════════════")
            else:
                pass
    choice = input("""  
    ------------ Press Enter To Return -------------- """)
    print()
    menugame(username)


def nearestmultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


def lose(username):
    print("\n\nYou lose !")
    print("Jeff (computer) : Beat me next time (ﾉ `･∀･)ﾉﾞ")

    choice = input("""  
    ------------ Press Enter To Return -------------- """)
    print()
    menugame(username)


def checknumbers(numberlist):
    i = 1
    while i < len(numberlist):
        if (numberlist[i] - numberlist[i - 1]) != 1:
            return False
        i = i + 1
    return True


def victory(username):
    print("\n\nCONGRATULATIONS %s !!!" % username)
    print("YOU WON˛₍˴◅ˋ)੭✧ !!")
    with open('stamprally.txt', 'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            data = {}

    with open('stamprally.txt', 'wb') as file:
        data[username][1] = "JEFF STAMP"
        pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
        print()
        print("%s, YOU'VE RECEIVED \" ★ JEFF STAMP ★ \" (ﾉ^ヮ^)ﾉ*:・ﾟ✧!! " % username)
        print()

        saving = 'SAVING SUCCESS ...'
        for i in range(18):
            print(saving[i], sep=' ', end=' ', flush=True);
            sleep(0.1)

        print()
        print()

        file.close()

    menugame(username)


def startgame(username):
    numberlist = []
    last = 0
    deathnum = random.randint(24, 35)
    print()

    generate = 'GENERATING TABOO NUMBER ...'
    for i in range(27):
        print(generate[i], sep=' ', end=' ', flush=True);
        sleep(0.1)

    print()
    print()
    print("Jeff (computer) : The Taboo number is【 %d 】!!!" % deathnum)
    print()

    while True:

        playerselect = ["Enter 'p1' to play first.", "Enter 'p2' to play second."]

        for s in playerselect:
            print(s);
            sleep(0.6)

        playerturn = input('>> ')

        if playerturn == "p1" or playerturn == "P1":
            while True:
                if last == deathnum - 1:
                    lose(username)
                else:
                    print()
                    yourturn = 'YOUR TURN ...'
                    for i in range(13):
                        print(yourturn[i], sep=' ', end=' ', flush=True);
                        sleep(0.1)

                    print()
                    print(
                        "\nHow many numbers do you want to enter ? ( Min : 1 & Max : 3 ) ( Taboo Number :【 %d 】)" % deathnum)
                    try:
                        usernum = int(input('>> '))
                    except ValueError:
                        print("Invalid input !! ... You are eliminated ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                        lose(username)

                    if usernum > 0 and usernum <= 3:
                        comjeff = random.randint(1, 3)
                    else:
                        print("Invalid input !! ... You are eliminated ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                        lose(username)

                    i, j = 1, 1

                    print("Please enter your value : ")
                    while i <= usernum:
                        try:
                            value = input('>> ')
                            value = int(value)
                            if len(numberlist) == 0 and value > 1:
                                lose(username)

                            if value == deathnum:
                                numberlist.append(value)
                                print("Number after your turn is : ")
                                print(numberlist)
                                lose(username)

                        except ValueError:
                            print(
                                "Invalid input !! ... You are eliminated ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                            lose(username)

                        numberlist.append(value)
                        i = i + 1

                    last = numberlist[-1]

                    if len(numberlist) == deathnum - 4 or len(numberlist) == deathnum - 8:
                        comjeff = 3
                    elif len(numberlist) == deathnum - 3 or len(numberlist) == deathnum - 7:
                        comjeff = 2
                    elif len(numberlist) == deathnum - 2 or len(numberlist) == deathnum - 1 or len(
                            numberlist) == deathnum - 6:
                        comjeff = 1

                    if checknumbers(numberlist) == True:
                        if last == deathnum:
                            lose(username)

                        else:
                            while j <= comjeff:
                                numberlist.append(last + j)
                                j = j + 1
                            print("Numbers after Jeff the computer turn is : ")
                            print(numberlist)
                            last = numberlist[-1]
                            if len(numberlist) >= deathnum:
                                victory(username)

                    else:
                        print(
                            "\nYou did't enter consecutive integers. You are eliminated ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ !!")
                        lose(username)


        elif playerturn == "p2" or playerturn == "P2":
            comjeff = 1
            last = 0
            while True:
                j = 1
                while j <= comjeff:
                    numberlist.append(last + j)
                    j = j + 1

                print()
                print("Number after Jeff the computer turns : ")
                print(numberlist)

                if len(numberlist) >= deathnum:
                    victory(username)

                if numberlist[-1] == deathnum - 1:
                    lose(username)

                else:
                    print()
                    yourturn = 'YOUR TURN ...'
                    for i in range(13):
                        print(yourturn[i], sep=' ', end=' ', flush=True);
                        sleep(0.1)

                    print()
                    print(
                        "\nHow many number do you want to enter ? ( Min : 1 & Max : 3 ) ( Taboo Number :【 %d 】)" % deathnum)

                    try:
                        usernum = input('>> ')
                        usernum = int(usernum)
                    except ValueError:
                        print("Invalid input !! ... You are eliminated ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                        lose()
                    if usernum > 0 and usernum <= 3:
                        comjeff = random.randint(1, 3)
                    else:
                        print("Invalid input !! ... You are eliminated ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                        lose(username)

                    i = 1

                    print("Please enter your values : ")
                    while i <= usernum:
                        try:
                            value = input('>> ')
                            value = int(value)

                            if value == deathnum:
                                numberlist.append(value)
                                print("Number after your turn is : ")
                                print(numberlist)
                                lose(username)

                        except ValueError:
                            print(
                                "Invalid input !! ... You are eliminated ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                            lose(username)

                        numberlist.append(value)
                        i = i + 1
                    last = numberlist[-1]

                    if checknumbers(numberlist) == True:
                        near = nearestmultiple(last)
                        comjeff = near - last
                        if comjeff == 4:
                            comjeff = 3
                        else:
                            comjeff = comjeff

                    else:
                        print(
                            "\nYou did't enter consecutive integes. You are eliminated ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ !!")
                        lose(username)

                    if len(numberlist) == deathnum - 4 or len(numberlist) == deathnum - 8:
                        comjeff = 3
                    elif len(numberlist) == deathnum - 3 or len(numberlist) == deathnum - 7:
                        comjeff = 2
                    elif len(numberlist) == deathnum - 2 or len(numberlist) == deathnum - 1 or len(numberlist) == deathnum - 6:
                        comjeff = 1

        else:
            print()
            print("Invalid choice.. Please re-enter .. (｡•́︿•̀｡)")


def game(username):
    game = True
    while game == True:
        print()

        gameload = 'LOADING...'
        for i in range(10):
            print(gameload[i], sep=' ', end=' ', flush=True);
            sleep(0.2)

        print()
        print()
        print("=====✧ HI ~ %s, I'm Jeff the computer ✧===== " % username)
        print("Do you want to play Taboo Count with me ? (Yes / No)")
        choice = input('>> ')
        if choice == "Yes" or choice == "yes" or choice == "YES":
            startgame(username)

        elif choice == "No" or choice == "no" or choice == "NO":
            print()
            print("Do you want to quit taboo count ?")
            print("Jeff the computer will be sad (｡•́︿•̀｡)) (Yes / No)")

            choice2 = input('>> ')

            if choice2 == "Yes" or choice2 == "yes" or choice2 == "YES":
                print()
                print("Jeff the computer said goodbye へ[ •́ ‸ •̀ ]ʋ")
                sleep(0.8)
                print()
                menugame(username)
            elif choice2 == "No" or choice2 == "no" or choice2 == "NO":
                print()
                print("OK ! Let's play !（=´∇｀=）")
            else:
                print("Invalid choice.. Please re-enter .. (｡•́︿•̀｡)")

        else:
            print("Invalid choice.. Please re-enter .. (｡•́︿•̀｡)")


if __name__ == '__main__':
    maingame()

