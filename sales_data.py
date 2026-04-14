import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("sample_sales_data.xlsx")
df = pd.DataFrame(data)

print(df)

#Comparison of Totals in different regions
plt.bar(df["Region"], df["Total"])
plt.title("Total vs Region")
plt.show()

#Comparison of Totals between each category
x = df.groupby("Category").sum("Total")
# print(x["Total"])
plt.pie(x=x["Total"], labels=np.unique(df["Category"]), colors=['Pink', 'Grey', 'beige'])
plt.title("Category vs Total")
plt.show()

#Comparison of Total between each product
plt.pie(x=df["Total"], labels=df["Product"])
plt.title("Product vs Total")
plt.show()

#Sale Trend over the month
plt.plot(df["Date"], df["Total"])
plt.title("Total vs Date")
plt.show()

# Average sale
avg = df["Total"].mean()
print("Average Sales: ", avg)

# #Top buyer
max_sale = max(df["Total"])
ind = df.index[df["Total"] == max_sale]
print("Top Customer: ", df["Customer"][1])
print("Amount: ", max_sale)
