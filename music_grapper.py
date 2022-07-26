from database.channel_database import ChannelDatabase
from database.title_database import TitleDatabase
from util.console_tools import printProgressBar
from pytube import Channel, YouTube

class MusicGrapper:
    def __init__(self):
        self.channel_db = ChannelDatabase("database/channel_db")
        self.title_db = TitleDatabase("database/title_db")
        self.to_be_downloaded = []

    def populate_intital_channel_db(self):
        print("Checking if new channels need to be added...")
        with open("database/youtube_channels", "r") as reader:
            num_lines = sum(1 for line in reader)
            reader.seek(0) # Reset after line counter
            for i, channel_url in enumerate(reader):
                printProgressBar(i, num_lines, length=10, printEnd="\r")
                if self.channel_db.check_channel_existence(self.get_channel_id(channel_url))[0][0] == 0:
                    print(f"Adding channel: {self.get_channel_name(channel_url)}!")
                    self.channel_db.insert_single_item(
                        self.get_channel_name(channel_url),
                        self.get_channel_id(channel_url),
                        self.get_channel_video_count(channel_url)
                    )
            print("Finished channel_db population!")

    def populate_intital_title_db(self):
        channel_ids = self.channel_db.fetch_channel_ids()
        for channel_id in channel_ids:
            channel = Channel(f"https://www.youtube.com/channel/{channel_id[0]}")
            for i, video in enumerate(channel.videos):
                printProgressBar(i, len(channel.videos), length=10, printEnd="\r")
                if self.title_db.check_song_existence(video.video_id)[0][0] == 0:
                    print(f"Adding {video.title} by {channel.channel_name}!")
                    self.title_db.insert_single_item(
                        channel.channel_name,
                        channel.channel_id,
                        video.title.replace("'", ""),
                        video.video_id,
                        video.length)
            print(f"Finished adding tracks for channel: {channel.channel_name}")
        print("Finished title_db population!")

    def check_new_videos(self):
        for channel_id, channel_total_videos in zip(grapper.channel_db.fetch_channel_ids(), grapper.channel_db.fetch_channel_video_counts()):
            youtube_url = f"https://www.youtube.com/channel/{channel_id[0]}"
            if int(channel_total_videos[0]) != grapper.get_channel_video_count(youtube_url):
                print("bruh")

    def get_channel_name(self, channel_url):
        channel = Channel(channel_url)
        return channel.channel_name

    def get_channel_id(self, channel_url):
        channel = Channel(channel_url)
        return channel.channel_id

    def get_channel_video_count(self, channel_url):
        channel = Channel(channel_url)
        return len(channel.videos)


if __name__ == '__main__':
    grapper = MusicGrapper()