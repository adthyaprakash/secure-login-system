import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="vaultdb",
        user="postgres",
        password="root"  # use your correct password
    )
    return conn
