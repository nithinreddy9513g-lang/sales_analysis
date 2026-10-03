import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["Unit_Price"]

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Extract month
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

# Calculate monthly revenue
monthly_revenue = df.groupby("Month")["Revenue"].sum()

print("\nMonthly Revenue:")
print(monthly_revenue)

# Calculate revenue by product
product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Product:")
print(product_revenue)

# Calculate revenue by category
category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Category:")
print(category_revenue)

# Calculate revenue by region
region_revenue = (
    df.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Region:")
print(region_revenue)

# Monthly revenue chart
plt.figure(figsize=(9, 5))

monthly_revenue.plot(kind="bar")

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("monthly_revenue.png")

plt.show()

# Product revenue chart
plt.figure(figsize=(9, 5))

sns.barplot(
    x=product_revenue.index,
    y=product_revenue.values
)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("product_revenue.png")

plt.show()