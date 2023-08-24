import json
import requests
import mysql.connector
from mysql.connector import Error



with open("all_names.txt", mode="r", ) as all_names:
    all_names = all_names.readlines()

account_sid = "AC3b5221bb5596629972b2b6ae4aa544dd"
auth_token = "07bce56806894bfe5e1a4ef87af2ba4d"

print(all_names[0])
for name in all_names:

    CITY = name
    api_key = "5db25b6161b0a4675d5ab518684e4b33"
    API_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"

    parameters = {
        "q": CITY,
        "appid": api_key,
    }

    response = requests.get(API_ENDPOINT, params=parameters)
    response.raise_for_status()
    loaction_data = response.json()

    NAME = loaction_data[0]["name"]
    LAT = loaction_data[0]["lat"]
    LON = loaction_data[0]["lon"]

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
                                       SET lat ={LAT} 
                                       WHERE name = '{NAME}';""")
            cursor.execute(f"""UPDATE cities 
                                               SET lon ={LON} 
                                               WHERE name = '{NAME}';""")
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

