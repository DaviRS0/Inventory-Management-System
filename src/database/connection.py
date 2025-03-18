import psycopg2
from config import DATABASE

def get_connection():
    conn = psycopg2.connect(
        host=DATABASE['host'],
        port=DATABASE['port'],
        dbname=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        sslmode=DATABASE['sslmode']
    )
    return conn