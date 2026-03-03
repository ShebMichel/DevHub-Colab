import turtle
import random

# --- Setup Screen ---
screen = turtle.Screen()
screen.title("Catch the Falling Stars")
screen.bgcolor("skyblue")
screen.setup(width=600, height=600)

# --- Player (Basket) ---
basket = turtle.Turtle()
basket.shape("square")
basket.shapesize(stretch_wid=1, stretch_len=5)
basket.color("brown")
basket.penup()
basket.goto(0, -250)

# --- Score ---
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-250, 260)
score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

# --- Falling Star ---
star = turtle.Turtle()
star.shape("circle")
star.color("yellow")
star.penup()
star.speed(0)
star.goto(random.randint(-280, 280), 250)

# --- Basket Movement ---
def go_left():
    x = basket.xcor()
    x -= 20
    if x < -280:
        x = -280
    basket.setx(x)

def go_right():
    x = basket.xcor()
    x += 20
    if x > 280:
        x = 280
    basket.setx(x)

screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# --- Game Loop ---
def game_loop():
    global score
    # Move star down
    y = star.ycor()
    y -= 10
    star.sety(y)

    # Check for catching the star
    if star.ycor() < -240 and abs(star.xcor() - basket.xcor()) < 50:
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))
        star.goto(random.randint(-280, 280), 250)

    # If star missed, reset it
    if star.ycor() < -280:
        star.goto(random.randint(-280, 280), 250)

    screen.ontimer(game_loop, 100)  # repeat every 100ms

# Start game
game_loop()
screen.mainloop()