import random

def roll_dice():
    # Simulate rolling two dice and print the results
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Print the results of the roll
    print(f"Roll: {die1}, {die2}")
    
def main():
    # Roll the dice 3 times
    for _ in range(3):
        roll_dice()

# Calling the main function to run the program
main()
