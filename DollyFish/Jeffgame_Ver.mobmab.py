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
    print("═════ ♡♡♡♡ Welcome to Taboo Count ∠( ᐛ 」∠)＿ !! ♡♡♡♡ ═════")
    choice = input("""      
      ---------- Press Enter To Start ----------- """)
    print()
    menugame(username)


def menugame(username):
    print("          ════════════════════════════════════")
    print("          Ready for Taboo Count ? ٩(ˊᗜˋ*)و ~✧ ")
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
        print("𝙅𝙚𝙛𝙛 𝙩𝙝𝙚 𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧 𝙨𝙖𝙞𝙙 𝙜𝙤𝙤𝙙𝙗𝙮𝙚 へ[ •́ ‸ •̀ ]ʋ")
        sleep(1)
        print()
        Menu.displaygame(username)
    else:
        print()
        print("𝙔𝙤𝙪 𝙢𝙪𝙨𝙩 𝙤𝙣𝙡𝙮 𝙨𝙚𝙡𝙚𝙘𝙩 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝙜𝙞𝙫𝙚𝙣 𝙘𝙝𝙤𝙞𝙘𝙚")
        print("𝙋𝙡𝙚𝙖𝙨𝙚 𝙩𝙧𝙮 𝙖𝙜𝙖𝙞𝙣... (｡•́︿•̀｡)")
        print()
        menugame(username)


