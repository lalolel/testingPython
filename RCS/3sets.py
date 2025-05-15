'''
In Python, a set is an unordered collection of unique elements. Unlike lists or tuples, sets do not allow duplicate values and are useful for mathematical operations like union, intersection, and difference

Key Features:
- Unordered: Elements do not have a fixed position.
- Unique: No duplicate values.
- Mutable: You can add or remove elements.
- Efficient Membership Testing: Checking if an item exists is fast

'''
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Creating an empty set (use set(), not {})
empty_set = set()


# Adding elements
my_set.add(6)

# Removing elements
my_set.remove(3)  # Raises error if element is missing
my_set.discard(4)  # No error if element is missing

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b  # {1, 2, 3, 4, 5}
intersection_set = set_a & set_b  # {3}
difference_set = set_a - set_b  # {1, 2}
