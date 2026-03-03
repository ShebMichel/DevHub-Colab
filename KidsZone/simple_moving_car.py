import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Drive the Car!")
screen.bgcolor("gray")
screen.setup(width=600, height=600)

# Draw road lines
road = turtle.Turtle()
road.hideturtle()
road.penup()
road.goto(-200, -300)
road.pendown()
road.pensize(5)
road.color("white")
road.goto(-200, 300)

road.penup()
road.goto(200, -300)
road.pendown()
road.goto(200, 300)

# Car
car = turtle.Turtle()
car.shape("square")
car.color("blue")
car.shapesize(stretch_wid=1, stretch_len=2)
car.penup()
car.goto(0, -250)

# Move left
def move_left():
    x = car.xcor()
    if x > -180:   # left road limit
        car.setx(x - 20)

# Move right
def move_right():
    x = car.xcor()
    if x < 180:    # right road limit
        car.setx(x + 20)

# Keyboard controls
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.mainloop()