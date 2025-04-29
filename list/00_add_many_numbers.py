def sum_of_numbers(numbers):
    # Initialize a variable to hold the sum
    total = 0
    
    # Iterate through each number in the list and add it to total
    for num in numbers:
        total += num
    
    # Return the calculated sum
    return total

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = sum_of_numbers(numbers)
print(f"The sum of the numbers is: {result}")
