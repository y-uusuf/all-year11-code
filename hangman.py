from random import random as r

words = [
    "python",
    "javascript",
    "hello",
    "yusuf"
]


def choose_word():
    r(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("//Hangman//")

    while attempts > 0:
        current_display = display_word(word, guessed_letters)
        print("Word:", current_display)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess!")
            attempts -= 1

        guessed_letters.append(guess)

        if set(word) <= set(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break

        print(f"Attempts remaining: {attempts}")

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was: {word}")

hangman()
