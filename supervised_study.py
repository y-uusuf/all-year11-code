from random import randint as rnd
from time import sleep as sl
from os import system as sy

r = [
    "Cherry",
    "Bell",
    "Lemon",
    "Orange",
    "Star",
    "Skull"
]

c = 1.00

def game():
 sy('cls')

 global c

 if c < 0:
    print("I'm sorry, you don't have enough credit to play.")
    exit()

 c = c - 0.2

 print("\n\nSpinning...")
 sl(1.5)

 spin_1 = rnd(0,4)
 spin_2 = rnd(0,4)
 spin_3 = rnd(0,4)

 print(f'{r[spin_1]}!')
 sl(0.5)
 print(f'{r[spin_2]}!')
 sl(0.5)
 print(f'{r[spin_3]}!')
 sl(0.5)

 print(f'\nFinal roll: {r[spin_1]} - {r[spin_2]} - {r[spin_3]}.')

 if spin_1 == spin_2 or spin_2 == spin_3 or spin_1 == spin_3:
    print("You rolled 2 of the same things!\n\nAwarded: 50p credit.")
    c = c + 0.5
    print(f"\nYou now have: £{c}.")
 if spin_1 == spin_2 and spin_1 == spin_3 and spin_2 == spin_3:
    if spin_1 == 1 and spin_2 == 1 and spin_3 == 1:
        print("You got 3 bells!\n\nAwarded: £5 credit.") 
        c = c + 5
    
    if spin_1 == 4 and spin_2 == 4 and spin_3 == 4:
        print("You rolled 3 skulls, you can't play anymore!")
        exit()
    if spin_1 == 4 and spin_2 == 4 or spin_2 == 4 and spin_3 == 4 or spin_1 == 4 and spin_3 == 4:
        print("You rolled 2 skulls, sorry!\n\nDeducted: -£1.")
        c = c - 1
        if c < 0:
         print("You can't play anymore, you're out of money!")
         exit()
        else:
            print(f"You now have: £{c}.")

 input('Click [ENTER] to play again.')
 game()

input('Click [ENTER] to roll: ')
game()