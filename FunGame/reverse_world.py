
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''


def reverse_word():
    print('''Notes:: 
           1-Ask the user for a word.
           2-Print the word in reverse (e.g., "hello" → "olleh")''')
    word = input("Enter a word: ")
    reversed_word = word[::-1]
    print(f"Reversed word: {reversed_word}")

if __name__ == "__main__":
    reverse_word()


'''
Output


'''