import random

def guess_my_number():
    # The program picks a random number between 0 and 99
    number_to_guess = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        # Get the player's guess
        guess = int(input("Enter a guess: "))
        
        # Check if the guess is too high, too low, or correct
        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess > number_to_guess:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break  # Exit the loop if the guess is correct

# Start the game
guess_my_number()
