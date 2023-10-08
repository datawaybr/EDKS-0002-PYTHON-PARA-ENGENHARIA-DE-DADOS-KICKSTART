import sqlite3

conn = sqlite3.connect('./databases/test.db')


cursor = conn.execute("SELECT * from EMPRESA;")
for row in cursor:
   print(f"row: {row}")


cursor = conn.execute("SELECT id, nome, limite_credito from EMPRESA;")
for row in cursor:
   print(f"row: {row}")

conn.close()