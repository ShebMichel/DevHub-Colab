
# 1. Creating and Accessing Elements in a List
# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[2])  # Output: cherry


# 2. Adding and Removing Items from a List
# Start with an empty list
colors = []

# Adding items
colors.append("red")
colors.append("blue")
colors.append("green")

# Removing an item
colors.remove("blue")

print(colors)  # Output: ['red', 'green']

#3. Creating and Accessing a Dictionary
# Create a dictionary with name-age pairs
person = {"Alice": 25, "Bob": 30, "Charlie": 35}

# Accessing values using keys
print(person["Alice"])   # Output: 25
print(person["Charlie"]) # Output: 35

#4. Adding and Updating Values in a Dictionary
# Create a dictionary
phone_book = {"Alice": "123-456", "Bob": "987-654"}

# Adding a new entry
phone_book["Charlie"] = "555-555"

# Updating an existing entry
phone_book["Bob"] = "000-000"

print(phone_book)
# Output: {'Alice': '123-456', 'Bob': '000-000', 'Charlie': '555-555'}

#5. Combining Lists and Dictionaries

# A list of dictionaries
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 19}
]

# Accessing information from the list of dictionaries
for student in students:
    print(f"{student['name']} is {student['age']} years old.")

# Output:
# Alice is 20 years old.
# Bob is 22 years old.
# Charlie is 19 years old.