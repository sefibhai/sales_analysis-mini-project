sales_data = {
    "Date": [
        "2024-01-01","2024-01-01","2024-01-02","2024-01-02","2024-01-03",
        "2024-01-03","2024-01-04","2024-01-04","2024-01-05","2024-01-05"
    ],
    "Product": [
        "Notebook","Pencil","Notebook","Eraser","Pen",
        "Notebook","Marker","Highlighter","Notebook","Pencil"
    ],
    "Units_Sold": [10, 25, 5, 12, 20, 7, 15, 9, 11, 30],
    "Unit_Price": [3.5, 1.0, 3.5, 0.5, 2.0, 3.5, 1.5, 2.0, 3.5, 1.0],
    "Revenue": [35, 25, 17.5, 6, 40, 24.5, 22.5, 18, 38.5, 30]
}
import pandas as pd

df = pd.DataFrame(sales_data)

df.to_csv("sales_data.csv", index=False)


import matplotlib.pyplot as plt

plt.plot(df["Date"], df["Revenue"])
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title("Daily Revenue Trend")
plt.xticks(rotation=45)
plt.show()


product_sales = df.groupby("Product")["Units_Sold"].sum()

plt.bar(product_sales.index, product_sales.values)
plt.xlabel("Product")
plt.ylabel("Total Units Sold")
plt.title("Units Sold per Product")
plt.show()


product_revenue = df.groupby("Product")["Revenue"].sum()

plt.bar(product_revenue.index, product_revenue.values)
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Revenue per Product")
plt.show()


plt.savefig("revenue_plot.png")
