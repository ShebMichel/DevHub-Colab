"""
Program to create a Bi-pyramid structure
Source : CODE PROBLEM (Youtube)
"""

import turtle

scr = turtle.Screen()   # create screen object
scr.bgcolor('black')

turtle.speed(0)      # the fastest speed
turtle.pensize(2)   # set the width of the drawing pen

turtle.color('skyblue')     # set pencolor to 'skyblue'

for i in range(30):
    turtle.fd(i*10)
    turtle.right(120)

for j in range(29,0,-1):
     turtle.fd(j*10)    # move forward
     turtle.left(120)   

turtle.hideturtle()     # hiding the turtle after the completion of the drawing
turtle.done()   # for holding the screen