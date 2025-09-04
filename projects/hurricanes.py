# Hurricane Analysis Project
# Analyzing Category 5 Hurricanes in the Atlantic Region

# Sample data for testing (based on typical hurricane data structure)
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael', 'Laura', 'Eta']

months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October', 'August', 'November']

years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018, 2020, 2020]

max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 185, 175, 160, 150, 140]

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['United States Gulf Coast', 'Mexico'], ['The Caribbean', 'Eastern United States'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Jamaica', 'The Caribbean', 'Mexico', 'United States Gulf Coast'], ['Bahamas', 'United States Gulf Coast'], ['United States Gulf Coast', 'Mexico'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America', 'Mexico'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic'], ['Central America', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'United States Gulf Coast'], ['Central America']]

damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B', '19.1B', '6.2B']

deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 11374, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74, 149, 138]

# Task 1: Function to convert damage data from strings to float values
def update_damages(damages_list):
    """
    Convert damage data from string format to float values.
    
    Args:
        damages_list (list): List of damage strings with 'M' (millions) or 'B' (billions) suffixes
    
    Returns:
        list: Updated list with float values for recorded damages and original strings for unrecorded
    """
    updated_damages = []
    
    for damage in damages_list:
        # Check if damage was not recorded
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        else:
            # Remove the last character (M or B) and convert to float
            if damage[-1] == 'M':
                # Convert millions to actual number
                updated_damages.append(float(damage[:-1]) * 1000000)
            elif damage[-1] == 'B':
                # Convert billions to actual number  
                updated_damages.append(float(damage[:-1]) * 1000000000)
    
    return updated_damages

# Test Task 1
updated_damages = update_damages(damages)
print("Task 1 - Updated damages (first 5):", updated_damages[:5])
print()

# Task 2: Function to create hurricane dictionary with names as keys
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    """
    Create a dictionary of hurricanes with names as keys and hurricane data as values.
    
    Args:
        names, months, years, max_sustained_winds, areas_affected, damages, deaths: Lists of hurricane data
    
    Returns:
        dict: Dictionary with hurricane names as keys and dictionaries of hurricane data as values
    """
    hurricanes = {}
    
    # Iterate through all hurricanes using index
    for i in range(len(names)):
        # Create a dictionary for each hurricane with all relevant data
        hurricanes[names[i]] = {
            'Name': names[i],
            'Month': months[i], 
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damage': damages[i],
            'Deaths': deaths[i]
        }
    
    return hurricanes

# Test Task 2
hurricanes_by_name = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print("Task 2 - Hurricane dictionary for 'Cuba I':")
print(hurricanes_by_name['Cuba I'])
print()

# Task 3: Function to organize hurricanes by year
def hurricanes_by_year(hurricanes_dict):
    """
    Organize hurricanes by year.
    
    Args:
        hurricanes_dict (dict): Dictionary of hurricanes with names as keys
    
    Returns:
        dict: Dictionary with years as keys and lists of hurricane dictionaries as values
    """
    hurricanes_year = {}
    
    # Iterate through each hurricane in the dictionary
    for hurricane in hurricanes_dict.values():
        year = hurricane['Year']
        
        # If year doesn't exist in dictionary, create new list
        if year not in hurricanes_year:
            hurricanes_year[year] = []
        
        # Add hurricane to the appropriate year list
        hurricanes_year[year].append(hurricane)
    
    return hurricanes_year

# Test Task 3
hurricanes_by_year_dict = hurricanes_by_year(hurricanes_by_name)
print("Task 3 - Hurricanes in 1932:")
print(f"Number of hurricanes in 1932: {len(hurricanes_by_year_dict[1932])}")
print()

# Task 4: Function to count areas affected by hurricanes
def count_affected_areas(hurricanes_dict):
    """
    Count how many times each area was affected by hurricanes.
    
    Args:
        hurricanes_dict (dict): Dictionary of hurricanes
    
    Returns:
        dict: Dictionary with areas as keys and count of times affected as values
    """
    affected_areas_count = {}
    
    # Iterate through each hurricane
    for hurricane in hurricanes_dict.values():
        # Check each area affected by the hurricane
        for area in hurricane['Areas Affected']:
            # Count occurrences of each area
            if area in affected_areas_count:
                affected_areas_count[area] += 1
            else:
                affected_areas_count[area] = 1
    
    return affected_areas_count

