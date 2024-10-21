def triple(a):
    a = a * 3
    return a

num1 = int(input("Number? "))
print("\n" + triple(num1))




def increase_score(b):
    if b == "yes":
        score = score + 1

score = 0
prompt = int(input("Increase? "))
increase_score(prompt)

def change_colour(a, b):
    colour = input(f"Your current colour is: {colour}\n\nWhat would you like to change it to?")

colour = "Red"
change_colour()

def change_direction(a):
    direction = a
    print(f"Direction set to; {direction}")
    return direction

def change_speed(a):
    print(f"Old speed: {speed}")
    speed = a
    print(f"New speed: {a}")
    return speed

speed = 10
direction = "North"

ddirection = input(f"Your current direction is to {direction}; where to now? ")
change_direction(ddirection)
sspeed = input(f"Your current speed is to {speed}; How fast? ")
change_speed(sspeed)

