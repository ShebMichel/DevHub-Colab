"""
Program to create a Bi-pyramid structure
Source : CODE PROBLEM (Youtube)
"""
import turtle
turtle.Screen().bgcolor("black")       # set the background color to black
turtle.speed(0)     # the fastest speed
turtle.pensize(2)   # set the width of the drawing pen
rainbow = ['red', 'orange', 'yellow','green', 'blue', 'indigo']
for i in range(110):
    turtle.color(rainbow[i%6])
    turtle.fd(100)
    turtle.right(28)
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(70)
    turtle.right(30)
    turtle.fd(50)

    turtle.penup()
    turtle.setposition(0,0)
    turtle.pendown()
    turtle.right(1)
    
#hide the turtle after the shape has been drawn
turtle.hideturtle() 
turtle.done()