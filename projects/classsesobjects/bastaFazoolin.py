# Basta Fazoolin' Restaurant Management System
# A comprehensive system for managing menus, franchises, and businesses

# MAKING THE MENUS

# Task 1: Create a Menu class
class Menu:
    # Task 2: Constructor with parameters self, name, items, start_time, and end_time
    def __init__(self, name, items, start_time, end_time):
        """
        Initialize a Menu object
        
        Parameters:
        - name: string representing the menu name
        - items: dictionary with item names as keys and prices as values
        - start_time: integer representing start hour (24-hour format)
        - end_time: integer representing end hour (24-hour format)
        """
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    # Task 8: String representation method
    def __repr__(self):
        """
        Return string representation showing menu name and availability times
        """
        # Convert 24-hour time to 12-hour format for display
        start_display = f"{self.start_time}am" if self.start_time < 12 else f"{self.start_time - 12}pm"
        if self.start_time == 12:
            start_display = "12pm"
        
        end_display = f"{self.end_time}am" if self.end_time < 12 else f"{self.end_time - 12}pm"
        if self.end_time == 12:
            end_display = "12pm"
        
        return f"{self.name} menu available from {start_display} to {end_display}"
    
    # Task 10: Calculate bill method
    def calculate_bill(self, purchased_items):
        """
        Calculate total bill for purchased items
        
        Parameters:
        - purchased_items: list of item names that were purchased
        
        Returns:
        - float: total cost of all purchased items
        """
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total

# Task 3: Create brunch menu (11am to 4pm)
brunch_items = {
    'pancakes': 7.50, 
    'waffles': 9.00, 
    'burger': 11.00, 
    'home fries': 4.50, 
    'coffee': 1.50, 
    'espresso': 3.00, 
    'tea': 1.00, 
    'mimosa': 10.50, 
    'orange juice': 3.50
}
brunch = Menu("brunch", brunch_items, 11, 16)

# Task 4: Create early_bird menu (3pm to 6pm)
early_bird_items = {
    'salumeria plate': 8.00, 
    'salad and breadsticks (serves 2, no refills)': 14.00, 
    'pizza with quattro formaggi': 9.00, 
    'duck ragu': 17.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 1.50, 
    'espresso': 3.00
}
early_bird = Menu("early_bird", early_bird_items, 15, 18)

# Task 5: Create dinner menu (5pm to 11pm)
dinner_items = {
    'crostini with eggplant caponata': 13.00, 
    'caesar salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 
    'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 
    'coffee': 2.00, 
    'espresso': 3.00
}
dinner = Menu("dinner", dinner_items, 17, 23)

# Task 6: Create kids menu (11am to 9pm)
kids_items = {
    'chicken nuggets': 6.50, 
    'fusilli with wild mushrooms': 12.00, 
    'apple juice': 3.00
}
kids = Menu("kids", kids_items, 11, 21)

# Task 9: Test string representation
print("Testing Menu string representation:")
print(brunch)
print()

# Task 11: Test calculate_bill with breakfast order
print("Testing calculate_bill:")
breakfast_order = ['pancakes', 'home fries', 'coffee']
breakfast_total = brunch.calculate_bill(breakfast_order)
print(f"Breakfast order total: ${breakfast_total}")

# Task 12: Test early-bird purchase
early_bird_order = ['salumeria plate', 'mushroom ravioli (vegan)']
early_bird_total = early_bird.calculate_bill(early_bird_order)
print(f"Early-bird order total: ${early_bird_total}")
print()

# CREATING THE FRANCHISES

# Task 13: Create Franchise class
class Franchise:
    # Task 14: Constructor with address and menus parameters
    def __init__(self, address, menus):
        """
        Initialize a Franchise object
        
        Parameters:
        - address: string representing the franchise address
        - menus: list of Menu objects available at this franchise
        """
        self.address = address
        self.menus = menus
    
    # Task 16: String representation for Franchise
    def __repr__(self):
        """
        Return string representation showing franchise address
        """
        return f"Franchise at {self.address}"
    
    # Task 17: Available menus method
    def available_menus(self, time):
        """
        Return list of menus available at given time
        
        Parameters:
        - time: integer representing current hour (24-hour format)
        
        Returns:
        - list: Menu objects that are available at the given time
        """
        available = []
        for menu in self.menus:
            # Check if current time falls within menu's operating hours
            if menu.start_time <= time < menu.end_time:
                available.append(menu)
        return available

# Task 15: Create two franchises
all_menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)

print("Testing Franchise string representation:")
print(flagship_store)
print(new_installment)
print()

# Task 18: Test available_menus at 12 noon (12pm = 12 in 24-hour format)
print("Testing available_menus method:")
noon_menus = flagship_store.available_menus(12)
print(f"Available menus at 12 noon: {[menu.name for menu in noon_menus]}")

# Task 19: Test available_menus at 5pm (17 in 24-hour format)
five_pm_menus = flagship_store.available_menus(17)
print(f"Available menus at 5pm: {[menu.name for menu in five_pm_menus]}")
print()

# CREATING BUSINESSES

# Task 20: Define Business class
class Business:
    # Task 21: Constructor with name and franchises parameters
    def __init__(self, name, franchises):
        """
        Initialize a Business object
        
        Parameters:
        - name: string representing the business name
        - franchises: list of Franchise objects owned by this business
        """
        self.name = name
        self.franchises = franchises
    
    def __repr__(self):
        """
        Return string representation of the business
        """
        return f"Business: {self.name} with {len(self.franchises)} franchise(s)"

# Task 22: Create first Business
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

print("Testing Business creation:")
print(basta_fazoolin)
print()

# Task 23: Create arepas menu (10am to 8pm)
arepas_items = {
    'arepa pabellon': 7.00, 
    'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 
    'jamon arepa': 7.50
}
arepas_menu = Menu("Take a' Arepa", arepas_items, 10, 20)

# Task 24: Create Take a' Arepa franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Task 25: Create Take a' Arepa business
take_a_arepa = Business("Take a' Arepa", [arepas_place])

print("Testing Take a' Arepa business:")
print(take_a_arepa)
print(arepas_place)
print(arepas_menu)

# Task 26: Final demonstration
print("\n" + "="*50)
print("FINAL DEMONSTRATION")
print("="*50)

print(f"\n{basta_fazoolin.name} has {len(basta_fazoolin.franchises)} locations:")
for franchise in basta_fazoolin.franchises:
    print(f"- {franchise.address}")

print(f"\n{take_a_arepa.name} has {len(take_a_arepa.franchises)} locations:")
for franchise in take_a_arepa.franchises:
    print(f"- {franchise.address}")

print(f"\nSample menu availability at flagship store at 3pm:")
three_pm_menus = flagship_store.available_menus(15)
for menu in three_pm_menus:
    print(f"- {menu.name}")

print(f"\nSample bill calculation for dinner order:")
dinner_order = ['caesar salad', 'duck ragu', 'coffee']
dinner_total = dinner.calculate_bill(dinner_order)
print(f"Items: {', '.join(dinner_order)}")
print(f"Total: ${dinner_total}")

print("\nSystem successfully implemented! All 26 tasks completed.")
