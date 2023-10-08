import pandas as pd
from datetime import datetime as dt

# pd.read_csv(): Ler dados de arquivos CSV

df =  pd.read_csv('./data/users.csv')

print('------ DATAFRAME ------')
print(df)


print('------ CRIAR COLUNA COM VALOR FIXO ------')
df['process'] = 'data_analysis'
print(df)


print('------ CRIAR COLUNA age_plus_10 somando 10 a idade ------')
df['age_plus_10'] = df['age'] + 10
print(df)


print('------ CRIAR COLUNA fullname ------')
df['fullname'] = df['firstname'] + ' ' + df['lastname']
print(df)


print('------ CRIAR COLUNA COM A DATA HORA ATUAL ------')
df['created_datetime'] = dt.now()
df['created_date'] = dt.today().strftime('%Y-%m-%d')
print(df)