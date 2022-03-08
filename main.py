import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='db_name',
                                         user='root',
                                         password='')

    sql_select_Query = "select * from table_name"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Employee ID = ", row[1])
        print("Name  = ", row[2] +" "+ row[3])
        print("Department ID  = ", row[4])
        print("Salary  = ", row[5], "\n")

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
