def check_voting_eligibility(age):
    # Peturksbouipo voting age is 16
    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")
    
    # Stanlau voting age is 25
    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")
    
    # Mayengua voting age is 48
    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

# Ask for user input
age = int(input("How old are you? "))
check_voting_eligibility(age)
