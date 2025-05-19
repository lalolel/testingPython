print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

8's bit  4's bit  2's bit  1's bit
    1       0       1      0 
    8   +   0    +  2   +  0  = 10 

2 ** 0 = 1
2 ** 1 = 2
2 ** 2 = 4
2 ** 3 = 8
2 ** 4 = 16
2 ** 5 = 32
2 ** 6 = 64
2 ** 7 = 128
2 ** 8 = 256
2 ** 9 = 512
2 ** 10 = 1024

one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six  = 0b110
seven = 0b111
eight = 0b1000
nine  = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)

''' In the console are several different ways that you can use the int function’s second parameter.On line 7, use int to print the base 10 equivalent of the binary number 11001001. '''

print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)

'''  Shift the variable shift_right to the right twice (>> 2) and shift the variable shift_left to the left twice (<< 2). Try to guess what the printed output will be! '''

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)

'''The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of both numbers are 1. 
print out the result of calling bin() on 0b1110 & 0b101.

See if you can guess what the output will be! 0b100 '''

print bin(0b1110 & 0b101)

''' The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1. 
For practice, print out the result of using | on 0b1110 and 0b101 as a binary string. 
Try to do it on your own without using the | operator if you can help it.
 '''

print bin(0b1110 | 0b101)

''' The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both. '''

print bin(0b1110 ^ 0b101)

''' The bitwise NOT operator (~) just flips all of the bits in a single number. '''

print ~1
print ~2
print ~3
print ~42
print ~123


''' A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.

1.
Define a function, check_bit4, with one argument, input, an integer.

It should check to see if the fourth bit from the right is on.

If the bit is on, return "on" (not print!)

If the bit is off, return "off". '''

check_bit4(0b1) # ==> "off"
check_bit4(0b11011) # ==> "on"
check_bit4(0b1010) # ==> "on"

def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"

      ''' You can also use masks to turn a bit in a number on using |. For example, let’s say I want to make sure the rightmost bit of number a is turned on. 
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7
Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.


In the editor is a variable, a. Use a bitmask and the value a in order to achieve a result where the third bit from the right of a is turned on. Be sure to print your answer as a bin() string! '''
a = 0b10111011

mask = 0b100
desired = a | mask
print bin(desired)
