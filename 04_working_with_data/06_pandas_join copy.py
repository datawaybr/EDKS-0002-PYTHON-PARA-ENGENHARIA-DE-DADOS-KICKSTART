import pandas as pd

# pd.read_csv(): Ler dados de arquivos CSV

df_users =  pd.read_csv('./data/users.csv')
df_users_status =  pd.read_csv('./data/users_status.csv')

print('------ DATAFRAME USERS ------')
print(df_users)

print('------ DATAFRAME USERS STATUS ------')
print(df_users_status)


# pd.merge() pode ser usado tanto para juntar DataFrames em suas colunas quanto em seus índices.
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html

# df.join() só pode ser usado para juntar DataFrames em seus índices ou coluna chave.
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join

print('------ REALIZAR UM INNER JOIN ENTRE OS DOIS DATAFRAMES PELA COLUNA id ------')
df_inner_join = pd.merge(df_users, df_users_status, on='id', how='inner')
print(df_inner_join)


print('------ REALIZAR UM LEFT JOIN ENTRE OS DOIS DATAFRAMES PELA COLUNA id ------')
df_left_join = pd.merge(df_users, df_users_status, on='id', how='left')
print(df_left_join)

#print('------ REALIZAR UM JOIN ENTRE OS DOIS DATAFRAMES POR MULTIPLAS COLUNAS ------')
#merged_df = pd.merge(df1, df2, left_on=['ID1', 'Name1'], right_on=['ID2', 'Name2'], how='inner')

