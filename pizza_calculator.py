total = 0


#Crusts



thick = 8
thin = 10

inch = int(input("How many inches?     £"))

if inch > 10:
    total = inch * 0.6

hasCheese = input("Do you want cheese? [Y/N]  ")

if hasCheese == "Y" or hasCheese == "y":
    total = total + 0.5
else:
    total = total - 0.5

print("\nWhat type of pizza do you want? \n\nMargarita,\nVegetable,Hawaiian,Meat Feast.\n\n")

type = input().lower()

if type == "margarita":
    total = total
if type == "vegetable":
    total = total + 1
if type == "hawaiian":
    total = total + 2
if type == "meat feast":
    total = total + 2


print("If you have a promo code, enter it here.\n\nOtherwise, type N.")

promoCode = input().lower()

if promoCode != "n":
    if promoCode == "funfriday":
        total = total - 2
        

print(f"Your total comes to £{total}.")
exit

