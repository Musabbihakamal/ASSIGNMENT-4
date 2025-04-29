def add_three_copies(my_list, data):
    for _ in range(3):  # Loop 3 times
        my_list.append(data)  # Add the message each time

# Example usage:
message = input("Enter a message to copy: ")

# Start with an empty list
my_list = []

# Print the list before adding copies
print("List before:", my_list)

# Call the function to add three copies of the message
add_three_copies(my_list, message)

# Print the list after adding copies
print("List after:", my_list)
