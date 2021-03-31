import pandas as pd

df = pd.read_csv("pandas/datas/covid_19.csv")

df[(df.Year == 2018)].head()
#df[(df.Year == 2015) and (df.Direction == Exports)]

print(df[(df.Year == 2015)]["Direction"].head())