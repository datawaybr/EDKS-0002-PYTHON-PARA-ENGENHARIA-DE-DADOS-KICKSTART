import pandas as pd
from datetime import datetime as dt

# pd.read_csv(): Ler dados de arquivos CSV

df_users =  pd.read_csv('./data/users.csv')


# Criando coluna com datahora de processamento
df_users['created_datetime'] = dt.now()


# Salvando arquivo em formato CSV
df_users.to_csv('./data/raw/csv/users.csv', index=False)


# Salvando arquivo em formato JSON
df_users.to_json('./data/raw/json/users.json', orient='records')

