import time
import random
import sys


def start():
    global jewel
    jewel = 2
    global health
    health = 10
    global energy
    energy = 10
    global melee
    melee = 1
    global fireRange
    fireRange = 0
    global ammo
    ammo = 0
    global fullhealth
    fullhealth = 10
    global fightNo
    fightNo = 0
    hut()
# definig functions


def print_pause(text, delay):
    time.sleep(delay)
    print(text)


def checkStatus():
    print_pause("\n--------", 1)
    print("jewel:", jewel)
    time.sleep(1)
    print("Health:", health, "/", fullhealth)
    time.sleep(1)
    print("Melee:", melee)
    time.sleep(1)
    print ("Energy:", energy)
    time.sleep(1)
    global fireRange
    if fireRange > 0:
        print("fire range:", fireRange)
        time.sleep(1)
        print("Ammo:", ammo)
        time.sleep(1)
    print("--------")


def userRespond():
    x = input("Choose one:\n>>> ")
    return x


def retry():
    print_pause("-------------------------------------------", 1)
    print_pause("I dont know what is this, blease try again", 1)
# Places:
# hut


def hut():
    print_pause("-------------------------------------------", 1)
    print_pause("You are in your hut in the small island.", 1)
    print_pause("what will you do?", 1)
    print_pause("\nOptions:", 1)
    print_pause("1- Go Outside\n2- Rest\n9- check status\n", 1)
    respond = userRespond()
    if respond.lower().strip() in ("go outside", "outside",
                                   "1", "leave", "go", "out"):
        centralplace()
    elif respond.lower().strip() in ("rest", "2"):
        print_pause("-------------------------------------------", 1)
        print ("You are back to full health."
               "(", fullhealth, "/", fullhealth, ")")
        global health
        health = fullhealth
        hut()
    elif respond.lower().strip() in ("check status",
                                     "check", "status", "9"):
        checkStatus()
        hut()
    else:
        retry()
        hut()
# centralplace


def centralplace():
    print_pause("-------------------------------------------", 1)
    print_pause("You are now in the central place.", 1)
    time.sleep(1)
    print("A few people are walking in the streets,"
          "going to their work as usual.")
    print_pause("\nOptions:", 1)
    time.sleep(1)
    print("\n1- Enter the hut.\n"
          "2- explore the woods.\n"
          "3- Walk to the beach.\n"
          "9- check status.\n")
    respond = userRespond()
    if respond.lower().strip() in ("enter the hut", "hut", "return", "1"):
        hut()
    elif respond.lower().strip() in ("explore the woods",
                                     "woods", "explore", "2"):
        woods()
    elif respond.lower().strip() in ("walk to the beach", "beach", "3"):
        beach()
    elif respond.lower().strip() in ("check status", "check", "status", "9"):
        checkStatus()
        centralplace()
    else:
        retry()
        centralplace()
# woods


def woods():
    global beast
    beast = ["snake", "poisonous frog", "honey bee"]
    global Rbeast
    Rbeast = random.choice(beast)
    global Rnum
    Rnum = random.randint(1, 9)
    print_pause("-------------------------------------------", 1)
    print_pause("You are in the woods. It's too dark and frightening.\n", 1)

    # if this is the firt time to enter the woods
    # the player will lose "random number" of health point.
    global fightNo
    if fightNo == 0:
        print_pause("--------", 1)
        time.sleep(1)
        print("You are attacked by a", Rbeast,
              "\nyou could beat it but unfortunately your health"
              "dropped by", Rnum, "\nwhat will you do now?")

        # this line increases fight number by "1"
        # -records that tha player had a fight-.
        fightNo = 1
        global health
        health = health - Rnum
    # if the player have entered before this is what will happen
    if fightNo == 1:
        print_pause("Options:", 1)
        print_pause("\n1. Go back to the centralplace", 1)
        print_pause("2. Pick up stones", 1)
        print_pause("3. Explore deeper into the woods", 1)
        print_pause("9. check status", 1)
        respond = userRespond()
        if respond.lower().strip() in ("1", "return", "centralplace",
                                       "Go back to the centralplace"):
            centralplace()
        elif respond.lower().strip() in ("2", "pick up stones",
                                         "pick up", "stones"):
            stones()
            woods()
        elif respond.lower().strip() in ("3", "explore",
                                         "explore deeper", "woods",
                                         "deeper",
                                         "explore deeper into the woods"):
            lose()
        elif respond.lower().strip() in ("check status",
                                         "check", "status", "9"):
            checkStatus()
            woods()
        else:
            retry()
            woods()
# beach


def beach():
    print_pause("----------------------------------------", 1)
    print_pause("You are at the beach,\n", 1)
    print_pause("what will you do now?\n", 1)
    time.sleep(1)
    print("Options:\n1. Go back to the centralplace"
          "\n2. Talk to fisherman\n3. Talk to captain"
          "\n4. Pick up stones\n9. check status")
    respond = userRespond()
    if respond.lower().strip() in ("1", "return", "centralplace",
                                   "Go back to the centralplace"):
        centralplace()
    elif respond.lower().strip() in ("2", "talk to the fisherman",
                                     "fisherman"):
        fisherman()
    elif respond.lower().strip() in ("3", "talk to the captain", "captain"):
        captain()
    elif respond.lower().strip() in ("4", "pick up stones",
                                     "pick up", "stones"):
        stones()
        beach()
    elif respond.lower().strip() in ("check status", "check", "status", "9"):
        checkStatus()
        beach()
    else:
        retry()
        beach()