# Test Task 4
affected_areas = count_affected_areas(hurricanes_by_name)
print("Task 4 - Areas affected count (first 5):")
for i, (area, count) in enumerate(affected_areas.items()):
    if i < 5:
        print(f"{area}: {count}")
print()

# Task 5: Function to find the area most affected by hurricanes
def most_affected_area(affected_areas_dict):
    """
    Find the area most frequently affected by hurricanes.
    
    Args:
        affected_areas_dict (dict): Dictionary of areas and their hurricane counts
    
    Returns:
        tuple: (area_name, count) of the most affected area
    """
    max_area = ""
    max_count = 0
    
    # Find the area with maximum hurricane count
    for area, count in affected_areas_dict.items():
        if count > max_count:
            max_count = count
            max_area = area
    
    return max_area, max_count

# Test Task 5
most_affected = most_affected_area(affected_areas)
print(f"Task 5 - Most affected area: {most_affected[0]} with {most_affected[1]} hurricanes")
print()

# Task 6: Function to find hurricane causing most deaths
def deadliest_hurricane(hurricanes_dict):
    """
    Find the hurricane that caused the most deaths.
    
    Args:
        hurricanes_dict (dict): Dictionary of hurricanes
    
    Returns:
        tuple: (hurricane_name, death_count) of the deadliest hurricane
    """
    max_deaths = 0
    deadliest_hurricane_name = ""
    
    # Find hurricane with maximum death count
    for hurricane_name, hurricane_data in hurricanes_dict.items():
        if hurricane_data['Deaths'] > max_deaths:
            max_deaths = hurricane_data['Deaths']
            deadliest_hurricane_name = hurricane_name
    
    return deadliest_hurricane_name, max_deaths

# Test Task 6
deadliest = deadliest_hurricane(hurricanes_by_name)
print(f"Task 6 - Deadliest hurricane: {deadliest[0]} with {deadliest[1]} deaths")
print()

# Task 7: Function to rate hurricanes by mortality scale
def hurricanes_by_mortality(hurricanes_dict):
    """
    Rate hurricanes on a mortality scale based on death count.
    
    Args:
        hurricanes_dict (dict): Dictionary of hurricanes
    
    Returns:
        dict: Dictionary with mortality ratings as keys and lists of hurricanes as values
    """
    # Define mortality scale
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    
    # Initialize dictionary for each mortality rating
    hurricanes_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    
    # Categorize each hurricane based on death count
    for hurricane in hurricanes_dict.values():
        deaths = hurricane['Deaths']
        
        # Determine mortality rating based on death count
        if deaths == 0:
            hurricanes_mortality[0].append(hurricane)
        elif deaths <= 100:
            hurricanes_mortality[1].append(hurricane)
        elif deaths <= 500:
            hurricanes_mortality[2].append(hurricane)
        elif deaths <= 1000:
            hurricanes_mortality[3].append(hurricane)
        elif deaths <= 10000:
            hurricanes_mortality[4].append(hurricane)
        else:
            hurricanes_mortality[5].append(hurricane)
    
    return hurricanes_mortality

# Test Task 7
mortality_rating = hurricanes_by_mortality(hurricanes_by_name)
print("Task 7 - Hurricanes by mortality rating:")
for rating, hurricane_list in mortality_rating.items():
    print(f"Mortality rating {rating}: {len(hurricane_list)} hurricanes")
print()

