# TASK 3: Create the Main Script
# This is the main program for the Time Traveler's Toolkit project

# TASK 4: Import necessary modules
import datetime as dt  # Import datetime module with alias 'dt'
from decimal import Decimal  # Import Decimal for precise financial calculations
from random import randint, choice  # Import randint and choice functions from random module
import custom_module  # Import our custom module (must be in same directory)

print("=" * 50)
print("🌟 WELCOME TO THE TIME TRAVELER'S TOOLKIT 🌟")
print("=" * 50)

# TASK 5: Get Today's Date
# Use datetime module to retrieve current date and time
current_datetime = dt.datetime.now()
current_date = current_datetime.date()
current_time = current_datetime.time()

# TASK 6: Print current date and time
# Display the current date and time in a clear, readable format
print(f"\n📅 Current Date: {current_date}")
print(f"🕐 Current Time: {current_time.strftime('%H:%M:%S')}")
print(f"📍 Current Year: {current_datetime.year}")

# TASK 7: Calculate the Time Travel Cost
# Use Decimal module for precise financial calculations
base_cost = Decimal('1000.00')  # Base cost as a Decimal object
current_year = current_datetime.year

# TASK 9: Random Year Selection
# Generate a random year within a specified range (1800 to 2200)
target_year = randint(1800, 2200)
print(f"\n🎯 Randomly selected target year: {target_year}")

# Calculate cost multiplier based on year difference
year_difference = abs(current_year - target_year)
cost_multiplier = Decimal(str(year_difference * 0.5))  # $0.50 per year difference

# Calculate final cost
final_cost = base_cost + cost_multiplier

# TASK 8: Format the final cost to two decimal places
# Ensure cost is formatted to exactly two decimal places
final_cost = final_cost.quantize(Decimal('0.01'))
print(f"💰 Calculated time travel cost: ${final_cost}")

# TASK 10: Random Destination Selection
# Create a list of possible destinations and randomly select one
destinations = [
    "Ancient Rome",
    "Medieval England",
    "Renaissance Italy",
    "Wild West America",
    "Ancient Egypt",
    "Victorian London",
    "Feudal Japan",
    "Ancient Greece",
    "Roaring Twenties New York",
    "Future Mars Colony"
]

# Use choice() function to randomly select a destination
selected_destination = choice(destinations)
print(f"🗺️  Randomly selected destination: {selected_destination}")

# TASK 11: Using the Custom Module
# Use the custom function with our generated values
print(f"\n🎉 Generating your personalized time travel message...")
print("-" * 50)

# Call the function from our custom module
time_travel_message = custom_module.generate_time_travel_message(
    year=target_year,
    destination=selected_destination,
    cost=final_cost
)

# Print the generated message
print(time_travel_message)

print("🎊 Congratulations! Your Time Traveler's Toolkit is complete!")
print("=" * 50)
