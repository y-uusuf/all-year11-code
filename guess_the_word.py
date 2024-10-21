from random import randint as ra



word = "aramsamsam"

def guess():
 counter = len(word)
 hintCounter = 0

 while counter != 0:
     guessedLetters = [""]
     hints = 0
     count = 0

     print(f"\n{counter} word(s) remaining!")

     inn = input("Guess a letter: ")

     if len(inn) > 1:
         print("You can only print 1 letter!")

     
     
     for letters in word and guessedLetters:
      if inn == letters and inn != guessedLetters:
       count = count + 1
       check=+1
      else:
       count = 0
       check=+1
    
        
     if count > 0:
             print(f'Sucess! You guessed {count} letter(s).')
             counter = counter - count
             count = 0
             guessedLetters.append(inn)
     else:
             if hints > 3:
               hint = ra(1, len(word))
               print(f"HINT: One of the letters is a {word[hint]}")
               hints = 0
               hintCounter = hintCounter + 1  
             else:
               print("You didn't get any letters.")
               hints = hints + 1    

 print(f"You won with {hintCounter} hint(s)!")

guess()
    

    