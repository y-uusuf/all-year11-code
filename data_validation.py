try:
    number = int(input("Enter a number between 1 - 10: "))
    if number < 10:
     Validated = True
    elif number > 1:
     Validated = True
    else:
     print("Number out of range.")
     
except ValueError:
    print("It must be between 1 & 10.")
    exit


# Range Check



name = input("Name? ")
nameLen = len(name)

if nameLen == 0:
    print("Invalid.\n")
elif nameLen < 2:
    print("Invalid.\n")
else:
    print(f"Name Stored: {name}.\n")