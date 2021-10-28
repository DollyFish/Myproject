import csv, pickle, ChickyDaoWord, Jeffgame, Merb
from time import sleep

def main():
    print()
    process = "PROCESSING PROTOCOL"
    for i in range(19):
        print(process[i], sep=' ', end=' ', flush=True);
        sleep(0.07)

    load = '....★'
    for i in range(5):
        print(load[i], sep=' ', end=' ', flush=True);
        sleep(0.4)
    print()
    process = "PROCESSING SUCCESS"
    for i in process:
        print(i, sep=' ', end=' ', flush=True);
        sleep(0.07)
    print()
    print()
    sleep(0.7)
    loading = "LOADING FILE GAME"
    for i in loading:
        print(i, sep=' ', end=' ', flush=True);
        sleep(0.07)
    load = '....★'
    for i in range(5):
        print(load[i], sep=' ', end=' ', flush=True);
        sleep(0.4)
    print()
    sleep(0.7)
    loading = "LOADING SUCCESS"
    for i in loading:
        print(i, sep=' ', end=' ', flush=True);
        sleep(0.07)
    print()
    print()
    sleep(0.7)
    ai = "CONNECTING TO AI SYSTEM"
    for i in ai:
        print(i, sep=' ', end=' ', flush=True);
        sleep(0.07)
    load = '....★'
    for i in range(5):
        print(load[i], sep=' ', end=' ', flush=True);
        sleep(0.4)
    print()
    sleep(0.7)
    ai = "AI SYSTEM WILL BE START"
    for i in ai:
        print(i, sep=' ', end=' ', flush=True);
        sleep(0.07)
    sleep(0.7)
    print()
    print()
    talk = "HELLO PLAYER,"
    for i in talk:
        print(i, sep=' ', end=' ', flush=True);
        sleep(0.07)
    sleep(0.7)
    talk = "WELCOME TO DOLLYFISH ISLAND"
    for i in talk:
        print(i, sep=' ', end=' ', flush=True);
        sleep(0.07)
    print()
    print()
    print()
    sleep(0.7)
    menu()

def menu():
    print("════════════════════ DollyFish IslanD ════════════════════")
    choice = input("""
                     -> A: Login   
                     -> B: Register
                     -> Q: Exit    
 
                Please enter your choice: """)

    if choice == "A" or choice == "a":
        login()
    elif choice == "B" or choice == "b":
        register()
    elif choice == "Q" or choice == "q":
        bye = "Good Bye ~"
        for i in bye:
            print(i, sep=' ', end='', flush=True);
            sleep(0.075)
        print()
        sleep(1)
        exit(0)
    else:
        select = "You must only select either A or B or C"
        for i in select:
            print(i, sep=' ', end='', flush=True);
            sleep(0.02)
        select = "Please try again"
        print()
        for i in select:
            print(i, sep=' ', end='', flush=True);
            sleep(0.02)
        sleep(0.5)
        print()
        print()
        menu()

