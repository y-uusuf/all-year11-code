inital = input("What is your first inital? ")
surname = input("\nWhat is your surname? ")
age = int(input("\nWhat is your age? "))

likesMarmite = input("\nDo you like marmite? [Y/N] ").lower()

if likesMarmite  == "y":
    likesMarmite = True
else:
    likesMarmite = False

decades = float((age / 10))

print(f"\nWell hello {inital}, {surname}!\nIt's {likesMarmite} that you like marmite.\nThis is because you are {decades} decades old!")