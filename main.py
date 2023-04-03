equip = False


def monster():
    actions = ["fight", "run away"]
    global equip
    print("A monster has appeared from nowhere. You can either run or fight! Please pick an option?")
    userInput = ""
    while userInput not in actions:
        print("Options: run away/fight")
        userInput = input()
        if userInput == "fight":
            if equip:
                print(
                    "You have killed the monster with the Sword. And found the way out. Congrats!")
            else:
                print("The monster has defeated you.")
            quit()
        elif userInput == "run away":
            darkJungle()
        else:
            print("It is invalid. Please choose the above two options.")


def darkJungle():
    directions = ["backward", "forward"]
    global equip
    print("You are being watched by someone, be careful. Please pick an option to go ahead?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/backward/forward")
        userInput = input()
        if userInput == "left":
            print("You have found a divine Sword.")
            equip = True
        elif userInput == "backward":
            introductionScene()
        elif userInput == "forward":
            monster()
        else:
            print("It is invalid. Please choose the given options.")


def dangerZone():
    directions = ["right", "left", "backward"]
    print("It seems you have awoken a monster. Please pick an option to go ahead with?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            print("You have encountered many monsters. Hence, you have been killed.")
            quit()
        elif userInput == "left":
            print("Hurrah ! You are out of danger and found way out.")
            quit()
        elif userInput == "backward":
            introductionScene()
        else:
            print("It is invalid. Please choose the given options.")


def clueScene():
    directions = ["forward", "backward"]
    print(
        "You found a clue that someone has been here recently. Which option would you pick to go ahead?")
    userInput = ""
    while userInput not in directions:
        print("Options: forward/backward")
        userInput = input()
        if userInput == "forward":
            print("Hurrah! you have found a way out. Congrats!")
            quit()
        elif userInput == "backward":
            monsterDiscovery()
        else:
            print("It is invalid. Please choose the given options.")


def monsterDiscovery():
    directions = ["right", "backward"]
    print("You sense something has appeared which is creeping you out. Which option would you like to pick?")
    userInput = ""
    while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
        if userInput == "right":
            clueScene()
        elif userInput == "left":
            print("You faced a deadend.")
        elif userInput == "backward":
            introductionScene()
        else:
            print("It is invalid. Please choose the given options.")


def introductionScene():
    directions = ["left", "right", "forward"]
    print(
        "You encountered a junction, and you been asked to choose any of the available 4 options. Where would you go?")
    userInput = ""
    while userInput not in directions:
        print("Options: left/right/backward/forward")
        userInput = input()
        if userInput == "left":
            monsterDiscovery()
        elif userInput == "right":
            darkJungle()
        elif userInput == "forward":
            dangerZone()
        elif userInput == "backward":
            print("You faced a deadend.")
        else:
            print("It is invalid. Please choose the above 4 options.")


if __name__ == "__main__":
    while True:
        print("Welcome to the Dangerous Adventure Game!")
        print("You are visiting the Amazon Jungle.")
        print("However, you been lost while exploring the Jungle.")
        print("You been provided options to walk in multiple directions in order to seek way out alive.")
        print("We shall begin with your name: ")
        name = input()
        print("All the best, " + name + "!")
        introductionScene()