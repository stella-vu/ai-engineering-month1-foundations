import os
import psycopg2
import dotenv
from psycopg2.extras import RealDictCursor

dotenv.load_dotenv()

password = os.getenv("POSTGRES_PASSWORD")

class Database:

    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="expense_tracker",
            user="postgres",
            password=password
        )

    def get_cursor(self):
        return self.conn.cursor(cursor_factory=RealDictCursor)
    
    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.conn.close()

