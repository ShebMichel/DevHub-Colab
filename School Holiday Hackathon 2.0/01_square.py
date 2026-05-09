# 01_square.py
# Draw a square using turtle!

import turtle

t = turtle.Turtle()   # create a turtle to draw with
t.speed(1)            # drawing speed: 1 = slow, 10 = fast, 0 = instant
t.width(5)            # pen thickness in pixels

# Move to the top-left corner without drawing a line
t.penup()        # lift the pen so moving won't leave a line
t.goto(-150, 150)  # move to (x=-150, y=150) — top-left of the square
t.pendown()      # put the pen down so drawing starts here

# Draw a square: repeat 4 times because a square has 4 equal sides,
# turning right 90 degrees at each corner.
for i in range(4):
    t.forward(300)
    t.right(90)

turtle.done()
