
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''


def fizzbuzz(n):
    print(''' Notes: Print numbers from 1 to 20.
If a number is divisible by 3, print "Fizz".
If it's divisible by 5, print "Buzz".
If it's divisible by both, print "FizzBuzz"..''')
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} is FizzBuzz")
        elif i % 3 == 0:
            print(f"{i} is Fizz")
        elif i % 5 == 0:
            print(f"{i} is Buzz")
        else:
            print(f"{i} is not either divisible by 3 or 5")

if __name__ == "__main__":
    fizzbuzz(20)



'''
Output


'''