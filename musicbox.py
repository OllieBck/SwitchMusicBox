import os
from gpiozero import Button
from time import sleep
from signal import pause
import subprocess

class Switch:

    def __init__(self, pinNumber, path):
        self.buttonCounter = 0
        self.pushButton = Button(pinNumber)
        self.dirPath = path
        self.funSongs = os.listdir(self.dirPath)
        self.buttonCounter = 0
        self.funSongsPlaylist=[]
        for self.songNames in self.funSongs:
            if self.songNames.endswith(".wav") and not self.songNames.startswith("."):
                self.funSongsPlaylist.append(self.songNames)

    def playPushButton(self, buttonCounter):
        print(self.buttonCounter)
        self.playThisSong = self.funSongsPlaylist[self.buttonCounter]
        subprocess.call(['killall', 'aplay'])
        subprocess.Popen(['aplay', self.dirPath + self.playThisSong])

    def buttonPressCounter(self):
        self.songCount = len(self.funSongsPlaylist)
        if self.buttonCounter == self.songCount:
            self.buttonCounter = 0
            self.playPushButton(self.buttonCounter)
        else:
            self.playPushButton(self.buttonCounter)
            self.buttonCounter = self.buttonCounter + 1

pressSwitch = Switch(13, "/home/pi/SwitchMusicBox/Songs/")
squeezeSwitch = Switch(12, "/home/pi/SwitchMusicBox/Songs/Playlist 1/")

pressSwitch.pushButton.when_pressed = pressSwitch.buttonPressCounter
squeezeSwitch.pushButton.when_pressed = squeezeSwitch.buttonPressCounter

pause()