# win


def win():
    time.sleep(1)
    print("-------------------------"
          "------------ Home Sweet Home -----------"
          "--------------------------")
    print_pause("congratulations you won", 1)
# ammo and fire range


def stones():
    global fireRange
    global ammo
    if fireRange == 0:
        print_pause("---------", 1)
        print_pause("\nYou found 5 stones you can throw at an enemy.", 1)
        print_pause("(+1 fire range) (+5 ammo)", 1)
        fireRange = 1
        ammo = 5
    elif fireRange >= 1 and ammo < 5:
        ammo = 5
        print_pause("--------", 1)
        print_pause("You stuff a few stones in your bag for later.", 1)
    elif fireRange >= 1 and ammo > 4:
        print_pause("--------")
        print_pause(
            "You couldn't find any suitable stones.\ntry something else", 1)
# lose


def lose():
    print_pause("----------------", 1)
    time.sleep(1)
    print("unfortunately You have been attacked"
          " by a fantasy monster. What do you do?")
    print_pause(
        "\n1. Run\n2. Fight\n3. Make friendship with it", 1)
    respond = userRespond()
    if respond.lower().strip() in ("1", "run"):
        woods()
    elif respond.lower().strip() in ("2", "fight"):
        print_pause("---------", 1)
        print_pause("You have just been killed by a fantasy monster!!", 1)
        print_pause("GAME OVER!!!!!", 1)
    elif respond.lower().strip() in ("3", "friendship", "friend",
                                     "make friendship with it"):
        print_pause("---------", 1)
        print_pause("You have just been killed by a fantasy monster!!", 1)
        print_pause("GAME OVER!!!!!", 1)
# Training


def fisherman():
    print_pause("--------", 1)
    time.sleep(1)
    print('Fisherman: "I think there are no fishes today'
          '. Want me to teach you a few melee movements?')
    print_pause("1. Yes\n2. No", 1)
    global melee
    respond = userRespond()
    if respond.lower().strip() in ("1", "yes") and melee < 2:
        melee = 2
        print_pause("--------", 1)
        time.sleep(1)
        print("""Fisherman: "Now you are a good"""
              """ fighter,\nbut remember.....you """
              """shouldn't be crul to people.\n(+1 melee)""")
        beach()
    elif respond.lower().strip() in ("1", "yes") and melee > 1:
        print_pause("--------", 1)
        time.sleep(1)
        print("""Fisherman "I think you are already"""
              """ know every thing I know.""")
        beach()
    elif respond.lower().strip() in ("2", "no"):
        print_pause("---------", 1)
        print_pause("""Fisherman: "Well, as you like, It's your choise.""", 1)
        beach()
    else:
        retry()
        beach()


def captain():
    print_pause("--------", 1)
    time.sleep(1)
    print("""Boat captain: "I can sail you to you"""
          """ country for a nominal fee."\n1. Okay\n2. No thanks""")
    respond = userRespond()
    if respond.lower().strip() in ("1", "okay"):
        print_pause("--------", 1)
        print_pause("The boatman sails you to your country.", 1)
        print_pause("(-2 jewel)", 1)
        global jewel
        jewel = jewel - 2
        win()
    elif respond.lower().strip() in ("2", "no", "no thanks", "thanks"):
        beach()
    else:
        retry()
        beach()


def game():
    while True:
        print("\ndo you want to play??")
        print_pause("\noptions:", 1)
        print_pause("1. yes", 1)
        print_pause("2. no", 1)
        time.sleep(1)
        answer = input(">>> ")
        if answer.lower().strip() in ("1", "yes"):
            time.sleep(1)
            print("----------------------------"
                  "--------------------------------------")
            print("----------------Welcome to my te"
                  "xt adventure game-----------------")
            print("----------------------------"
                  "--------------------------------------")
            print_pause("Zzzzzzz !!!", 1)
            time.sleep(1)
            print("Gosh, the plane on board was hit by an accident"
                  " and all the engines stopped")
            print_pause("Oh no!!!!!", 1)
            print_pause("the plane is falling", 1)
            print_pause("The plane has fallen", 2)
            time.sleep(1)
            print(
                "Whatever the case,thank god, you are th"
                "e only one who survived the crash")
            print_pause("the waves took you to the shore of an island.", 1)
            print_pause("what a luck,", 1)
            print_pause("this island have some people living on", 1)
            time.sleep(1)
            print(
                "they saved you and gave you "
                "some kind of a shelter and two jewls")
            start()
        elif answer.lower().strip() in ("2", "no"):
            print_pause("\nThat is too bad.", 1)
            print_pause("bye.", 1)
            sys.exit()
        else:
            print_pause("\nI don't Know what is this, try again", 1)
            game()


game()
