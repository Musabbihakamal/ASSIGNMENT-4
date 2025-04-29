def main():
    # Ask the user to input a length in feet
    feet = float(input("Enter a length in feet: "))
    
    # Convert feet to inches (12 inches per foot)
    inches = feet * 12
    
    # Output the result
    print(f"{feet} feet is equal to {inches} inches.")

# Calling the main function to run the program
main()
