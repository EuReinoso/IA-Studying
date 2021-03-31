import pandas as pd

df = pd.read_csv("pandas/datas/business.csv")

df_test = df.iloc[0:6,0:4]

#crescente
print(df_test.sort_values("Period"))

#decrescente
print(df_test.sort_values("Period",ascending = False))

