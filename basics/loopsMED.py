# Python Loops: Medical Insurance Estimates vs. Costs Project

# Initial data provided
names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

print("=== ORIGINAL DATA ===")
print("Names:", names)
print("Estimated costs:", estimated_insurance_costs)
print("Actual costs:", actual_insurance_costs)
print()

# Task 1: Create total_cost variable
total_cost = 0

# Task 2: Use for loop to add up all actual insurance costs
for cost in actual_insurance_costs:
    total_cost += cost

# Task 3: Calculate average cost
average_cost = total_cost / len(actual_insurance_costs)

# Task 4: Print average cost
print(f"Average Insurance Cost: {average_cost} dollars.")
print()

# Task 5 & 6: For loop using range to iterate through indices
print("=== INDIVIDUAL INSURANCE COSTS ===")
for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    print(f"The insurance cost for {name} is {insurance_cost} dollars.")
    
    # Task 8: Add conditions inside the loop
    if insurance_cost > average_cost:
        print(f"The insurance cost for {name} is above average.")
    elif insurance_cost < average_cost:
        print(f"The insurance cost for {name} is below average.")
    else:
        print(f"The insurance cost for {name} is equal to the average.")
    print()  # Add spacing between individuals

# Task 10: Create list comprehension to update estimated costs
updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs]

# Task 11: Print updated estimated costs
print("=== LIST COMPREHENSION RESULTS ===")
print("Original estimated costs:", estimated_insurance_costs)
print("Updated estimated costs:", updated_estimated_costs)
print("Actual insurance costs:", actual_insurance_costs)
print("Updated costs match actual costs:", updated_estimated_costs == actual_insurance_costs)
print()

# Task 12: Extra Practice
print("=== EXTRA PRACTICE ===")

# Extra 1: Convert first for loop to while loop
print("--- Converting to While Loop ---")
total_cost_while = 0
index = 0
while index < len(actual_insurance_costs):
    total_cost_while += actual_insurance_costs[index]
    index += 1

average_cost_while = total_cost_while / len(actual_insurance_costs)
print(f"Average cost calculated with while loop: {average_cost_while} dollars.")
print(f"Results match: {average_cost == average_cost_while}")
print()

# Extra 2: Modified second for loop with difference calculations
print("--- Detailed Analysis with Differences ---")
for i in range(len(names)):
    name = names[i]
    actual_cost = actual_insurance_costs[i]
    estimated_cost = estimated_insurance_costs[i]
    
    print(f"=== Analysis for {name} ===")
    print(f"Actual insurance cost: ${actual_cost}")
    print(f"Original estimated cost: ${estimated_cost}")
    
    # Calculate differences from average
    difference_from_average = actual_cost - average_cost
    
    if actual_cost > average_cost:
        print(f"The insurance cost for {name} is above average by ${difference_from_average:.2f}")
    elif actual_cost < average_cost:
        print(f"The insurance cost for {name} is below average by ${abs(difference_from_average):.2f}")
    else:
        print(f"The insurance cost for {name} is equal to the average.")
    
    # Calculate accuracy of estimate
    estimation_difference = actual_cost - estimated_cost
    estimation_accuracy = (estimated_cost / actual_cost) * 100
    
    print(f"Estimation was off by: ${estimation_difference:.2f}")
    print(f"Estimation accuracy: {estimation_accuracy:.1f}%")
    print()

# Additional comprehensive analysis
print("=== COMPREHENSIVE ANALYSIS ===")

# Summary statistics
print("--- Summary Statistics ---")
min_cost = min(actual_insurance_costs)
max_cost = max(actual_insurance_costs)
cost_range = max_cost - min_cost

print(f"Minimum insurance cost: ${min_cost}")
print(f"Maximum insurance cost: ${max_cost}")
print(f"Cost range: ${cost_range}")
print(f"Total insurance costs: ${total_cost}")
print(f"Average insurance cost: ${average_cost}")

# Count people above/below/equal to average
above_average_count = 0
below_average_count = 0
equal_average_count = 0

for cost in actual_insurance_costs:
    if cost > average_cost:
        above_average_count += 1
    elif cost < average_cost:
        below_average_count += 1
    else:
        equal_average_count += 1

print(f"\nDistribution relative to average:")
print(f"Above average: {above_average_count} people")
print(f"Below average: {below_average_count} people")
print(f"Equal to average: {equal_average_count} people")

# Estimation accuracy analysis
print(f"\n--- Estimation Accuracy Analysis ---")
total_estimation_error = 0
for i in range(len(estimated_insurance_costs)):
    error = abs(actual_insurance_costs[i] - estimated_insurance_costs[i])
    total_estimation_error += error

average_estimation_error = total_estimation_error / len(estimated_insurance_costs)
print(f"Average estimation error: ${average_estimation_error:.2f}")
print(f"All estimates were exactly 10% lower than actual costs")

# Find the person with costs closest to average
closest_to_average = None
smallest_difference = float('inf')

for i in range(len(names)):
    difference = abs(actual_insurance_costs[i] - average_cost)
    if difference < smallest_difference:
        smallest_difference = difference
        closest_to_average = names[i]

print(f"\nPerson with cost closest to average: {closest_to_average}")
print(f"Their difference from average: ${smallest_difference:.2f}")

# Using different loop types for same calculation
print(f"\n--- Loop Type Comparison ---")

# For loop with enumerate
total_enumerate = 0
for i, cost in enumerate(actual_insurance_costs):
    total_enumerate += cost
print(f"Total using enumerate: ${total_enumerate}")

# List comprehension for sum
total_comprehension = sum([cost for cost in actual_insurance_costs])
print(f"Total using list comprehension: ${total_comprehension}")

# Built-in sum function
total_builtin = sum(actual_insurance_costs)
print(f"Total using built-in sum: ${total_builtin}")

print(f"All methods give same result: {total_cost == total_enumerate == total_comprehension == total_builtin}")
