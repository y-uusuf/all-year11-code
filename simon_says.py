from random import randint

ss = [
"Hands on Head", 
"Hands on Ears", 
"Right hand Up", 
"Left hand Up", 
"Hands on Shoulders", 
"Left leg Up", 
"Left leg Shake", 
"Right leg Up", 
"Right leg Shake",
"Shake whole body."
]

def simonSays():
 index = int(input('Pick a number between 1 & 10.'))

 if index > 10 or index < 1:
    print("Number not in range.")
 else:
    print(f"Simon says: {ss[index]}")
    