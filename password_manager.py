usernames = ["yusuf"]
passwords = ["lol"]

def login(x, y):
    for name in usernames:
        if x == name:
            foundUser = True
        else:
            foundUser = False

    for name in passwords:
        if y == name:
            foundPassword = True
        else:
            foundPassword = False

    if foundUser != True and foundPassword == True:
        print(f"Username '{x}' not found/incorrect.")
    elif foundUser == True and foundPassword != True:
        print(f"Password '{y}' not found/incorrect.")
    elif foundUser == False & foundPassword == False:
        print(f"Both your username & password were not found/incorrect.")
    else:
        print("Logged in!")


inputUser = input("Username? ")
inputPassword = input("Password? ")

login(inputUser, inputPassword)