import turtle
import random

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.title("2-Player Emoji Racing Game")
screen.bgcolor("gray")
screen.setup(width=600, height=600)
screen.tracer(0)

# ---------------- ROAD LINES ----------------
lines = []
for i in range(-250, 300, 100):
    line = turtle.Turtle()
    line.hideturtle()
    line.penup()
    line.goto(0, i)
    line.write("|", align="center", font=("Arial", 30, "bold"))
    lines.append(line)

# ---------------- PLAYERS ----------------
vehicles = ["🚗", "🚙", "🏎️", "🚕", "🚌"]

# Player 1
car1 = turtle.Turtle()
car1.hideturtle()
car1.penup()
car1_vehicle = random.choice(vehicles)
car1_x, car1_y = -100, -230

# Player 2
car2 = turtle.Turtle()
car2.hideturtle()
car2.penup()
car2_vehicle = random.choice(vehicles)
car2_x, car2_y = 100, -230

def draw_cars():
    car1.clear()
    car1.goto(car1_x, car1_y)
    car1.write(car1_vehicle, align="center", font=("Arial", 30, "normal"))
    
    car2.clear()
    car2.goto(car2_x, car2_y)
    car2.write(car2_vehicle, align="center", font=("Arial", 30, "normal"))

# ---------------- OBSTACLE ----------------
obstacle = turtle.Turtle()
obstacle.hideturtle()
obstacle.penup()
obstacle_emoji = "🚧"
obstacle_x = random.randint(-200, 200)
obstacle_y = 300

def draw_obstacle():
    obstacle.clear()
    obstacle.goto(obstacle_x, obstacle_y)
    obstacle.write(obstacle_emoji, align="center", font=("Arial", 30, "normal"))

# ---------------- MOVEMENT ----------------
def car1_left():
    global car1_x
    if car1_x > -250:
        car1_x -= 30
        draw_cars()

def car1_right():
    global car1_x
    if car1_x < 0:
        car1_x += 30
        draw_cars()

def car2_left():
    global car2_x
    if car2_x < 250:
        car2_x -= 30
        draw_cars()

def car2_right():
    global car2_x
    if car2_x > 0:
        car2_x += 30
        draw_cars()

screen.listen()
# Player 1: Left/Right arrows
screen.onkey(car1_left, "Left")
screen.onkey(car1_right, "Right")
# Player 2: A/D keys
screen.onkey(car2_left, "a")
screen.onkey(car2_right, "d")

# ---------------- GAME LOOP ----------------
game_running = True

def game_loop():
    global obstacle_y, obstacle_x, game_running
    
    if not game_running:
        return

    # Move road lines (scrolling effect)
    for line in lines:
        y = line.ycor() - 10
        if y < -300:
            y = 300
        line.goto(0, y)

    # Move obstacle down
    obstacle_y -= 15
    if obstacle_y < -300:
        obstacle_y = 300
        obstacle_x = random.randint(-200, 200)
    draw_obstacle()

    # Collision detection for car1
    if abs(obstacle_y - car1_y) < 30 and abs(obstacle_x - car1_x) < 30:
        game_running = False
        car1.clear()
        car2.clear()
        obstacle.clear()
        car1.goto(-50, 0)
        car2.goto(50, 0)
        car1.write("💥 Car 1 CRASHED 💥", align="center", font=("Arial", 24, "bold"))
        car2.write("🎉 Car 2 WINS 🎉", align="center", font=("Arial", 24, "bold"))
        return

    # Collision detection for car2
    if abs(obstacle_y - car2_y) < 30 and abs(obstacle_x - car2_x) < 30:
        game_running = False
        car1.clear()
        car2.clear()
        obstacle.clear()
        car1.goto(-50, 0)
        car2.goto(50, 0)
        car1.write("🎉 Car 1 WINS 🎉", align="center", font=("Arial", 24, "bold"))
        car2.write("💥 Car 2 CRASHED 💥", align="center", font=("Arial", 24, "bold"))
        return

    screen.update()
    screen.ontimer(game_loop, 50)

# ---------------- START GAME ----------------
draw_cars()
draw_obstacle()
game_loop()
screen.mainloop()