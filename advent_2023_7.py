num = int(input("What was your score? "))

if num > 100:
    print("Score too high.")
elif num < 50:
    print("You're on the naughty list!")
elif num > 50:
    print("You're on the nice list!")
else:
    print("Score too low.")