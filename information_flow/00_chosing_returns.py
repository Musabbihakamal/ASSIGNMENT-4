# Constant for adult age in the U.S.
ADULT_AGE = 18

def is_adult(age):
    # Return True if age is 18 or older, otherwise False
    return age >= ADULT_AGE

def main():
    try:
        age = int(input("How old is this person?: "))
        print(is_adult(age))
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
