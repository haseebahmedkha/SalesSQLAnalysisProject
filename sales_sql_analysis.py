import sqlite3
#coonect to the database
conn = sqlite3.connect('sales_data.db')
# Create a cursor object using the connection and execute a query
cursor = conn.cursor()

# Create a table for sales data if it doesn't exist
cursor.execute('''
               CREATE TABLE IF NOT EXISTS sales (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT,
               product TEXT,
               category TEXT,
               quantity INTEGER,
               price REAL,)
               ''')

# Insert sample data into the sales table
sample_data = [('2023-01-01', 'Product A', 'Category 1', 10, 15.99),
               ('2023-01-02', 'Product B', 'Category 2', 5, 25.50),
               ('2023-01-03', 'Product A', 'Category 1', 8, 15.99),
               ('2023-01-04', 'Product C', 'Category 3', 12, 10.00),
               ('2023-01-05', 'Product B', 'Category 2', 7, 25.50),
               ('2023-01-06', 'Product A', 'Category 1', 6, 15.99),
               ('2023-01-07', 'Product C', 'Category 3', 4, 10.00),
               ('2023-01-08', 'Product B', 'Category 2', 9, 25.50),
               ('2023-01-09', 'Product A', 'Category 1', 11, 15.99),
               ('2023-01-10', 'Product C', 'Category 3', 5, 10.00)]

# Insert sample data into the sales table
cursor.executemany('''INSERT INTO sales_data (date, product, category, quantity, price) Values (?, ?, ?, ?, ?)''', sample_data)
# Commit the changes to the database
conn.commit()
# Query to get total sales for each product
conn.close()

print("database created and sample data inserted successfully.")
