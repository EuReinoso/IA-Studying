import pandas as pd
import matplotlib.pyplot
from tabulate import tabulate

df = pd.read_csv('pandas/datas/entradas_breast.csv',header=0,  nrows=10)

print(df)