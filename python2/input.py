my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()


my_file = open("output.txt", "r")
print my_file.read()
my_file.close()


my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print read_file.read()

read_file.close()

''' You may not know this, but file objects contain a special pair of built-in methods: __enter__() and __exit__(). The details aren’t important, but what is important is that when a file object’s __exit__() method is invoked, it automatically closes the file. How do we invoke this method? With with and as. '''

with open("text.txt", "w") as textfile:
  textfile.write("Success!")

with open("text.txt", "w") as my_file:
  my_file.write("My Data!")
  
if not file.closed:
  file.close()

print my_file.closed

f = open("bg.txt")
f.closed
# False
f.close()
f.closed
# True
