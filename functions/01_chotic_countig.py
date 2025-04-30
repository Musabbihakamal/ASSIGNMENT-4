import random

DONE_LIKELIHOOD = 0.3  # Set the likelihood to 30%

def done():
    # This function returns True with the likelihood defined by DONE_LIKELIHOOD
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    for i in range(1, 11):
        if done():  # Check if done() returns True
            return  # Stop the function if done() returns True
        print(i)

def main():
    chaotic_counting()
    print("I'm done.")

if __name__ == '__main__':
    main()
