# Install Mysql Connector
 ``pip install mysql-connector-python``
 
 # Import Mysql Connector
 ```python
 import mysql.connector
 ```
 # Define Database Connection
 ```python
 try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mycompany',
                                         user='root',
                                         password='')
 ```
 # Select Data from mysql database Table
 ```python
 sql_select_Query = "select * from db_table"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
```
# Fetch Data
```python
for row in records:
        print("Id = ", row[0], )
        print("Employee ID = ", row[1])
        print("Name  = ", row[2] +" "+ row[3])
        print("Department ID  = ", row[4])
        print("Salary  = ", row[5], "\n")
```
