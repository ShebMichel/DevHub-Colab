
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''


'''
A fun matching game where players flip two cards at a time, trying to find matching pairs. 
Cards are hidden and shuffled at the start, and correct matches remain visible. 
The game continues until all pairs are found.
'''
import random

cards = ["🐱", "🐶", "🦊", "🐻", "🐼", "🐰", "🐨", "🦁"] * 2
random.shuffle(cards)
board = ["?"] * 16

def print_board():
    print(" ".join(board))

while "?" in board:
    print_board()
    first = int(input("Pick first card (0-15): "))
    second = int(input("Pick second card (0-15): "))

    if cards[first] == cards[second]:
        board[first] = cards[first]
        board[second] = cards[second]
        print("Matched!")
    else:
        print("Try again!")

print("You matched all pairs! 🎉")





'''
Output


'''