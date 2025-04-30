def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    repeats_input = input("Enter a number of times to repeat your message: ")
    if repeats_input.isdigit():
        repeats = int(repeats_input)
        print_multiple(message, repeats)
    else:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()

