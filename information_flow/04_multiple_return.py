def get_user_data():
    # Ask the user for their first name
    first_name = input("What is your first name?: ")
    
    # Ask the user for their last name
    last_name = input("What is your last name?: ")
    
    # Ask the user for their email address
    email = input("What is your email address?: ")
    
    # Return all three pieces of data as a tuple
    return first_name, last_name, email

def main():
    # Call get_user_data() to get the user's information
    user_data = get_user_data()
    
    # Print the received data
    print(f"Received the following user data: {user_data}")

# Run the main function
if __name__ == "__main__":
    main()
