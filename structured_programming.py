def cost(x, y):
    days = x * 7
    total = days * y

    return total

days = int(input("How many days was the dog walked? "))
time = int(input("How many times was the dog walked? "))

print(f"Your total cost is £{cost(days, time)}.")