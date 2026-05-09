shape = input("Choose a shape (triangle, square, pyramid, diamond): ").lower()
size = int(input("Enter size: "))

if shape == "triangle":
    for i in range(1, size + 1):
        print("* " * i)

elif shape == "square":
    for i in range(size):
        print("* " * size)

elif shape == "pyramid":
    for i in range(1, size + 1):
        print(" " * (size - i) + "* " * i)

elif shape == "diamond":
    # top
    for i in range(1, size + 1):
        print(" " * (size - i) + "* " * i)
    # bottom
    for i in range(size - 1, 0, -1):
        print(" " * (size - i) + "* " * i)

else:
    print("❌ Unknown shape")