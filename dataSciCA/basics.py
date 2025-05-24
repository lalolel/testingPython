import codecademylib3_seaborn  # Import Codecademy's custom library for visualizations (specific to their platform)
import pandas as pd  # Import Pandas for working with dataframes
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
import seaborn as sns  # Import Seaborn for statistical visualization

# Step 1: Read the CSV files and create Pandas DataFrames
user_data = pd.read_csv("user_data.csv")  # Reads user data from 'user_data.csv'
pop_data = pd.read_csv("pop_data.csv")  # Reads population data from 'pop_data.csv'

# Step 2: Print the first 15 rows of user_data for inspection
print(user_data.head(15))  # Displays the first 15 rows of user_data to check the structure

# Step 3: Merge user_data and pop_data DataFrames
new_df = pd.merge(user_data, pop_data)  # Combines the two DataFrames based on a common column
print(new_df.head(15))  # Prints the first 15 rows of the merged DataFrame to verify the merge

# Step 4: Categorize locations based on population size
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"  # Assigns 'rural' to locations with population below 100,000
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"  # Assigns 'urban' to locations with population 100,000 or above

# Step 5: Print the updated DataFrame with location classification
print(new_df.head(15))  # Displays the updated DataFrame to see the newly assigned 'location' column

# Paste histogram code:
age = new_df["age"]
sns.displot(age)
plt.show()

# Paste mean age location code:
location_mean_age = new_df.groupby("location").age.mean()
print(location_mean_age)

# Paste barplot code:
plt.close()
sns.barplot(
    data=new_df,
    x= "location",
   	y= "age"
)
plt.show()

# Paste violinplot code:
plt.close()
sns.violinplot(data=new_df, x="location", y="age") 
plt.show()
