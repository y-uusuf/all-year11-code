
#variables: slice of pizza, how many people, how many slices each and remaining slices
#mod=%  interger division=//

print("Welcome to the Split My Pizza app!\n")

people = int(input("\nHow many people will there be? "))
if people == 1:
  print("\nDo you really need to use this app for 1 person?")

else:
  slices = int(input("\nHow many slices of pizza are there? "))

  slices_per_person = slices // people
  remaining_slices = slices % people

  print(f"\nEverybody should have {slices_per_person} slices of pizza.")
  if remaining_slices > 1:
    print(f"\nWhoever is hungry there are {remaining_slices} slices left.")
  elif remaining_slices == 1:
    print("\nThere is one last pizza slice.")
  else:
    print("\nUnfortunately all the slices are finished, those who are hungry will remain hungry.")

choice = input("\nWould you like to split the bill? ").lower()

if choice == "yes":
  price=float(input("\nCost? "))

  amount_of_people = int(input("\nHow many people are splitting the bill? "))

  cost = price / amount_of_people

  print(f"People paying must pay £{cost}! \nThank you for paying and have a great day.")

elif choice == "no":
  print("Thank you for paying, have a great day.")
 
else:
  exit