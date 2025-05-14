

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
