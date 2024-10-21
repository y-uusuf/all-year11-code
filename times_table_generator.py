from random import randint
from time import sleep

def multiplier(y, z):
 
 try: 
   z = int(input("Up to? [Max Value] "))
   z = z + 1
 except ValueError:
   print("You need to enter an integer.")
   exit

 answer = 0

 print(f"Here is the {y} times table (Up to 12.):\n")
 for x in range (1, z):
     answer = x * y
     print(f"{x} times {y} is equal to {answer}.\n")

times_table = int(input("What times table? "))
range = int(input("Up to? "))

multiplier(times_table, range)

"""
def quiz():
  multiplier = randint(2, 12)
  score = 0
  print(f"I will test your knowledge of the {multiplier} times table.\n")

  for x in range (1, 13):
    answer = x * multiplier

    check = int(input(f"What is {x} * {multiplier}? "))

    if check == answer:
      print("Correct!\n")
      score = score + 1
      sleep(2)
    else:
      print("Wrong answer! It was " + answer + ".")
  
  print(f"You got {score}/12.")


  choice = int(input("1 for Quiz, 2 for multiplier: "))

  if choice == 1:
    quiz()
  elif choice == 2:
    multiplier()
  else:
    exit
    """