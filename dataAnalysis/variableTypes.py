# Census Variables Data Cleaning Project
# Cleaning census data for a local community

import pandas as pd
import numpy as np
from io import StringIO

print("CENSUS VARIABLES DATA CLEANING PROJECT")
print("=" * 50)
print("Cleaning census data for local community")
print("=" * 50)
print()

# Load the census data from the provided CSV content
csv_data = """,first_name,last_name,birth_year,voted,num_children,income_year,higher_tax,marital_status
0,Denise,Ratke,2005,False,0,92129.41,disagree,single
1,Hali,Cummerata,1987,False,0,75649.17,neutral,divorced
2,Salomon,Orn,1992,True,2,166313.45,agree,single
3,Sarina,Schiller,1965,False,2,71704.81,strongly agree,married
4,Gust,Abernathy,1945,False,2,143316.08,agree,married
5,Lady,Hills,1951,True,0,160391.2,disagree,widowed
6,Tremaine,Pacocha,1963,False,1,49801.77,strongly disagree,divorced
7,Jaime,Towne,1949,False,2,140803.16,agree,single
8,Tex,Lynch,1950,False,1,122486.71,agree,single
9,Nathanial,Gislason,1971,True,4,157088.26,strongly agree,married
10,Dori,Weissnat,2007,True,3,134265.92,disagree,married
11,Baldwin,Johnson,1944,False,0,38891.56,disagree,widowed
12,Catrina,Nader,1963,True,3,194333.01,agree,single
13,Arlena,Crona,1995,True,4,181611.71,agree,married
14,Loring,Kling,1973,False,4,119504.61,agree,single
15,Roll,Bogisich,1946,True,3,102269.35,disagree,divorced
16,Geraldo,Kautzer,1954,False,3,74991.2,disagree,divorced
17,Lexis,Lockman,1994,True,4,193123.43,disagree,single
18,Norine,Hand,1989,False,0,65926.5,neutral,divorced
19,Derald,Pfeffer,1947,True,0,80073.83,disagree,married
20,Ted,Christiansen,1993,True,2,52389.69,strongly disagree,divorced
21,Jamal,Connelly,1989,True,4,160391.21,neutral,single
22,Lindy,Dooley,1976,True,1,75930.78,disagree,married
23,Jarret,Douglas,1984,False,3,46704.79,strongly agree,married
24,Fumiko,Monahan,1949,False,0,112923.53,disagree,single
25,Johnie,Runolfsson,missing,True,3,80478.48,neutral,divorced
26,Francesca,Beahan,1966,False,1,87453.19,strongly disagree,single
27,King,Donnelly,1945,False,1,154919.13,agree,married
28,Zola,Mayer,1992,False,0,47814.99,neutral,divorced
29,Seymour,Sanford,1941,False,3,108892.58,agree,divorced
30,Armando,Carter,2000,False,4,189335.31,disagree,married
31,Nathalie,Runte,1951,True,0,48370.32,disagree,widowed
32,Trevor,Monahan,1953,False,3,149052.29,strongly agree,single
33,Laverne,Streich,1971,True,1,116482.23,disagree,divorced
34,Linna,Monahan,1956,False,3,197143.58,agree,divorced
35,Daulton,Prohaska,1960,False,0,105501.13,strongly agree,single
36,Celestine,Gusikowski,1994,False,1,44727.06,disagree,married
37,Arminda,Stark,2001,True,1,68482.2,disagree,single
38,Erline,Abbott,1980,True,1,99337.46,neutral,married
39,Denisse,Orn,1954,False,1,46537.19,disagree,married
40,Augustine,Bayer,1963,False,3,174789.4,agree,divorced
41,Mart,Jacobson,1951,True,0,99867.58,neutral,single
42,Branson,Morissette,2007,True,2,113621.33,disagree,married
43,Ricci,Cartwright,1953,False,1,104480.48,strongly agree,married
44,Nikki,Jacobs,1955,False,4,35635.14,neutral,married
45,Ottilia,Haley,1992,False,3,58615.04,strongly agree,married
46,Loretta,Schimmel,1985,False,4,151979.07,agree,married
47,Meaghan,McLaughlin,1985,True,2,48135.37,disagree,divorced
48,Manford,Brekke,1996,False,1,170502.75,disagree,married
49,Estefania,Feeney,1968,True,0,192918.73,agree,divorced
50,Orrie,Reilly,1979,True,2,188906.81,neutral,divorced
51,Sharif,Wuckert,2006,False,1,182474.58,disagree,married
52,Johnnie,Lynch,1962,True,3,50025.81,disagree,married
53,Lular,Crona,1981,False,2,189155.9,disagree,divorced
54,Mollie,Brakus,1959,False,4,46859.13,strongly disagree,widowed
55,Leeann,Johnston,1977,False,3,81952.24,strongly disagree,single
56,Chantelle,Prohaska,1984,False,4,80552.78,disagree,divorced
57,Audie,O'Kon,1941,False,3,125831.81,strongly agree,widowed
58,Alyssia,Olson,1960,False,3,133419.12,strongly agree,divorced
59,Dania,Kuhn,1978,True,2,76658.53,agree,married
60,Tyrone,Paucek,1978,False,2,69115.63,disagree,married
61,Sheena,Franecki,1971,False,1,134539.93,agree,married
62,Maxx,Cormier,1983,True,0,79993.17,disagree,married
63,Adria,Carroll,1995,False,0,54709.57,disagree,single
64,Tarsha,Runte,1957,True,3,187941.7,disagree,married
65,Braeden,Crooks,1973,True,1,89332.54,disagree,married
66,Judi,Jacobi,2006,False,0,89958.19,disagree,married
67,Wood,O'Reilly,1955,False,1,114179.75,agree,divorced
68,Maci,Kohler,1961,True,1,44890.07,strongly disagree,divorced
69,Stanton,Volkman,1982,True,3,186258.61,strongly disagree,married
70,Khalid,Corwin,2002,True,0,76100.19,strongly agree,single
71,Arietta,Leannon,2005,True,0,67569.21,disagree,single
72,Skyla,Renner,1998,True,0,90124.23,disagree,single
73,Karyl,Bernhard,2007,True,4,153016.41,agree,divorced
74,Manley,VonRueden,2005,True,3,134271.07,disagree,married
75,Rueben,Walter,1966,True,0,90276.54,strongly agree,single
76,Hudson,Ward,1961,False,2,69871.65,agree,single
77,Triston,Thiel,1999,True,1,130838.2,agree,widowed
78,Francisco,Kub,2006,True,0,178833.15,agree,single
79,Otha,Mraz,1952,True,2,198123.77,disagree,single
80,Christa,Gibson,1940,True,2,68903.12,strongly disagree,married
81,Stephen,Corkery,1961,False,0,76425.08,disagree,married
82,Willis,Rippin,1989,True,1,186772.31,disagree,single
83,Randle,DuBuque,1986,True,3,118041.92,agree,single
84,Haden,Spencer,1998,True,2,112195.23,strongly agree,single
85,Gilford,Smitham,1949,False,2,186446.0,agree,single
86,Creed,Kozey,1946,False,4,50457.06,strongly agree,single
87,Elianna,Moore,1946,False,4,122003.16,strongly disagree,single
88,Rollin,Hyatt,1966,False,0,148942.08,agree,divorced
89,Debrah,Nikolaus,1978,True,1,123484.78,agree,single
90,Arleth,Stamm,1954,True,0,115489.82,agree,single
91,Germaine,Pfannerstill,1949,True,4,86055.84,strongly agree,married
92,Dawson,Satterfield,1973,True,1,174961.51,strongly disagree,married
93,Jaydin,Marvin,1995,True,0,61556.72,disagree,married
94,Fumiko,Stehr,1962,False,4,180735.05,agree,single
95,Carisa,Hills,1958,False,3,157117.14,agree,married
96,Tameka,Collins,2001,False,1,61518.34,strongly disagree,single
97,Adams,Leuschke,1987,False,0,41784.87,strongly agree,single
98,Earnestine,Gutmann,1985,True,4,79021.46,disagree,widowed
99,Rosa,Runolfsson,1961,True,3,82300.02,strongly agree,single"""

