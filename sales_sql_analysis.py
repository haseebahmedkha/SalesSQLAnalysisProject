# Import necessary libraries
import sqlite3
import pandas as pd
import pymysql
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import matplotlib.pyplot as plt
import seaborn as sns


username = 'root'
password = quote_plus('Chodrykhan@880')
host = 'localhost'
port = '3306'
database = 'sales_data'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

#list all tables in the database
print("list of tables in the database")
query = "SHOW TABLES;"
df = pd.read_sql(query, engine)
print(df)

print("\n====================")


print("list of data in the products table")
query = "select * from products;"
df = pd.read_sql(query, engine)
print(df)

print("\n====================")


print("Table structure of the products table")
#describe the table structure
columns_df = pd.read_sql("DESCRIBE products;", engine)
print(columns_df)


print("\n====================")




#performing analysis on the sales table
print("Sales data analysis as per products")
query = "select name, sum(quantity) as total_sale from products group by name  order by total_sale desc limit 5"
df = pd.read_sql(query, engine)
print(df)
print("\n====================")



#Analyse data from the sales table as BAR chart
plt.figure(figsize=(12,6))
sns.barplot(x='name', y='total_sale', data=df, palette='mako')
plt.title(('Quantity in Stock per Product'))
plt.xlabel('Name of Products')
plt.ylabel('Quantity of Products')
plt.tight_layout()
plt.savefig('quantity_in_stock_per_product.png')
plt.show()


# Analyzing the sales data using Pie Chart (Product Category)
query = "select name, count(*) as count from products group by name;"
df = pd.read_sql(query, engine)

#Shows data on Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(df['count'], labels=df['name'], autopct='%1.1f%%', startangle=140)
plt.title('Product Category Distribution')
plt.tight_layout()
plt.savefig('product_category_distribution.png')
plt.show()
plt.close()



























# #coonect to the database
# conn = sqlite3.connect('sales_data.db')
# # Create a cursor object using the connection and execute a query   
# cursor = conn.cursor()

# # Create a table for sales data if it doesn't exist
# cursor.execute('''
#                CREATE TABLE IF NOT EXISTS sales (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                date TEXT,
#                product TEXT,
#                category TEXT,
#                quantity INTEGER,
#                price REAL)
#                ''')

# # Insert sample data into the sales table
# sample_data = [('2023-01-01', 'Product A', 'Category 1', 10, 15.99),
#                ('2023-01-02', 'Product B', 'Category 2', 5, 25.50),
#                ('2023-01-03', 'Product A', 'Category 1', 8, 15.99),
#                ('2023-01-04', 'Product C', 'Category 3', 12, 10.00),
#                ('2023-01-05', 'Product B', 'Category 2', 7, 25.50),
#                ('2023-01-06', 'Product A', 'Category 1', 6, 15.99),
#                ('2023-01-07', 'Product C', 'Category 3', 4, 10.00),
#                ('2023-01-08', 'Product B', 'Category 2', 9, 25.50),
#                ('2023-01-09', 'Product A', 'Category 1', 11, 15.99),
#                ('2023-01-10', 'Product C', 'Category 3', 5, 10.00)]

# # Insert sample data into the sales table
# cursor.executemany('''INSERT INTO sales (date, product, category, quantity, price) Values (?, ?, ?, ?, ?)''', sample_data)
# # Commit the changes to the database
# conn.commit()
# # Query to get total sales for each product
# conn.close()

# print("database created and sample data inserted successfully.")


