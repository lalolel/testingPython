"""
Description:
This program calculates the area of a circle or a triangle based on user input. 
The user can select 'C' for Circle or 'T' for Triangle. 
The program then asks for the necessary dimensions and calculates the area.
Author: 
"""
# Inform the user that the program is starting
print("Welcome to the Area Calculator!")

# Prompt the user to select a shape
option = input("Enter C for Circle or T for Triangle: ").upper()

# Calculate the area based on the user's choice
if option == 'C':
    # Ask for the radius of the circle
    radius = float(input("Enter radius: "))
    
    # Validate that radius is positive
    while radius <= 0:
        print("Please enter a positive number.")
        radius = float(input("Enter radius: "))
        
    # Calculate the area of the circle
    area = 3.14159 * (radius ** 2)
    
    # Print the result
    print(f"The area of the circle is: {area:.2f}")
    
elif option == 'T':
    # Ask for the base of the triangle
    base = float(input("Enter base: "))
    
    # Validate that base is positive
    while base <= 0:
        print("Please enter a positive number.")
        base = float(input("Enter base: "))
    
    # Ask for the height of the triangle
    height = float(input("Enter height: "))
    
    # Validate that height is positive
    while height <= 0:
        print("Please enter a positive number.")
        height = float(input("Enter height: "))
    
    # Calculate the area of the triangle
    area = 0.5 * base * height
    
    # Print the result
    print(f"The area of the triangle is: {area:.2f}")
    
else:
    # Handle invalid input
    print("Invalid shape selection. Please enter C for Circle or T for Triangle.")

# Inform the user that the program is exiting
print("Thank you for using the Area Calculator. Goodbye!")
