# Scrabble Game Point Calculator
# This program processes Scrabble game data to calculate player scores

# Initial data provided for the game
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# ===============================
# BUILD YOUR POINT DICTIONARY
# ===============================

# Task 1: Create a dictionary mapping letters to their point values
# Using zip() to combine the letters and points lists into key-value pairs
# Using dict() and zip() to create the dictionary efficiently
letter_to_points = dict(zip(letters, points))

# Task 2: Add blank tile support
# Blank tiles in Scrabble are worth 0 points
letter_to_points[" "] = 0

print("Letter to Points Dictionary:")
print(letter_to_points)
print()

# ===============================
# SCORE A WORD
# ===============================

# Task 3: Define function to calculate word score
def score_word(word):
    """
    Calculate the total point value of a word in Scrabble
    
    Args:
        word (str): The word to score
    
    Returns:
        int: Total points for the word
    """
    
    # Task 4: Initialize point total to zero
    point_total = 0
    
    # Task 5: Loop through each letter in the word
    for letter in word:
        # Get the point value for each letter from our dictionary
        # Use .get() method with default value 0 for letters not in dictionary
        letter_points = letter_to_points.get(letter, 0)
        # Add the letter's points to our running total
        point_total += letter_points
    
    # Task 6: Return the total points calculated
    return point_total

# Task 7: Test the function with "BROWNIE"
brownie_points = score_word("BROWNIE")

# Task 8: Print the result to verify it equals 15 points
print(f"Points for 'BROWNIE': {brownie_points}")
print("Expected: 15 points (B=3, R=1, O=1, W=4, N=1, I=1, E=1)")
print()

# ===============================
# SCORE A GAME
# ===============================

# Task 9: Create dictionary mapping players to their words
# This represents the game data from the table provided
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

print("Player to Words:")
for player, words in player_to_words.items():
    print(f"{player}: {words}")
print()

# Task 10: Create empty dictionary to store player points
player_to_points = {}

# Task 11: Iterate through each player and their words
for player, words in player_to_words.items():
    # Initialize each player's point total to zero
    player_points = 0
    
    # Task 12: Calculate points for each word the player has played
    for word in words:
        # Use our score_word function to get points for each word
        word_points = score_word(word)
        # Add the word's points to the player's total
        player_points += word_points
        print(f"{player} played '{word}' for {word_points} points")
    
    # Task 13: Store the player's total points in our results dictionary
    player_to_points[player] = player_points
    print(f"{player} total: {player_points} points")
    print()

# Task 14: Display final standings
print("=== FINAL GAME STANDINGS ===")
# Sort players by points (highest first) for better display
sorted_players = sorted(player_to_points.items(), key=lambda x: x[1], reverse=True)

for i, (player, points) in enumerate(sorted_players, 1):
    print(f"{i}. {player}: {points} points")

print()
print("Raw player_to_points dictionary:")
print(player_to_points)

# ===============================
# EXTENDED PRACTICE FUNCTIONS
# ===============================

# Task 15: Additional functions for extended practice

def play_word(player, word, player_to_words_dict):
    """
    Add a word to a player's list of played words
    
    Args:
        player (str): Player name
        word (str): Word to add
        player_to_words_dict (dict): Dictionary to update
    """
    # Check if player already exists in dictionary
    if player in player_to_words_dict:
        # Add word to existing player's list
        player_to_words_dict[player].append(word)
    else:
        # Create new entry for player with first word
        player_to_words_dict[player] = [word]
    
    print(f"Added '{word}' to {player}'s words")

def update_point_totals(player_to_words_dict):
    """
    Calculate and return updated point totals for all players
    
    Args:
        player_to_words_dict (dict): Dictionary of players to their words
    
    Returns:
        dict: Dictionary mapping players to their total points
    """
    updated_points = {}
    
    # Loop through each player and their words
    for player, words in player_to_words_dict.items():
        total_points = 0
        
        # Calculate total points for all words
        for word in words:
            total_points += score_word(word)
        
        # Store the total
        updated_points[player] = total_points
    
    return updated_points

# Enhanced letter_to_points dictionary that handles lowercase
def create_case_insensitive_letter_points():
    """
    Create a letter-to-points dictionary that handles both uppercase and lowercase
    
    Returns:
        dict: Dictionary with both upper and lowercase letter mappings
    """
    # Start with our existing dictionary
    enhanced_dict = letter_to_points.copy()
    
    # Add lowercase versions of all letters
    for letter, points in letter_to_points.items():
        if letter != " ":  # Skip the blank space
            enhanced_dict[letter.lower()] = points
    
    return enhanced_dict

# Create the enhanced dictionary
enhanced_letter_to_points = create_case_insensitive_letter_points()

def enhanced_score_word(word):
    """
    Enhanced version of score_word that handles both uppercase and lowercase letters
    
    Args:
        word (str): Word to score (can be mixed case)
    
    Returns:
        int: Total points for the word
    """
    point_total = 0
    
    for letter in word:
        # Use the enhanced dictionary that handles both cases
        point_total += enhanced_letter_to_points.get(letter, 0)
    
    return point_total

# ===============================
# DEMONSTRATION OF EXTENDED FEATURES
# ===============================

print("\n=== EXTENDED PRACTICE DEMONSTRATION ===")

# Test the play_word function
test_dict = {"TestPlayer": ["HELLO"]}
print("Before adding word:", test_dict)
play_word("TestPlayer", "WORLD", test_dict)
print("After adding word:", test_dict)

# Test update_point_totals function
updated_totals = update_point_totals(player_to_words)
print(f"\nUpdated point totals: {updated_totals}")

# Test case-insensitive scoring
test_word_upper = "HELLO"
test_word_lower = "hello"
test_word_mixed = "HeLLo"

print(f"\nCase-insensitive scoring test:")
print(f"'{test_word_upper}' (uppercase): {enhanced_score_word(test_word_upper)} points")
print(f"'{test_word_lower}' (lowercase): {enhanced_score_word(test_word_lower)} points")
print(f"'{test_word_mixed}' (mixed case): {enhanced_score_word(test_word_mixed)} points")
