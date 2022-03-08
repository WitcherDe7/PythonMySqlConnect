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
 # Select Data from Table => Database
 ```python
 sql_select_Query = "select * from employees"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
```
