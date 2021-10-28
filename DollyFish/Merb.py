import random, pickle, Menu ,time
from time import sleep

def StartGame(username):
    print()
    print()
    Loading = "               LOADING..."
    for i in range(25):
        print(Loading[i], sep=' ', end=' ', flush=True);
        sleep(0.1)
    print("")
    print("")
    sleep(0.8)
    print("                           ===== Hi I`m Merb ===== ")
    sleep(0.8)
    print("          Merb :Do you want to play Rock Paper Scissors with me? (Yes / No)")
    sleep(0.8)
    choice = input('          You >> ')
    if choice == "Yes" or choice == "yes" or choice == "YES":
        MainGame(username)

    elif choice == "No" or choice == "no" or choice == "NO":
        MenuGame(username)
    else:
        print("          Merb : That is invalid choice.Please check your spelling.")
        StartGame(username)

def MenuGame(username):
    print("""
                            ♦♦♦ Welcome to game ♦♦♦
                                    ☻ Merb ☻
                               Rock Paper Scissors

                              -->1: Start game
                              -->2: Tutorial
                              -->S: Checkstamp
                              -->R: Return to menu""")
    print("                         ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    Selection = input("                              Enter your choice :")
    if Selection == '1':
        StartGame(username)
    elif Selection == '2':
        Tutoriel(username)
    elif Selection == 'S' or Selection == 's':
        Stamp(username)
    elif Selection == 'R' or Selection == 'r':
        print()
        print("                              Merb : See you later ")
        sleep(1)
        print()
        Menu.displaygame(username)
    else:
        print()
        print("            ══════════════════════════════════════════════════════════")
        print("                    Invalid number.Please enter your choice again")
        print("            ══════════════════════════════════════════════════════════")
    MenuGame(username)

def MainGame(username):
    t = ["rock","paper","scissors"]

    DirectionsB = ["I said I had never lost anyone before", "Try to guess what I`ll play"]
    DirectionsMW = ["Oh, you are not so good \n                              at this are not you???"
                    ,"Your really think you can beat me?"]
    DirectionsML = ["Hmm not bad", "This is just the start", "I`m firing up"]
    DirectionsT = ["oh,it seems like \n                               we both have the same thought"
                    , "Did you just read my mind??"]

    counterUser = 0
    counterMerb = 0

    def Shownt():
        sleep(0.8)
        print("                               ☺Your :", User)
        sleep(0.8)
        print("                               ☻Merb :", Merb)
        sleep(0.8)

    def Score():
        sleep(0.8)
        print("                                ===========")
        sleep(0.8)
        print("                                 ♥Score♥")
        print("                                You  :", counterUser)
        print("                                Merb :", counterMerb)
        sleep(0.8)
    Load()
    while counterUser < 3 and counterMerb < 3:
        User = input("""
                ════════════════════════════════════════════════
                              -->1: Rock
                              -->2: Paper
                              -->3: Scissors
                ════════════════════════════════════════════════
                        Please enter your choice:""")
        User = RPS(User)
        Merb = random.choice(t)
        if User.lower() == Merb:
            Shownt()
            print("                            Tie!",Merb,"VS",User)
            Score()
            print("                       Merb : ",random.choice(DirectionsT))
        elif User.lower() == "rock":
            if Merb == "paper":
                Shownt()
                print("                       You lost!", Merb, "covers", User)
                counterMerb += 1
                sleep(0.8)
                print("                       Merb :",random.choice(DirectionsMW))
                Score()
            else:
                Shownt()
                print("                       You win!", User, "smashes", Merb)
                counterUser += 1
                sleep(0.8)
                print("                       Merb :",random.choice(DirectionsML))
                Score()
        elif User.lower() == "paper":
            if Merb == "scissors":
                Shownt()
                print("                       You lost!", Merb, "cut", User)
                counterMerb += 1
                sleep(0.8)
                print("                       Merb :",random.choice(DirectionsMW))
                Score()
            else:
                Shownt()
                print("                       You win!", User, "covers", Merb)
                counterUser += 1
                sleep(0.8)
                print("                       Merb :",random.choice(DirectionsML))
                Score()
        elif User.lower() == "scissors":
            if  Merb == "rock":
                Shownt()
                print("                       You lost...", Merb, "smashes", User)
                sleep(0.8)
                print("                       Merb :",random.choice(DirectionsMW))
                counterMerb += 1
                Score()
            else:
                Shownt()
                print("                       You win!", User, "cut", Merb)
                sleep(0.8)
                print("                       Merb :",random.choice(DirectionsML))
                counterUser += 1
                Score()
        else:
                print()
                print("                ◘══════════════════════════════════════════════◘")
                print("                    That's not a valid play. Please try again          ")
                print("                ◘══════════════════════════════════════════════◘")

    if counterUser == 3:
        victory(username)
    elif counterMerb == 3:
        Lose()
    EndGame(username)



def victory(username):
    print("                ════════════════════════════════════════════════")
    print("                                Your Victory")
    print("                ════════════════════════════════════════════════")
    print("""
                          Merb : Did i just lose?
                                 This stamp for you
                                                        """)
    with open('stamprally.txt', 'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            data = {}
    with open('stamprally.txt', 'wb') as file:
        data[username][2] = "MERB STAMP"
        pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
        print("                ════════════════════════════════════════════════")
        print("                        %s, YOU GET \"MERB Stamp\" !! " % username)
        print("                          Merb : I want to re-match")
        save = '           SAVING SUCCESS ...'
        for i in save:
            print(i, sep=' ', end=' ', flush=True);
            sleep(0.1)
        file.close()

def Lose():
    print()
    print("               =================================================")
    print("                                   Your Lost")
    print("               =================================================")
    print()
    print("                        Merb : Do you want to play again?")

#กำหนดค่าของ User
def RPS(User):
    if User == "1":
        User = "rock"
    elif User == "2":
        User = "paper"
    elif User == "3":
        User = "scissors"
    return User


def Tutoriel(username):
    print()
    tut = "            [[ •Tutorial• ]]"
    for i in range(28):
        print(tut[i], sep=' ', end=' ', flush=True);
        sleep(0.1)

    tutorial= [

                "    "
              ,"          1. Players will have the option to choose one of 3 options"
              ,"                              Rock", "                              Paper","                              Scissors"
              ,"          2. Merb will then randomly pick a fight with you."
              ,"          3. You have to win Merb provides up to three times in order to Stamp."

              ,"             !!♦ Rule ♦!!"
              ,"          1. Rock beats Scissors"
              ,"          2. Paper beats Rock"
              ,"          3. Scissors beats Paper"
              ]
    for s in tutorial:
        print(s);
        sleep(1)

    input( """
                      ▬▬▬ Press Enter for return to menu ▬▬▬""")
    MenuGame(username)


def Stamp(username):
        print()
        with open('stamprally.txt', 'rb') as file:
            display = pickle.load(file)
            for row in display:
              if row == username:
                print("                       ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘")
                print("                             ✧ %s 's stamp ✧ :" % row,
                      "\n                              ①", display[row][0],
                      "\n                              ②", display[row][1],
                      "\n                              ③", display[row][2])
                print("                       ◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘")
              else:
                  pass
        choice = input(""" 
                      ===================================
                            Press Enter To Return
                      ===================================
                                                        """)
        print()
        MenuGame(username)


def EndGame(username):
    print(" ")
    print("                ═══════════════════════════════════════════════")
    End = input("""
                            -->1: Play again
                            -->2: Return to menu
                          Please enter your choice: """)
    if End == "1":
        MainGame(username)
    elif End == "2":
        MenuGame(username)
    else:
        print()
        print("                 Invalid number.Please enter your choice again")
        EndGame(username)

def Load():
    print()
    print()
    LO ="               LET`S GO"
    for i in range(23):
        print(LO[i], sep=' ', end=' ', flush=True);
        sleep(0.1)
    sleep(1)

def Guess():
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
    MenuGame(username)


if __name__ == '__main__':
    Guess()

