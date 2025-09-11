# A/B Testing Analysis for ShoeFly.com
# Data Science Foundations II Project
# Analyzing ad performance across different platforms and experimental groups

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

print("A/B TESTING ANALYSIS FOR SHOEFLY.COM")
print("=" * 50)
print("Analyzing ad performance across platforms and experimental groups")
print("=" * 50)
print()

# Create realistic sample data for A/B testing analysis
# This simulates the ad_clicks dataset that would typically be provided

# Set random seed for reproducible results
np.random.seed(42)
random.seed(42)

# Define parameters for realistic data generation
n_users = 2000  # Total number of ad impressions
utm_sources = ['email', 'facebook', 'twitter', 'google']
experimental_groups = ['A', 'B']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Generate sample data
sample_data = []
base_date = datetime(2024, 1, 1)  # Starting date

for i in range(n_users):
    # Generate user_id
    user_id = f"user_{i+1}"
    
    # Randomly assign utm_source (with realistic distribution)
    utm_source = np.random.choice(utm_sources, p=[0.3, 0.25, 0.2, 0.25])
    
    # Randomly assign experimental group (should be roughly 50/50)
    experimental_group = np.random.choice(experimental_groups)
    
    # Generate day of week
    day = np.random.choice(days_of_week)
    
    # Generate ad_click_timestamp based on realistic click rates
    # Different platforms and ads have different click rates
    click_probability = 0.1  # Base click rate
    
    # Adjust click probability based on utm_source
    if utm_source == 'email':
        click_probability = 0.15  # Email typically has higher engagement
    elif utm_source == 'facebook':
        click_probability = 0.12
    elif utm_source == 'google':
        click_probability = 0.08
    else:  # twitter
        click_probability = 0.06
    
    # Adjust click probability based on experimental group (Ad B is slightly better)
    if experimental_group == 'B':
        click_probability *= 1.2  # Ad B performs 20% better
    
    # Adjust by day of week (weekends typically have different patterns)
    if day in ['Saturday', 'Sunday']:
        click_probability *= 0.8  # Lower engagement on weekends
    elif day in ['Tuesday', 'Wednesday']:
        click_probability *= 1.1  # Higher engagement mid-week
    
    # Determine if there was a click
    has_click = np.random.random() < click_probability
    
    # Generate timestamp if there was a click, otherwise null
    if has_click:
        # Generate random timestamp within the day
        random_hour = np.random.randint(0, 24)
        random_minute = np.random.randint(0, 60)
        ad_click_timestamp = base_date + timedelta(
            days=np.random.randint(0, 30),  # Random day in month
            hours=random_hour,
            minutes=random_minute
        )
    else:
        ad_click_timestamp = None
    
    sample_data.append({
        'user_id': user_id,
        'utm_source': utm_source,
        'day': day,
        'ad_click_timestamp': ad_click_timestamp,
        'experimental_group': experimental_group
    })

# Create DataFrame
ad_clicks = pd.DataFrame(sample_data)

print("Sample A/B testing data created for analysis")
print("(In real scenario, this would be loaded from actual ad tracking data)")
print(f"Dataset contains {len(ad_clicks)} ad impressions")
print()

# Task 1: Examine the first few rows of ad_clicks
print("Task 1: First few rows of ad_clicks dataset:")
print("-" * 60)
print(ad_clicks.head())
print()

# Display basic dataset information
print("Dataset Overview:")
print(f"Total rows: {len(ad_clicks)}")
print(f"Columns: {list(ad_clicks.columns)}")
print(f"Data types:\n{ad_clicks.dtypes}")
print()

# Task 2: Find which ad platform is getting the most views
print("Task 2: Views (impressions) by utm_source:")
print("-" * 45)

# Count the number of rows (views) for each utm_source
views_by_source = ad_clicks['utm_source'].value_counts().sort_values(ascending=False)
print("Platform\t\tViews\t\tPercentage")
print("-" * 45)

total_views = len(ad_clicks)
for source, views in views_by_source.items():
    percentage = (views / total_views) * 100
    print(f"{source}\t\t{views}\t\t{percentage:.1f}%")

print(f"\nTotal views: {total_views}")
print(f"Most popular platform: {views_by_source.index[0]} with {views_by_source.iloc[0]} views")
print()

# Task 3: Create is_click column based on ad_click_timestamp
print("Task 3: Creating 'is_click' column:")
print("-" * 35)

# Create is_click column: True if ad_click_timestamp is not null, False otherwise
ad_clicks['is_click'] = ad_clicks['ad_click_timestamp'].notnull()

# Display summary of clicks
total_clicks = ad_clicks['is_click'].sum()
total_impressions = len(ad_clicks)
overall_click_rate = (total_clicks / total_impressions) * 100

print(f"✓ Created 'is_click' column")
print(f"Total clicks: {total_clicks}")
print(f"Total impressions: {total_impressions}")
print(f"Overall click rate: {overall_click_rate:.2f}%")
print()

# Show sample of the new column
print("Sample of data with is_click column:")
print(ad_clicks[['utm_source', 'ad_click_timestamp', 'is_click']].head(10))
print()

