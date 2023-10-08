# pip install pyarrow

import pandas as pd
import time

# pd.read_parquet(): Ler dados de arquivos PARQUET
# df.to_parquet(): Escrever dados de um dataframe em um arquivo PARQUET

df_orgs = pd.read_csv('./data/organizations-100k.csv')

df_orgs.to_parquet('./data/raw/organizations/organizations-100k.parquet')


# engine
# Use pyarrow ou fastparquet
# O comportamento padrão é tentar pyarrow, caso não esteja disponível, é utilizado fastparquet.

# compression
# Use None para não comprimir os dados.
# Opções de compressão: snappy (padrão), gzip, brotli, lz4, zstd

# storage_options
# pode ser usado para passar argumentos para o armazenamento em núvem, como um bucket S3 na AWS.

(
    df_orgs
    .to_parquet(
        path='./data/raw/organizations_partitioned/',
        engine='pyarrow',
        compression='snappy',
        index=False,
        partition_cols=['Founded']
    )
)


# Lendo dados de um diretório com um arquivo parquet

start_all = time.process_time()
df_all = pd.read_parquet(
    path='./data/raw/organizations/',
)

time_elapsed_all = round( time.process_time() - start_all, 4)
print( df_all.head() )

# Lendo dados de um diretório com um arquivo parquet particionado
# Evitando ler arquivos desnecessários

start_filter = time.process_time()
df_founded_2010 = pd.read_parquet(
    path='./data/raw/organizations_partitioned/',
    engine='pyarrow',
    filters=[('Founded', '==', 2010)]
)
time_elapsed_filter = round( time.process_time() - start_filter, 4)
print( df_founded_2010.head() )

# Melhor modo para ler uma tabela, é não ler ela
# Não de forma completa, mas apenas o necessário

difference_percent = round( (time_elapsed_all / time_elapsed_filter) * 100, 2)
print(f"Diferença de tempo: {difference_percent}%")

# Pense em tabelas com gigabytes, terabytes ou petabytes de dados ...