import pandas as pd

data = pd.read_excel("sample_sales_data.xlsx")
df = pd.DataFrame(data)

print(df)
