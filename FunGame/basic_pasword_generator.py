
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''

import random
import string

def generate_password(length=12):
	print('''
		This code generates a password of the specified length (default 12), 
		using uppercase and lowercase letters, digits, and punctuation. 
		You can customize it further by changing the allowed characters or the password length.

		''')
	characters = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(characters) for i in range(length))
	return password

# Example usage
password = generate_password(12)  # You can adjust the length
print("Generated Password:", password)


'''
Output


'''