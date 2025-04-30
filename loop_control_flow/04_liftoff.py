# Countdown from 10 to 1, and print "Liftoff!" at the end.

# Start the countdown at 10
print("The countdown to liftoff is starting...")

# Loop through the countdown numbers from 10 down to 1
for i in range(10, 0, -1):
    if i == 1:
        # When it's the last number, print it without a trailing space
        print(i)
    else:
        # Print the current number followed by a space
        print(i, end=" ")

# After the countdown, print "Liftoff!" to indicate the launch
print("Liftoff!")

# Additional message for excitement!
print("The spaceship has successfully launched into space!")