# Task 8: Function to find hurricane causing greatest damage
def greatest_damage_hurricane(hurricanes_dict):
    """
    Find the hurricane that caused the greatest financial damage.
    
    Args:
        hurricanes_dict (dict): Dictionary of hurricanes
    
    Returns:
        tuple: (hurricane_name, damage_amount) of the most costly hurricane
    """
    max_damage = 0
    most_costly_hurricane = ""
    
    # Find hurricane with maximum damage cost
    for hurricane_name, hurricane_data in hurricanes_dict.items():
        damage = hurricane_data['Damage']
        
        # Skip hurricanes with unrecorded damage
        if damage == "Damages not recorded":
            continue
        
        # Check if this hurricane caused more damage than current maximum
        if damage > max_damage:
            max_damage = damage
            most_costly_hurricane = hurricane_name
    
    return most_costly_hurricane, max_damage

# Test Task 8
most_costly = greatest_damage_hurricane(hurricanes_by_name)
print(f"Task 8 - Most costly hurricane: {most_costly[0]} with ${most_costly[1]:,.2f} in damages")
print()

# Task 9: Function to rate hurricanes by damage scale
def hurricanes_by_damage_scale(hurricanes_dict):
    """
    Rate hurricanes on a damage scale based on financial cost.
    
    Args:
        hurricanes_dict (dict): Dictionary of hurricanes
    
    Returns:
        dict: Dictionary with damage ratings as keys and lists of hurricanes as values
    """
    # Define damage scale
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    
    # Initialize dictionary for each damage rating
    hurricanes_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    
    # Categorize each hurricane based on damage cost
    for hurricane in hurricanes_dict.values():
        damage = hurricane['Damage']
        
        # Skip hurricanes with unrecorded damage
        if damage == "Damages not recorded":
            hurricanes_damage[0].append(hurricane)
            continue
        
        # Determine damage rating based on cost
        if damage == 0:
            hurricanes_damage[0].append(hurricane)
        elif damage <= 100000000:
            hurricanes_damage[1].append(hurricane)
        elif damage <= 1000000000:
            hurricanes_damage[2].append(hurricane)
        elif damage <= 10000000000:
            hurricanes_damage[3].append(hurricane)
        elif damage <= 50000000000:
            hurricanes_damage[4].append(hurricane)
        else:
            hurricanes_damage[5].append(hurricane)
    
    return hurricanes_damage

# Test Task 9
damage_rating = hurricanes_by_damage_scale(hurricanes_by_name)
print("Task 9 - Hurricanes by damage rating:")
for rating, hurricane_list in damage_rating.items():
    print(f"Damage rating {rating}: {len(hurricane_list)} hurricanes")

# Additional analysis functions for comprehensive hurricane data insights
def summary_statistics(hurricanes_dict):
    """
    Generate summary statistics for the hurricane dataset.
    
    Args:
        hurricanes_dict (dict): Dictionary of hurricanes
    
    Returns:
        dict: Summary statistics
    """
    total_hurricanes = len(hurricanes_dict)
    total_deaths = sum(h['Deaths'] for h in hurricanes_dict.values())
    
    # Calculate total damages (excluding unrecorded)
    recorded_damages = [h['Damage'] for h in hurricanes_dict.values() if h['Damage'] != "Damages not recorded"]
    total_damage = sum(recorded_damages)
    
    # Wind speed statistics
    wind_speeds = [h['Max Sustained Wind'] for h in hurricanes_dict.values()]
    avg_wind_speed = sum(wind_speeds) / len(wind_speeds)
    max_wind_speed = max(wind_speeds)
    min_wind_speed = min(wind_speeds)
    
    return {
        'Total Hurricanes': total_hurricanes,
        'Total Deaths': total_deaths,
        'Total Damage (USD)': total_damage,
        'Average Wind Speed (mph)': round(avg_wind_speed, 2),
        'Maximum Wind Speed (mph)': max_wind_speed,
        'Minimum Wind Speed (mph)': min_wind_speed
    }

# Display summary statistics
print("\n" + "="*50)
print("HURRICANE ANALYSIS SUMMARY")
print("="*50)
stats = summary_statistics(hurricanes_by_name)
for key, value in stats.items():
    if 'Damage' in key:
        print(f"{key}: ${value:,.2f}")
    else:
        print(f"{key}: {value}")

print("\nProject completed successfully! All 9 tasks have been implemented with comprehensive hurricane analysis functions.")
