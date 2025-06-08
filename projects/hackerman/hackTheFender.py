# Hacking The Fender - File Manipulation Project
# Mission: Retrieve compromised passwords, notify boss, and scramble the data
# This project demonstrates working with CSV files, text files, and JSON in Python

# ===============================
# READING IN THE PASSWORDS
# ===============================

# Task 1: Import the CSV module for parsing CSV data
import csv

# Task 2: Create a list to store users whose passwords have been compromised
compromised_users = []

# Create sample passwords.csv file for demonstration
# In a real scenario, this file would already exist
sample_passwords_data = """Username,Password
jean49,ilovemyfamily1_2
burgess-stephanie,stephi3
danielleclark,n0t1n4hu11
jonesday,iygtr23
kerrymccoy,sammy123
benhoward,n0ahmmad4
webbc-alex,ipa_princess1994
simpson-jamie,vip3r_omg
"""

# Write sample data to passwords.csv for demonstration
with open("passwords.csv", "w") as f:
    f.write(sample_passwords_data)

# Task 3: Open up the passwords.csv file
# Using 'with' statement ensures proper file handling and automatic closure
with open("passwords.csv") as password_file:
    
    # Task 4: Parse the CSV file using csv.DictReader
    # DictReader treats the first row as headers and creates dictionaries for each row
    password_csv = csv.DictReader(password_file)
    
    # Task 5: Iterate through each row in the CSV file
    for password_row in password_csv:
        
        # Task 6: Print each username (for testing purposes)
        # This shows us what usernames are being processed
        print(f"Processing user: {password_row['Username']}")
        
        # Task 7: Add each username to the compromised_users list
        # Using append() method to add usernames instead of printing
        compromised_users.append(password_row['Username'])

# Task 8: Remove the print statement (already done above)
# Task 9: Exit the with block (automatically handled)

print(f"\nTotal compromised users found: {len(compromised_users)}")
print("Compromised users:", compromised_users)

# Task 10: Create a new file to store the compromised usernames
# Opening compromised_users.txt in write mode
with open("compromised_users.txt", "w") as compromised_user_file:
    
    # Task 11: Start a new for loop to iterate over compromised users
    for user in compromised_users:
        
        # Task 12: Write each username to the file
        # Adding newline character to separate usernames on different lines
        compromised_user_file.write(user + "\n")

print("Compromised users have been written to compromised_users.txt")

# Task 13: Exit the with block (automatically handled)

# ===============================
# NOTIFYING THE BOSS
# ===============================

# Task 14: Import the JSON module for encoding messages
import json

# Task 15: Open a new JSON file in write mode for the boss message
with open("boss_message.json", "w") as boss_message:
    
    # Task 16: Create a Python dictionary with the boss message
    # This dictionary contains the recipient and success message
    boss_message_dict = {
        "recipient": "The Boss",
        "message": "Mission Success"
    }
    
    # Task 17: Write the dictionary to the JSON file
    # json.dump() converts the Python dictionary to JSON format and writes it
    json.dump(boss_message_dict, boss_message)

print("Boss message has been sent (saved to boss_message.json)")

# ===============================
# SCRAMBLING THE PASSWORD
# ===============================

# Task 18: Create a new file to replace the old passwords file
# Opening new_passwords.csv in write mode
with open("new_passwords.csv", "w") as new_passwords_obj:
    
    # Task 19: Add Slash Null's signature to frame him for the hack
    # This is a multi-line ASCII art signature that will be written to the file
    slash_null_sig = """ _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/"""
    
    # Task 20: Write the signature to the new passwords file
    # This replaces the original password data with Slash Null's signature
    new_passwords_obj.write(slash_null_sig)

print("New passwords file created with Slash Null's signature")

# ===============================
# MISSION SUMMARY AND VERIFICATION
# ===============================

print("\n" + "="*50)
print("MISSION COMPLETE - SUMMARY")
print("="*50)

# Verify compromised_users.txt was created
try:
    with open("compromised_users.txt", "r") as f:
        user_count = len(f.readlines())
    print(f"✓ Compromised users file created: {user_count} users saved")
except FileNotFoundError:
    print("✗ Error: compromised_users.txt not found")

# Verify boss_message.json was created
try:
    with open("boss_message.json", "r") as f:
        boss_data = json.load(f)
    print(f"✓ Boss message sent: {boss_data['message']} to {boss_data['recipient']}")
except FileNotFoundError:
    print("✗ Error: boss_message.json not found")

# Verify new_passwords.csv was created with signature
try:
    with open("new_passwords.csv", "r") as f:
        content = f.read()
    if "SLASH" in content:
        print("✓ New passwords file created with Slash Null's signature")
    else:
        print("✗ Error: Slash Null's signature not found in new file")
except FileNotFoundError:
    print("✗ Error: new_passwords.csv not found")

print("\nMission Status: SUCCESS")
print("The Fender's password file has been compromised and replaced!")
print("All evidence points to Slash Null as the perpetrator.")

# ===============================
# ADDITIONAL DEMONSTRATION
# ===============================

print("\n" + "="*50)
print("FILE CONTENTS VERIFICATION")
print("="*50)

# Show contents of compromised_users.txt
print("\n--- compromised_users.txt ---")
try:
    with open("compromised_users.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

# Show contents of boss_message.json
print("\n--- boss_message.json ---")
try:
    with open("boss_message.json", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

# Show first few lines of new_passwords.csv
print("\n--- new_passwords.csv (first 10 lines) ---")
try:
    with open("new_passwords.csv", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines[:10]):
            print(line.rstrip())
        if len(lines) > 10:
            print(f"... and {len(lines) - 10} more lines")
except FileNotFoundError:
    print("File not found")
