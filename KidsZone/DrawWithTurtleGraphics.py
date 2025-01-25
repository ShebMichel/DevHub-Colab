import turtle
import time

screen = turtle.Screen()
t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)
    time.sleep(4)

turtle.done()
