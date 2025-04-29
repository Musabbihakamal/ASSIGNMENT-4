def main():
    # Prompt the user for an adjective, noun, and verb
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Define the sentence structure
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

    # Combine the words into the sentence and print the result
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

# Calling the main function to run the program
main()
