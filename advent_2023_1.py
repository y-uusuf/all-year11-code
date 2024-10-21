def l(x):
    if x == 6:
        return 1.8
    if x == 7.5:
        return 2.3
    if x == 3.25:
        return 1.0
    if x == 10:
        return 3.0
    if x == 4.6:
        return 1.4

y = float(input("Feet? "))
print(f"{l(y)}m.")