# 03_spiral.py
# Draw a spiral galaxy using turtle!

import turtle

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)          # Fastest speed
t.width(2)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "white"]

for i in range(200):
    t.color(colors[i % len(colors)])
    t.forward(i * 1.5)
    t.right(59)

turtle.done()
