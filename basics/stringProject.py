medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
# Python Strings: Medical Insurance Project

# Task 1: Print original medical data
print("=== TASK 1: ORIGINAL MEDICAL DATA ===")
print(medical_data)
print()

# Task 2: Replace # with $
updated_medical_data = medical_data.replace('#', '$')
print("=== TASK 2: UPDATED MEDICAL DATA (# replaced with $) ===")
print(updated_medical_data)
print()

# Task 3: Initialize num_records
num_records = 0

# Task 4: Count medical records by counting $ symbols
for character in updated_medical_data:
    if character == '$':
        num_records += 1

# Task 5: Print number of records
print(f"=== TASK 5: RECORD COUNT ===")
print(f"There are {num_records} medical records in the data.")
print()

# Task 6: Split medical data into list of records
medical_data_split = updated_medical_data.split(';')
print("=== TASK 6: SPLIT MEDICAL DATA ===")
print(medical_data_split)
print()

# Task 7: Create empty list for medical records
medical_records = []

# Task 8: Split each record by comma and add to medical_records
for record in medical_data_split:
    medical_records.append(record.split(','))

print("=== TASK 8: MEDICAL RECORDS SPLIT BY COMMA ===")
print(medical_records)
print()

# Task 9: Create empty list for clean records
medical_records_clean = []

# Task 10-12: Clean up whitespace from each record
for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)

# Task 13: Print cleaned medical records
print("=== TASK 13: CLEANED MEDICAL RECORDS ===")
print(medical_records_clean)
print()

# Task 14: Print names of all individuals
print("=== TASK 14: NAMES OF INDIVIDUALS ===")
for record in medical_records_clean:
    print(record[0])
print()

# Task 15: Print names in uppercase
print("=== TASK 15: NAMES IN UPPERCASE ===")
for record in medical_records_clean:
    record[0] = record[0].upper()
    print(record[0])
print()

# Task 16: Create separate lists for each data type
names = []
ages = []
bmis = []
insurance_costs = []

# Task 17: Populate the separate lists
for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

# Task 18: Print all separate lists
print("=== TASK 18: SEPARATE LISTS ===")
print("Names:", names)
print("Ages:", ages)
print("BMIs:", bmis)
print("Insurance Costs:", insurance_costs)
print()

# Task 19: Initialize total_bmi
total_bmi = 0

# Task 20: Calculate total BMI
for bmi in bmis:
    total_bmi += float(bmi)

# Task 21: Calculate and print average BMI
average_bmi = total_bmi / len(bmis)
print(f"=== TASK 21: AVERAGE BMI ===")
print(f"Average BMI: {average_bmi}")
print()

# Task 22: Extra Practice
print("=== TASK 22: EXTRA PRACTICE ===")

# Extra 1: Calculate average insurance cost
total_insurance_cost = 0
for cost in insurance_costs:
    # Remove the $ symbol and convert to float
    clean_cost = float(cost.replace('$', ''))
    total_insurance_cost += clean_cost

average_insurance_cost = total_insurance_cost / len(insurance_costs)
print(f"Average Insurance Cost: ${average_insurance_cost:.2f}")
print()

# Extra 2: Format individual information strings
print("=== INDIVIDUAL SUMMARIES ===")
for i in range(len(names)):
    name = names[i]
    age = ages[i]
    bmi = bmis[i]
    cost = insurance_costs[i]
    print(f"{name} is {age} years old with a BMI of {bmi} and an insurance cost of {cost}.")
print()

# Additional Analysis and Summary
print("=== COMPREHENSIVE DATA ANALYSIS ===")

# Age statistics
ages_float = [float(age) for age in ages]
min_age = min(ages_float)
max_age = max(ages_float)
average_age = sum(ages_float) / len(ages_float)

print(f"--- Age Statistics ---")
print(f"Youngest person: {min_age} years old")
print(f"Oldest person: {max_age} years old")
print(f"Average age: {average_age:.1f} years")
print()

# BMI statistics
bmis_float = [float(bmi) for bmi in bmis]
min_bmi = min(bmis_float)
max_bmi = max(bmis_float)

print(f"--- BMI Statistics ---")
print(f"Lowest BMI: {min_bmi}")
print(f"Highest BMI: {max_bmi}")
print(f"Average BMI: {average_bmi:.1f}")
print()

# Insurance cost statistics
costs_float = [float(cost.replace('$', '')) for cost in insurance_costs]
min_cost = min(costs_float)
max_cost = max(costs_float)

print(f"--- Insurance Cost Statistics ---")
print(f"Lowest insurance cost: ${min_cost}")
print(f"Highest insurance cost: ${max_cost}")
print(f"Average insurance cost: ${average_insurance_cost:.2f}")
print(f"Total insurance costs: ${sum(costs_float):.2f}")
print()

# Find specific individuals
print("=== NOTABLE INDIVIDUALS ===")

# Find person with highest BMI
highest_bmi_index = bmis_float.index(max_bmi)
print(f"Highest BMI: {names[highest_bmi_index]} with BMI of {max_bmi}")

# Find person with highest insurance cost
highest_cost_index = costs_float.index(max_cost)
print(f"Highest insurance cost: {names[highest_cost_index]} with cost of ${max_cost}")

# Find youngest person
youngest_index = ages_float.index(min_age)
print(f"Youngest person: {names[youngest_index]} at {min_age} years old")

# Find oldest person
oldest_index = ages_float.index(max_age)
print(f"Oldest person: {names[oldest_index]} at {max_age} years old")
print()

print("=== DATA PROCESSING COMPLETE ===")
print("✓ All 22 tasks completed successfully!")
print("✓ Medical data has been cleaned and analyzed")
print("✓ Individual records are now properly formatted")
print("✓ Statistical analysis has been performed")
