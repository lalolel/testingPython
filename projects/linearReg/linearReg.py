# Linear Regression from Scratch Project
# Finding the line of best fit using trial and error method
# Understanding how linear regression works under the hood

print("LINEAR REGRESSION FROM SCRATCH")
print("=" * 50)
print("Finding the best line: y = m*x + b")
print("=" * 50)
print()

# PART 1: CALCULATING ERROR

# Task 1: Create get_y() function to calculate y-value on a line
def get_y(m, b, x):
    """
    Calculate the y-value for a given x on a line with slope m and y-intercept b.
    
    Args:
        m (float): Slope of the line
        b (float): Y-intercept of the line  
        x (float): X-coordinate for which to calculate y
    
    Returns:
        float: Y-coordinate on the line for the given x
    """
    # Linear equation: y = mx + b
    return m * x + b

# Test get_y() function
print("Task 1: Testing get_y() function")
print(f"get_y(1, 0, 7) = {get_y(1, 0, 7)} (expected: 7)")
print(f"get_y(5, 10, 3) = {get_y(5, 10, 3)} (expected: 25)")
print()

# Task 2 & 3: Create calculate_error() function
def calculate_error(m, b, point):
    """
    Calculate the error (distance) between a point and a line.
    
    Args:
        m (float): Slope of the line
        b (float): Y-intercept of the line
        point (tuple): A point as (x, y) coordinates
    
    Returns:
        float: Absolute distance between the point and the line
    """
    # Extract x and y coordinates from the point
    x_point = point[0]
    y_point = point[1]
    
    # Calculate what the y-value would be on the line for this x
    y_on_line = get_y(m, b, x_point)
    
    # Find the difference between actual y and predicted y
    error = y_point - y_on_line
    
    # Return absolute value of the error (distance)
    return abs(error)

# Task 4: Test calculate_error() function
print("Task 4: Testing calculate_error() function")
print(f"calculate_error(1, 0, (3, 3)) = {calculate_error(1, 0, (3, 3))} (expected: 0)")
print(f"calculate_error(1, 0, (3, 4)) = {calculate_error(1, 0, (3, 4))} (expected: 1)")
print(f"calculate_error(1, -1, (3, 3)) = {calculate_error(1, -1, (3, 3))} (expected: 1)")
print(f"calculate_error(-1, 1, (3, 3)) = {calculate_error(-1, 1, (3, 3))} (expected: 5)")
print()

# Task 5: Create calculate_all_error() function for multiple points
def calculate_all_error(m, b, points):
    """
    Calculate the total error between a line and a set of data points.
    
    Args:
        m (float): Slope of the line
        b (float): Y-intercept of the line
        points (list): List of (x, y) coordinate tuples
    
    Returns:
        float: Sum of all individual errors between points and the line
    """
    total_error = 0
    
    # Iterate through each point and accumulate the error
    for point in points:
        # Add the error for this point to the running total
        total_error += calculate_error(m, b, point)
    
    return total_error

# Sample dataset: bouncy ball width vs bounce height
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
print("Sample Dataset (bouncy balls):")
print("Width (cm) -> Bounce Height (m)")
for width, height in datapoints:
    print(f"{width}cm -> {height}m")
print()

# Task 6: Test calculate_all_error() function
print("Task 6: Testing calculate_all_error() function")
print(f"calculate_all_error(1, 0, datapoints) = {calculate_all_error(1, 0, datapoints)} (expected: 4)")
print(f"calculate_all_error(-1, 1, datapoints) = {calculate_all_error(-1, 1, datapoints)} (expected: 18)")
print(f"calculate_all_error(1, 1, datapoints) = {calculate_all_error(1, 1, datapoints)} (expected: 5)")
print()

# PART 2: TRY A BUNCH OF SLOPES AND INTERCEPTS

print("PART 2: FINDING THE BEST LINE")
print("=" * 40)

# Task 8: Create possible m values (slopes) to test
# Using list comprehension to create values from -10 to 10 in steps of 0.1
possible_ms = [m/10 for m in range(-100, 101)]  # -10.0 to 10.0 in 0.1 steps
print(f"Task 8: Created {len(possible_ms)} possible slope values from -10 to 10")

