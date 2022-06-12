from youtube_search import YoutubeSearch
from pytube import YouTube
import os

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from googlecontroller import GoogleAssistant

from flask import Flask
import threading
from time import sleep

from src.GPT3Interface import GPT3

from configs import secrets, config

# Establish connection to Google Home
host = "10.0.0.73"
home = GoogleAssistant(host=host)

use_open_tunnel = True


# Create gpt3 interface object
gpt3 = GPT3()


#home.say("Hello, I am your personal assistant. How can I help you?")

#home.serve_media("BachGavotteShort.mp3", "./", opentunnel=0)

def generate_speak(text):
    authenticator = IAMAuthenticator(secrets.IBM)
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/d480862a-60ee-45e1-a585-8e640d85efff')

    with open(config.PHILO_FILE,'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(text,voice=config.PHILO_VOICE,accept='audio/mp3').get_result().content)

def play_keyword(keyword):

    global use_open_tunnel

    ##home.serve_media("BachGavotteShort.mp3", "./", opentunnel=0)

    print("play keyword called")
    log("play keyword called")

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

    print("attempting to play")
    # Finally, play the file
    if use_open_tunnel:
        print("using open tunner")
        log("use open tunnel")
        home.serve_media("output.mp4","./", opentunnel=0) # , opentunnel=0)
        use_open_tunnel=False
    else:
        print("not using open tunnel")
        home.serve_media("output.mp4","./")
    log("finished")
    #home.volume(100)

#play_keyword("can't hold us")

def log(message):
    with open("log.txt", "a") as logfile:
        logfile.write(message + "\n")

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
    print("dj called")
    log("dj called but new")
    print(prompt)
    print(prompt)


    # Gets GPT-3's recommendation
    print("seeking gpt3")
    gpt3_response = gpt3.ask_dj(prompt)
    print(gpt3_response)
    play_keyword(gpt3_response)

    #play_keyword(prompt)
    #play_keyword("can't hold us")
    return "Playing"

@app.route("/philosopher/<prompt>")
def philosopher(prompt):

    global use_open_tunnel

    print("philosopher called")
    print(prompt)

    # Gets GPT-3's recommendation
    print("seeking gpt3")
    gpt3_response = gpt3.ask_philosopher(prompt)
    print(gpt3_response)

    #phrase="hellllo world. I need to make this longer so I shall. Once upon a timeWhen I talk about this and other such things as food/drink/exercise/sleep as causing either deep or illusory pleasures , my point is not just simply appreciating these things on aggregate; rather, these activities lead us into deeper joys from experiencing them at each moment . So 'Pleasure' isn't an abstract theoretical property: Pleasure isn't even something with which cognitive agents are concerned (although they could be interested towards calculative pursuits), but instead a quality of experience – the impact derived by selves out of instigating self-enhancement processes within themselves"
    # phrase="hellllo world. I need to make this longer so I shall. Once upon a timeWhen I talk about this and other such things a"

    # if len(phrase) > 265:
    #     print("Forced to trim message")
    #     phrase = phrase[:240] + " !!! Out of space"

    
    #home.say(phrase)

    print("generating speak")
    
    generate_speak(gpt3_response)

    if use_open_tunnel:
        print("using open tunner")
        log("use open tunnel")
        home.serve_media(config.PHILO_FILE,"./", opentunnel=0) # , opentunnel=0)
        use_open_tunnel=False
    else:
        print("not using open tunnel")
        home.serve_media(config.PHILO_FILE,"./")
        log("finished")

    print("speak sent finished")
 
    #play_keyword(prompt)
    #play_keyword("can't hold us")
    return "Playing"

@app.route("/james/<prompt>")
def james(prompt):
    print("james called")
    print(prompt)

    # Gets GPT-3's recommendation
    print("seeking gpt3")
    gpt3_response = gpt3.ask_james(prompt)
    print(gpt3_response)
    home.say(gpt3_response)

    #play_keyword(prompt)
    #play_keyword("can't hold us")
    return "Playing"

# print("generating voice")
# speak("Hello, I am your personal assistant. How can I help you?")
# print("speak done")

if __name__ == "__main__":
    #sleep(5) # sleep to make sure it has console priority
    print("running")
    app.run(host=fhost, port=port, debug=debug)