# Read the census data
census = pd.read_csv(StringIO(csv_data), index_col=0)

print("Census data loaded successfully")
print(f"Dataset contains {len(census)} respondents")
print()

# Task 1: Call .head() method to view first five rows
print("Task 1: First five rows of census data")
print("=" * 60)
print(census.head())
print()

# Task 2: Assess variable types from the head output
print("Task 2: Variable Type Assessment")
print("=" * 40)
print("Based on .head() output, here's what we observe:")
print()
print("Variable Analysis:")
print("- first_name: Text/names (should be string/object)")
print("- last_name: Text/names (should be string/object)")
print("- birth_year: Years (should be int, but appears to be object/string)")
print("- voted: Boolean True/False (currently bool)")
print("- num_children: Count/integer (should be int)")
print("- income_year: Decimal values (should be float)")
print("- higher_tax: Categorical responses (should be ordered category)")
print("- marital_status: Categorical status (nominal category)")
print()

# Task 3: Compare with actual data types using .dtypes
print("Task 3: Actual data types using .dtypes")
print("=" * 45)
print(census.dtypes)
print()
print("Key observations:")
print("- birth_year is 'object' (string) instead of int - needs conversion")
print("- higher_tax is 'object' instead of ordered category - needs conversion")
print("- marital_status is 'object' - will need one-hot encoding for ML")
print()

