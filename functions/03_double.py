def double(num):
    # Multiply the number by 2 and return the result
    return num * 2

def main():
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        result = double(number)
        print(f"Double that is {result}")
    except ValueError:
        print("That's not a valid number.")

# Required to run the main function
if __name__ == '__main__':
    main()
