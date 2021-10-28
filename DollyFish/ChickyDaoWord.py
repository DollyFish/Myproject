import random, Menu, csv, pickle,time

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
    welcome =["  ▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼",
              "",
              "                     Welcome to ChickyDaoWord",
              "",
              "  ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲"]
    for i in welcome:
        print(i)
        time.sleep(0.3)
    print()
    choice = input("                        >> Press Enter <<    ")
    print()
    menugame(username)

def menugame(username):
    print("=======================♥  ChickyDaoWord  ♥========================")
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
        print("Chicky : Bye Bye ")
        time.sleep(1)
        print()
        Menu.displaygame(username)
    else:
        print("Chicky : You must only select from the given choice")
        print("Chicky : Please try again")
        menugame(username)

def Tutorial(username):
    print()
    tutorial = ["Chicky : Welcome to ChickyDaoWord",
                "Chicky : I will give you the meaning of the word",
                "Chicky : Enter the letter that you think. You have 10 chance to wrong and every chance I will substract your score.",
                "",
                "Example: Word : Ant",
                "Mean: A small insect, often with a sting, that usually lives in a complex social colony with breeding queens.",
                "Please enter one letter or a 3-letter word.",
                "",
                "Chicky : If you enter A or a , the game will display",
                "Oh! You correct this word contain 1 \"A\"",
                "A**",
                "",
                "Chicky : If you enter wrong letter example is X , the game will display",
                "Huh! This word doesn't contain this letter.",
                "",
                "Chicky : If you enter same letter that you already enter it, the game will display",
                "You have already guessed letter",
                "",
                "Chicky : If you know the word, you can enter full word",
                "",
                "Chicky : If you enter wrong 10 times, the game will over",
                "Chicky : !! But !!",
                "Chicky : If you win, the game will display the word",
                "Chicky : And you will get CHICKYDAO STAMP!"]

    for i in tutorial:
        print(i)
        time.sleep(1.3)
    print()
    print("                       >> Press Enter <<    ")
    choice = input("                       - Return To Menu -    ")
    print()
    menugame(username)

#random word
def ran_word():
    words = ['academy', 'addition', 'address', 'adventure', 'alternate', 'archaeologist',
             'blackmail', 'brilliant', 'camouflage', 'capillary', 'casualties', 'communicate',
             'decentralize', 'democracy', 'demonstrate', 'equivalent', 'exile', 'experiment',
             'family', 'federal', 'fiscal', 'fluke', 'generate', 'geography', 'grateful',
             'handicraft', 'history', 'hospital', 'millennium', 'read']
    return random.choice(words).upper()

#Check and print * for put the letter to it
def check(word,guesses,guess,counter):
    status = ""
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += "*"
        if letter == guess:
            matches += 1
    if matches > 1:
        print("Chicky : Oh! You correct this word contain",matches,'"'+ guess +'"'+'s' )
    elif matches == 1:
        print("Chicky : Oh! You correct this word contain",matches,'"'+ guess +'"')
    else:
        print("Chicky : Huh! This word doesn't contain this letter.")
        counterincrease(counter)
        counter = counterincrease(counter)
    return status, counter

def counterincrease(counter):
    counter += 1
    return counter

def meanword(word):
    if word.lower() == "academy":
        mean = "connected with education, especially studying in schools and universities."
    elif word.lower() == "addition":
        mean = "a thing that is added to something else."
    elif word.lower() == "address":
        mean = "details of where somebody lives or works and where letters, etc. can be sent."
    elif word.lower() == "adventure":
        mean = "an unusual, exciting or dangerous experience, journey or series of events."
    elif word.lower() == "alternate":
        mean = "if something happens on alternate days, nights, etc. it happens on one day, etc. but not on the next."
    elif word.lower() == "archaeologist":
        mean = "a person who studies archaeology."
    elif word.lower() == "blackmail":
        mean = "the crime of demanding money from a person by threatening to tell somebody else a secret about them."
    elif word.lower() == "brilliant":
        mean = "extremely clever or impressive."
    elif word.lower() == "camouflage":
        mean = "a way of hiding soldiers and military equipment, using paint, leaves or nets, so that they look like part of what is around or near them."
    elif word.lower() == "capillary":
        mean = "any of the smallest tubes in the body that carry blood."
    elif word.lower() == "casualties":
        mean = "a person who is killed or injured in war or in an accident Our primary objective is reducing road casualties."
    elif word.lower() == "communicate":
        mean = "to share or exchange information, news, ideas, feelings, etc."
    elif word.lower() == "decentralize":
        mean = "to give some of the power of a central government, organization, etc. to smaller parts or organizations around the country."
    elif word.lower() == "democracy":
        mean = "a system of government in which the people of a country can vote to elect their representatives."
    elif word.lower() == "demonstrate":
        mean = "to show something clearly by giving proof or evidence."
    elif word.lower() == "democracy":
        mean = "a system of government in which the people of a country can vote to elect their representatives."
    elif word.lower() == "demonstrate":
        mean = "to show something clearly by giving proof or evidence."
    elif word.lower() == "equivalent":
        mean = "a thing, amount, word, etc. that is equal in value, meaning or purpose to something else."
    elif word.lower() == "exile":
        mean = "the state of being sent to live in another country that is not your own, especially for political reasons or as a punishment."
    elif word.lower() == "experiment":
        mean = "a scientific test that is done in order to study what happens and to gain new knowledge."
    elif word.lower() == "family":
        mean = "a group consisting of one or two parents and their children."
    elif word.lower() == "federal":
        mean = "having a system of government in which the individual states of a country have control over their own affairs, but are controlled by a central government for national decisions, etc."
    elif word.lower() == "fiscal":
        mean = "connected with government or public money, especially taxes."
    elif word.lower() == "fluke":
        mean = "a lucky or unusual thing that happens by accident, not because of planning or skill."
    elif word.lower() == "generate":
        mean = "generate something to produce energy, especially electricity."
    elif word.lower() == "geography":
        mean = "the scientific study of the earth’s surface, physical features, divisions, products, population, etc."
    elif word.lower() == "grateful":
        mean = "feeling or showing thanks because somebody has done something kind for you or has done as you asked."
    elif word.lower() == "handicraft":
        mean = "the activity of making attractive objects by hand."
    elif word.lower() == "history":
        mean = "all the events that happened in the past."
    elif word.lower() == "hospital":
        mean = "a large building where people who are ill or injured are given medical treatment and care."
    elif word.lower() == "millennium":
        mean = "a period of 1000 years, especially as calculated before or after the birth of Christ."
    elif word.lower() == "read":
        mean = "to look at and understand the meaning of written or printed words or symbols."

    time.sleep(0.8)
    print ("Chicky : The word contain",len(word),"letters.")
    time.sleep(0.8)
    print("Chicky : This word means", mean)
    time.sleep(0.8)

