import random
import time

NUM_ROUNDS = 5
score = 0

print("Hey there! 👋 Welcome to the High-Low Game!")
print("Let's see how good your guessing skills really are 😎")
print("-" * 40)
time.sleep(1)

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"\n🔁 Round {round_num}")
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    time.sleep(1)
    print(f"🎲 Your number is: {user_number}")
    time.sleep(0.5)
    
    guess = input("Do you think your number is *higher* or *lower* than the computer's? 🤔 ").strip().lower()
    
    while guess not in ["higher", "lower"]:
        guess = input("Hmm... Please type 'higher' or 'lower': ").strip().lower()

    print("Let me check that for you...")
    time.sleep(1.2)

    if (user_number > computer_number and guess == "higher") or \
       (user_number < computer_number and guess == "lower"):
        print(f"✅ You're right! The computer's number was {computer_number}.")
        score += 1
    elif user_number == computer_number:
        print(f"😅 Oops! It’s a tie — both numbers were {user_number}. That doesn't count as a win!")
    else:
        print(f"❌ Nope, the computer's number was {computer_number}. Better luck next round!")

    print(f"📊 Your current score: {score}")
    time.sleep(1)

print("\n🎉 Game Over!")
print("-" * 30)
print(f"🏁 You finished with a score of {score} out of {NUM_ROUNDS}!")

# End-game messages
if score == NUM_ROUNDS:
    print("🌟 Incredible! You nailed every round perfectly. Well done!")
elif score >= NUM_ROUNDS // 2:
    print("👍 Nice! You did pretty well. Keep it up!")
else:
    print("🙃 Tough luck! But hey, it's just a game — try again and beat your score!")

print("\nThanks for playing! See you next time 👋")
