players = []
player = {}

def addPlayer():
    global player
    global players

    user = input("What's your username? ")
    pwd = input("What's your password? ")
    c_pwd = input("Confirm your password: ")

    if c_pwd != pwd:
        print("Incorrect password entered.")
    else:
        player = {
            "username": user,
            "password": pwd
        }

    players.append(player)
        

def main():  
 answer = int(input("Would you like to add another player?\n1 for yes, 2 for no.\n\n> "))

 if answer == 1:
    addPlayer()
 elif answer == 2:
    exit
 else:
    print("Incorrect answer.")