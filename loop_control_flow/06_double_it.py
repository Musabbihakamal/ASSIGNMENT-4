# Ask the user to input a number
user_input = int(input("Enter a number: "))

# Initialize curr_value with the user's input
curr_value = user_input

# Use a while loop to repeatedly double the value until it reaches 100 or more
while curr_value < 100:
    # Double the current value
    curr_value = curr_value * 2
    # Print the doubled value after each iteration
    print(curr_value, end=" ")

print()  # To ensure the output ends with a newline.
