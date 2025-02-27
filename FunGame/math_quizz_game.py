
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''


'''
A simple arithmetic quiz where players answer randomly generated math questions (addition, subtraction, multiplication). 
Each correct answer increases the score, and the final score is displayed at the end. 
Great for practicing math skills!
'''

import random

score = 0

N=int(input('Enter the max value of your range: '))

for _ in range(5):  # 5 questions
    num1, num2 = random.randint(1, N), random.randint(1, N)
    operation = random.choice(["+", "-", "*"])
    
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    user_answer = int(input(f"What is {num1} {operation} {num2}? "))
    
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {answer}.")

print(f"Your final score is {score}/5.")



'''
Output
What is 7 - 7? 0
Correct!
What is 8 * 4? 32
Correct!
What is 9 + 8? 17
Correct!
What is 2 + 5? 7
Correct!
What is 9 - 6? 3
Correct!
Your final score is 5/5.

'''