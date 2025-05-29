''' You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

You have been provided with three lists:

hairstyles: the names of the cuts offered at Carly’s Clippers.
prices: the price of each hairstyle in the hairstyles list.
last_week: the number of purchases for each hairstyle type in the last week.
Each index in hairstyles corresponds to an associated index in prices and last_week.

For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was purchased 2 times in the last week as shown in the last_week list. Each of these elements are in the first index of their respective lists.
 '''

# Given data
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# PRICES AND CUTS

# Task 1: Create variable total_price and set it to 0
total_price = 0

# Task 2: Loop through prices list and add each price to total_price
for price in prices:
    total_price += price

# Task 3: Calculate average price
average_price = total_price / len(prices)

# Task 4: Print the average price
print(f"Average Haircut Price: {average_price}")

# Task 5: Create new_prices with each price reduced by $5
new_prices = [price - 5 for price in prices]

# Task 6: Print new_prices
print(new_prices)

# REVENUE

# Task 7: Create total_revenue variable and set it to 0
total_revenue = 0

# Task 8 & 9: Loop through indices and calculate total revenue
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

# Task 10: Print total revenue
print(f"Total Revenue: {total_revenue}")

# Task 11: Calculate and print average daily revenue
average_daily_revenue = total_revenue / 7
print(f"Average Daily Revenue: {average_daily_revenue}")

# Task 12: Create list of cuts under $30 using new_prices
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# Task 13: Print cuts under $30
print(cuts_under_30)
