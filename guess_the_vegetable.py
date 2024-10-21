print("Welcome to guess the vegetable!")
print("\nThink of either a Carrot, Sweetcorn, Brocoli, or Pea!")
print("\nType 1 for yes, and 0 for no.")
print("\nPress [ENTER] to begin!")
input()

isGreen = int(input("\nIs it green? "))

if isGreen == 1:
    isFluffy = int(input("\nDoes it have fluff on the top? "))
    if isFluffy == 1:
        print("\nYou're thinking of brocoli!")
    else:
        print("You're thinking of peas!")
else:
    isOrange = int(input("\nIs it orange? "))
    if isOrange == 1:
        print("\nIt's a carrot!")
    else:
        print("\nIt's a sweetcorn!")

