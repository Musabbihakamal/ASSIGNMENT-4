def main():
    # Initialize an empty list
    user_list = []
    
    while True:
        # Prompt the user to enter a value
        value = input("Enter a value: ")
        
        # Check if the user pressed enter without typing anything
        if value == "":
            # Exit the loop and print the list
            print(f"Here's the list: {user_list}")
            break
        else:
            # Add the entered value to the list
            user_list.append(value)

# Run the program
if __name__ == "__main__":
    main()