# Task 9: Create possible b values (y-intercepts) to test
# Using list comprehension to create values from -20 to 20 in steps of 0.1
possible_bs = [b/10 for b in range(-200, 201)]  # -20.0 to 20.0 in 0.1 steps
print(f"Task 9: Created {len(possible_bs)} possible y-intercept values from -20 to 20")

# Task 10: Initialize variables for optimization
smallest_error = float("inf")  # Start with infinity so any error will be smaller
best_m = 0  # Best slope found so far
best_b = 0  # Best y-intercept found so far
print(f"Task 10: Initialized optimization variables")
print(f"Starting values - smallest_error: {smallest_error}, best_m: {best_m}, best_b: {best_b}")
print()

# Task 11 & 12: Find the best line using nested loops
print("Searching for the best line... (this may take a moment)")
print("Testing", len(possible_ms) * len(possible_bs), "different lines")

# Nested loops to try every combination of m and b values
for m in possible_ms:
    for b in possible_bs:
        # Calculate total error for this line with our data
        current_error = calculate_all_error(m, b, datapoints)
        
        # If this line has less error than our current best, update our best values
        if current_error < smallest_error:
            smallest_error = current_error
            best_m = m
            best_b = b

# Task 12: Print the results
print(f"\nTask 12: Optimization complete!")
print(f"Best slope (m): {best_m}")
print(f"Best y-intercept (b): {best_b}")
print(f"Smallest error: {smallest_error}")
print(f"Best line equation: y = {best_m}x + {best_b}")
print()

# PART 3: WHAT DOES OUR MODEL PREDICT?

print("PART 3: MAKING PREDICTIONS")
print("=" * 30)

# Task 13: Use our model to predict bounce height for a 6cm ball
prediction_x = 6
predicted_y = get_y(best_m, best_b, prediction_x)

print(f"Task 13: Prediction for 6cm ball")
print(f"Using our best line: y = {best_m}x + {best_b}")
print(f"For x = {prediction_x}: y = {best_m} * {prediction_x} + {best_b} = {predicted_y}")
print(f"Prediction: A {prediction_x}cm ball will bounce {predicted_y}m high")
print()

# Additional analysis and visualization of results
print("ADDITIONAL ANALYSIS")
print("=" * 25)

# Show how well our line fits each data point
print("How well does our line fit the data?")
print("Point\t\tActual\tPredicted\tError")
print("-" * 45)
total_error_check = 0
for x, y_actual in datapoints:
    y_predicted = get_y(best_m, best_b, x)
    error = abs(y_actual - y_predicted)
    total_error_check += error
    print(f"({x}, {y_actual})\t\t{y_actual}\t{y_predicted:.1f}\t\t{error:.1f}")

print(f"\nTotal error: {total_error_check:.1f} (matches smallest_error: {smallest_error})")

# Make predictions for different ball sizes
print("\nPredictions for different ball sizes:")
print("Width (cm)\tPredicted Bounce (m)")
print("-" * 35)
test_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for size in test_sizes:
    bounce = get_y(best_m, best_b, size)
    print(f"{size}\t\t{bounce:.1f}")

# Function to make predictions for new data
def predict_bounce_height(width):
    """
    Predict bounce height for a ball of given width using our model.
    
    Args:
        width (float): Width of the ball in cm
    
    Returns:
        float: Predicted bounce height in meters
    """
    return get_y(best_m, best_b, width)

# Test the prediction function
print(f"\nUsing predict_bounce_height() function:")
print(f"3.5cm ball: {predict_bounce_height(3.5):.1f}m")
print(f"7.2cm ball: {predict_bounce_height(7.2):.1f}m")

# Summary of what we learned
print("\n" + "=" * 50)
print("PROJECT SUMMARY")
print("=" * 50)
print("✓ Created functions to calculate y-values on a line")
print("✓ Implemented error calculation between points and lines")  
print("✓ Built a function to calculate total error for datasets")
print("✓ Used brute force optimization to find the best line")
print("✓ Made predictions using our linear model")
print(f"\nFinal Model: y = {best_m}x + {best_b}")
print(f"This line has a total error of {smallest_error} on our training data")
print("\nReggie can now predict bouncy ball behavior for his ball pit!")
