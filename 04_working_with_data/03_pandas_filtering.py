import pandas as pd

# pd.read_csv(): Ler dados de arquivos CSV

df =  pd.read_csv('./data/users.csv')

print('------ DATAFRAME ------')
print(df)


print('------ APENAS ALGUMAS COLUNAS ------')
df_cols = df[['firstname', 'email', 'age']]
print(df_cols)


print('------ IDADE MAIOR QUE 30 ------')
df_30_plus = df[df['age'] > 30]
print(df_30_plus)


print('------ IDADE MAIOR QUE 30 E PROFISSÃO = firefighter ------')
#df_30_plus = df[(df['age'] > 30) & (df['profession'] == 'firefighter')]

df_30_plus = (
    df[
        ( df['age'] > 30 )
        & 
        ( df['profession'] == 'firefighter' )
    ]
)
print(df_30_plus)

print('------ EMAIL ou EMAIL2 COM.BR ------')
df_email_br = (
    df[
        ( df['email'].str.contains('com.br') )
        | 
        ( df['email2'].str.contains('com.br') )
    ]
)
print(df_email_br)