import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
port = os.environ.get("PORT")
database = os.environ.get("DATABASE")

def create_table(table, columns):
    try:
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        cur = conn.cursor()
        cur.execute(f'CREATE TABLE IF NOT EXISTS {table} {columns};')
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False

create_table(table='Users',
    columns="""(id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255),
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")

def insert_data(insert_query, data):
    try:
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        cur = conn.cursor()
        cur.execute(insert_query, data)
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False
    
def get_data(query):
    try:
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        conn.close()
        return data
    except mysql.connector.Error as err:
        print("Error:", err)
        return False
    
def update_data(update_query, data):
    try:
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        cur = conn.cursor()
        cur.execute(update_query, data)
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False
    