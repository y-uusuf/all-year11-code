word = input("Give me a festive word! ")
letter = input("OK, now a letter! ")

count = 0

for letter in word:
    count =+ 1

print(f"The letter '{letter}' comes up {count} time(s)!")