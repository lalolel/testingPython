# Medical Insurance Dictionary Project
# Creating a program to organize and update medical records efficiently

print("MEDICAL INSURANCE PROJECT - PYTHON DICTIONARIES")
print("=" * 55)
print()

# PART 1: STORING PATIENT NAMES AND INSURANCE COSTS

# Task 1: Create an empty dictionary called medical_costs
medical_costs = {}
print("Task 1: Created empty medical_costs dictionary")

# Task 2: Populate medical_costs dictionary with initial patients
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
print("Task 2: Added Marina and Vinay to medical_costs")

# Task 3: Add three more patients using one line of code
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
print("Task 3: Added Connie, Isaac, and Valentina to medical_costs")

# Task 4: Print medical_costs dictionary
print("\nTask 4: Current medical_costs dictionary:")
print(medical_costs)

# Task 5: Update Vinay's insurance cost and print updated dictionary
medical_costs["Vinay"] = 3325.0
print("\nTask 5: Updated Vinay's insurance cost:")
print(medical_costs)

# Task 6: Calculate total cost by iterating through dictionary values
total_cost = 0

# Loop through all values in medical_costs and add to total_cost
for cost in medical_costs.values():
    total_cost += cost

print(f"\nTask 6: Total cost calculated: ${total_cost}")

# Task 7: Calculate and print average cost
average_cost = total_cost / len(medical_costs)
print(f"\nTask 7: Average Insurance Cost: ${average_cost:.2f}")

print("\n" + "=" * 55)
print("PART 2: LIST COMPREHENSION TO DICTIONARY")
print("=" * 55)

# Task 8: Create lists for names and ages
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]
print("Task 8: Created names and ages lists")
print(f"Names: {names}")
print(f"Ages: {ages}")

# Task 9: Create zipped list of name-age pairs
zipped_ages = list(zip(names, ages))
print(f"\nTask 9: Created zipped_ages: {zipped_ages}")

# Task 10: Create names_to_ages dictionary using list comprehension
names_to_ages = {name: age for name, age in zipped_ages}
print(f"\nTask 10: Created names_to_ages dictionary:")
print(names_to_ages)

# Task 11: Use .get() method to retrieve Marina's age
marina_age = names_to_ages.get("Marina", None)
print(f"\nTask 11: Marina's age is {marina_age}")

print("\n" + "=" * 55)
print("PART 3: MEDICAL DATABASE USING NESTED DICTIONARIES")
print("=" * 55)

# Task 12: Create empty medical_records dictionary
medical_records = {}
print("Task 12: Created empty medical_records dictionary")

# Task 13: Add Marina's complete medical record
medical_records["Marina"] = {
    "Age": 27, 
    "Sex": "Female", 
    "BMI": 31.1, 
    "Children": 2, 
    "Smoker": "Non-smoker", 
    "Insurance_cost": 6607.0
}
print("Task 13: Added Marina's complete medical record")

# Task 14: Add remaining patients' medical records
medical_records["Vinay"] = {
    "Age": 24,
    "Sex": "Male",
    "BMI": 26.9,
    "Children": 0,
    "Smoker": "Non-smoker",
    "Insurance_cost": 3225.0
}

medical_records["Connie"] = {
    "Age": 43,
    "Sex": "Female",
    "BMI": 25.3,
    "Children": 3,
    "Smoker": "Non-smoker",
    "Insurance_cost": 8886.0
}

medical_records["Isaac"] = {
    "Age": 35,
    "Sex": "Male",
    "BMI": 20.6,
    "Children": 4,
    "Smoker": "Smoker",
    "Insurance_cost": 16444.0
}

medical_records["Valentina"] = {
    "Age": 52,
    "Sex": "Female",
    "BMI": 18.7,
    "Children": 1,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6420.0
}

print("Task 14: Added all remaining patients' medical records")

# Task 15: Print complete medical_records dictionary
print("\nTask 15: Complete medical_records database:")
for name, record in medical_records.items():
    print(f"{name}: {record}")

# Task 16: Access and print Connie's insurance cost
connie_cost = medical_records["Connie"]["Insurance_cost"]
print(f"\nTask 16: Connie's insurance cost is ${connie_cost} dollars.")

# Task 17: Remove Vinay from medical_records
del medical_records["Vinay"]
print("\nTask 17: Removed Vinay from medical_records")

# Task 18: Iterate through medical_records and print formatted information
print("\nTask 18: Patient medical record summaries:")
print("-" * 80)

for name, record in medical_records.items():
    # Extract data from nested dictionary for cleaner formatting
    age = record["Age"]
    sex = record["Sex"]
    smoker = record["Smoker"]
    bmi = record["BMI"]
    insurance_cost = record["Insurance_cost"]
    
    # Print formatted patient information
    print(f"{name} is a {age} year old {sex} {smoker} with a BMI of {bmi} and insurance cost of ${insurance_cost}")

