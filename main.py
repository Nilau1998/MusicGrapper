from database.channel_database import ChannelDatabase

from pytube import Channel, YouTube
import os
from time import sleep

if __name__ == '__main__':
    channel_database = ChannelDatabase(r"database/channel_db")

    yt = YouTube("https://www.youtube.com/watch?v=9Nn2tr3uyFo")
    channel = Channel("https://www.youtube.com/channel/UC_YRhLOi-aImlvc7CwTF5Jw")

    for video, video_url in zip(channel.videos, channel.video_urls):
        sleep(2)
        print(video.title)
        print(video_url)
        file = YouTube(video_url).streams.filter(only_audio=True).first().download("test/")
        basename = os.path.basename(file)
        base, ext = os.path.splitext(basename)
        newfile = base + ".mp3"
        os.rename(file, "test/" + channel.channel_name + " - " + newfile)