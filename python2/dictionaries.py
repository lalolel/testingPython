my_dict = {
  'name': 'Nick',
  'age':  31,
  'occupation': 'Dentist',
}

print my_dict.keys()
print my_dict.values()

for key in my_dict:
  print key, my_dict[key]

for number in range(5):
  print number,

d = { 
  "name": "Eric",
  "age": 26
}

for key in d:
  print key, d[key],

for letter in "Eric":
  print letter,  # note the comma!

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print even_squares

cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

my_list = range(1, 11) # List of numbers 1 - 10

# Omitting Indices Add your code below!
print my_list[::2]

my_list = range(1, 11)

# Reversing a List Add your code below!
backwards = my_list[::-1]

''' A positive stride length traverses the list from left to right, and a negative one traverses the list from right to left.

Further, a stride length of 1 traverses the list “by ones,” a stride length of 2 traverses the list “by twos,” and so on. '''

to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens
''' Create a list, to_21, that’s just the numbers from 1 to 21, inclusive.

Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on). Use list slicing for this one instead of a list comprehension.

Finally, create a third list, middle_third, that’s equal to the middle third of to_21, from 8 to 14, inclusive. '''

to_21 = range(1, 22)

odds = to_21[::2]

middle_third = to_21[7:14]


''' One of the more powerful aspects of Python is that it allows for a style of programming called functional programming, which means that you’re allowed to pass 
Preview: Docs Loading link description
functions
 around just as if they were 
Preview: Docs A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character . The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed. A variable can have a short name (like x and y) or a more descriptive name (age, grade, grocerylist). Rules for Python variables: - A variable name must start with a letter or the underscore character. It cannot start with a number. - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _). - Variable names are case-sensitive (num, Num, and NUM are three different variables).
variables
 or values. Sometimes we take this for granted, but not all languages allow this!

Check out the code at the right. See the 
Preview: Docs Produces an anonymous function expression.
lambda
 bit? Typing

lambda x: x % 3 == 0


Is the same as

def by_three(x):
  return x % 3 == 0 '''


my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

''' Lambda functions are defined using the following syntax:

my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)


Lambdas are useful when you need a quick function to do some work for you.

If you plan on creating a function you’ll use over and over, you’re better off using def and giving that function a name. '''

languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x: x == "Python", languages)
