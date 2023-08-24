import mysql.connector
from mysql.connector import Error

with open("currtemp.txt", mode="r", ) as currtemp:
    temperature = currtemp.read()

print(temperature)
tempf = float(temperature)
print(tempf)
temp = int(tempf)
print(temp)

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
        cursor.execute(f"""UPDATE cities 
                           SET temperature ={temp} 
                           WHERE name = 'Ortáše';""")

        cursor.execute("SELECT * FROM cities WHERE name = 'Ortáše'")

        record = cursor.fetchone()
        cursor.execute("SELECT * FROM cities WHERE name = 'Ortáše'")
        record = cursor.fetchone()
        print(record)
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


