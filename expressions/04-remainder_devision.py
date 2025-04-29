def main():
    # Ask the user for two numbers
    numerator = int(input("Please enter an integer to be divided: "))
    denominator = int(input("Please enter an integer to divide by: "))
    
    # Calculate the quotient and remainder
    quotient = numerator // denominator
    remainder = numerator % denominator
    
    # Print the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# Calling the main function to run the program
main()
