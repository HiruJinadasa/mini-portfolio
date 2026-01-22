# customer_analysis.py
# Beginner-friendly Data Science project: Customer Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample customer dataset
data = {
    "CustomerID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [25, 34, 28, 45, 52, 23, 37, 31],
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Male", "Female"],
    "Annual_Spend($)": [500, 700, 300, 1200, 1500, 400, 900, 650],
    "Visits_Per_Year": [5, 7, 3, 12, 15, 4, 9, 6]
}

df = pd.DataFrame(data)

# Show first rows
print("First 5 rows of the dataset:")
print(df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Average spend by gender
avg_spend_gender = df.groupby("Gender")["Annual_Spend($)"].mean()
print("\nAverage Annual Spend by Gender:")
print(avg_spend_gender)

# Visualize Age vs Annual Spend
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="Age", y="Annual_Spend($)", hue="Gender")
plt.title("Age vs Annual Spend by Gender")
plt.show()

# Visualize Visits per Year distribution
plt.figure(figsize=(6,4))
sns.histplot(df["Visits_Per_Year"], bins=5, kde=False)
plt.title("Distribution of Visits Per Year")
plt.xlabel("Visits Per Year")
plt.ylabel("Number of Customers")
plt.show()
