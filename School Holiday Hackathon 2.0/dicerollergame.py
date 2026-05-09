import random
import time

# 🎨 Colors (ANSI escape codes)
RED = "\033[91m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(YELLOW + "🎲 Dice Battle with Colors!" + RESET)
print("First to roll a 6 wins!\n")


def roll_animation(player_name, color):
    print(color + f"{player_name} is rolling... 🎲" + RESET)

    for _ in range(10):
        print(color + str(random.randint(1, 6)) + RESET, end="\r")
        time.sleep(0.1)

    roll = random.randint(1, 6)
    print(color + f"{player_name} rolled: {roll}     " + RESET)
    return roll


while True:
    input(BLUE + "Player 1 (BLUE) press Enter..." + RESET)
    p1 = roll_animation("Player 1", BLUE)

    if p1 == 6:
        print(GREEN + "🏆 Player 1 WINS!" + RESET)
        break

    input(RED + "Player 2 (RED) press Enter..." + RESET)
    p2 = roll_animation("Player 2", RED)

    if p2 == 6:
        print(GREEN + "🏆 Player 2 WINS!" + RESET)
        break

    print(YELLOW + "No winner yet... 🔁 Next round!\n" + RESET)