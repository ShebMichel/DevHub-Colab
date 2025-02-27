
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''


'''
This Python program allows users to manage a simple to-do list using a command-line interface. 
Users can add tasks, remove tasks, view their current list, and exit the program. 
It utilizes lists to store tasks and loops to continuously accept user input until they choose to quit.
'''

tasks = []

while True:
    action = input("Add, Remove, View or Quit: ").lower()
    if action == "add":
        task = input("Enter task: ")
        tasks.append(task)
    elif action == "remove":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found.")
    elif action == "view":
        print("Your Tasks:", tasks)
    elif action == "quit":
        break
    else:
        print("Invalid option.")


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