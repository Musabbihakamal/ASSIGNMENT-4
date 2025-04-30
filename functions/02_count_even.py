def count_even():
    lst = []

    # Prompt user for integers until they press enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("That's not a valid integer. Try again.")

    # Count even numbers
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1

    print(f"There are {even_count} even numbers in the list.")

# Call the function
count_even()