# Task 4: Print unique values of birth_year to identify issues
print("Task 4: Inspecting birth_year unique values")
print("=" * 50)
print("Unique values in birth_year column:")
unique_birth_years = census['birth_year'].unique()
print(unique_birth_years)
print()
print("Issue identified: 'missing' value found in birth_year column")
print("This prevents conversion to integer data type")
print()

# Task 5: Replace missing value with 1967 and verify
print("Task 5: Replacing missing value in birth_year")
print("=" * 50)
print("Before replacement:")
print(f"Unique values: {sorted([str(x) for x in census['birth_year'].unique()])}")
print()

# Replace 'missing' with '1967'
census['birth_year'] = census['birth_year'].replace('missing', '1967')

print("After replacement:")
unique_birth_years_after = census['birth_year'].unique()
print(f"Unique values: {sorted([str(x) for x in unique_birth_years_after])}")
print("Verified: 'missing' has been replaced with '1967'")
print()

# Task 6: Change birth_year datatype to int and verify
print("Task 6: Converting birth_year to integer")
print("=" * 45)
print("Before conversion:")
print(f"birth_year dtype: {census['birth_year'].dtype}")
print()

# Convert to integer
census['birth_year'] = census['birth_year'].astype(int)

print("After conversion:")
print(f"birth_year dtype: {census['birth_year'].dtype}")
print()
print("All data types after birth_year conversion:")
print(census.dtypes)
print()

# Task 7: Calculate average birth year
print("Task 7: Calculating average birth year")
print("=" * 45)
average_birth_year = census['birth_year'].mean()
print(f"Average birth year of respondents: {average_birth_year:.2f}")
print(f"Rounded: {round(average_birth_year)}")
print()

# Task 8: Convert higher_tax to ordered categorical
print("Task 8: Converting higher_tax to ordered category")
print("=" * 55)
print("Before conversion:")
print(f"higher_tax dtype: {census['higher_tax'].dtype}")
print(f"Unique values: {census['higher_tax'].unique()}")
print()

# Define the order for the higher_tax variable
tax_order = ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree']

# Convert to ordered categorical
census['higher_tax'] = pd.Categorical(
    census['higher_tax'],
    categories=tax_order,
    ordered=True
)

print("After conversion to ordered category:")
print(f"higher_tax dtype: {census['higher_tax'].dtype}")
print(f"Is ordered: {census['higher_tax'].cat.ordered}")
print(f"Categories in order: {census['higher_tax'].cat.categories.tolist()}")
print()

# Verify order using .unique()
print("Verification using .unique():")
print(census['higher_tax'].unique())
print()

# Task 9: Label encode higher_tax and find median
print("Task 9: Label encoding higher_tax and finding median")
print("=" * 60)

# Create label encoded version (codes)
census['higher_tax_codes'] = census['higher_tax'].cat.codes

print("Label encoding mapping:")
for i, category in enumerate(tax_order):
    print(f"  {i}: {category}")
print()

# Calculate median
median_tax_sentiment = census['higher_tax_codes'].median()
print(f"Median encoded value: {median_tax_sentiment}")
print(f"This corresponds to: '{tax_order[int(median_tax_sentiment)]}'")
print()

# Task 10: One-Hot Encode marital_status
print("Task 10: One-Hot Encoding marital_status")
print("=" * 50)
print("Before One-Hot Encoding:")
print(f"marital_status dtype: {census['marital_status'].dtype}")
print(f"Unique values: {census['marital_status'].unique()}")
print(f"DataFrame shape: {census.shape}")
print()

# One-Hot Encode marital_status
census = pd.get_dummies(census, columns=['marital_status'], prefix='marital')

print("After One-Hot Encoding:")
print(f"DataFrame shape: {census.shape}")
print()

# List the new dummy variables
marital_columns = [col for col in census.columns if col.startswith('marital_')]
print(f"New marital status columns created: {marital_columns}")
print()

# Show first 5 rows
print("First five rows of updated dataframe (scroll right to see dummy variables):")
print(census.head())
print()

# Task 11: Extra explorations
print("Task 11: Additional Explorations")
print("=" * 40)
print()

