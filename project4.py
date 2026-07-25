score = 0

print("=== GENERAL KNOWLEDGE QUIZ ===")

answer = input("1. What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

answer = input("\n2. Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

answer = input("\n3. How many days are there in a week? ")
if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

print("\n=== QUIZ COMPLETED ===")
print("Your Final Score:", score, "/3")

if score == 3:
    print("Excellent! 🎉")
elif score == 2:
    print("Good Job! 👍")
elif score == 1:
    print("Keep Practicing! 😊")
else:
    print("Better luck next time! 💪")