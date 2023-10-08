import sqlite3

conn = sqlite3.connect('./databases/test.db')

conn.execute(
    """
        CREATE TABLE IF NOT EXISTS EMPRESA(
            ID INT PRIMARY  KEY       NOT NULL,
            NOME            TEXT      NOT NULL,
            ENDERECO        CHAR(50),
            LIMITE_CREDITO  REAL      NOT NULL
        );
    """)

conn.execute(
    """
        INSERT INTO EMPRESA (ID, NOME, ENDERECO, LIMITE_CREDITO)
        VALUES (1, 'EMPRESA_X', 'BRAZIL', 20000.00 );
    """)

cursor = conn.execute("SELECT id, nome, endereco, limite_credito from EMPRESA;")
for row in cursor:
   print(f"row: {row}")

conn.close()