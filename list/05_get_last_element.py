def get_last_element(lst):
    # Print the last element of the list
    print(f"The last element in the list is: {lst[-1]}")

# Example usage:
# Asking the user to input elements for the list
lst = []

# Loop to get input from the user and add it to the list
n = int(input("How many elements do you want to enter? "))
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    lst.append(element)

# Call the function to print the last element
get_last_element(lst)
