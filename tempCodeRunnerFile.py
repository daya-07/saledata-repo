import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("sample_sales_data.xlsx")
df = pd.DataFrame(data)

print(df)