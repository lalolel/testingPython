print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if len(original) > 0:
  print original
else:
  print "empty"

original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print original
else:
  print "empty"


pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]    
else:
    print 'empty'
