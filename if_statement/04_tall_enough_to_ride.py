def check_height():
    # Set the minimum height requirement
    min_height = 50

    while True:
        # Ask the user for their height
        height = input("How tall are you? ")

        # If the user does not input anything, exit the loop
        if not height:
            break

        # Convert the input to a number
        height = int(height)

        # Check if the user is tall enough to ride
        if height >= min_height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# Call the function to check the height
check_height()
