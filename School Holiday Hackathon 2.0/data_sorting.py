print("🎮 Welcome to Python Data Explorer!")
print("Learn Lists, Dictionaries, and Sets through play!\n")

# -------------------
# 📦 LIST
# -------------------
print("📦 LIST CHALLENGE")
fruits_list = []

for i in range(5):
    fruit = input(f"Add fruit {i+1}: ")
    fruits_list.append(fruit)

print("\nYour LIST:", fruits_list)
print("👉 Lists keep order AND allow duplicates!\n")


# -------------------
# 🔥 SET
# -------------------
print("🔥 SET CHALLENGE (no duplicates allowed)")
fruits_set = set()

for i in range(5):
    fruit = input(f"Add fruit {i+1}: ")
    fruits_set.add(fruit)

print("\nYour SET:", fruits_set)
print("👉 Sets remove duplicates automatically!\n")


# -------------------
# 🧠 DICTIONARY
# -------------------
print("🧠 DICTIONARY CHALLENGE (fruit → color)")
fruit_dict = {}

for i in range(3):
    fruit = input("Fruit name: ")
    color = input("Color: ")
    fruit_dict[fruit] = color

print("\nYour DICTIONARY:", fruit_dict)
print("👉 Dictionaries store key → value pairs!\n")


# -------------------
# 🎯 MINI QUIZ
# -------------------
print("🎯 QUIZ TIME!")

answer = input("Which structure removes duplicates? ")

if answer.lower() == "set":
    print("🎉 Correct! You're a data ninja 🥷")
else:
    print("❌ Nope! The answer is SET 🔥")

print("\n🏁 Game Over — Data Explorer Complete!")