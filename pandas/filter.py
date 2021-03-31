import pandas as pd

df = pd.read_csv('pandas/datas/covid_19.csv')

df.filter(items= ["Date","Year"])
df.filter(like= "da")
#df.filter(regex=)

print(df.filter(items =["Date"]).head())