#imports
from moviepy.editor import *
import subprocess
import os

#AudioFy
#Functions
def downloadVid(file):
    os.system(f"yt-dlp -o '%(id)s.%(ext)s' -P /Videos -a {file}")


#get User Input for URL
file = input("File name: ")

downloadVid(file)

#reads output location for songs
with open("CONF.txt") as conf:
    location = conf.readline()

#generate audio file

for video in os.listdir('Videos'):
    clip = AudioFileClip(f'{video}.webm')

    name = input("Name of mp3 file: ")

    #create file in dir
    clip.write_audiofile(f'({location}/{name}.mp3')

    #removes video
    if os.path.exists(f"/Videos/{video}.webm"):
        os.remove(f"/Videos/{video}.webm")
    else:
        print("File does not exist")
