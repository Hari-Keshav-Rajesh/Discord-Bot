import mysql.connector
from mysql.connector import Error

from apikeys import password_mysql

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