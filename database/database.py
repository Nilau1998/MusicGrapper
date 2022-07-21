import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.c = None
        self.create_connection()
        self.create_cursor()

    def create_connection(self):
        """create a database connection to a SQLite database"""
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def create_cursor(self):
        """create the cursor"""
        self.c = self.conn.cursor()

    def create_table(self):
        raise NotImplementedError

    def insert_single_item(self):
        raise NotImplementedError

    def delete_single_item(self):
        raise NotImplementedError

    def fetch_one_item(self):
        raise NotImplementedError

    def fetch_many_items(self):
        raise NotImplementedError

    def fetch_all_items(self):
        raise NotImplementedError

    def commit_changes(self):
        try:
            self.conn.commit()
        except Error as e:
            print(e)

    def close_connection(self):
        """close the connection to the current db"""
        try:
            self.conn.close()
            print(f"{self.db_file} has been closed!")
        except Error as e:
            print(e)
