import psycopg2
from datetime import date

# Database connection details
HOST = "localhost"
PORT = 5432
DATABASE = "derafsh"
USER = "admin"  # Replace with your actual username
PASSWORD = "admin"  # Replace with your actual password

def save_data_to_db(name):
  """Saves the current date and name to a PostgreSQL database table.

  Args:
      name: The name to be saved (string).
  """
  try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(host=HOST, port=PORT, dbname=DATABASE, user=USER, password=PASSWORD)

    # Create a cursor object
    cur = conn.cursor()

    # Get today's date
    today = date.today().strftime('%Y-%m-%d')  # Format date as YYYY-MM-DD

    # Construct the SQL INSERT statement
    sql = f"INSERT INTO sensors (date, value) VALUES (%s, %s)"
    cur.execute(sql, (today, name_to_save)) 

    # Commit the changes to the database
    conn.commit()

    # Print success message
    print("Data saved successfully!")

  except (Exception, psycopg2.Error) as error:
    print("Error saving data to database:", error)
  finally:
    # Close the cursor and connection
    if cur is not None:
      cur.close()
    if conn is not None:
      conn.close()

# Example usage
name_to_save = "{Amir Nikravan}"
save_data_to_db(name_to_save)
