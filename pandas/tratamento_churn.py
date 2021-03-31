import pandas as pd

#lendo o dataframe
df = pd.read_csv("pandas/datas/Churn.csv",sep=';')

#Renomeando as colunas
df.columns = ["Id","Score","Estado","Gênero","Idade","Patrimonio","Saldo","Produtos","TemCartãoCredito","Ativo","Salario","Saiu"]

agrupado = df.groupby(["Estado"]).size()
print(agrupado)
