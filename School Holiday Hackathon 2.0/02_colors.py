# 02_colors.py
# Draw a colored square and change the background!

import turtle

screen = turtle.Screen()
screen.bgcolor("black")       # Change the background color!

t = turtle.Turtle()
t.speed(1)                    # drawing speed: 1 = slow, 10 = fast, 0 = instant
t.width(7)                    # pen thickness in pixels
t.color("cyan")               # Outline color
t.fillcolor("magenta")        # Fill color

# Move to the top-left corner without drawing a line
t.penup()        # lift the pen so moving won't leave a line
t.goto(-150, 150)  # move to (x=-150, y=150) — top-left of the square
t.pendown()      # put the pen down so drawing starts here

t.begin_fill()
for i in range(4):
    t.forward(300)
    t.right(90)
t.end_fill()

# Try it yourself:
# Change bgcolor, color, and fillcolor to your favorites!

turtle.done()
