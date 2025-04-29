def main():
    number_count = {}  # Dictionary to store number count
    
    while True:
        number = input("Enter a number: ")
        if not number:  # If the user presses Enter without typing anything, stop the loop
            break
        
        number = int(number)  # Convert the input to an integer
        
        if number in number_count:
            number_count[number] += 1  # Increment count if the number is already in the dictionary
        else:
            number_count[number] = 1  # Add the number to the dictionary with a count of 1
    
    for number, count in number_count.items():  # Iterate through the dictionary and print results
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()
