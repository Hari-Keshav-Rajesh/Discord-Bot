import os
from dotenv import load_dotenv

import mysql.connector
from mysql.connector import Error

load_dotenv()
password_mysql = os.getenv('password_mysql')

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password_mysql,
        database="test"
    )

    if connection.is_connected():
        print("Connected to MySQL database")
except Error as e:
    print(f"Error: {e}")

'''
File to declare the SQL connection
'''