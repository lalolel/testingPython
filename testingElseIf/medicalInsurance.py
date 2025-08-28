# Python Control Flow: Medical Insurance Project

# Task 3 & 4: Create analyze_smoker() function
def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")

# Task 1: Function to estimate insurance cost
def estimate_insurance_cost(age, sex, num_of_children, smoker):
    estimated_cost = 400 * age - 128 * sex + 425 * num_of_children + 10000 * smoker - 2500
    print(f"The estimated insurance cost for this person is {estimated_cost} dollars.")
    
    # Task 5: Call analyze_smoker() function
    analyze_smoker(smoker)
    
    return estimated_cost

# Task 1: Test with Keanu's information
print("=== Keanu's Insurance Analysis ===")
keanu_insurance_cost = estimate_insurance_cost(age=29, sex=1, num_of_children=3, smoker=1)

print()  # Add some spacing

# Task 6: Analyze your own insurance cost
print("=== My Insurance Analysis ===")
# Replace these values with your own information
my_age = 25
my_sex = 0  # 0 for female, 1 for male
my_num_of_children = 0
my_smoker_status = 0  # 0 for non-smoker, 1 for smoker

my_insurance_cost = estimate_insurance_cost(age=my_age, sex=my_sex, num_of_children=my_num_of_children, smoker=my_smoker_status)

print()  # Add some spacing

# Task 7: Additional functionality (Extra Practice)
print("=== Additional Analysis ===")

def analyze_age(age):
    if age < 30:
        print("You are in a lower age bracket. Your insurance costs may increase as you get older.")
    elif age < 50:
        print("You are in a moderate age bracket. Consider planning for potential cost increases.")
    else:
        print("You are in a higher age bracket, which contributes to higher insurance costs.")

def analyze_children(num_of_children):
    if num_of_children == 0:
        print("You have no children, which helps keep your insurance costs lower.")
    elif num_of_children <= 2:
        print("You have a small family. Each child adds to insurance costs.")
    else:
        print("You have a larger family. Consider family insurance plans for potential savings.")

def analyze_bmi_advice():
    print("Tip: Maintaining a healthy BMI through diet and exercise can help lower insurance costs.")

def comprehensive_analysis(age, sex, num_of_children, smoker):
    print("=== Comprehensive Insurance Cost Analysis ===")
    
    # Calculate and display cost
    cost = estimate_insurance_cost(age, sex, num_of_children, smoker)
    
    print("\n--- Additional Insights ---")
    
    # Analyze each factor
    analyze_age(age)
    analyze_children(num_of_children)
    analyze_bmi_advice()
    
    # Overall advice
    print("\n--- Cost Reduction Strategies ---")
    total_advice_count = 0
    
    if smoker == 1:
        total_advice_count += 1
        print(f"{total_advice_count}. Quit smoking (potential savings: $10,000)")
    
    if age > 40:
        total_advice_count += 1
        print(f"{total_advice_count}. Consider health screenings to catch issues early")
    
    if num_of_children > 2:
        total_advice_count += 1
        print(f"{total_advice_count}. Look into family insurance plans for better rates")
    
    total_advice_count += 1
    print(f"{total_advice_count}. Maintain a healthy lifestyle with regular exercise")
    total_advice_count += 1
    print(f"{total_advice_count}. Shop around and compare insurance plans annually")
    
    if total_advice_count == 2:  # Only the default advice was given
        print("You're already doing well! Keep up the healthy lifestyle.")
    
    return cost

# Example of comprehensive analysis
print("\n" + "="*50)
print("COMPREHENSIVE ANALYSIS EXAMPLE")
print("="*50)
comprehensive_analysis(age=35, sex=0, num_of_children=2, smoker=1)
