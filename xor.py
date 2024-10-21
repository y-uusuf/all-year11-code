def xor(a, b):
    if a == True and b == True:
        c = False
    elif a == False and b == False:
        c = False
    else:
        c = True
    return c


one = 4 == 4  
two = 2 != 2

print(xor(one, two))

if xor(one, two):
    print("This is true.")
else:
    print("This is false.")