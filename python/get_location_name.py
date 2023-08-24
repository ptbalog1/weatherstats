import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='weather',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)



except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():

        cursor.execute("SELECT name FROM cities")
        record = cursor.fetchall()
        print(record)
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


with open("all_names.txt", mode="w", ) as all_names:
    for name in range(0, len(record)):
        all_names.write(record[name][0])
        all_names.write("\n")
