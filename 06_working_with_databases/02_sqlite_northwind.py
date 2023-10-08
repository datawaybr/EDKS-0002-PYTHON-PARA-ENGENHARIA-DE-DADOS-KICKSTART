import sqlite3
from pprint import pprint

conn = sqlite3.connect('./databases/sqlite/northwind.db')


print('------ BUSCAR TODAS AS TABELAS DA BASE SQLITE ------')
cursor = conn.execute("""
   SELECT name 
     FROM sqlite_master
    WHERE type='table';
   """
)
tables = cursor.fetchall()
print(tables)


print('\n------ BUSCAR SCHEMA DE UMA TABELA ------')
cursor = conn.execute("""
   SELECT sql
     FROM sqlite_master
    WHERE type = 'table' 
      AND name = 'Orders'
   """
)
orders_schema = cursor.fetchall()
pprint(orders_schema)


cursor = conn.execute("SELECT * from Orders limit 5;")
for row in cursor:
   print(f"row: {row}")



print('\n------ SELECT COLS ------')
cursor = conn.execute("""
   SELECT OrderID,
          CustomerID,
          OrderDate
     from Orders
    limit 5;
   """)

for row in cursor:
   print(f"row: {row}")



conn.close()