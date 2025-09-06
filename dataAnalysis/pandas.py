# Petal Power Inventory Analysis
# Data Science Foundations II Project
# Analyzing inventory data for a chain of gardening stores

import pandas as pd
import numpy as np

print("PETAL POWER INVENTORY ANALYSIS")
print("=" * 50)
print("Analyzing inventory data for gardening store chain")
print("=" * 50)
print()

# Create sample inventory data (since we don't have the actual CSV file)
# This data structure matches what would be expected in the inventory.csv file
sample_data = {
    'location': ['Staten Island'] * 10 + ['Brooklyn'] * 8 + ['Queens'] * 7 + ['Manhattan'] * 5,
    'product_type': [
        # Staten Island (first 10 rows)
        'seeds', 'seeds', 'garden_tools', 'fertilizer', 'pots', 
        'seeds', 'garden_tools', 'fertilizer', 'pots', 'seeds',
        # Brooklyn
        'seeds', 'seeds', 'seeds', 'garden_tools', 'fertilizer', 
        'pots', 'seeds', 'garden_tools',
        # Queens  
        'fertilizer', 'pots', 'seeds', 'garden_tools', 'seeds', 
        'fertilizer', 'pots',
        # Manhattan
        'garden_tools', 'fertilizer', 'pots', 'seeds', 'garden_tools'
    ],
    'product_description': [
        # Staten Island
        'Sunflower Seeds', 'Tomato Seeds', 'Pruning Shears', 'Organic Compost', 'Clay Pots',
        'Basil Seeds', 'Garden Rake', 'Plant Food', 'Ceramic Planters', 'Lettuce Seeds',
        # Brooklyn
        'Rose Seeds', 'Pepper Seeds', 'Marigold Seeds', 'Watering Can', 'Nitrogen Fertilizer',
        'Plastic Pots', 'Herb Mix Seeds', 'Hand Trowel',
        # Queens
        'Bone Meal', 'Terracotta Pots', 'Carrot Seeds', 'Garden Hoe', 'Spinach Seeds',
        'Liquid Fertilizer', 'Decorative Pots',
        # Manhattan
        'Pruning Knife', 'Potting Mix', 'Window Boxes', 'Orchid Seeds', 'Soil Thermometer'
    ],
    'quantity': [25, 15, 8, 12, 20, 30, 5, 18, 0, 22, 18, 25, 12, 6, 20, 15, 8, 10, 25, 18, 14, 7, 16, 22, 12, 4, 8, 10, 0, 3],
    'price': [2.99, 3.49, 12.99, 8.50, 4.99, 2.79, 15.99, 6.25, 7.99, 2.89, 4.99, 3.25, 3.75, 18.99, 12.50, 3.99, 4.50, 8.99, 9.75, 5.99, 2.65, 22.50, 3.15, 11.25, 6.75, 28.99, 7.50, 15.99, 45.00, 12.75]
}

# Create DataFrame from sample data
inventory = pd.DataFrame(sample_data)

print("Sample inventory data created for demonstration purposes")
print("(In real scenario, this would be loaded from inventory.csv)")
print()

# Task 1: Load the data into a DataFrame called inventory
# Note: In real scenario, this would be:
# inventory = pd.read_csv('inventory.csv')
print("Task 1: ✓ Data loaded into DataFrame called 'inventory'")
print(f"DataFrame shape: {inventory.shape} (rows: {inventory.shape[0]}, columns: {inventory.shape[1]})")
print()

# Task 2: Inspect the first 10 rows of inventory
print("Task 2: First 10 rows of inventory:")
print("-" * 60)
print(inventory.head(10))
print()

# Task 3: Select first 10 rows and save to staten_island
staten_island = inventory.head(10)
print("Task 3: ✓ Selected first 10 rows (Staten Island location)")
print("Staten Island inventory:")
print(staten_island)
print()

# Task 4: Select product_description column from staten_island for customer request
product_request = staten_island['product_description']
print("Task 4: Products available at Staten Island location:")
print("-" * 50)
print("Customer Email Response:")
print("Dear Customer,")
print("Here are the products available at our Staten Island location:")
for i, product in enumerate(product_request, 1):
    print(f"{i}. {product}")
print("\nThank you for your inquiry!")
print("- Petal Power Customer Service")
print()

# Task 5: Select Brooklyn location seeds for customer request
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]
print("Task 5: Seeds available at Brooklyn location:")
print("-" * 50)
print("Customer Email Response:")
print("Dear Customer,")
print("Here are the seeds available at our Brooklyn location:")
print(seed_request[['product_description', 'quantity', 'price']])
print("\nThank you for your inquiry!")
print("- Petal Power Customer Service")
print()

