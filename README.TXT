In order to use AudioFy, a few packages must be installed

1: yt-dlp - Used to download the video from Youtube
MAC/Linux:
Homebrew
Follow instructions and install homebrew at https://brew.sh/
Then type 

brew install yt-dlp

into a terminal
After it installs, type 

brew install ffmpeg


Make sure to have python installed


Windows:
Run the following commands

pip install yt-dlp
pip install ffmpeg



Enter the URLs for the youtube videos you want your song to come from in the songs.txt file
Specify the locations of where you want your songs to end up and the location of the videos folder using their ABSOLUTE paths inside the .py file, under the comment specifiying their locations, located in the assets folder
EX: /Users/[username]/Desktop/songs

Remember the order of the URLs that you put in the songs.txt file, as the program will ask for a name for each song in from the first line to last.

Run and enjoy
