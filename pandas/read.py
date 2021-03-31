import pandas as pd

df_csv = pd.read_csv('pandas/datas/entradas_breast.csv',header=0,  nrows=10)

df_excel = pd.read_excel('pandas/datas/investment_household.xlsx')

print(df_excel)