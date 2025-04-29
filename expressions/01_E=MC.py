def main():
    # Constant for the speed of light in meters per second
    c = 299792458  # speed of light in m/s
    
    while True:
        # Ask the user for mass in kilograms
        mass = float(input("Enter kilos of mass: "))
        
        # Calculate the energy using Einstein's equation E = m * c^2
        energy = mass * c**2
        
        # Print the results
        print(f"\ne = m * C^2...\n")
        print(f"m = {mass} kg")
        print(f"C = {c} m/s")
        print(f"{energy} joules of energy!\n")

# Calling the main function to run the program
main()
