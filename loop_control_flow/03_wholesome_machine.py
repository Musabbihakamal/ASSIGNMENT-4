# The affirmation we want the user to type
affirmation = "I am capable of doing anything I put my mind to."

# Keep asking the user to type the affirmation until they get it correct
while True:
    user_input = input("Please type the following affirmation: ")
    
    if user_input == affirmation:
        print("That's right! :)")
        break  # Exit the loop once the affirmation is typed correctly
    else:
        print("Hmmm That was not the affirmation.")

