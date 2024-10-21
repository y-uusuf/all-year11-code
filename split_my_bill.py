print("#~~~ Welcome to [SPLIT MY BILL] ~~~#\n")

b = float(input("Total bill?     "))
p = int(input("How many people are sharing?      "))
t = int(input("How much % tip are you willing to leave?     "))

d = t / 100
tt = b * d
b = b + tt 
b = b / p




print(f"\nYour total is:          {b}")