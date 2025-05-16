phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == 'a':
    print 'X',
  else:
    print char,

#Don't delete this print statement!
print

numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print num

# Add your loop below!
for num in numbers:
  print num ** 2

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print key, d[key]

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
    print max(a, b)

# zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

# zip can handle three or more lists as well!

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'

  
''' Just like with while, for 
Preview: Docs A loop is a control structure that can execute a statement or group of statements repeatedly.
loops may have an else associated with them.

In this case, the else statement is executed after the for, but only if the for ends normally—that is, not with a break. This code will break when it hits 'tomato', so the else block won’t be executed. '''

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
  print 'A', f
else:
  print 'A fine selection of fruits!'
