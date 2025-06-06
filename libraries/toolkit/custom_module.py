# TASK 1: Create the Custom Module
# This file serves as our custom module for the Time Traveler's Toolkit project

# TASK 2: Define generate_time_travel_message function
def generate_time_travel_message(year, destination, cost):
    """
    Generate a formatted time travel message.
    
    Parameters:
    year (int): The target year for time travel
    destination (str): The destination for time travel
    cost (Decimal): The cost of the time travel experience
    
    Returns:
    str: A formatted message about the time travel experience
    """
    message = f"""
🚀 TIME TRAVEL CONFIRMATION 🚀
================================
Destination Year: {year}
Location: {destination}
Total Cost: ${cost}
================================
Prepare for an amazing journey through time!
Your adventure to {destination} in the year {year} awaits.
Safe travels, time traveler!
    """
    return message
