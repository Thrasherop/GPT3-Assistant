from youtube_search import YoutubeSearch
from pytube import YouTube
import os

results = YoutubeSearch('fight_song', max_results=1).to_dict() # .to_json()

print(results)

print(results[0]['url_suffix'])

url = "youtube.com" + results[0]['url_suffix']
print(url)

# download mp3 of the url using pytube and output as "output.mp3"
yt = YouTube(url)
yt.streams.filter(progressive=True, file_extension='mp4').first().download(filename="output.mp4")

# os.rename(yt.streams.first().default_filename, 'new_filename.ext')

