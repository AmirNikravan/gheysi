import psycopg2
from psycopg2 import Error
import datetime

class Server:
    def __init__(self):
        self.dbname = 'derafsh'
        self.user = 'admin'
        self.password = 'admin'
        self.host = 'localhost'
        self.port = '5432'
        self.connection = None

    def collect(self, data):
        try:
            self.connect()
            self.insert_data('sensors',  datetime.datetime.now(), data)
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

    def insert_data(self, table, date_value, dictionary_value):
        if not self.connection:
            raise psycopg2.OperationalError('Database connection is closed.')
        
        try:
            cursor = self.connection.cursor()

            # Convert dictionary_value to string representation
            data_string = str(dictionary_value)

            query = f"INSERT INTO {table} (date, value) VALUES (%s, %s)"
            cursor.execute(query, (date_value, data_string))
            self.connection.commit()
            print("Data inserted successfully.")
        except Error as e:
            print(f"Error inserting data: {e}")
            self.connection.rollback()
            raise

    def receive_data(self, query):
        if not self.connection:
            raise psycopg2.OperationalError('Database connection is closed.')

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Error as e:
            print(f"Error receiving data: {e}")
            raise

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database.")

# Example usage:
if __name__ == "__main__":
    try:
        server = Server()

        # Example of collecting data
        data_to_insert = {"temperature": 25, "humidity": 60}
        server.collect(data_to_insert)

        # Example of receiving data
        query = "SELECT * FROM sensors"
        result = server.receive_data(query)
        print("Received data:", result)

    except Exception as e:
        print(f"Error: {e}")
