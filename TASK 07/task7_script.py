
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Walmart_Sales.csv")

# Simulate quantity sold (assuming avg price = $20)
df['quantity'] = (df['Weekly_Sales'] / 20).astype(int)

# Create SQLite DB and insert data
conn = sqlite3.connect("sales_data.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

# Run SQL query
query = """
SELECT 
    Store, 
    SUM(quantity) AS total_quantity, 
    SUM(Weekly_Sales) AS total_revenue
FROM sales
GROUP BY Store
ORDER BY Store;
"""
summary_df = pd.read_sql_query(query, conn)
conn.close()

# Display result
print(summary_df)

# Plot revenue per store
plt.figure(figsize=(12, 6))
plt.bar(summary_df['Store'].astype(str), summary_df['total_revenue'], color='skyblue')
plt.title("Total Revenue by Store")
plt.xlabel("Store")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
