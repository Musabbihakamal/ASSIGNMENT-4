def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')
    print()  # For a clean newline after the output

def main():
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        number = int(user_input)
        print_divisors(number)
    else:
        print("Please enter a valid positive integer.")

if __name__ == '__main__':
    main()
