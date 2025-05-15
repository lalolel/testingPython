# Create a list
my_list = [10, 20, 30, 40, 50, 60, 70, 80]

# Access the first two elements
first_two = my_list[:2]

# Access the last two elements
last_two = my_list[-2:]

# Create a new variable storing the previous list with a step of 2
stepped_list = my_list[::2]

# Create a list with strings
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the first and last element using index
print("First element:", words[0])
print("Last element:", words[-1])

# Replace the second element with a different word
words[1] = "blueberry"

# Print the whole new list
print("Updated list:", words)

# Create a list with strings
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the first and last element in one statement
print("First and last elements:", words[0], words[-1])

# Define a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using list comprehension
first_last = [[sublist[0], sublist[-1]] for sublist in nested_list]
print("First and last elements:", first_last)

# Using a loop
for sublist in nested_list:
    print("First:", sublist[0], "Last:", sublist[-1])
