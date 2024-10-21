import random

dice = random.randint(1,6)

yorn = input("Wanna roll a dice? [Y/N]: ").lower()

if yorn == 'y':
    print(f"The number you got was:\n{dice}")
else:
    exit