from database.database import Database

class ChannelDatabase(Database):
    def __init__(self, db_file):
        super().__init__(db_file)

    def create_table(self):
        self.c.execute("""CREATE TABLE channels (
            channel_name text,
            channel_id text,
            channel_video_count real
        )""")
        self.commit_changes()

    def insert_single_item(self, channel_name: str, channel_id: str, channel_video_count: int):
        self.c.execute(f"INSERT INTO channels VALUES ('{channel_name}', '{channel_id}', '{channel_video_count}')")
        self.commit_changes()

    def delete_single_item(self, channel_id: str):
        self.c.execute(f"DELETE from channels WHERE channel_id = '{channel_id}'")
        self.commit_changes()

    def fetch_one_item(self):
        pass

    def fetch_many_items(self):
        pass

    def fetch_all_items(self):
        self.c.execute("SELECT * FROM channels")
        return self.c.fetchall()

    def update_channel_name(self, channel_id: str, new_channel_name: str):
        self.c.execute(f"""UPDATE channels SET channel_name = '{new_channel_name}'
                        WHERE channel_id = '{channel_id}'""")
        self.commit_changes()

    def update_channel_video_count(self, channel_id: str, new_channel_video_count: int):
        self.c.execute(f"""UPDATE channels SET channel_name = '{new_channel_video_count}'
                        WHERE channel_id = '{channel_id}'""")
        self.commit_changes()