import sqlite3
from sqlite3 import Error

class Databank:
    def __init__(self):
        pass

    def create_connection(self, db_file):
        """create a database connection to a SQLite database"""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()



if __name__ == "__main__":
    databank = Databank()
    databank.create_connection(r"database/channel_db")