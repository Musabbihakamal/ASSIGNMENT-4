def main():
    # Prompt the user for the lengths of the three sides
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    
    # Calculate the perimeter of the triangle
    perimeter = side1 + side2 + side3
    
    # Print the perimeter
    print(f"The perimeter of the triangle is {perimeter}")

# Calling the main function to run the program
main()
