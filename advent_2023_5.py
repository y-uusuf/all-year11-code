def combination(x, y ,z):
 print(f"[ {x}, {y}, {z} ]")
 print(f"[ {x}, {z}, {y} ]")
 print(f"[ {y}, {x}, {z} ]")
 print(f"[ {y}, {z}, {x} ]")
 print(f"[ {z}, {y}, {x} ]")
 print(f"[ {z}, {x}, {y} ]")
    
name1 = input("Name [1]: ")
name2 = input("Name [2]: ")
name3 = input("Name [3]: ")

combination(name1, name2, name3)

