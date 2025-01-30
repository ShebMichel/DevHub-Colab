
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''

def emoji_translator():
    print(''' Notes::
        1-Ask the user for a feeling (e.g., "happy", "sad").
        2-Print a matching emoji (🙂, 😢) using a dictionary.

        ''')
    #print("😊".encode('utf-8').decode('utf-8'))
    emoji_dict = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😠",
        "love": "❤️",
        "surprised": "😲",
        "cool": "😎",
        "laugh": "😂",
        "cry": "😭"
    }
    
    emotion = input("Enter an emotion (happy, sad, angry, love, surprised, cool, laugh, cry): ").lower()
    
    if emotion in emoji_dict:
        print(f"Emoji for {emotion}: {emoji_dict[emotion]}")
    else:
        print("Sorry, I don't have an emoji for that emotion.")

if __name__ == "__main__":
    emoji_translator()



'''
Output


'''