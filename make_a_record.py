player = {

}

playerUser = input("What's your name? ")
playerPassword = input("What's your password? ")
playerISBN = int(input("What's your ISBN? "))

player = {
    "user" : playerUser,
    "pwd" : playerPassword,
    "isbn" : playerISBN
}

print(f"Just to recap..\n\nYour name is '{player['user']}'\nYour password is '{player['pwd']}\nYour ISBN is '{player['isbn']}")