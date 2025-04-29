def double_elements(numbers):
    # Iterate through the list and double each element in place
    for i in range(len(numbers)):
        numbers[i] *= 2  # Double the element at the current index

# Example usage:
numbers = [1, 2, 3, 4]
double_elements(numbers)
print(f"After doubling, the list is: {numbers}")
