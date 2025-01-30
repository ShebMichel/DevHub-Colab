
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''

import random

def magic_8_ball():
    print(''' Notes: Create a list of random answers like "Yes", "No", "Ask again later".
Let the user ask a question and print a random answer.''')
    responses = [
        "Yes, definitely!",
        "No way!",
        "Ask again later...",
        "It is certain.",
        "Very doubtful.",
        "Better not tell you now.",
        "Absolutely!",
        "My sources say no."
    ]
    
    print("Welcome to the Magic 8-Ball! Ask me a yes or no question.")
    input("What is your question? ")
    print("\nThe Magic 8-Ball says:")
    print(random.choice(responses))

if __name__ == "__main__":
    magic_8_ball()


'''
Output


'''

## Extra questions:
# Will I become a millionaire one day?
# Should I order pizza for dinner?
# Is today going to be a lucky day for me?
# Will I travel to a new country this year?
# Should I start learning a new language?
# Is my next project going to be successful?
# Will I find something I lost soon?
# Should I watch a movie or read a book tonight?
# Am I going to meet someone special soon?
# Is my favorite sports team going to win their next game?