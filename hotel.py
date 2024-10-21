j = int(input("\nHow many juniors? "))
a = int(input("\nHow many adults? "))
b = int(input("\nHow many bags? "))
r = int(input("\bHow many days of room service? "))

t = (j * 4.5) + (a * 9) + (b * 1.25) + (r * 2)
 
print("\n\nYour total comes to:  £", int(t))
