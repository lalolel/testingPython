

for item in list:
  print item

for i in range(len(list)):
  print list[i]

n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in range(0,len(numbers)):
    result += numbers[i]
  return result

n = ["Michael", "Lieberman"]
# Add your function here

def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result

print join_strings(n)


m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!

def join_lists(x, y):
	return x + y


print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append(number)
  return results

print flatten(n)