# Task 4: Group by utm_source and is_click, count user_ids
print("Task 4: Grouping by utm_source and is_click:")
print("-" * 50)

# Group by utm_source and is_click, count user_ids in each group
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
clicks_by_source.columns = ['utm_source', 'is_click', 'count']

print("Clicks and non-clicks by source:")
print(clicks_by_source)
print()

# Task 5: Pivot the data with is_click as columns and utm_source as index
print("Task 5: Pivoting data for better analysis:")
print("-" * 45)

# Pivot table with utm_source as index, is_click as columns, and user_id count as values
clicks_pivot = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().unstack(fill_value=0)

print("Pivoted data (rows=utm_source, columns=is_click):")
print(clicks_pivot)
print()

# Task 6: Calculate percent_clicked for each utm_source
print("Task 6: Calculating click rates by source:")
print("-" * 45)

# Calculate percentage of users who clicked from each utm_source
clicks_pivot['percent_clicked'] = (clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])) * 100

print("Click rates by platform:")
print("Platform\t\tClicks\tNo Clicks\tClick Rate")
print("-" * 55)

for source in clicks_pivot.index:
    clicks = clicks_pivot.loc[source, True]
    no_clicks = clicks_pivot.loc[source, False]
    click_rate = clicks_pivot.loc[source, 'percent_clicked']
    print(f"{source}\t\t{clicks}\t{no_clicks}\t\t{click_rate:.2f}%")

print(f"\nHighest performing platform: {clicks_pivot['percent_clicked'].idxmax()} "
      f"({clicks_pivot['percent_clicked'].max():.2f}% click rate)")
print()

# Analyze differences in click rates
print("Analysis of click rate differences:")
max_rate = clicks_pivot['percent_clicked'].max()
min_rate = clicks_pivot['percent_clicked'].min()
print(f"Range: {max_rate:.2f}% - {min_rate:.2f}% = {max_rate - min_rate:.2f} percentage points")

if max_rate - min_rate > 2:
    print("✓ There are significant differences in click rates between platforms")
else:
    print("• Click rates are relatively similar across platforms")
print()

# Task 7: Check if approximately same number of people shown both ads
print("ANALYZING A/B TEST")
print("=" * 30)
print("Task 7: Distribution of experimental groups:")
print("-" * 45)

# Count users in each experimental group
group_distribution = ad_clicks['experimental_group'].value_counts()
print("Experimental Group Distribution:")

for group, count in group_distribution.items():
    percentage = (count / len(ad_clicks)) * 100
    print(f"Group {group}: {count} users ({percentage:.1f}%)")

# Check if distribution is balanced (roughly 50/50)
group_a_pct = (group_distribution['A'] / len(ad_clicks)) * 100
group_b_pct = (group_distribution['B'] / len(ad_clicks)) * 100
difference = abs(group_a_pct - group_b_pct)

print(f"\nDifference between groups: {difference:.1f} percentage points")

if difference < 5:
    print("✓ Groups are well balanced (difference < 5%)")
else:
    print("⚠ Groups may be unbalanced (difference ≥ 5%)")
print()

# Task 8: Compare click rates between Ad A and Ad B
print("Task 8: Comparing click rates for Ad A vs Ad B:")
print("-" * 50)

# Calculate click rates for each experimental group
ab_click_rates = ad_clicks.groupby('experimental_group').agg({
    'is_click': ['sum', 'count', 'mean']
}).round(4)

# Flatten column names
ab_click_rates.columns = ['clicks', 'total_impressions', 'click_rate']
ab_click_rates['click_rate_percent'] = ab_click_rates['click_rate'] * 100

print("A/B Test Results:")
print("Group\tClicks\tImpressions\tClick Rate")
print("-" * 45)

for group in ab_click_rates.index:
    clicks = int(ab_click_rates.loc[group, 'clicks'])
    impressions = int(ab_click_rates.loc[group, 'total_impressions'])
    rate = ab_click_rates.loc[group, 'click_rate_percent']
    print(f"{group}\t{clicks}\t{impressions}\t\t{rate:.2f}%")

# Determine which ad performed better
if ab_click_rates.loc['A', 'click_rate_percent'] > ab_click_rates.loc['B', 'click_rate_percent']:
    winner = 'A'
    difference = ab_click_rates.loc['A', 'click_rate_percent'] - ab_click_rates.loc['B', 'click_rate_percent']
else:
    winner = 'B'
    difference = ab_click_rates.loc['B', 'click_rate_percent'] - ab_click_rates.loc['A', 'click_rate_percent']

print(f"\n🏆 Ad {winner} performs better by {difference:.2f} percentage points")
print()

# Task 9: Create separate DataFrames for A and B groups
print("Task 9: Creating separate DataFrames for each experimental group:")
print("-" * 65)

# Filter data for each experimental group
a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A'].copy()
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B'].copy()

print(f"✓ Created a_clicks DataFrame: {len(a_clicks)} rows (Group A)")
print(f"✓ Created b_clicks DataFrame: {len(b_clicks)} rows (Group B)")
print()

