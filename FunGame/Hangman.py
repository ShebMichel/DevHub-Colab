
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''


'''
A classic word-guessing game where the player tries to guess a hidden word letter by letter. 
Incorrect guesses reduce the number of attempts available. 
The game ends when the word is fully guessed or the player runs out of attempts.
'''

import random

words = ["python", "programming", "developer", "hangman", "learning"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = letter
    else:
        attempts -= 1
        print(f"Wrong guess! {attempts} attempts left.")

if "_" not in guessed:
    print("You win! The word was:", word)
else:
    print("You lost! The word was:", word)



'''
Output
Word: _ _ _ _ _ _
Guess a letter: hangman
Wrong guess! 5 attempts left.
Word: _ _ _ _ _ _
Guess a letter: python
Word: _ _ _ _ _ _
Guess a letter: learning
Wrong guess! 4 attempts left.
Word: _ _ _ _ _ _
Guess a letter: hangman
Wrong guess! 3 attempts left.
Word: _ _ _ _ _ _
Guess a letter: developer
Wrong guess! 2 attempts left.
Word: _ _ _ _ _ _
Guess a letter: developer
Wrong guess! 1 attempts left.
Word: _ _ _ _ _ _
Guess a letter: hangman
Wrong guess! 0 attempts left.
You lost! The word was: python

'''