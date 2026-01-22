# sales_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    "Region": ["North", "South", "East", "West"],
    "Sales": [2500, 4000, 3000, 3500]
}

df = pd.DataFrame(data)

# Calculate total sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Create a bar chart
df.plot(kind="bar", x="Region", y="Sales", title="Sales by Region")
plt.show()
