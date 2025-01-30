
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''

def pig_latin_translator():
    print(''' Notes::
        1-Take a word from the user.
        2-Move the first letter to the end and add "ay" (e.g., "hello" → "ellohay")
          
        ''')
    word = input("Enter a word: ").strip().lower()
    
    if word[0] in "aeiou":
        pig_latin_word = word + "way"
    else:
        pig_latin_word = word[1:] + word[0] + "ay"
    
    print(f"Pig Latin translation: {pig_latin_word}")

if __name__ == "__main__":
    pig_latin_translator()



'''
Output
Apple → appleway
Banana → ananabay
Orange → orangeway
Guitar → uitargay
Elephant → elephantway
Strawberry → trawberrysay
Python → ythonpay
Umbrella → umbrellaway
Chocolate → hocolatecay
Laptop → aptoplay


'''