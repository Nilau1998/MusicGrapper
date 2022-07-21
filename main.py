from pytube import Channel

c = Channel("https://www.youtube.com/channel/UC_YRhLOi-aImlvc7CwTF5Jw")

for video in c.videos:
    print(video.title)