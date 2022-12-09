from random import randint
from datetime import datetime
from argparse import ArgumentParser
import webbrowser

def OpenVideo():
    file = "E:\Programacion\Python\YoutubeVideos.txt"
    ArrayVideos = []    
    for urlYoutube in open(file):
        ArrayVideos.append(urlYoutube)
    #print(ArrayVideos)
    webbrowser.open(ArrayVideos[randint(0, len(ArrayVideos))], new=2)

def Time():
    parser = ArgumentParser()
    hour = parser.add_argument("--hour", help="The hour of the day")
    minute = parser.add_argument("--minute", help="The minutes of the day")
    seconds = parser.add_argument("--seconds", help="The seconds of the day")

    args = vars(parser.parse_args())
    argsTime = str(args['hour']) + ":" + str(args['minute']) + ":" + str(args['seconds'])
    return argsTime

time = Time()
now = 0

while (time != now):
    now = datetime.now().strftime('%H:%M:%S')
    print("It's not the time")
else:
    print("Video played")
    OpenVideo()