# Task 6: Add in_stock column based on quantity
inventory['in_stock'] = inventory['quantity'] > 0
print("Task 6: ✓ Added 'in_stock' column")
print("Stock status summary:")
in_stock_count = inventory['in_stock'].sum()
out_of_stock_count = len(inventory) - in_stock_count
print(f"Items in stock: {in_stock_count}")
print(f"Items out of stock: {out_of_stock_count}")
print()

# Show some examples of the in_stock column
print("Sample of inventory with stock status:")
print(inventory[['product_description', 'quantity', 'in_stock']].head(10))
print()

# Task 7: Create total_value column (price * quantity)
inventory['total_value'] = inventory['price'] * inventory['quantity']
print("Task 7: ✓ Added 'total_value' column (price × quantity)")
print()

# Calculate and display inventory value statistics
total_inventory_value = inventory['total_value'].sum()
average_item_value = inventory['total_value'].mean()
print("Inventory Value Analysis:")
print("-" * 30)
print(f"Total inventory value: ${total_inventory_value:,.2f}")
print(f"Average item value: ${average_item_value:.2f}")
print()

# Show inventory value by location
print("Inventory value by location:")
location_values = inventory.groupby('location')['total_value'].sum().sort_values(ascending=False)
for location, value in location_values.items():
    print(f"{location}: ${value:,.2f}")
print()

# Task 8: Create the combine_lambda function
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

print("Task 8: ✓ Created combine_lambda function")
print("Lambda function combines product_type and product_description")
print("Example: 'seeds' + 'Sunflower Seeds' = 'seeds - Sunflower Seeds'")
print()

# Task 9: Use combine_lambda to create full_description column
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print("Task 9: ✓ Added 'full_description' column using combine_lambda")
print()

print("Sample of full descriptions for Marketing catalog:")
print("-" * 55)
for i, desc in enumerate(inventory['full_description'].head(10), 1):
    print(f"{i:2d}. {desc}")
print()

# Display final DataFrame structure
print("FINAL INVENTORY DATAFRAME")
print("=" * 40)
print("DataFrame Info:")
print(f"Shape: {inventory.shape}")
print(f"Columns: {list(inventory.columns)}")
print()

print("Complete inventory with all new columns:")
print(inventory)
print()

# Additional Analysis for Business Insights
print("ADDITIONAL BUSINESS INSIGHTS")
print("=" * 40)

# Product type analysis
print("1. Product Type Distribution:")
product_type_counts = inventory['product_type'].value_counts()
for product_type, count in product_type_counts.items():
    print(f"   {product_type}: {count} items")
print()

# Location analysis
print("2. Inventory by Location:")
location_analysis = inventory.groupby('location').agg({
    'quantity': 'sum',
    'total_value': 'sum',
    'product_description': 'count'
}).round(2)
location_analysis.columns = ['Total Quantity', 'Total Value ($)', 'Number of Products']
print(location_analysis)
print()

# Out of stock analysis
print("3. Out of Stock Analysis:")
out_of_stock = inventory[inventory['quantity'] == 0]
if len(out_of_stock) > 0:
    print("Items needing restocking:")
    for _, item in out_of_stock.iterrows():
        print(f"   {item['location']}: {item['full_description']}")
else:
    print("   ✓ All items are currently in stock!")
print()

# High-value items
print("4. Top 5 Most Valuable Items:")
top_value_items = inventory.nlargest(5, 'total_value')[['full_description', 'location', 'total_value']]
for i, (_, item) in enumerate(top_value_items.iterrows(), 1):
    print(f"   {i}. {item['full_description']} ({item['location']}): ${item['total_value']:.2f}")
print()

# Summary for management
print("EXECUTIVE SUMMARY")
print("=" * 25)
print(f"• Total locations: {inventory['location'].nunique()}")
print(f"• Total products: {len(inventory)}")
print(f"• Total inventory value: ${total_inventory_value:,.2f}")
print(f"• Items in stock: {in_stock_count}/{len(inventory)} ({in_stock_count/len(inventory)*100:.1f}%)")
print(f"• Most common product type: {product_type_counts.index[0]} ({product_type_counts.iloc[0]} items)")
print(f"• Highest value location: {location_values.index[0]} (${location_values.iloc[0]:,.2f})")

print(f"\n✅ All 9 tasks completed successfully!")
print("Petal Power now has comprehensive inventory analysis tools!")
