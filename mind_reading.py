from time import sleep

print("Hello! My name is Yusuf,\n")
sleep(2)
name = input("Tell me your name?: ")
sleep(1)
print(f"\nWelcome {name}, I am going to perform a mind trick on you.\n")
num = int(input("Think of a number between 1 and 10: "))
print("\nMultiply the number in your head by 2.")
currentNum = num * 2

sleep(4)

print("\nNext, multiply your new number by 5.")
currentNum = currentNum * 5

sleep(4)

print("\nNow, divide your current num by the original number.")
currentNum = currentNum / num

sleep(4)

print("\nFinally, subtract 7 from your current number.")
currentNum = currentNum - 7

sleep(2)
print("\nHmm, let me think!")
sleep(3)

guess = input(f"\nIs your current num {currentNum}? (true or false): ").lower()
if guess == "true":
  print("\nI told you I could read your mind! ")
elif guess=="false":
  print(f"\nSuch a liar {name}!")
  sleep(2)
  print("\nTry again, perhaps use a calculator if you struggle with the calculations, dummy.")
else:
  print("Follow my intructions as told.")   