# utils.py
import pandas as pd
import psycopg2  # or your specific database library

conn = psycopg2.connect(
    dbname="telecom", 
    user="postgres", 
    password="123456", 
    host="localhost", 
    port="5432"
)

# Assuming conn is a global connection object
def fetch_data(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM xdr_data;")
        data = cur.fetchall()
        column_names = [column[0] for column in cur.description]
        data_frame = pd.DataFrame(data, columns=column_names)
        return data_frame
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
