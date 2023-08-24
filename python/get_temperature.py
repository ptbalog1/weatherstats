import json
import requests
import mysql.connector
from mysql.connector import Error

account_sid = "AC3b5221bb5596629972b2b6ae4aa544dd"
auth_token = "07bce56806894bfe5e1a4ef87af2ba4d"


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

        cursor.execute("SELECT name,stormdays,lat,lon FROM cities")
        record = cursor.fetchall()
        print(record)
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")




for location in record:
    NAME = location[0]
    STORMDAYS = location[1]
    MY_LAT = location[2]
    MY_LNG = location[3]
    api_key = "5db25b6161b0a4675d5ab518684e4b33"
    units = "metric"
    API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"



    parameters = {
        "lat": MY_LAT,
        "lon": MY_LNG,
        "appid": api_key,
        "units": units
    }


    response = requests.get(API_ENDPOINT, params=parameters)
    response.raise_for_status()
    weather_data = response.json()
    temperature = weather_data["main"]["temp"]
    curr_weather = weather_data["weather"][0]["main"]
    print(curr_weather)
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

            if curr_weather == "Thunderstorm":

                STORMDAYS += 1
                cursor.execute(f"""UPDATE cities 
                                                       SET stormdays ={STORMDAYS} 
                                                       WHERE name = '{NAME}';""")
                connection.commit()

            cursor.execute(f"""UPDATE cities 
                                       SET temperature ={temperature} 
                                       WHERE name = '{NAME}';""")
            cursor.execute(f"""UPDATE cities 
                                            SET actualweather ='{curr_weather}' 
                                            WHERE name = '{NAME}';""")
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")





#CONNECT TO DB
#GET LOCATION NAME - DONE
#GET LAT AND LONG VIA API BASED ON LOCATION NAME
#GET TEMPERATURE DATA VIA OPEN WEATHER API AND INSERT IT INTO DB
#NOTE SUNNY DAYS,RAIN, STORMS, SNOWING