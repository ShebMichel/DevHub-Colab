
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''
#Examples include words like enormous, doglike, silly, yellow, fun, and fast. 
#Adjectives have three forms: absolute (describing one thing, like messy),
#comparative (comparing two things, like messier), 
# and superlative (indicating the highest degree, like messiest)

#A noun is a word that represents a person, thing, concept, or place (e.g., “John,” “house,” “affinity,” “river”).

def mad_libs():
    print("Welcome to the Mad Libs Game! Fill in the blanks to create a fun story.\n")
    print(''' Examples include words like enormous, doglike, silly, yellow, fun, and fast. 
              Adjectives have three forms: absolute (describing one thing, like messy),
              comparative (comparing two things, like messier), 
              and superlative (indicating the highest degree, like messiest)

              #A noun is a word that represents a person, thing, concept, 
              or place (e.g., “John,” “house,” “affinity,” “river”).   ''' )
    
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")
    
    story = f"One day, a {adjective} {noun} decided to {verb} all the way to {place}. It was an unforgettable adventure!"
    
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()

'''
Output

Welcome to the Mad Libs Game! Fill in the blanks to create a fun story.

Enter a noun: Michel
Enter a verb: play
Enter an adjective: fun
Enter a place: mossman park

Here's your Mad Libs story:
One day, a fun Michel decided to play all the way to mossman park. It was an unforgettable adventure!
'''