# Task 10: Calculate percent of users who clicked by day for each group
print("Task 10: Click rates by day of week for each group:")
print("-" * 55)

# Calculate click rates by day for Group A
a_daily_clicks = a_clicks.groupby('day').agg({
    'is_click': ['sum', 'count', 'mean']
})
a_daily_clicks.columns = ['clicks', 'impressions', 'click_rate']
a_daily_clicks['click_rate_percent'] = a_daily_clicks['click_rate'] * 100

# Calculate click rates by day for Group B  
b_daily_clicks = b_clicks.groupby('day').agg({
    'is_click': ['sum', 'count', 'mean']
})
b_daily_clicks.columns = ['clicks', 'impressions', 'click_rate']
b_daily_clicks['click_rate_percent'] = b_daily_clicks['click_rate'] * 100

# Order days of week properly
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
a_daily_clicks = a_daily_clicks.reindex(day_order)
b_daily_clicks = b_daily_clicks.reindex(day_order)

print("GROUP A - Daily Click Rates:")
print("Day\t\tClicks\tImpressions\tClick Rate")
print("-" * 50)
for day in day_order:
    if day in a_daily_clicks.index:
        clicks = int(a_daily_clicks.loc[day, 'clicks'])
        impressions = int(a_daily_clicks.loc[day, 'impressions'])
        rate = a_daily_clicks.loc[day, 'click_rate_percent']
        print(f"{day}\t{clicks}\t{impressions}\t\t{rate:.2f}%")

print(f"\nGROUP B - Daily Click Rates:")
print("Day\t\tClicks\tImpressions\tClick Rate")
print("-" * 50)
for day in day_order:
    if day in b_daily_clicks.index:
        clicks = int(b_daily_clicks.loc[day, 'clicks'])
        impressions = int(b_daily_clicks.loc[day, 'impressions'])
        rate = b_daily_clicks.loc[day, 'click_rate_percent']
        print(f"{day}\t{clicks}\t{impressions}\t\t{rate:.2f}%")
print()

# Task 11: Compare results and make recommendation
print("Task 11: Weekly Performance Comparison and Recommendation:")
print("-" * 65)

# Create comparison table
comparison = pd.DataFrame({
    'Group_A_Rate': a_daily_clicks['click_rate_percent'],
    'Group_B_Rate': b_daily_clicks['click_rate_percent']
})
comparison['Difference'] = comparison['Group_B_Rate'] - comparison['Group_A_Rate']
comparison['B_Better'] = comparison['Difference'] > 0

print("Day-by-Day Comparison:")
print("Day\t\tGroup A\tGroup B\tDifference\tB Better?")
print("-" * 60)
for day in day_order:
    if day in comparison.index:
        a_rate = comparison.loc[day, 'Group_A_Rate']
        b_rate = comparison.loc[day, 'Group_B_Rate']
        diff = comparison.loc[day, 'Difference']
        b_better = "Yes" if comparison.loc[day, 'B_Better'] else "No"
        print(f"{day}\t{a_rate:.1f}%\t{b_rate:.1f}%\t{diff:+.1f}pp\t\t{b_better}")

# Analysis and recommendation
print(f"\nWEEKLY PERFORMANCE ANALYSIS:")
print("-" * 35)

days_b_better = comparison['B_Better'].sum()
total_days = len(comparison)
b_better_percentage = (days_b_better / total_days) * 100

print(f"Days where B outperformed A: {days_b_better}/{total_days} ({b_better_percentage:.0f}%)")
print(f"Average daily difference: {comparison['Difference'].mean():+.2f} percentage points")

# Overall recommendation
overall_a_rate = ab_click_rates.loc['A', 'click_rate_percent']
overall_b_rate = ab_click_rates.loc['B', 'click_rate_percent']
overall_difference = overall_b_rate - overall_a_rate

print(f"\nOVERALL RECOMMENDATION:")
print("=" * 25)

if overall_difference > 1 and days_b_better >= total_days * 0.6:
    recommendation = "B"
    reason = f"consistently outperforms A by {overall_difference:.2f}pp overall"
elif overall_difference < -1 and days_b_better <= total_days * 0.4:
    recommendation = "A"
    reason = f"outperforms B by {abs(overall_difference):.2f}pp overall"
else:
    recommendation = "Further Testing"
    reason = "performance differences are not conclusive"

print(f"🎯 RECOMMENDATION: Use Ad {recommendation}")
print(f"📊 REASON: Ad {reason}")

if recommendation in ['A', 'B']:
    print(f"📈 IMPACT: Expected {abs(overall_difference):.2f} percentage point improvement in click rate")
    
    # Calculate potential revenue impact
    baseline_rate = min(overall_a_rate, overall_b_rate)
    improved_rate = max(overall_a_rate, overall_b_rate)
    relative_improvement = ((improved_rate - baseline_rate) / baseline_rate) * 100
    print(f"💰 BUSINESS IMPACT: {relative_improvement:.1f}% relative improvement in click-through rate")

print(f"\n✅ All 11 tasks completed successfully!")
print("ShoeFly.com now has comprehensive A/B testing insights!")
