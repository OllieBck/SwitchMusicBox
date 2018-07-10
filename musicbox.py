import os
from gpiozero import Button
from time import sleep
from signal import pause
import subprocess

pushButton = Button(13)

buttonCounter = 0

dirPath = "/home/pi/Desktop/SwitchBoxSongs/"

funSongs = os.listdir(dirPath);

funSongsPlaylist = []
for songNames in funSongs:
    if songNames.endswith(".wav"):
        funSongsPlaylist.append(songNames)

def playPushButton(buttonCounter):
        playThisSong = funSongsPlaylist[buttonCounter]
        subprocess.call(['killall', 'aplay'])
        subprocess.Popen(['aplay', dirPath + playThisSong])

def buttonPressCounter():
    global buttonCounter
    songCount = len(funSongsPlaylist)
    if buttonCounter == songCount:
        buttonCounter = 0
        playPushButton(buttonCounter)
    else:
        playPushButton(buttonCounter)
        buttonCounter = buttonCounter + 1

pushButton.when_pressed = buttonPressCounter

pause()
