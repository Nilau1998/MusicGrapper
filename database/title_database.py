from database.database import Database

class TitleDatabase(Database):
    def __init__(self, db_file):
        super().__init__(db_file)

    def create_table(self):
        self.c.execute("""CREATE TABLE titels (
            channel_name text,
            channel_id text,
            song_title text,
            song_id text,
            song_length real
        )""")

    def insert_single_item(self, channel_name: str, channel_id: str, song_title: str, song_id: str, song_length: int):
        self.c.execute(f"INSERT INTO titels VALUES ('{channel_name}', '{channel_id}', '{song_title}', '{song_id}', '{song_length}')")
        self.commit_changes()

    def delete_single_item(self, song_id: str):
        self.c.execute(f"DELETE from titels WHERE song_id = '{song_id}'")
        self.commit_changes()

    def fetch_one_item(self, song_id: str):
        self.c.execute(f"SELECT from titels WHERE song_id = '{song_id}'")
        return self.c.fetchall()

    def fetch_many_items(self):
        pass

    def fetch_all_items(self):
        self.c.execute("SELECT * FROM titels")
        return self.c.fetchall()