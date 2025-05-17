"""
Command Line Calendar

This program provides a simple command line interface for a calendar application.
Users can:
- View the calendar
- Add an event to the calendar
- Update an existing event
- Delete an existing event

The program continues running until the user chooses to exit.
"""
# Step 1: Added multi-line comment above describing the program

# Step 2-4: Import sleep and strftime from the time module
from time import sleep, strftime

# Step 5: Create a constant variable for the user's name
USER_NAME = "Alex"

# Step 7: Create an empty dictionary for the calendar
calendar = {}

# Step 8-13: Create welcome function
def welcome():
    """Display welcome message and current date/time information"""
    # Step 9: Print welcome message with user's name
    print("\nWelcome to the Command Line Calendar, " + USER_NAME + "!")
    
    # Step 10: Print opening message and sleep
    print("Opening calendar...")
    sleep(1)
    
    # Step 11: Print current date using strftime
    print("Today is: " + strftime("%A %B %d, %Y"))
    
    # Step 12: Print current time using strftime and sleep
    print("Current time: " + strftime("%H:%M:%S"))
    sleep(1)
    
    # Step 13: Prompt the user
    print("What would you like to do?")

# Step 14: Create start_calendar function
def start_calendar():
    """Main function to start and run the calendar application"""
    # Step 15: Call the welcome function
    welcome()
    
    # Step 16: Create a variable and while loop to keep the program running
    start = True
    while start:
        # Step 17: Prompt user for their choice and convert to uppercase
        user_choice = input("\nEnter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()
        
        # Step 18-21: View calendar functionality
        if user_choice == "V":
            # Step 20: Check if calendar is empty
            if len(calendar.keys()) < 1:
                print("\nYour calendar is empty.")
            # Step 21: If not empty, print the calendar
            else:
                print("\nYour Calendar:")
                for date in sorted(calendar.keys()):
                    print(f"{date}: {calendar[date]}")
                    
        # Step 22-25: Update calendar functionality
        elif user_choice == "U":
            # Step 23: Prompt for date and update
            date = input("What date? ")
            if date not in calendar:
                print(f"No event found on {date}")
                continue
                
            update = input("Enter the update: ")
            # Step 24: Update the calendar
            calendar[date] = update
            # Step 25: Print success message and updated calendar
            print(f"\nEvent on {date} successfully updated!")
            print("\nYour Calendar:")
            for date in sorted(calendar.keys()):
                print(f"{date}: {calendar[date]}")
                
        # Step 26-34: Add to calendar functionality
        elif user_choice == "A":
            # Step 27: Prompt for event and date
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            
            # Step 28-29: Validate date format and year
            if len(date) > 10 or (int(date[6:]) < int(strftime("%Y"))):
                # Step 30: Print invalid date message
                print("\nInvalid date was entered.")
                # Step 31: Ask if user wants to try again
                try_again = input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                
                # Step 32: If yes, continue the loop
                if try_again == "Y":
                    continue
                # Step 33: If no, exit the program
                else:
                    start = False
            # Step 34: If date is valid, add to calendar
            else:
                calendar[date] = event
                print(f"\nEvent '{event}' successfully added to {date}!")
                print("\nYour Calendar:")
                for date in sorted(calendar.keys()):
                    print(f"{date}: {calendar[date]}")
                    
        # Step 35-42: Delete from calendar functionality
        elif user_choice == "D":
            # Step 36: Check if calendar is empty
            if len(calendar.keys()) < 1:
                print("\nYour calendar is empty.")
            # Step 37-42: If not empty, proceed with deletion
            else:
                # Step 37: Prompt for event to delete
                event = input("What event? ")
                event_found = False
                
                # Step 38: Loop through dates in calendar
                for date in calendar.keys():
                    # Step 39: Check if event exists
                    if calendar[date] == event:
                        # Step 40: Delete the event
                        del calendar[date]
                        # Step 41: Print success message and updated calendar
                        print(f"\nEvent '{event}' successfully deleted!")
                        event_found = True
                        print("\nYour Calendar:")
                        for date in sorted(calendar.keys()):
                            print(f"{date}: {calendar[date]}")
                        break
                
                # Step 42: If event not found, print message
                if not event_found:
                    print(f"\nEvent '{event}' not found in the calendar.")
                    
        # Step 43: Exit functionality
        elif user_choice == "X":
            print("\nExiting calendar. Goodbye!")
            start = False
            
        # Step 44: Handle invalid commands
        else:
            print("\nInvalid command entered.")
            print("Exiting calendar. Goodbye!")
            start = False

# Step 45: Call the start_calendar function
if __name__ == "__main__":
    start_calendar()
