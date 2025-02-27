
'''
DevHub Colab Thursday, Jan 30, 2025 @ Armadale Public Library 5 to 7pm
Online Python - IDE, Editor, Compiler, Interpreter
https://www.online-python.com/
'''


'''
A simple snake game using the Turtle module where the player moves a snake with arrow keys. 
The snake moves continuously in the chosen direction. 
The objective is to control movement and avoid collisions (food and growth can be added for more features).
'''
import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Simple Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create the snake (single segment)
snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake.speed(0)

# Movement functions
def move():
	snake.forward(20)
	screen.ontimer(move, 100)  # Keep moving every 100ms

def go_up():
	if snake.heading() != 270:
		snake.setheading(90)

def go_down():
	if snake.heading() != 90:
		snake.setheading(270)

def go_left():
	if snake.heading() != 0:
		snake.setheading(180)

def go_right():
	if snake.heading() != 180:
		snake.setheading(0)

# Listen for keyboard input
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Start the movement
for i in range(10):
	move()
	time.sleep(0.1)
	go_up()
	time.sleep(0.1)
	go_right()
	time.sleep(0.1)
	go_down()
	time.sleep(0.1)
	go_left()
# Keep the window open
screen.mainloop()





'''
Output


'''