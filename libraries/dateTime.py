# Import datetime from datetime below:
from datetime import datetime

current_time = datetime.now()

print(current_time)

# 1 Get today's date
today = date.today()

# Print today's date
print(f"Today's date is: {today}")
# Extract year, month, and day
year = today.year
month = today.month
day = today.day

# Print them separately
print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
# Print the formatted output
print(f"Today is {year}, {day} of {month} ")

#2  Ask the user for a date input in "DD.MM.YYYY" format
user_date = input("Enter a date (DD.MM.YYYY): ")

# Convert the input string to a datetime object
date_obj = datetime.strptime(user_date, "%d.%m.%Y")

# Define two reference dates for comparison
delta1 = datetime(2025, 1, 1)
delta2 = datetime(2025, 6, 1)

# Calculate the difference between the two dates
difference = delta2 - delta1

# Print the result
print(f"Difference between delta2 and delta1: {difference}")

# Ask the user for two dates in "DD.MM.YYYY" format
date1_str = input("Enter the first date (DD.MM.YYYY): ")
date2_str = input("Enter the second date (DD.MM.YYYY): ")

# Convert input strings to datetime objects
date1 = datetime.strptime(date1_str, "%d.%m.%Y")
date2 = datetime.strptime(date2_str, "%d.%m.%Y")

# Calculate the difference between the two dates
difference = abs(date2 - date1)  # Using abs() ensures a positive difference

# Print the result
print(f"Difference between the two dates: {difference.days} days")

from datetime import datetime, timedelta

# Ask the user for a date
date_str = input("Enter a date (DD.MM.YYYY): ")

# Convert input string to datetime object
user_date = datetime.strptime(date_str, "%d.%m.%Y")

# Add 7 days to the date
new_date = user_date + timedelta(days=7)

# Print the new date
print(f"Date after adding 7 days: {new_date.strftime('%d.%m.%Y')}")
