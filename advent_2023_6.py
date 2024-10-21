def calc(x, y):
    z = x / y
    return z

num1 = int(input("How much toys? "))
num2 = int(input("How much elves? "))

print(f"It will take {calc(num1, num2)} hours.")