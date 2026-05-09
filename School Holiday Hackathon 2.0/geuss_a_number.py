import random

secret = random.randint(1, 10)

print("🎮 You vs Computer Guessing Game!")
print("First to guess the correct number wins!\n")

while True:
    # 👤 Player turn
    try:
        player_guess = int(input("👤 Your guess (1-10): "))

        if player_guess == secret:
            print("🎉 You win!")
            break
        elif player_guess < secret:
            print("⬇️ Too small")
        else:
            print("⬆️ Too big")

    except ValueError:
        print("❌ Please enter a number!")
        continue

    # 🤖 Computer turn
    computer_guess = random.randint(1, 10)
    print(f"🤖 Computer guesses: {computer_guess}")

    if computer_guess == secret:
        print("💀 Computer wins!")
        break
    elif computer_guess < secret:
        print("🤖 Computer: too small")
    else:
        print("🤖 Computer: too big")

    print("🔁 Next round...\n")
            