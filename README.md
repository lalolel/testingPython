# Python Basics Guide

## Table of Contents
1. [What is Python?](#what-is-python)
2. [Getting Started](#getting-started)
3. [Basic Syntax](#basic-syntax)
4. [Variables and Data Types](#variables-and-data-types)
5. [Operators](#operators)
6. [Control Structures](#control-structures)
7. [Functions](#functions)
8. [Data Structures](#data-structures)
9. [String Manipulation](#string-manipulation)
10. [File Handling](#file-handling)
11. [Error Handling](#error-handling)
12. [Object-Oriented Programming](#object-oriented-programming)
13. [Modules and Packages](#modules-and-packages)
14. [Common Built-in Functions](#common-built-in-functions)
15. [Best Practices](#best-practices)

## What is Python?

**Python** is a high-level, interpreted programming language known for its simplicity and readability. Created by Guido van Rossum in 1991, Python emphasizes code readability and allows developers to express concepts in fewer lines of code.

### Key Features:
- **Easy to learn**: Simple, readable syntax
- **Versatile**: Web development, data science, AI, automation, etc.
- **Large ecosystem**: Extensive standard library and third-party packages
- **Cross-platform**: Runs on Windows, macOS, Linux
- **Interpreted**: No compilation step needed
- **Dynamic typing**: Variables don't need explicit type declarations

### Common Use Cases:
- Web development (Django, Flask)
- Data analysis and visualization
- Machine learning and AI
- Automation and scripting
- Desktop applications
- Game development

## Getting Started

### Installation
Download Python from [python.org](https://python.org) or use package managers:

```bash
# macOS (using Homebrew)
brew install python

# Ubuntu/Debian
sudo apt install python3

# Windows (using Chocolatey)
choco install python
```

### Running Python
```bash
# Interactive interpreter
python3

# Run a script
python3 script.py

# Check version
python3 --version
```

### Python REPL (Interactive Shell)
```python
>>> print("Hello, World!")
Hello, World!
>>> 2 + 3
5
>>> exit()
```

## Basic Syntax

### Key Syntax Rules
- **Indentation matters**: Python uses indentation to define code blocks
- **No semicolons**: Line breaks end statements
- **Case sensitive**: `variable` and `Variable` are different
- **Comments**: Use `#` for single-line, `"""` or `'''` for multi-line

### Basic Structure
```python
# This is a comment
print("Hello, World!")  # This is also a comment

"""
This is a
multi-line comment
"""

# Variables
name = "Python"
version = 3.11

# Simple function
def greet(name):
    return f"Hello, {name}!"

# Function call
message = greet("World")
print(message)
```

## Variables and Data Types

### Variable Assignment
```python
# No need to declare type
name = "Alice"
age = 25
height = 5.6
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 0
```

### Basic Data Types

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integers | `42`, `-17`, `0` |
| `float` | Floating-point numbers | `3.14`, `-2.5`, `1.0` |
| `str` | Strings | `"Hello"`, `'World'` |
| `bool` | Boolean values | `True`, `False` |
| `NoneType` | Null value | `None` |

### Type Checking and Conversion
```python
# Check type
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hello"))   # <class 'str'>

# Type conversion
x = "123"
y = int(x)      # Convert string to integer
z = float(x)    # Convert string to float
w = str(456)    # Convert integer to string

# Check if variable is of certain type
isinstance(42, int)     # True
isinstance(3.14, str)   # False
```

## Operators

### Arithmetic Operators
```python
a, b = 10, 3

print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333...
print(a // b)   # Floor division: 3
print(a % b)    # Modulus: 1
print(a ** b)   # Exponentiation: 1000
```

### Comparison Operators
```python
x, y = 5, 10

print(x == y)   # Equal: False
print(x != y)   # Not equal: True
print(x < y)    # Less than: True
print(x > y)    # Greater than: False
print(x <= y)   # Less than or equal: True
print(x >= y)   # Greater than or equal: False
```

### Logical Operators
```python
a, b = True, False

print(a and b)  # Logical AND: False
print(a or b)   # Logical OR: True
print(not a)    # Logical NOT: False

# Short-circuit evaluation
print(True or print("This won't execute"))   # True
print(False and print("This won't execute")) # False
```

### Assignment Operators
```python
x = 10
x += 5   # x = x + 5, result: 15
x -= 3   # x = x - 3, result: 12
x *= 2   # x = x * 2, result: 24
x /= 4   # x = x / 4, result: 6.0
x //= 2  # x = x // 2, result: 3.0
x %= 2   # x = x % 2, result: 1.0
x **= 3  # x = x ** 3, result: 1.0
```

## Control Structures

### Conditional Statements
```python
# if-elif-else
age = 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# Ternary operator
status = "Adult" if age >= 18 else "Minor"

# Multiple conditions
if age >= 18 and age <= 65:
    print("Working age")
```

### Loops

#### For Loops
```python
# Iterate over a range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Iterate with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Iterate over dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
```

#### While Loops
```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While with else (executes if loop completes normally)
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop completed")
```

#### Loop Control
```python
# break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue - skip iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4

# pass - placeholder (do nothing)
for i in range(5):
    if i == 2:
        pass  # TODO: implement later
    print(i)
```

## Functions

### Basic Function Definition
```python
def greet(name):
    """This function greets someone"""
    return f"Hello, {name}!"

# Function call
message = greet("Alice")
print(message)
```

### Function Parameters
```python
# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!

# Keyword arguments
def create_profile(name, age, city="Unknown"):
    return f"Name: {name}, Age: {age}, City: {city}"

profile = create_profile(name="Alice", age=30, city="New York")
profile2 = create_profile("Bob", city="Boston", age=25)

# Variable arguments (*args, **kwargs)
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
```

### Lambda Functions
```python
# Lambda (anonymous) functions
square = lambda x: x ** 2
print(square(5))  # 25

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
```

### Scope and Global Variables
```python
global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    global global_var
    global_var = "Modified global"
    print(local_var)

my_function()
print(global_var)  # Modified global
```

## Data Structures

### Lists
```python
# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List operations
fruits.append("grape")           # Add to end
fruits.insert(1, "mango")       # Insert at index
fruits.remove("banana")         # Remove by value
popped = fruits.pop()           # Remove and return last item
fruits.extend(["kiwi", "peach"]) # Add multiple items

# List indexing and slicing
print(fruits[0])        # First item
print(fruits[-1])       # Last item
print(fruits[1:3])      # Slice [1:3)
print(fruits[:2])       # First 2 items
print(fruits[2:])       # From index 2 to end

# List comprehensions
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### Tuples
```python
# Creating tuples (immutable)
coordinates = (10, 20)
colors = ("red", "green", "blue")

# Tuple unpacking
x, y = coordinates
r, g, b = colors

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)
```

### Dictionaries
```python
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Dictionary operations
person["email"] = "alice@example.com"  # Add key-value pair
person.update({"phone": "123-456-7890", "age": 31})  # Update multiple
del person["city"]                     # Delete key
age = person.get("age", 0)            # Get with default value

# Dictionary methods
keys = person.keys()                   # Get all keys
values = person.values()               # Get all values
items = person.items()                 # Get key-value pairs

# Dictionary comprehensions
squares = {x: x**2 for x in range(5)}
filtered = {k: v for k, v in person.items() if len(str(v)) > 3}
```

### Sets
```python
# Creating sets (unique elements)
fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 2, 1])  # {1, 2, 3}

# Set operations
fruits.add("grape")
fruits.remove("banana")
fruits.discard("kiwi")  # Won't raise error if not found

# Set mathematics
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2           # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2    # {3, 4}
difference = set1 - set2      # {1, 2}
symmetric_diff = set1 ^ set2  # {1, 2, 5, 6}
```

## String Manipulation

### String Basics
```python
# String creation
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """Multi-line
string"""

# String concatenation
full_name = "John" + " " + "Doe"
repeated = "Ha" * 3  # "HaHaHa"

# f-strings (formatted string literals)
name = "Alice"
age = 30
message = f"My name is {name} and I'm {age} years old"
```

### String Methods
```python
text = "  Hello, World!  "

# Case methods
print(text.upper())      # "  HELLO, WORLD!  "
print(text.lower())      # "  hello, world!  "
print(text.title())      # "  Hello, World!  "
print(text.capitalize()) # "  hello, world!  "

# Whitespace methods
print(text.strip())      # "Hello, World!"
print(text.lstrip())     # "Hello, World!  "
print(text.rstrip())     # "  Hello, World!"

# Search and replace
print(text.find("World"))        # 9
print(text.replace("World", "Python"))  # "  Hello, Python!  "
print(text.startswith("  Hello")) # True
print(text.endswith("!  "))      # True

# Split and join
words = "apple,banana,orange".split(",")
joined = " | ".join(words)       # "apple | banana | orange"

# String validation
print("123".isdigit())    # True
print("abc".isalpha())    # True
print("abc123".isalnum()) # True
```

### String Formatting
```python
name = "Alice"
age = 30
score = 95.567

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")
print(f"Score: {score:.2f}")  # 2 decimal places

# .format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {name}, Age: {age}".format(name=name, age=age))

# % formatting (older style)
print("Name: %s, Age: %d" % (name, age))
```

## File Handling

### Reading Files
```python
# Method 1: Basic file reading
file = open("example.txt", "r")
content = file.read()
file.close()

# Method 2: Using with statement (recommended)
with open("example.txt", "r") as file:
    content = file.read()
    # File automatically closed after this block

# Read line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
```

### Writing Files
```python
# Write to file (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")

# Append to file
with open("output.txt", "a") as file:
    file.write("\nThis line is appended.")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### File Modes
| Mode | Description |
|------|-------------|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites file) |
| `"a"` | Append |
| `"x"` | Create (fails if file exists) |
| `"b"` | Binary mode (e.g., `"rb"`, `"wb"`) |
| `"t"` | Text mode (default) |

### Working with CSV Files
```python
import csv

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing CSV
data = [["Name", "Age", "City"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Boston"]]

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Using DictReader/DictWriter
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])
```

## Error Handling

### Try-Except Blocks
```python
# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Exception Details
```python
try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError as e:
    print(f"Error: {e}")

# Catch all exceptions
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")
```

### Finally and Else
```python
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
    print(content)
finally:
    print("This always executes")
    if 'file' in locals():
        file.close()
```

### Raising Exceptions
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot be greater than 150")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")
```

### Common Exception Types
| Exception | Description |
|-----------|-------------|
| `ValueError` | Invalid value for operation |
| `TypeError` | Wrong data type |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File doesn't exist |
| `AttributeError` | Object has no attribute |
| `ImportError` | Module cannot be imported |

## Object-Oriented Programming

### Classes and Objects
```python
class Person:
    # Class variable
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday! {self.name} is now {self.age}")

# Create objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.introduce())
person1.have_birthday()
```

### Inheritance
```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        pass
    
    def info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"
    
    def fetch(self):
        return f"{self.name} is fetching the ball!"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed
    
    def make_sound(self):
        return "Meow!"

# Using inherited classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Persian")

print(dog.info())          # Buddy is a Dog
print(dog.make_sound())    # Woof!
print(dog.fetch())         # Buddy is fetching the ball!

print(cat.info())          # Whiskers is a Cat
print(cat.make_sound())    # Meow!
```

### Special Methods (Magic Methods)
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        return (self.title == other.title and 
                self.author == other.author)

book1 = Book("1984", "George Orwell", 328)
book2 = Book("1984", "George Orwell", 328)

print(str(book1))      # 1984 by George Orwell
print(repr(book1))     # Book('1984', 'George Orwell', 328)
print(len(book1))      # 328
print(book1 == book2)  # True
```

### Property Decorators
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

circle = Circle(5)
print(circle.radius)        # 5
print(circle.area)          # 78.53975
circle.radius = 10          # Uses setter
print(circle.area)          # 314.159
```

## Modules and Packages

### Importing Modules
```python
# Import entire module
import math
print(math.pi)
print(math.sqrt(16))

# Import specific functions
from math import pi, sqrt
print(pi)
print(sqrt(16))

# Import with alias
import math as m
print(m.pi)

# Import all (not recommended)
from math import *
```

### Creating Your Own Module
```python
# File: my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159

# File: main.py
import my_module

print(my_module.greet("Alice"))
print(my_module.add(5, 3))
print(my_module.PI)
```

### Packages
```python
# Directory structure:
# mypackage/
#   __init__.py
#   math_utils.py
#   string_utils.py

# File: mypackage/__init__.py
from .math_utils import add, multiply
from .string_utils import capitalize_words

# Usage:
from mypackage import add, capitalize_words
```

### Popular Standard Library Modules
```python
# datetime - Date and time operations
from datetime import datetime, date, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)

# random - Random number generation
import random
print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'orange']))

# os - Operating system interface
import os
print(os.getcwd())  # Current directory
os.makedirs('new_folder', exist_ok=True)

# json - JSON encoder/decoder
import json
data = {'name': 'Alice', 'age': 30}
json_string = json.dumps(data)
parsed_data = json.loads(json_string)

# collections - Specialized container datatypes
from collections import Counter, defaultdict
counter = Counter(['apple', 'banana', 'apple', 'orange', 'apple'])
print(counter.most_common(2))  # [('apple', 3), ('banana', 1)]
```

## Common Built-in Functions

### Essential Built-ins
```python
# len() - Get length
print(len("Hello"))        # 5
print(len([1, 2, 3, 4]))   # 4

# range() - Generate sequence of numbers
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8, 2):   # 2, 4, 6
    print(i)

# enumerate() - Get index and value
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# zip() - Combine iterables
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### Functional Programming Functions
```python
numbers = [1, 2, 3, 4, 5]

# map() - Apply function to all items
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter() - Filter items based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# reduce() - Reduce sequence to single value
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # 15

# any() and all()
print(any([True, False, False]))   # True
print(all([True, False, False]))   # False
```

### Type and Object Functions
```python
# type() - Get object type
print(type(42))           # <class 'int'>
print(type("hello"))      # <class 'str'>

# isinstance() - Check if object is instance of class
print(isinstance(42, int))        # True
print(isinstance("hello", str))   # True

# hasattr() - Check if object has attribute
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(hasattr(person, 'name'))    # True
print(hasattr(person, 'age'))     # False

# getattr() - Get attribute value
name = getattr(person, 'name', 'Unknown')
age = getattr(person, 'age', 0)
```

## Best Practices

### 1. Follow PEP 8 Style Guide
```python
# Good: Use snake_case for variables and functions
user_name = "alice"
def calculate_total_price():
    pass

# Good: Use UPPER_CASE for constants
MAX_CONNECTIONS = 100
PI = 3.14159

# Good: Use descriptive names
def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate) ** time

# Poor: Use unclear names
def calc(p, r, t):
    return p * (1 + r) ** t
```

### 2. Use List Comprehensions Appropriately
```python
# Good: Simple transformations
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Poor: Complex logic (use regular loops instead)
# result = [complex_function(x) if condition(x) else other_function(x) 
#          for x in items if another_condition(x)]
```

### 3. Handle Exceptions Appropriately
```python
# Good: Specific exception handling
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")

# Poor: Catch-all exception handling
try:
    risky_operation()
except:
    pass  # Silent failure is dangerous
```

### 4. Use Context Managers
```python
# Good: Automatic resource cleanup
with open("file.txt", "r") as f:
    content = f.read()
# File automatically closed

# Poor: Manual resource management
f = open("file.txt", "r")
content = f.read()
f.close()  # Easy to forget
```

### 5. Write Docstrings
```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value
    
    Raises:
        ValueError: If weight or height is negative
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive")
    
    return weight / (height ** 2)
```

### 6. Use Type Hints (Python 3.5+)
```python
from typing import List, Dict, Optional

def process_names(names: List[str]) -> Dict[str, int]:
    """Process a list of names and return name lengths."""
    return {name: len(name) for name in names}

def find_user(user_id: int) -> Optional[str]:
    """Find user by ID, return name or None if not found."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)
```

### 7. Use Virtual Environments
```bash
# Create virtual environment
python -m venv myenv

# Activate (Linux/Mac)
source myenv/bin/activate

# Activate (Windows)
myenv\Scripts\activate

# Install packages
pip install requests numpy pandas

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

### 8. Organize Code Structure
```
project/
├── main.py
├── requirements.txt
├── README.md
├── tests/
│   ├── __init__.py
