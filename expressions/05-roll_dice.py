import random

def roll_dice():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Calculate the total of the two rolls
    total = die1 + die2
    
    # Print the results of each die and the total
    print(f"Roll 1: {die1}")
    print(f"Roll 2: {die2}")
    print(f"Total: {total}\n")
    
def main():
    # Simulate rolling two dice and print the results
    roll_dice()

# Calling the main function to run the program
main()
