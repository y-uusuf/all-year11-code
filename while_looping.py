def name():
    while True:
        animal = input("What\'s your name? ")
        if animal.lower() == "yusuf":
            print("How do you do, Yusuf? \n")
        else:
            print("You\'re not Yusuf. \n")
            break

# Start the game
name()
