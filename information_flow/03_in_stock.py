# Helper function to simulate Sophia's inventory
def num_in_stock(fruit):
    # Example inventory of fruits and their quantities
    inventory = {
        'apple': 150,
        'banana': 200,
        'pear': 1000,
        'orange': 500,
        'kiwi': 0,  # Example fruit with 0 stock
    }
    
    # Return the number in stock for the given fruit
    return inventory.get(fruit.lower(), 0)

def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ").lower()
    
    # Get the number of that fruit in stock
    stock = num_in_stock(fruit)
    
    # Check if the fruit is in stock
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

# Run the main function
if __name__ == "__main__":
    main()
