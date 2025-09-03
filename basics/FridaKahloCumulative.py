# Art Exhibition Audio Tour Master List

# Task 1: Create a list of paintings
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']
print("Task 1 - Initial paintings list:")
print(paintings)
print()

# Task 2: Create a list of dates
dates = [1939, 1933, 1946, 1940]
print("Task 2 - Dates list:")
print(dates)
print()

# Task 3: Zip paintings and dates together
paintings = list(zip(paintings, dates))
print("Task 3 - Paintings paired with dates:")
print(paintings)
print()

# Task 4: Append additional paintings with dates
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))

print("Task 4 - After adding last minute additions:")
print(paintings)
print()

# Task 5: Find the length of the paintings list
num_paintings = len(paintings)
print(f"Task 5 - Total number of paintings: {num_paintings}")
print()

# Task 6: Generate audio tour identification numbers
audio_tour_number = list(range(1, num_paintings + 1))
print("Task 6 - Audio tour identification numbers:")
print(audio_tour_number)
print()

# Task 7: Create master list by zipping audio tour numbers with paintings
master_list = list(zip(audio_tour_number, paintings))
print("Task 7 - Master list with ID numbers:")
print(master_list)
print()

# Display the master list in a more readable format
print("=== FINAL AUDIO TOUR MASTER LIST ===")
print("ID | Painting Title                | Year")
print("-" * 45)
for item in master_list:
    id_num = item[0]
    painting_title = item[1][0]
    year = item[1][1]
    print(f"{id_num:2d} | {painting_title:28s} | {year}")

print()
print("Audio tour setup complete!")
print(f"Total paintings in exhibition: {len(master_list)}")

# Additional verification
print("\n=== VERIFICATION ===")
print("All tasks completed successfully:")
print("✓ Task 1: Created paintings list")
print("✓ Task 2: Created dates list") 
print("✓ Task 3: Zipped paintings and dates")
print("✓ Task 4: Added 3 additional paintings")
print("✓ Task 5: Found total length of paintings")
print("✓ Task 6: Generated audio tour numbers")
print("✓ Task 7: Created master list with ID numbers")
