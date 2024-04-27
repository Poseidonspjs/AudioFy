#imports
import os


#Functions
def downloadVid(file):
    os.system(f"yt-dlp -o '%(id)s.%(ext)s' -P {videoLocation} -x -a {file}")

#ENTER LOCATIONS HERE
location = ''
videoLocation = ''

#get User Input for URL
print("Downloading files...")

#Run func
downloadVid('songs.txt')



#convert OPUS to mp3

print('Converting to audio')
for video in os.listdir('Videos'):
    if(video == '.DS_Store'):
        print('Skipping DS file') #PESTY FILE
    else:
        print(video)
        print()
        name = input(f'name of mp3 file for {video}: ')
        print()
        print(f'ffmpeg -i {videoLocation}/{video} -c:a libmp3lame {location}/{name}.mp3')
        print()
        os.system(f'ffmpeg -i {videoLocation}/{video} -c:a libmp3lame {location}/{name}.mp3')

    #CLEANUP
    if os.path.exists(f"{videoLocation}/{video}"):
        os.remove(f"{videoLocation}/{video}")
    else:
        print("File does not exist")
