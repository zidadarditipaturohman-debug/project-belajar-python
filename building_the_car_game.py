command = ""
stared = False
while command != "exit":
    command = input(" > ").lower()
    if command == "start":
        if stared :
            print("You have already started the game")
        else:
            stared = True
        print("car started....")
    elif command == "stop":
        if not stared:
            print("You have already stopped the game")
        else:
            stared = False
        print("car stopped....")
    elif command == "help":
        print("""
        start - starts the game
        stop - stops the game
        quit - quits the game
        """)
    elif command == "exit":
        break
    else:
        print("Sorry, try again")

#tanda seru (!) artinya "tidak" dan jika digabung maka tidak "sama dengan"