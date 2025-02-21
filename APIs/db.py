# database configuration file
import mysql.connector

# Database config that i have on phpMyAdmin
dbConfig = {
    "host": "localhost",
    "user": "root",
    "password": "King#123",
    "database": "myDBUsingFlask"
}

# Function that will connect to database in phpMyAdmin


def connectTodatabase():
    try:
        conn = mysql.connector.connect(**dbConfig)
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


# Test the connection when the script runs
conn = connectTodatabase()
if conn:
    print("Databse connected successfully.....!")
    conn.close()
