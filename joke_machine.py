print("What is the start of my joke? \n\n")

score = 0
punchline = input().upper()

# Initialising variables.


if punchline == "THE PUNCHLINE":
    score = score + 1
    print("Well done, you are correct!\n\nScore: " + score)
else:
    print("Wrong, it was 'THE PUNCHLINE' ")

# if/else Function to check if "punchline" is equal to "THE PUNCHLINE"



punchline2 = input().upper()


if punchline2 == "PINK FLUFF":
    score = score + 1
    print("Well done, you are correct!\n\nScore: " + score)
else:
    print("Wrong, it was 'PINK FLUFF' ")

# if/else Function to check if "punchline" is equal to "PINK FLUFF"


print("\n\nWhat is the last joke? ")

# Asking for the last joke.

punchline3 = input().upper()


if punchline3 == "BROWN STICK":
    score = score + 1
    print("Well done, you are correct!\n\nScore: " + score)
else:
    print("Wrong, it was 'BROWN STICK' ")

# if/else Function to check if "punchline" is equal to "BROWN STICK", or "BLUE SKY"
