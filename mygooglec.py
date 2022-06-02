print("hello world")

# from googlehomepush import GoogleHome

# GoogleHome(host="10.0.0.73").say("test")
# #GoogleHome("LivingRoom").play("http://www.hubharp.com/web_sound/BachGavotteShort.mp3")


from googlecontroller import GoogleAssistant
from time import sleep
#from googlecontroller.http_server import serve_file # for local files
host = "10.0.0.73"
home = GoogleAssistant(host=host)
#home.say("test test test")
#"http://www.hubharp.com/web_sound/BachGavotteShort.mp3, opentunnel = 0"


#home.play("http://youtu.be/JrKwm4xJ5Gs", ignore=True)
#home.play("http://youtu.be/JrKwm4xJ5Gs")
print("doone")
#home.play("http://w
# 
# 
# 
# ww.hubharp.com/web_sound/BachGavotteShort.mp3", opentunnel = 0) # we are doing opentunnel as this is the first time doing it
#home.play("http://www.hubharp.com/web_sound/BachGavotteShort.mp3") # you do this after the first opening

#When serving media NEVER USE A \ ONLY USE /
#when doing your first home.serve_media you have to include a 3rd variable, opentunnle!For that 1 first time you have to set it manually to a 0!
#opentunnel = 0
#YOU MUST USE A DELAY IF DOING MULTIPLE IN A ROW FINE TUNE AS YOU SEE FIT
#like this home.serve_media("YourMedia.mp3", "C:/Users/YOU!/Music/", opentunnel)
#**then never use that variable again**
# home.serve_media("YourMedia.mp3", "C:/Users/YOU!/Music/") # 1st is the name of the media, second is the full path to media location!
# home.volume(100)
# home.volume(0)
#  


#
# This worked
#
#
#

#home.serve_media("BachGavotteShort.mp3","C:/Users/ultra/Downloads", opentunnel=0)
home.serve_media("output.mp4","./", opentunnel=0)
home.volume(100)