# Extra 1: Create marital_codes by label encoding original marital_status
print("EXTRA 1: Creating marital_codes variable")
print("-" * 45)

# Recreate marital_status from dummy variables for encoding
# Find which marital column has value 1 for each row
marital_mapping = {
    'marital_divorced': 'divorced',
    'marital_married': 'married',
    'marital_single': 'single',
    'marital_widowed': 'widowed'
}

# Create marital_status_reconstructed
def get_marital_status(row):
    for col, status in marital_mapping.items():
        if col in census.columns and row[col] == 1:
            return status
    return None

census['marital_status_reconstructed'] = census.apply(get_marital_status, axis=1)

# Convert to categorical and get codes
census['marital_codes'] = pd.Categorical(census['marital_status_reconstructed']).codes

print("Created marital_codes variable:")
print("Sample of first 10 rows:")
print(census[['marital_status_reconstructed', 'marital_codes']].head(10))
print()

# Extra 2: Create age_group variable
print("EXTRA 2: Creating age_group variable")
print("-" * 40)

# Calculate current age (assuming current year is 2024)
current_year = 2024
census['age'] = current_year - census['birth_year']

# Create age groups in 5-year increments
def assign_age_group(age):
    # Create groups: 0-20, 21-25, 26-30, etc.
    if age <= 20:
        return '0-20'
    elif age <= 25:
        return '21-25'
    elif age <= 30:
        return '26-30'
    elif age <= 35:
        return '31-35'
    elif age <= 40:
        return '36-40'
    elif age <= 45:
        return '41-45'
    elif age <= 50:
        return '46-50'
    elif age <= 55:
        return '51-55'
    elif age <= 60:
        return '56-60'
    elif age <= 65:
        return '61-65'
    elif age <= 70:
        return '66-70'
    elif age <= 75:
        return '71-75'
    elif age <= 80:
        return '76-80'
    else:
        return '81+'

census['age_group'] = census['age'].apply(assign_age_group)

print("Age groups created:")
print(census['age_group'].value_counts().sort_index())
print()

# Label encode age_group
age_group_order = ['0-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', 
                   '51-55', '56-60', '61-65', '66-70', '71-75', '76-80', '81+']

census['age_group'] = pd.Categorical(
    census['age_group'],
    categories=age_group_order,
    ordered=True
)

census['age_group_codes'] = census['age_group'].cat.codes

print("Sample of age grouping:")
print(census[['birth_year', 'age', 'age_group', 'age_group_codes']].head(10))
print()

# Final summary and analysis
print("=" * 60)
print("FINAL DATA CLEANING SUMMARY")
print("=" * 60)
print()

print("Transformations completed:")
print("1. Viewed first 5 rows with .head()")
print("2. Assessed variable types from data")
print("3. Compared with actual .dtypes")
print("4. Identified 'missing' value in birth_year")
print("5. Replaced 'missing' with 1967")
print("6. Converted birth_year to int")
print("7. Calculated average birth year: {:.0f}".format(average_birth_year))
print("8. Converted higher_tax to ordered category")
print("9. Label encoded higher_tax, median: {}".format(tax_order[int(median_tax_sentiment)]))
print("10. One-Hot Encoded marital_status")
print("11. Created marital_codes and age_group variables")
print()

print("Final DataFrame structure:")
print(f"Shape: {census.shape}")
print(f"Columns: {len(census.columns)}")
print()

print("Data types summary:")
print(census.dtypes)
print()

print("Dataset is now clean and ready for machine learning analysis!")
print()

# Additional insights
print("BONUS INSIGHTS FROM CLEANED DATA")
print("=" * 35)
print()

print("1. Demographics Summary:")
print(f"   - Age range: {census['age'].min()} to {census['age'].max()} years old")
print(f"   - Average age: {census['age'].mean():.1f} years")
print(f"   - Voter participation rate: {(census['voted'].sum() / len(census) * 100):.1f}%")
print()

print("2. Tax Opinion Distribution:")
for sentiment in tax_order:
    count = (census['higher_tax'] == sentiment).sum()
    pct = (count / len(census)) * 100
    print(f"   - {sentiment}: {count} ({pct:.1f}%)")
print()

print("3. Income Statistics:")
print(f"   - Average income: ${census['income_year'].mean():,.2f}")
print(f"   - Median income: ${census['income_year'].median():,.2f}")
print(f"   - Income range: ${census['income_year'].min():,.2f} - ${census['income_year'].max():,.2f}")
print()

print("All tasks completed successfully!")
print("The census team can now use this cleaned data for analysis and ML models.")
