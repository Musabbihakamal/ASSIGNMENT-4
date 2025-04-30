def find_average(num1, num2):
    # Calculate the average of the two numbers
    average = (num1 + num2) / 2
    return average

# Example usage
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Call the function and print the result
average = find_average(number1, number2)
print(f"The average of {number1} and {number2} is {average}")
