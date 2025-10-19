#!/usr/bin/env python3
"""
MySQLServer.py
This script connects to a MySQL server and creates the database 'alx_book_store'.
If the database already exists, it will not raise an error.
"""

import mysql.connector
from mysql.connector import Error

# Connect to MySQL server (update credentials as needed)
try:
    connection = mysql.connector.connect (
    user='backend',
    host="localhost",
    password="Week8_AlxDB@Into123!"
    )
    if connection.is_connected():
        print("Successfully connected to MySQL server")
        cursor = connection.cursor()
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Ensure cursor and connection are properly closed
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")