import math

def main():
    # Ask the user for the lengths of the two perpendicular sides
    AB = float(input("Enter the length of AB: "))
    AC = float(input("Enter the length of AC: "))
    
    # Calculate the length of the hypotenuse using the Pythagorean theorem
    BC = math.sqrt(AB**2 + AC**2)
    
    # Output the result
    print(f"The length of BC (the hypotenuse) is: {BC}")

# Calling the main function to run the program
main()
