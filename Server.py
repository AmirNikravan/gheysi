import psycopg2
from psycopg2 import Error
import json
import datetime

class Server:
    def __init__(self):
        self.dbname = 'derafsh'
        self.user = 'admin'
        self.password = 'admin'
        self.host = 'localhost'  # Corrected typo
        self.port = '5432'
        self.connection = None

    def collect(self, data):
        try:
            self.connect()
            self.insert_data('sensors', datetime.datetime.now(), data)

        except Exception as e:
            print(f"Error collecting data: {e}")
        finally:
            self.disconnect()

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connected to the database.")
        except Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    def insert_data(self, table, datetime_value, dictionary_value):
        if not self.connection:
            raise psycopg2.OperationalError('Database connection is closed.')
        
        try:
            cursor = self.connection.cursor()
            # Convert dictionary_value to JSON string
            json_data = json.dumps(dictionary_value)
            query = f"INSERT INTO {table} (date, value) VALUES (%s, %s::jsonb)"
            cursor.execute(query, (datetime_value, json_data))
            self.connection.commit()
            print("Data inserted successfully.")
        except Error as e:
            print(f"Error inserting data: {e}")
            self.connection.rollback()
            raise



    def receive_data(self, table):
        self.connect()
        if not self.connection:
            raise psycopg2.OperationalError('Database connection is closed.')

        try:
            cursor = self.connection.cursor()
            
            # Modify the SQL query to select the last row ordered by a specific column
            query = f"SELECT * FROM {table} ORDER BY id DESC LIMIT 1"
            
            cursor.execute(query)
            record = cursor.fetchone()  # Fetch the first (and only) row
            return record
        except Error as e:
            print(f"Error receiving data: {e}")
            raise


    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database.")

