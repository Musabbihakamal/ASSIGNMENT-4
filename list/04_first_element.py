def get_first_element(lst):
    # Check if the list is not empty and print the first element
    if lst:
        print(f"The first element in the list is: {lst[0]}")
    else:
        print("The list is empty. Cannot retrieve the first element.")

def get_elements_from_user():
    # This function gets input from the user and stores it in a list
    lst = []
    while True:
        # Ask the user for input
        element = input("Enter an element to add to the list (or type 'done' to finish): ")
        
        if element.lower() == 'done':
            # Stop if the user types 'done'
            break
        else:
            # Add the element to the list
            lst.append(element)
    
    return lst

def main():
    print("Welcome to the List Element Program!")
    print("You will be prompted to enter elements one by one. Type 'done' when you're finished.")
    
    # Get elements from the user
    lst = get_elements_from_user()
    
    # Print the entire list before showing the first element
    print(f"\nHere is your full list: {lst}")
    
    # Call the function to print the first element
    get_first_element(lst)
    
    # Provide an additional option to the user to perform another operation
    while True:
        user_choice = input("\nWould you like to perform another operation? (yes/no): ").strip().lower()
        
        if user_choice == 'yes':
            print("\nLet's go again! You can input a new list.")
            lst = get_elements_from_user()
            print(f"\nHere is your new list: {lst}")
            get_first_element(lst)
        elif user_choice == 'no':
            print("\nGoodbye! Thanks for using the program.")
            break
        else:
            print("Please respond with 'yes' or 'no'.")

# Run the program
if __name__ == "__main__":
    main()
