from os import system as s
from time import sleep as l

def encrypt(x,y):
    z = ""

    for i in range(len(x)):
        character = x[i]
        

        if character == " ":
            z += " "

        elif (character.isupper()):
            z += character((ord(character) + y-65) % 26 + 65)
 
        
        else:
            z += character((ord(character) + y-97) % 26 + 97)
    
    return z


while 1:
 shift = int(input("What shift do you want? "))
 text = str(input("What do you want to encrypt? "))
 print("Encrypted text is: " + encrypt(text,shift))
 l(3)
 s("cls")

