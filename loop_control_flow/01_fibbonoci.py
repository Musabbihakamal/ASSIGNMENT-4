# Constant for the maximum value in the Fibonacci sequence
MAX_VALUE = 10000

def fibonacci():
    # Initial values of the Fibonacci sequence
    fib_0, fib_1 = 0, 1
    
    # Print the first term in the Fibonacci sequence
    print(fib_0, end=" ")
    
    # Continue printing Fibonacci numbers as long as they are less than MAX_VALUE
    while fib_1 < MAX_VALUE:
        print(fib_1, end=" ")
        # Update fib_0 and fib_1 for the next Fibonacci number
        fib_0, fib_1 = fib_1, fib_0 + fib_1

# Call the function to print Fibonacci sequence
fibonacci()