def game(username):
    print()
    print("========================== ",end='')
    gen = "ChickyDaoWord "
    for i in range(14):
        print(gen[i], sep='', end='', flush=True);
        time.sleep(0.1)
    print(end ="===========================")
    print("\n\n")
    word = ran_word()
    guesses = []
    counter = 0
    guessed = False
    generate = 'Loading to ChickyDaoWord...'
    for i in range(27):
        print(generate[i], sep=' ', end=' ', flush=True);
        time.sleep(0.1)
    print()
    print()

    meanword(word)
    time.sleep(1)

    while not guessed:
        text = "Please enter one letter or a {}-letter word. ".format(len(word))

        guess = input(text)
        guess = guess.upper()
        if guess in guesses:
            print('Chicky : You have already guessed '+ guess +'')
            counterincrease(counter)
            counter = counterincrease(counter)
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print("Chicky : Sorry, That's not correct😊")
                counterincrease(counter)
                counter = counterincrease(counter)
        elif len(guess) == 1:
            guesses.append(guess)
            result =  check(word,guesses,guess,counter)
            counter = result[1]
            if result[0] == word:
                guessed = True
            else:
                print(result[0])
        else:
            print("Chicky : Invalid value")
            counterincrease(counter)
            counter = counterincrease(counter)
        if counter >= 10:
            gameover(username, word)
            guessed = True

    time.sleep(0.3)
    print("Chicky : Ah! You got it. The word is", word,"you got it in",len(guesses),"tries.")
    time.sleep(0.6)

    with open('stamprally.txt', 'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            data = {}

    with open('stamprally.txt', 'wb') as file:
        data[username][0] = "CHICKYDAO STAMP"
        pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
        print("%s, YOU GET \"CHICKYDAO STAMP\" !! " % username)
        print()
        save = 'SAVING SUCCESS ...'
        for i in save:
            print(i , sep=' ', end=' ', flush=True);
            time.sleep(0.1)
        print()
        print()
        time.sleep(0.5)
        file.close()

    endgame(username)

def gameover(username,word):
    print("Chicky : HaHa!! Game Over...")
    time.sleep(1)
    print("Chicky : You Lost")
    time.sleep(1)
    print("Chicky : The answer is ", word)
    time.sleep(1)
    print()
    print("                       >> Press Enter <<    ")
    choice = input("                       - Return To Menu -    ")
    print()
    menugame(username)

def endgame(username):
    print("Please select your choice")
    choice = input("""
            -> R. Replay
            -> Q. Back to menu
            -> S. CheckStamp
            Your Choice: """)
    if choice.lower() == "r":
        game(username)
    elif choice.lower() == "q":
        menugame(username)
    elif choice.lower() == "s":
        stamp(username)
    else:
        print("You must only select from the given choice")
        print("Please try again")
        endgame(username)

def stamp(username):
    print()
    with open('stamprally.txt', 'rb') as file:
        display = pickle.load(file)
        for row in display:
            if row == username:
                print("================================================================")
                print("                      > |%s 's stamps| <  " % row,
                      "\n                         ♦", display[row][0],"♦",
                      "\n                         ♦", display[row][1],"♦",
                      "\n                         ♦", display[row][2],"♦")
                print("================================================================")
            else:
                pass
    choice = input("                    >> Press Enter To Return <<    ")
    print()

    menugame(username)

if __name__ == '__main__':
    maingame()