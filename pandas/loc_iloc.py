import pandas as pd

df = pd.read_csv('pandas/datas/business.csv',header=0,  nrows=10)

#loc
df.loc[0:3]
df_test = df.loc[0:5,"Series_reference":"Data_value"]

#print(df.loc[0:3,"Series_reference":"Data_value"])

#iloc
df_test1 = df.iloc[0:5,0:5]
df_test1 = df.iloc[0:5,[0,2,4]]

print(df_test1)