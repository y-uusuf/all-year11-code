print("Pick either Ostrich, Lion ,Whale or Fish")
print("I will attempt to guess your choice")
print("Does the animal live in the water? Y/N")
answer=input().lower()

if answer =="n":
    print("Does the animal have wings? Y/N")
    answer=input().lower()
    if answer =="y":
        print("It must be an Ostrich!")
    else:
        print("It must be a Lion!")

if answer == "y":
     print("Is the animal a mammal? Y/N")
     answer=input().lower()
     if answer == "y":
         print("It must be a whale!")
     else:
         print("It must be a Fish!")