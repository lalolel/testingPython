''' Define a function is_even that will take a number x as input.

If x is even, then return True.

Otherwise, return False. '''

def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
  
print is_even(5)
print is_even(6)


''' Define a function is_int that takes a number x as an input.

Have it return True if the number is an integer (as defined above) and False otherwise.

For example:

is_int(7.0)   # True    
is_int(7.5)   # False    
is_int(-1)    # True      
 '''

def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(10)
print is_int(10.5)


