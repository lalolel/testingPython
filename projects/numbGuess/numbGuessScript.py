# This program rolls two dice, asks the user to guess the sum, and determines the winner.
"""
Codecademy - Learn Python
Number Guess
"""
# This program simulates rolling two dice, asks the user to guess the sum, and determines if they win.

# Import necessary modules
from random import randint  # For generating random numbers
from time import sleep  # For adding delays to simulate rolling

# Function to get the user's guess
def get_user_guess():
    # Prompt the user to enter their guess and convert it to an integer
    guess = int(input("Guess a number: "))
    return guess  # Return the guess for further use

# Function to simulate rolling two dice
def roll_dice(number_of_sides):
    # Generate random values for each die roll
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)

    # Calculate the maximum possible value from rolling two dice
    max_val = number_of_sides * 2
    print(f"The maximum possible value is {max_val}")

    # Get the user's guess
    guess = get_user_guess()

    # Ensure the user's guess is valid
    if guess > max_val:
        print("Invalid guess. Try again with a lower number.")
    else:
        print("Rolling...")  # Inform the user that the dice are being rolled
        sleep(2)  # Pause for realism
        print(f"First roll: {first_roll}")  # Display the first roll
        sleep(1)  # Pause for suspense
        print(f"Second roll: {second_roll}")  # Display the second roll
        sleep(1)  # Pause again for suspense

        # Calculate the total sum of the dice roll
        total_roll = first_roll + second_roll
        print(f"Total roll: {total_roll}")  # Show the total value
        print("Result...")  # Announce the result is coming
        sleep(1)  # Pause before showing outcome

        # Determine if the user won or lost
        if guess == total_roll:
            print("You won!")  # User guessed correctly
        else:
            print("You lost!")  # User guessed incorrectly

# Start the game with dice that have 6 sides
roll_dice(6)
