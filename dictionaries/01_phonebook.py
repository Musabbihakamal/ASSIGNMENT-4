def main():
    phonebook = {}  # Dictionary to store contact names and their corresponding phone numbers
    
    while True:
        print("\nPhonebook Menu:")
        print("1. Add a contact")
        print("2. Look up a contact")
        print("3. Display all contacts")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            name = input("Enter the name of the contact: ")
            phone_number = input("Enter the phone number: ")
            phonebook[name] = phone_number  # Add the contact to the phonebook
            print(f"Contact {name} added.")
        
        elif choice == '2':
            name = input("Enter the name of the contact to look up: ")
            if name in phonebook:
                print(f"{name}'s phone number is {phonebook[name]}")
            else:
                print(f"{name} not found in the phonebook.")
        
        elif choice == '3':
            if phonebook:
                print("\nAll Contacts:")
                for name, phone_number in phonebook.items():
                    print(f"{name}: {phone_number}")
            else:
                print("Phonebook is empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
