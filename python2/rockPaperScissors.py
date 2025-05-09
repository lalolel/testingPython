import random  # Import the random module for generating random choices

# List of possible choices
options = ["ROCK", "PAPER", "SCISSORS"]

# Dictionary of outcome messages
message = {
    "tie": "Yawn, it's a tie!",
    "won": "Yay, you won!",
    "lost": "Aww, you lost!"
}

# Function to determine the winner
def decide_winner(user_choice, computer_choice):
    print "You chose: {}".format(user_choice)  # Print the user's choice
    print "Computer chose: {}".format(computer_choice)  # Print the computer's choice

    # Check for a tie
    if user_choice == computer_choice:
        print message["tie"]
    # Check for cases where the user wins
    elif (user_choice == "ROCK" and computer_choice == "SCISSORS") or \
         (user_choice == "PAPER" and computer_choice == "ROCK") or \
         (user_choice == "SCISSORS" and computer_choice == "PAPER"):
        print message["won"]
    else:
        # If none of the conditions above are met, the user lost
        print message["lost"]

# Function to play the game
def play_RPS():
    # Prompt the user for input
    user_choice = raw_input("Enter Rock, Paper, or Scissors: ").upper()
    
    # Validate user input
    if user_choice not in options:
        print "Invalid choice, please try again!"
        return
    
    # Generate a random choice for the computer
    computer_choice = random.choice(options)

    # Determine the winner using the decide_winner function
    decide_winner(user_choice, computer_choice)

# Call the function to start the game
play_RPS()
