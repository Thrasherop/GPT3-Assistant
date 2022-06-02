from youtube_search import YoutubeSearch
from pytube import YouTube
import os

from googlecontroller import GoogleAssistant

from flask import Flask
import threading

# Establish connection to Google Home
host = "10.0.0.73"
home = GoogleAssistant(host=host)


def play_keyword(keyword):

    keyword = keyword.replace(" ", "_")

    # Search for keyword to get url
    results = YoutubeSearch(keyword, max_results=1).to_dict() # .to_json()

    print(results)

    print(results[0]['url_suffix'])

    url = "youtube.com" + results[0]['url_suffix']
    print(url)


    # download mp3 of the url using pytube and output as "output.mp3"
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').first().download(filename="output.mp4")

    # Finally, play the file
    home.serve_media("output.mp4","./", opentunnel=0)
    #home.volume(100)

#play_keyword("can't hold us")


port = 21000
debug = True
fhost = "0.0.0.0"

app = Flask(__name__)

@app.route("/")
def hello():
    print("recieved")
    return "Hello World!"

@app.route("/dj/<prompt>")
def dj(prompt):
    print("dj")
    play_keyword(prompt)
    # x = threading.Thread(target=play_keyword, args=(prompt,))
    # x.start()
    return "Playing"

if __name__ == "__main__":
    app.run(host=fhost, port=port, debug=debug)
