import pandas as pd
import datetime

# pd.read_csv(): Ler dados de arquivos CSV

df =  pd.read_csv('./data/users.csv')

print('------ DATAFRAME ------')
print(df)



print('------ AGRUPAR DATAFRAME POR profession E CALCULAR IDADE MEDIA, MIN, MAX E QUANTIDADE ------')
df_group = (
    df
    .groupby('profession')
    .agg(
        count_age=('age', 'count'),
        avg_age=('age', 'mean'),
        max_age=('age', 'max'),
        min_age=('age', 'min')
    )
)
print(df_group)

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html