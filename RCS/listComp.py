'''List comprehension in Python is a concise and elegant way to create lists using a single line of code. It allows you to construct lists dynamically, applying transformations or filters efficiently.
Basic Syntax
The general structure of a list comprehension looks like this:
new_list = [expression for item in iterable if condition]'''


# expression → The operation performed on each item.
# item → Each element from the iterable.
# iterable → A list, range, or any iterable object.
# condition (optional) → A filtering rule that selects only certain elements.

#Examples
#1. Creating a simple list
#Instead of writing:
numbers = []
for i in range(10):
    numbers.append(i)


#You can use list comprehension:
numbers = [i for i in range(10)]
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#2. Applying transformations
#You can modify items during iteration:
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]


#3. Filtering elements
#Select only even numbers from a list:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]


#4. Nested list comprehension
#Flatten a list of lists:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


#5. Using functions inside
#Apply a function to each element:
def double(x):
    return x * 2

doubled_values = [double(x) for x in range(5)]
print(doubled_values)  # Output: [0, 2, 4, 6, 8]


