def check_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, it's not a leap year unless divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")

# Ask for the year input
year = int(input("Enter a year: "))
check_leap_year(year)
