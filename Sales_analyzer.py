
import pandas as pd

# Sample sales data
data = {
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor",
        "Laptop", "Mouse", "Keyboard", "Monitor"
    ],
    "Category": [
        "Electronics", "Accessories", "Accessories", "Electronics",
        "Electronics", "Accessories", "Accessories", "Electronics"
    ],
    "Price": [55000, 800, 1500, 12000, 55000, 800, 1500, 12000],
    "Quantity": [2, 10, 5, 3, 1, 8, 4, 2],
    "Cost": [45000, 500, 1000, 9000, 45000, 500, 1000, 9000]
}

df = pd.DataFrame(data)

# Calculate revenue and profit
df["Revenue"] = df["Price"] * df["Quantity"]
df["Profit"] = (df["Price"] - df["Cost"]) * df["Quantity"]

print("\n===== SALES DATA =====")
print(df.to_string(index=False))

# Overall analysis
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
total_units = df["Quantity"].sum()

print("\n===== BUSINESS SUMMARY =====")
print(f"Total Revenue: Rs. {total_revenue:,.2f}")
print(f"Total Profit: Rs. {total_profit:,.2f}")
print(f"Units Sold: {total_units}")

# Product-wise analysis
product_sales = df.groupby("Product")["Revenue"].sum()
top_product = product_sales.idxmax()

print("\n===== PRODUCT ANALYSIS =====")
print(product_sales.sort_values(ascending=False))
print(f"\nTop Revenue Product: {top_product}")

# Category-wise analysis
category_sales = df.groupby("Category")["Revenue"].sum()

print("\n===== CATEGORY ANALYSIS =====")
print(category_sales.sort_values(ascending=False))

# Save report
df.to_csv("sales_analysis_report.csv", index=False)

print("\nReport saved to sales_analysis_report.csv")