def register():
    print()
    print("═══════════════════ > REGISTER FORM < ════════════════════")
    print()
    username = input("      > Please create your username : ")
    password = input("      > Please create your password : ")
    stamp = ["NOT HAVE", "NOT HAVE", "NOT HAVE"]
    print()
    with open("DollyFish.txt", 'r') as DollyFish:
        DollyFishReader = csv.reader(DollyFish)
        for row in DollyFishReader:
            for field in row:
                if row[0] == username :
                    load = '....✖'
                    for i in range(5):
                        print(load[i], sep=' ', end=' ', flush=True);
                        sleep(0.4)
                    sleep(0.4)
                    print()
                    already = "This username is already registered"
                    for i in already:
                        print(i, sep=' ', end=' ', flush=True);
                        sleep(0.02)
                    sleep(0.5)
                    print()

                    again = "Please login with this username again"
                    for i in again:
                        print(i, sep=' ', end=' ', flush=True);
                        sleep(0.02)

                    sleep(0.5)
                    print()
                    menu()

    with open('Dollyfish.txt', 'a') as DollyFish:
        DollyWriter = csv.writer(DollyFish)
        DollyWriter.writerow([username, password])
        load = '....★'
        for i in range(5):
            print(load[i], sep=' ', end=' ', flush=True);
            sleep(0.4)
        print()
        sleep(0.2)

        success = "Register Success !!"
        for i in success:
            print(i, sep=' ', end=' ', flush=True);
            sleep(0.1)

        sleep(0.4)
        DollyFish.close()
        print()
        print()
    with open('stamprally.txt', 'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            data = {}

    with open('stamprally.txt', 'wb') as file:
        data[username] = stamp
        pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
        file.close()
        menu()

def login():
    while True :
        print()
        print("═════════════════════ > ♫ LOGIN ♫ < ══════════════════════")
        print()
        with open("DollyFish.txt", 'r') as DollyFish:
            username = input("            > Enter username: ")
            password = input("            > Enter password: ")
            print()
            if username.lower() == "q" and password.lower() == "q" :
                print()
                menu()
            DollyFishReader = csv.reader(DollyFish)
            for row in DollyFishReader:
                for field in row:
                    if field == username and row[1] == password:
                        load = '....★'
                        for i in range(5):
                            print(load[i], sep=' ', end=' ', flush=True);
                            sleep(0.4)
                        print()
                        sleep(0.4)
                        success = "Login Success !!"
                        for i in success:
                            print(i, sep=' ', end=' ', flush=True);
                            sleep(0.1)

                        sleep(0.3)
                        print()
                        print()
                        gameload = 'LOADINGSAVE'
                        for i in range(11):
                            print(gameload[i], sep=' ', end=' ', flush=True);
                            sleep(0.1)

                        loading = '.... ★'
                        for i in range(6):
                            print(loading[i], sep=' ', end=' ', flush=True);
                            sleep(0.7)
                        print()
                        print()
                        sleep(0.35)
                        displaygame(username)
                        return

        load = '....✖'
        for i in range(5):
            print(load[i], sep=' ', end=' ', flush=True);
            sleep(0.4)

        print()
        sleep(0.3)
        notfind = "Cannot find your username or password. Please Try again"
        for i in notfind:
            print(i, sep=' ', end='', flush=True);
            sleep(0.02)
        print()
        sleep(0.4)
        printq = "If you not have user, Please Enter \"Q\" in Username and Password "
        for i in printq:
            print(i, sep=' ', end='', flush=True);
            sleep(0.02)
        sleep(0.4)
        print()


def Credits(username):
    print()

    member = ["═════════════════════ Vigilante Group ════════════════════",
              "",
              "         1. Dol       Hinta    623040188-0",
              "         2. Thipparat Sirirak  623040189-8",
              "         3. Thanapon  Srimukda 623040688-0",
              "         4. Tawatchai Sintop   623040689-8",
              "         5. Passawut  Uttakit  623040708-0"]
    for i in member:
        print(i);
        sleep(1.3)

    choice = input("""     
           ------------ Press Enter --------------
                     - Return To Menu - """)
    print()
    displaygame(username)

def displaygame(username):
    with open('stamprally.txt', 'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            data = {}

    if data[username][0] == "CHICKYDAO STAMP" and data[username][1] == "JEFF STAMP" and data[username][2] == "MERB STAMP":
        print()
        print("    ═══════════════════════════════════════════════════")
        print("           CONGRATULATION YOU GET ALL STAMP !!!!")
        print("    ═══════════════════════════════════════════════════")
        print()
        sleep(1)
    else:
        pass

    print("════════════════════ DollyFish IslanD ════════════════════")
    choice = input("""
                    -> 1. ChickyDaoWord
                    -> 2. Jeff TabooCount
                    -> 3. Merb RPS
                    -> S. CheckStamp
                    -> C. ENDCredit
                    -> L. Logout
                    -> Q. Exit
                    
══════════════════════════════════════════════════════════
                Please enter your choice: """)

    if choice == "1" :
        print()
        process = "PROCESSING TO CHICKYDAOWORD"
        for i in range(27):
            print(process[i], sep=' ', end=' ', flush=True);
            sleep(0.1)
        load = '....★'
        for i in range(5):
            print(load[i], sep=' ', end=' ', flush=True);
            sleep(0.6)
        print()
        print()
        ChickyDaoWord.main(username)

    elif choice == "2" :
        print()
        process = "PROCESSING TO TABOONUMBER"
        for i in range(25):
            print(process[i], sep=' ', end=' ', flush=True);
            sleep(0.1)
        load = '....★'
        for i in range(5):
            print(load[i], sep=' ', end=' ', flush=True);
            sleep(0.6)
        print()
        print()
        Jeffgame.main(username)

    elif choice == "3" :
        print()
        process = "PROCESSING TO RPS"
        for i in range(17):
            print(process[i], sep=' ', end=' ', flush=True);
            sleep(0.1)
        load = '....★'
        for i in range(5):
            print(load[i], sep=' ', end=' ', flush=True);
            sleep(0.6)
        print()
        Merb.MenuGame(username)

    elif choice == "S" or choice == "s" :
        print()
        process = "OPEN STAMP FILE"
        for i in process:
            print(i, sep=' ', end=' ', flush=True);
            sleep(0.1)
        load = '....★'
        for i in range(5):
            print(load[i], sep=' ', end=' ', flush=True);
            sleep(0.6)
        print()
        print()
        stamp(username)

    elif choice == "C" or choice == "c" :
        print()
        process = "EDITING CREDIT"
        for i in process:
            print(i, sep=' ', end=' ', flush=True);
            sleep(0.1)
        load = '....★'
        for i in range(5):
            print(load[i], sep=' ', end=' ', flush=True);
            sleep(0.6)
        print()
        print()
        Credits(username)

    elif choice == "L" or choice == "l":
        print()
        bye = "Good Bye ~ "
        for i in bye:
            print(i, sep=' ', end='', flush=True);
            sleep(0.075)
        sleep(0.8)
        print()
        menu()
    elif choice == "Q" or choice == "q" :
        print()
        bye = "Good Bye ~ "
        for i in bye:
            print(i, sep=' ', end='', flush=True);
            sleep(0.075)
        print()
        sleep(1)
        exit(0)
    else:
        select = "You must only select from the given game"
        for i in select:
            print(i, sep=' ', end='', flush=True);
            sleep(0.02)
        sleep(0.5)
        print()

        again = "Please try again"
        for i in again:
            print(i, sep=' ', end='', flush=True);
            sleep(0.02)
        sleep(0.5)
        print()
        print()
        displaygame(username)

def stamp(username):
    try:
        with open('stamprally.txt', 'rb') as file:
            display = pickle.load(file)
            for row in display:
                if row == username:
                    print("══════════════════════════════════════════════════════════")
                    print("                 > |%s 's stamps| <  " % row,
                          "\n                    ✪", display[row][0],
                          "\n                    ✪", display[row][1],
                          "\n                    ✪", display[row][2])
                    print("══════════════════════════════════════════════════════════")
                else:
                    pass
        choice = input("    ------------ Press Enter To Return --------------")
        print()
    except EOFError:
        print("══════════════════════════════════════════════════════════")
        print("                 > |NOT HAVE USER| <  ")
        print("══════════════════════════════════════════════════════════")

    displaygame(username)

if __name__ == '__main__':
    main()