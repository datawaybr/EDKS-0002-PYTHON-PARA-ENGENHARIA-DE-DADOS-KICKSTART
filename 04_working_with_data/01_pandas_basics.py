import pandas as pd

# pd.read_csv(): Ler dados de arquivos CSV
# pd.read_excel(): Ler dados de arquivos EXCEL
# pd.read_json(): Ler dados de um arquivo JSON
# pd.read_sql(): Ler dados de uma base SQL

# df.to_csv(): Escrever dados de um dataframe em um arquivo CSV
# df.to_excel(): Escrever dados de um dataframe em um arquivo EXCEL
# df.to_sql(): Escrever dados de um dataframe em uma base SQL
# df.to_json(): Escrever dados de um dataframe em um arquivo JSON

dataframe = pd.read_csv('./data/users.csv')
df = dataframe

print('------ TIPO ------')
print(type(df))

print('------ DATAFRAME ------')
print(df)

print('------ DATAFRAME DESCRIBE ------')
print(df.describe())

print('------ DATAFRAME HEAD ------')
print(df.head())

print('------ DATAFRAME COLUMNS ------')
print(df.columns)
