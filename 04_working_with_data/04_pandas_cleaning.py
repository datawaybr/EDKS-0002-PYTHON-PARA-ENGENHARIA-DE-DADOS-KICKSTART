import pandas as pd

# pd.read_csv(): Ler dados de arquivos CSV

df =  pd.read_csv('./data/users.csv')

print('------ DATAFRAME ------')
print(df)


print('------ FILTAR REGISTROS SEM IDADE ------')
df_age_null = df[df['age'].isnull()]
print(df_age_null)


print('------ REMOVER REGISTROS SEM IDADE ------')
df_drop_na = df.dropna(subset=['age'])
print(df_drop_na)


print('------ PREENCHER REGISTROS SEM IDADE APENAS NA COLUNA age COM MEDIA ------')
df_fill_na = df.fillna({'age': round( df['age'].mean(), 2) })
print(df_fill_na)


print('------ RENOMEAR A COLUNA profession PARA occupation ------')
df_rename = df.rename(columns={'profession': 'occupation'})
print(df_rename.head())