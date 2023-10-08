import sqlite3
import pandas as pd

conn = sqlite3.connect('./databases/northwind.db')

print('\n------ BUSCAR TODAS AS TABELAS DA BASE SQLITE ------')

query = """
   SELECT name 
     FROM sqlite_master
    WHERE type='table';
   """

df_all_tables = pd.read_sql_query(query, conn)
print(df_all_tables.head())



print('\n------ SELECT COLS ------')
query_cols = """
   SELECT OrderID,
          CustomerID,
          OrderDate,
          ShipCity
     FROM Orders
    ORDER by OrderDate desc
    LIMIT 5;
"""

df_recent_orders = pd.read_sql_query(query_cols, conn)
print(df_recent_orders)



print('\n------ SAVE TO DB ------')
query_all_orders = """
   SELECT *
     FROM Orders
"""

df_all_orders = pd.read_sql_query(query_all_orders, conn)
df_all_orders_by_city = (
   df_all_orders
   .groupby('ShipCity')
    .agg(
        count_orders=('OrderID', 'count')
    )
    .sort_values('count_orders', ascending=False)
)

df_all_orders_by_city.to_sql('OrdersByCityCount', conn, if_exists='replace')
print("Saved to DB!")



print('\n------ GET ANALYSIS FROM DB ------')
query_analysis = """
   SELECT * 
     FROM OrdersByCityCount
   """

df_orders_analysis = pd.read_sql_query(query_analysis, conn)
print(df_orders_analysis.head())