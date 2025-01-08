questions = {
    "What is the capital of France?": "paris",
    "What is 2 + 2?": "4",
    "What is the color of the sky?": "blue"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ").lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"Your final score is {score}/{len(questions)}")

