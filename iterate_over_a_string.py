word = "aramsamsam"
count = 0
char = input("Letter? ")

if len(char) > 1:
    print("Only 1 letter.")
    exit

for letter in word:
    if letter == char:
        count =+1

print(f"\nThe letter '{char}' came up {count} time(s).")