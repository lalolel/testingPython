# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,100) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

# Generate a random integer
rand_int = random.randint(1, 100)
print(f"Random integer: {rand_int}")

# Select a random item from a list
colors = ["red", "blue", "green", "yellow"]
rand_color = random.choice(colors)
print(f"Random color: {rand_color}")

# Shuffle a list
random.shuffle(colors)
print(f"Shuffled colors: {colors}")

options = ["apple", "banana", "cherry", "date", "elderberry"]

# Pick 2 unique choices
unique_choices = random.sample(options, 2)
print(f"Unique choices: {unique_choices}")

# Pick 2 choices (allowing duplicates)
duplicate_choices = random.choices(options, k=2)
print(f"Choices (with possible duplicates): {duplicate_choices}")
