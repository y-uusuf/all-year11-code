# Guess the number.

""" from random import randint as r

num = r(1,100)

attempt = 1
g = int(input(f"Guess a number 1-100: [Attempt: {attempt}] "))

while g != num:
    if g > num:
        print("Too high.")
    elif g < num:
        print("Too low.")
    else:
        print("Not a number between 1 - 100.")
    
    attempt = attempt + 1
    g = int(input(f"Guess a number 1-100: [Attempt: {attempt}] "))

print(f"You got it! It took you {attempt} attempt(s).")

"""


# Mad libs

"""
name = str(input("Name? "))
object = str(input("Object? "))
adverb = str(input("Adverb? "))
proper_noun = str(input("Proper Noun? "))

print(f"\n{name} flew to the school when he saw the {object} and {adverb} took it away to {proper_noun}!")
"""

# pw generator

"""
import string as s
import random as r


def gp(length):
    pu = int(input("Do you want to add punctuation?\n[1: YES]\n[2: NO]\n\n>> "))
    if pu == 1:
         ch = s.ascii_letters + s.digits + s.punctuation
    elif pu == 2:
          ch = s.ascii_letters + s.digits 
    else:
         print("Error, not a choice.")
         exit
    
    pw = ''.join(r.choice(ch) for _ in range(length))
    return pw

dl = int(input("Enter desired password length:\n!! Minimum of 8 characters !!\n\n>> "))

if dl < 8:
 print("Too low of a value.")
else: 
 g_p = gp(dl)
 print("Generated password:", g_p)

 """


# rock paper scisors

"""
from random import randint as r

ai_c = r(1, 3)

if ai_c == 1:
    ai_c = 'r'
if ai_c == 2:
    ai_c = 'p'
if ai_c == 3:
    ai_c == 's'


p_c = str(input("[ROCK] r\n[PAPER] p\n[SICISORS] s\n\n>> "))

p_c = p_c.lower()

if p_c not in ('r', 'p', 's'):
    print("Invalid answer.")
    exit()
else:
    if p_c == 'r' and ai_c == 'p':
        print("AI won with paper!")
    if p_c == 'p' and ai_c == 'r':
        print("You won with paper! [AI had rock.]")
    if p_c == 's' and ai_c == 'r':
        print("AI won with rock!")
    if p_c == 'r' and ai_c == 's':
        print("You won with rock! [AI had sicisors.]")
    if p_c == 's' and ai_c == 'r':
        print("AI won with rock!")
    if p_c == 'r' and ai_c == 's':
        print("You won with rock! [AI had sicisors.]")
    if p_c == 'p' and ai_c == 's':
        print("AI won with sicisors!")
    if p_c == 's' and ai_c == 'p':
        print("You won with sicisors! [AI had paper.]")
    
"""