


def calc(a, b, c):
     if c == "+":
        d = a + b
     if c == "-":
        d = a - b
     if c == "/":
        d = a / b
     if c == "*":
         d = a * b

     print(f"{a} + {b} = {d}")


while 1 == 1:
 print("Enter a number: ")
 num1 = int(input())

 print("Enter another number: ")
 num2 = int(input())

 print("Would you like to +, -, / or *? ")
 operation = input()

 calc(num1, num2, operation)
