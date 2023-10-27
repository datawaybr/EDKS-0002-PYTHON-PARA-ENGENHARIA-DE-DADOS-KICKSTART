# !pip install psycopg2-binary

import psycopg2

# Criar a conexão
conn = psycopg2.connect(
    host='host.docker.internal',
    user='postgres',
    port=5432,
    password='postgres',
    dbname='postgres'
)

# Criar um cursor
cur = conn.cursor()

# Executar o SQL
cur.execute("SELECT * FROM public.orders LIMIT 10;")

# Buscar os resultados
result = cur.fetchall()

# Mostrar cada registro
for record in result:
    print(record)

# Encerrar cursor e conexão
cur.close()
conn.close()