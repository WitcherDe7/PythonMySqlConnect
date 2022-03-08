# Install Mysql Connector
 ``pip install mysql-connector-python``
 
 # Import Mysql Connector
 ```
 import mysql.connector
 ```
 # Define Database Connection
 ```
 try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mycompany',
                                         user='root',
                                         password='')
 ```
 # Select Data from Table => Database
 ```
 sql_select_Query = "select * from employees"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
```