print("\n" + "=" * 55)
print("EXTRA TASKS - ADVANCED FUNCTIONALITY")
print("=" * 55)

# Task 19 Extra: Create update_medical_records function
def update_medical_records(name, age, sex, bmi, children, smoker, insurance_cost):
    """
    Function to update or add medical records for a patient.
    
    Args:
        name (str): Patient's name
        age (int): Patient's age
        sex (str): Patient's sex
        bmi (float): Patient's BMI
        children (int): Number of children
        smoker (str): Smoking status
        insurance_cost (float): Insurance cost
    """
    medical_records[name] = {
        "Age": age,
        "Sex": sex,
        "BMI": bmi,
        "Children": children,
        "Smoker": smoker,
        "Insurance_cost": insurance_cost
    }
    print(f"Updated medical record for {name}")

# Test the update function
print("Testing update_medical_records function:")
update_medical_records("David", 29, "Male", 24.5, 1, "Non-smoker", 4200.0)
update_medical_records("Sarah", 31, "Female", 22.8, 2, "Smoker", 12500.0)

# Additional creative dictionary: Emergency contacts
emergency_contacts = {
    "Marina": {"Contact": "Carlos Marina", "Relationship": "Spouse", "Phone": "555-0123"},
    "Connie": {"Contact": "James Johnson", "Relationship": "Partner", "Phone": "555-0456"},
    "Isaac": {"Contact": "Rebecca Isaac", "Relationship": "Sister", "Phone": "555-0789"},
    "Valentina": {"Contact": "Miguel Santos", "Relationship": "Son", "Phone": "555-0321"},
    "David": {"Contact": "Lisa David", "Relationship": "Wife", "Phone": "555-0654"},
    "Sarah": {"Contact": "Tom Wilson", "Relationship": "Husband", "Phone": "555-0987"}
}

print("\nExtra Creative Dictionary - Emergency Contacts:")
print("-" * 50)
for patient, contact_info in emergency_contacts.items():
    contact = contact_info["Contact"]
    relationship = contact_info["Relationship"]
    phone = contact_info["Phone"]
    print(f"{patient}: {contact} ({relationship}) - {phone}")

# Medical analysis functions
def get_patient_statistics():
    """
    Calculate and return various statistics about the patient database.
    
    Returns:
        dict: Dictionary containing various statistics
    """
    if not medical_records:
        return "No patients in database"
    
    ages = [record["Age"] for record in medical_records.values()]
    bmis = [record["BMI"] for record in medical_records.values()]
    costs = [record["Insurance_cost"] for record in medical_records.values()]
    children_counts = [record["Children"] for record in medical_records.values()]
    
    # Count smokers
    smokers = sum(1 for record in medical_records.values() if record["Smoker"] == "Smoker")
    
    # Count by gender
    males = sum(1 for record in medical_records.values() if record["Sex"] == "Male")
    females = sum(1 for record in medical_records.values() if record["Sex"] == "Female")
    
    return {
        "Total Patients": len(medical_records),
        "Average Age": round(sum(ages) / len(ages), 1),
        "Average BMI": round(sum(bmis) / len(bmis), 1),
        "Average Insurance Cost": round(sum(costs) / len(costs), 2),
        "Total Children": sum(children_counts),
        "Smokers": smokers,
        "Non-smokers": len(medical_records) - smokers,
        "Males": males,
        "Females": females
    }

def find_high_risk_patients(bmi_threshold=30, smoker_penalty=5000):
    """
    Identify high-risk patients based on BMI and smoking status.
    
    Args:
        bmi_threshold (float): BMI threshold for high risk
        smoker_penalty (float): Additional cost penalty for smokers
    
    Returns:
        list: List of high-risk patients
    """
    high_risk = []
    
    for name, record in medical_records.items():
        risk_factors = []
        
        # Check BMI
        if record["BMI"] >= bmi_threshold:
            risk_factors.append("High BMI")
        
        # Check smoking status
        if record["Smoker"] == "Smoker":
            risk_factors.append("Smoker")
        
        # Check high insurance cost (might indicate other health issues)
        if record["Insurance_cost"] > 10000:
            risk_factors.append("High Insurance Cost")
        
        if risk_factors:
            high_risk.append({"Name": name, "Risk Factors": risk_factors})
    
    return high_risk

# Display statistics
print("\n" + "=" * 55)
print("MEDICAL DATABASE ANALYSIS")
print("=" * 55)

stats = get_patient_statistics()
print("Database Statistics:")
for key, value in stats.items():
    if "Cost" in key:
        print(f"{key}: ${value}")
    else:
        print(f"{key}: {value}")

print("\nHigh-Risk Patient Analysis:")
high_risk_patients = find_high_risk_patients()
if high_risk_patients:
    for patient in high_risk_patients:
        name = patient["Name"]
        factors = ", ".join(patient["Risk Factors"])
        print(f"{name}: {factors}")
else:
    print("No high-risk patients identified")

print("\nProject completed successfully! All tasks implemented with additional functionality.")