def Tutorial(username):
    instruction = ["𝐈𝐧 𝐓𝐚𝐛𝐨𝐨 𝐂𝐨𝐮𝐧𝐭 ...",
                   "𝐏𝐥𝐚𝐲𝐞𝐫 𝐦𝐮𝐬𝐭 𝐜𝐨𝐦𝐩𝐞𝐭𝐞 𝐚𝐠𝐚𝐢𝐧𝐬𝐭 𝐉𝐞𝐟𝐟 𝐭𝐡𝐞 𝐜𝐨𝐦𝐩𝐮𝐭𝐞𝐫 ٩(ˊᗜˋ*)و ~✧",
                   "",
                   "1. 𝘼 𝙏𝙖𝙗𝙤𝙤 𝙣𝙪𝙢𝙗𝙚𝙧 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙜𝙚𝙣𝙚𝙧𝙖𝙩𝙚𝙙",
                   "",
                   "2. 𝘾𝙝𝙤𝙤𝙨𝙚 𝙩𝙤 𝙥𝙡𝙖𝙮 𝙛𝙞𝙧𝙨𝙩 𝙤𝙧 𝙨𝙚𝙘𝙤𝙣𝙙, 𝙖𝙨 𝙬𝙚𝙡𝙡 𝙖𝙨 𝙝𝙤𝙬 𝙢𝙖𝙣𝙮 𝙣𝙪𝙢𝙗𝙚𝙧𝙨 𝙮𝙤𝙪 𝙬𝙞𝙨𝙝 𝙩𝙤 𝙚𝙣𝙩𝙚𝙧 ...",
                   "",
                   "* 𝘽𝙐𝙏 𝙛𝙤𝙧 𝙚𝙖𝙘𝙝 𝙩𝙪𝙧𝙣, 𝙮𝙤𝙪 𝙘𝙖𝙣 𝙤𝙣𝙡𝙮 𝙚𝙣𝙩𝙚𝙧 𝙗𝙚𝙩𝙬𝙚𝙚𝙣 𝙤𝙣𝙚 𝙩𝙤 𝙩𝙝𝙧𝙚𝙚 𝙣𝙪𝙢𝙗𝙚𝙧𝙨 𝙖𝙩 𝙖 𝙩𝙞𝙢𝙚 *",
                   "* 𝙏𝙝𝙚 𝙣𝙪𝙢𝙗𝙚𝙧𝙨 𝙩𝙝𝙖𝙩 𝙮𝙤𝙪 𝙚𝙣𝙩𝙚𝙧 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙞𝙣𝙩𝙚𝙜𝙚𝙧𝙨 𝙖𝙣𝙙 𝙩𝙝𝙚𝙮 𝙢𝙪𝙨𝙩 𝙗𝙚 𝙞𝙣 𝙖 𝙘𝙤𝙣𝙨𝙚𝙘𝙪𝙩𝙞𝙫𝙚 𝙤𝙧𝙙𝙚𝙧 (𝙤𝙣𝙚 𝙖𝙛𝙩𝙚𝙧 𝙖𝙣𝙤𝙩𝙝𝙚𝙧) *",
                   "* 𝙄𝙛 𝙮𝙤𝙪 𝙖𝙧𝙚 𝙚𝙣𝙩𝙚𝙧𝙞𝙣𝙜 𝙢𝙤𝙧𝙚 𝙩𝙝𝙖𝙣 𝙤𝙣𝙚 𝙣𝙪𝙢𝙗𝙚𝙧, 𝙚𝙣𝙩𝙚𝙧 𝙤𝙣𝙚 𝙣𝙪𝙢𝙗𝙚𝙧 𝙖𝙩 𝙖 𝙩𝙞𝙢𝙚 𝙖𝙣𝙙 𝙥𝙧𝙚𝙨𝙨 𝙚𝙣𝙩𝙚𝙧 𝙖𝙛𝙩𝙚𝙧 𝙮𝙤𝙪'𝙫𝙚 𝙛𝙞𝙣𝙞𝙨𝙝𝙚𝙙 𝙚𝙣𝙩𝙚𝙧𝙞𝙣𝙜 𝙚𝙖𝙘𝙝 𝙫𝙖𝙡𝙪𝙚 *",
                   "",
                   "3. 𝙀𝙣𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙫𝙖𝙡𝙪𝙚𝙨",
                   "",
                   "4. 𝙒𝙖𝙞𝙩 𝙛𝙤𝙧 𝙅𝙚𝙛𝙛 𝙩𝙝𝙚 𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧 𝙩𝙤 𝙘𝙤𝙪𝙣𝙩 𝙞𝙩𝙨 𝙫𝙖𝙡𝙪𝙚𝙨 𝙖𝙣𝙙 𝙥𝙡𝙖𝙮𝙚𝙧𝙨 𝙬𝙞𝙡𝙡 𝙩𝙝𝙚𝙣 𝙩𝙖𝙠𝙚 𝙩𝙪𝙧𝙣𝙨",
                   "",
                   "𝙏𝙝𝙚 𝙥𝙡𝙖𝙮𝙚𝙧 𝙬𝙝𝙤 𝙘𝙤𝙪𝙣𝙩𝙨 𝙩𝙝𝙚 𝙏𝙖𝙗𝙤𝙤 𝙣𝙪𝙢𝙗𝙚𝙧 𝙡𝙤𝙨𝙚𝙨 𝙖𝙣𝙙 𝙩𝙝𝙚 𝙥𝙡𝙖𝙮𝙚𝙧 𝙬𝙝𝙤 𝙘𝙖𝙣 𝙖𝙫𝙤𝙞𝙙 𝙞𝙩 𝙬𝙞𝙣𝙨 !",
                   "",
                   "〚 ! 𝐖𝐀𝐑𝐍𝐈𝐍𝐆 ! 〛",
                   "𝐈𝐟 𝐲𝐨𝐮 𝐞𝐧𝐭𝐞𝐫 𝐧𝐮𝐦𝐛𝐞𝐫𝐬 𝐭𝐡𝐚𝐭 𝐚𝐫𝐞... ",
                   "! 𝐍𝐎𝐓 𝐢𝐧𝐭𝐞𝐠𝐞𝐫𝐬",
                   "! 𝐍𝐎𝐓 𝐢𝐧 𝐚 𝐜𝐨𝐧𝐬𝐞𝐜𝐮𝐭𝐢𝐯𝐞 𝐨𝐫𝐝𝐞𝐫",
                   "! 𝐄𝐧𝐭𝐞𝐫 𝐌𝐎𝐑𝐄 𝐓𝐇𝐀𝐍 𝐨𝐧𝐞 𝐭𝐨 𝐭𝐡𝐫𝐞𝐞 𝐧𝐮𝐦𝐛𝐞𝐫𝐬 𝐚𝐭 𝐚 𝐭𝐢𝐦𝐞",
                   "! 𝐄𝐧𝐭𝐞𝐫 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐧𝐮𝐦𝐛𝐞𝐫𝐬",
                   "𝙔𝙊𝙐 𝙒𝙄𝙇𝙇 𝘼𝙐𝙏𝙊𝙈𝘼𝙏𝙄𝘾𝘼𝙇𝙇𝙔 𝘽𝙀 𝙀𝙇𝙄𝙈𝙄𝙉𝘼𝙏𝙀𝘿 𝙁𝙍𝙊𝙈 𝙏𝙃𝙀 𝙂𝘼𝙈𝙀 ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃",
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
                print("                  ✧ %s '𝙨 𝙨𝙩𝙖𝙢𝙥𝙨 ✧ :" % row,
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
    print("\n\n𝙔𝙊𝙐 𝙇𝙊𝙎𝙀 !")
    print("𝙅𝙚𝙛𝙛 (𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧) : 𝘽𝙚𝙖𝙩 𝙢𝙚 𝙣𝙚𝙭𝙩 𝙩𝙞𝙢𝙚 (ﾉ `･∀･)ﾉﾞ")

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
    print("\n\n𝘾𝙊𝙉𝙂𝙍𝘼𝙏𝙐𝙇𝘼𝙏𝙄𝙊𝙉𝙎 %s !!!" % username)
    print("𝙔𝙊𝙐 𝙒𝙊𝙉˛₍˴◅ˋ)੭✧ !!")
    with open('stamprally.txt', 'rb') as file:
        try:
            data = pickle.load(file)
        except EOFError:
            data = {}

    with open('stamprally.txt', 'wb') as file:
        data[username][1] = "JEFF STAMP"
        pickle.dump(data, file, protocol=pickle.HIGHEST_PROTOCOL)
        print()
        print("%s, 𝙔𝙊𝙐'𝙑𝙀 𝙍𝙀𝘾𝙀𝙄𝙑𝙀𝘿 \" ★ 𝙅𝙀𝙁𝙁 𝙎𝙏𝘼𝙈𝙋 ★ \" (ﾉ^ヮ^)ﾉ*:・ﾟ✧!! " % username)
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
    print("𝙅𝙚𝙛𝙛 (𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧) : 𝙏𝙝𝙚 𝙏𝙖𝙗𝙤𝙤 𝙣𝙪𝙢𝙗𝙚𝙧 𝙞𝙨【 %d 】!!!" % deathnum)
    print()

    while True:

        playerselect = ["𝐄𝐧𝐭𝐞𝐫 '𝐩𝟏' 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐟𝐢𝐫𝐬𝐭.", "𝐄𝐧𝐭𝐞𝐫 '𝐩𝟐' 𝐭𝐨 𝐩𝐥𝐚𝐲 𝐬𝐞𝐜𝐨𝐧𝐝."]

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
                        "\n𝐇𝐨𝐰 𝐦𝐚𝐧𝐲 𝐧𝐮𝐦𝐛𝐞𝐫𝐬 𝐝𝐨 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐞𝐧𝐭𝐞𝐫 ? ( 𝐌𝐢𝐧 : 𝟏 & 𝐌𝐚𝐱 : 𝟑 ) ( 𝐓𝐚𝐛𝐨𝐨 𝐍𝐮𝐦𝐛𝐞𝐫 :【 %d 】)" % deathnum)
                    try:
                        usernum = int(input('>> '))
                    except ValueError:
                        print("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙞𝙣𝙥𝙪𝙩 !! ... 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙚𝙡𝙞𝙢𝙞𝙣𝙖𝙩𝙚𝙙 ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                        lose(username)

                    if usernum > 0 and usernum <= 3:
                        comjeff = random.randint(1, 3)
                    else:
                        print("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙞𝙣𝙥𝙪𝙩 !! ... 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙚𝙡𝙞𝙢𝙞𝙣𝙖𝙩𝙚𝙙 ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                        lose(username)

                    i, j = 1, 1

                    print("𝙋𝙡𝙚𝙖𝙨𝙚 𝙚𝙣𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙫𝙖𝙡𝙪𝙚𝙨 : ")
                    while i <= usernum:
                        try:
                            value = input('>> ')
                            value = int(value)
                            if len(numberlist) == 0 and value > 1:
                                lose(username)

                            if value == deathnum:
                                numberlist.append(value)
                                print("𝙉𝙪𝙢𝙗𝙚𝙧𝙨 𝙖𝙛𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙩𝙪𝙧𝙣 𝙞𝙨 : ")
                                print(numberlist)
                                lose(username)

                        except ValueError:
                            print(
                                "𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙞𝙣𝙥𝙪𝙩 !! ... 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙚𝙡𝙞𝙢𝙞𝙣𝙖𝙩𝙚𝙙 ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
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
                            print("𝙉𝙪𝙢𝙗𝙚𝙧𝙨 𝙖𝙛𝙩𝙚𝙧 𝙅𝙚𝙛𝙛 𝙩𝙝𝙚 𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧'𝙨 𝙩𝙪𝙧𝙣 𝙞𝙨 : ")
                            print(numberlist)
                            last = numberlist[-1]
                            if len(numberlist) >= deathnum:
                                victory(username)

                    else:
                        print(
                            "\n𝙔𝙤𝙪 𝙙𝙞𝙙𝙣'𝙩 𝙚𝙣𝙩𝙚𝙧 𝙘𝙤𝙣𝙨𝙚𝙘𝙪𝙩𝙞𝙫𝙚 𝙞𝙣𝙩𝙚𝙜𝙚𝙧𝙨. 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙚𝙡𝙞𝙢𝙞𝙣𝙖𝙩𝙚𝙙 ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ !!")
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
                print("𝙉𝙪𝙢𝙗𝙚𝙧𝙨 𝙖𝙛𝙩𝙚𝙧 𝙅𝙚𝙛𝙛 𝙩𝙝𝙚 𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧'𝙨 𝙩𝙪𝙧𝙣 𝙞𝙨 : ")
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
                        "\n𝐇𝐨𝐰 𝐦𝐚𝐧𝐲 𝐧𝐮𝐦𝐛𝐞𝐫𝐬 𝐝𝐨 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐞𝐧𝐭𝐞𝐫 ? ( 𝐌𝐢𝐧 : 𝟏 & 𝐌𝐚𝐱 : 𝟑 ) ( 𝐓𝐚𝐛𝐨𝐨 𝐍𝐮𝐦𝐛𝐞𝐫 :【 %d 】)" % deathnum)

                    try:
                        usernum = input('>> ')
                        usernum = int(usernum)
                    except ValueError:
                        print("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙞𝙣𝙥𝙪𝙩 !! ... 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙚𝙡𝙞𝙢𝙞𝙣𝙖𝙩𝙚𝙙 ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                        lose()
                    if usernum > 0 and usernum <= 3:
                        comjeff = random.randint(1, 3)
                    else:
                        print("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙞𝙣𝙥𝙪𝙩 !! ... 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙚𝙡𝙞𝙢𝙞𝙣𝙖𝙩𝙚𝙙 ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
                        lose(username)

                    i = 1

                    print("𝙋𝙡𝙚𝙖𝙨𝙚 𝙚𝙣𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙫𝙖𝙡𝙪𝙚𝙨 : ")
                    while i <= usernum:
                        try:
                            value = input('>> ')
                            value = int(value)

                            if value == deathnum:
                                numberlist.append(value)
                                print("𝙉𝙪𝙢𝙗𝙚𝙧𝙨 𝙖𝙛𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙩𝙪𝙧𝙣 𝙞𝙨 : ")
                                print(numberlist)
                                lose(username)

                        except ValueError:
                            print(
                                "𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙞𝙣𝙥𝙪𝙩 !! ... 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙚𝙡𝙞𝙢𝙞𝙣𝙖𝙩𝙚𝙙 ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ ")
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
                            "\n𝙔𝙤𝙪 𝙙𝙞𝙙𝙣'𝙩 𝙚𝙣𝙩𝙚𝙧 𝙘𝙤𝙣𝙨𝙚𝙘𝙪𝙩𝙞𝙫𝙚 𝙞𝙣𝙩𝙚𝙜𝙚𝙧𝙨. 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙚𝙡𝙞𝙢𝙞𝙣𝙖𝙩𝙚𝙙 ( ง ᵒ̌皿ᵒ̌)ง⁼³₌₃ !!")
                        lose(username)

                    if len(numberlist) == deathnum - 4 or len(numberlist) == deathnum - 8:
                        comjeff = 3
                    elif len(numberlist) == deathnum - 3 or len(numberlist) == deathnum - 7:
                        comjeff = 2
                    elif len(numberlist) == deathnum - 2 or len(numberlist) == deathnum - 1 or len(numberlist) == deathnum - 6:
                        comjeff = 1

        else:
            print()
            print("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙘𝙝𝙤𝙞𝙘𝙚.. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙧𝙚-𝙚𝙣𝙩𝙚𝙧 .. (｡•́︿•̀｡)")


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
        print("=====✧ 𝙃𝙞 ~ %s, 𝙄'𝙢 𝙅𝙚𝙛𝙛 𝙩𝙝𝙚 𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧 ✧===== " % username)
        print("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙥𝙡𝙖𝙮 𝙏𝙖𝙗𝙤𝙤 𝘾𝙤𝙪𝙣𝙩 𝙬𝙞𝙩𝙝 𝙢𝙚 ? (Yes / No)")
        choice = input('>> ')
        if choice == "Yes" or choice == "yes" or choice == "YES":
            startgame(username)

        elif choice == "No" or choice == "no" or choice == "NO":
            print()
            print("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙩𝙤 𝙦𝙪𝙞𝙩 𝙏𝙖𝙗𝙤𝙤 𝘾𝙤𝙪𝙣𝙩 ?")
            print("𝙅𝙚𝙛𝙛 𝙩𝙝𝙚 𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙨𝙖𝙙 (｡•́︿•̀｡)) (Yes / No)")

            choice2 = input('>> ')

            if choice2 == "Yes" or choice2 == "yes" or choice2 == "YES":
                print()
                print("𝙅𝙚𝙛𝙛 𝙩𝙝𝙚 𝙘𝙤𝙢𝙥𝙪𝙩𝙚𝙧 𝙨𝙖𝙞𝙙 𝙜𝙤𝙤𝙙𝙗𝙮𝙚 へ[ •́ ‸ •̀ ]ʋ")
                sleep(0.8)
                print()
                menugame(username)
            elif choice2 == "No" or choice2 == "no" or choice2 == "NO":
                print()
                print("𝙊𝙆 ! 𝙇𝙚𝙩'𝙨 𝙥𝙡𝙖𝙮 !（=´∇｀=）")
            else:
                print("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙘𝙝𝙤𝙞𝙘𝙚.. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙧𝙚-𝙚𝙣𝙩𝙚𝙧 .. (｡•́︿•̀｡)")

        else:
            print("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙘𝙝𝙤𝙞𝙘𝙚.. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙧𝙚-𝙚𝙣𝙩𝙚𝙧 .. (｡•́︿•̀｡)")


if __name__ == '__main__':
    maingame()

