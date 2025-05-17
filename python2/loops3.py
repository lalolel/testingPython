def digit_sum(n):
  total = 0
  string_n = str(n)
  for char in string_n:
    total += int(char)
  return total

#Alternate Solution:

#def digit_sum(n):
#  total = 0
#  while n > 0:
#    total += n % 10
#    n = n // 10
#  return total
  
print digit_sum(1234)

def factorial(x):
    total = 1
    while x>0:
        total *= x
        x-=1
    return total
  
print factorial(5)

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print is_prime(13)
print is_prime(10)

  def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
  
print reverse("Hello World")

def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
print anti_vowel("hello book")

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

print scrabble_score("pizza")

def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print censor("this hack is wack hack", "hack")

def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count
  
print count([1, 2, 1, 1], 1)


''' Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result. For example, purify([1,2,3]) should return [2].

Do not directly modify the list you are given as input; instead, return a new list with only the even numbers. '''

def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res
  
print purify([1, 2, 3, 4])

''' Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list. For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).

Don’t worry about the list being empty.
Your function should return an integer.
 '''
def product(list):
  total = 1
  for num in list:
    total = total * num
  return total

print product([4, 5, 5])

''' Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2].

Don’t remove every occurrence, since you need to keep a single occurrence of a number.
The order in which you present your output does not matter. So returning [1, 2, 3] is the same as returning [3, 1, 2].
Do not modify the list you take as input! Instead, return a new list. '''

def remove_duplicates(inputlist):
    if inputlist == []:
        return []
    
    # Sort the input list from low to high    
    inputlist = sorted(inputlist)
    # Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

    # Go through the values of the sorted list and append to the output list
    # ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
  
print remove_duplicates([1, 1, 2, 2])


''' The median is the middle number in a sorted sequence of numbers.

Finding the median of [7, 12, 3, 1, 6] would first consist of sorting the sequence into [1, 3, 6, 7, 12] and then locating the middle value, which would be 6.

If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.

For example, the median of the sequence [7, 3, 1, 4] is 3.5, since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.

You can sort the sequence using the 
Preview: Docs Loading link description
sorted()
 function, like so:

sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]


Write a function called median that takes a list as an input and returns the median value of the list. For example: median([1, 1, 2]) should return 1.

The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
If the list contains an even number of elements, your function should return the average of the middle two.
 '''
def median(lst):
    sorted_list = sorted(lst)
    if len(sorted_list) % 2 != 0:
        #odd number of elements
        index = len(sorted_list)//2 
        return sorted_list[index]
    elif len(sorted_list) % 2 == 0:
        #even no. of elements
        index_1 = len(sorted_list)/2 - 1
        index_2 = len(sorted_list)/2
        mean = (sorted_list[index_1] + sorted_list[index_2])/2.0
        return mean
   
print median([2, 4, 5, 9])
''' The median is the middle number in a sorted sequence of numbers.

In order to find the median of a list with an even number of elements, you’re going to need to find the indices of the middle two elements.

You can find the middle two elements by halving the length of the array to find the index of the first element, and subtracting one from the first index to find the second index.

For example, with an array of length 6 like [0, 1, 2, 3, 4, 5], the two middle elements that need to be averaged in order find the median would be 2 and 3. You get 3 by cutting the length of the array in half and 2 by subtracting 1 from the previous index: 3. You can use a similar pattern to find the middle element of an odd-length list.

Last but not least, note that (2 + 3) / 2 is not the same as (2 + 3) / 2.0! The former is integer division, meaning Python will try to give you an integer back. You’ll want a float, so something like (2 + 3) / 2.0 is the way to go.
 '''
