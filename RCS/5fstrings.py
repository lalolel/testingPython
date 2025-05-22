# f strings
# v1
name = "Lalo"  # Replace with any name
age = 25  # Replace with any age

print(f"Hi, my name is {name} and I'm {age} years old.")

age += 1  # Increment age by 1
print(f"Next year, I'll be {age} years old.")


# v2
name = "Lalo"
age = 25

print(f"Hi, my name is {name} and I'm {age} years old.")
print(f"Next year, I'll be {age + 1} years old.")


'''You can perform a variety of calculations inside f-strings, including:
- Arithmetic: Addition, subtraction, multiplication, division, etc.''''

print(f"5 + 3 = {5 + 3}")
# Exponentiation: Using ** for powers.
print(f"2 squared is {2 ** 2}")
# Modulo (remainder): Using % to get the remainder.
print(f"10 divided by 3 gives a remainder of {10 % 3}")
# String manipulation: You can repeat strings.
print(f"Echo: {'Hello' * 3}")
# Rounding numbers: Using round() for better formatting.
pi = 3.14159
print(f"Pi rounded to 2 decimal places is {round(pi, 2)}")
# Length of a string: Using len().
name = "Lalo"
print(f"My name has {len(name)} letters.")


Essentially, anything that can be computed inside {} is fair game! What kind of calculations are you looking to try out?
