
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''


'''
A two-player game where "X" and "O" take turns placing their marks on a 3x3 grid. 
The first player to align three marks in a row, column, or diagonal wins. 
If all spaces are filled without a winner, the game is a draw.
'''

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("\n")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
turn = 0

while " " in [cell for row in board for cell in row]:
    print_board(board)
    row, col = map(int, input(f"Player {players[turn]}, enter row and column (0-2): ").split())
    
    if board[row][col] == " ":
        board[row][col] = players[turn]
        if check_winner(board, players[turn]):
            print_board(board)
            print(f"Player {players[turn]} wins!")
            break
        turn = 1 - turn
    else:
        print("Cell already occupied!")

print("Game Over!")


'''
Output
Add, Remove, View or Quit: I am working today
Invalid option.
Add, Remove, View or Quit: add
Enter task: I am going to sleep at 9pm
Add, Remove, View or Quit: add
Enter task: meeting at 7pm
Add, Remove, View or Quit: view
Your Tasks: ['I am going to sleep at 9pm', 'meeting at 7pm']

'''