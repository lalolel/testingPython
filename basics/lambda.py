# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a lambda function to filter out odd numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Use a lambda function to square each number
squares = list(map(lambda x: x ** 2, numbers))

# Print the results
print("Original numbers:", numbers)
print("Even numbers:", evens)
print("Squared numbers:", squares)

# Try creating your own lambda function!
# Uncomment and modify the line below:
# your_result = list(map(lambda x: # Your lambda function here, numbers))
# print("Your result:", your_result)
