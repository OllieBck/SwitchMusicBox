# SwitchMusicBox

Simple code for creating a music player with variable switches.  Each switch (door knob, squeeze mechanism, etc.) will trigger a different song.

A Samba file server allows user to upload songs to the Pi.

After installing Raspian OS and setting up WiFi, download the Adafruit Stereo Speaker Bonnet from https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi?view=all.

Adafruit's simple install link is:

```
curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash
```

Download this repo by opening up Terminal and `git clone https://github.com/OllieBck/SwitchMusicBox`.

Install Samba and edit the config file to link to this directory.

Step 1: Install Samba

```
$ sudo apt install -y samba
```

Step 2: Edit Config File

```
$ sudo nano /etc/samba/smb.conf
```

Add below at the end of the smb.conf file:

```
[musicbox Music]
 comment=musicbox share
 path=/home/pi/Desktop/SwitchBoxSongs
 browseable=Yes
 writeable=Yes
 only guest=No
 create mask=0740
 directory mask=0750
 public=no
 ```

Step 3: Create Sign-In

 ```
$ sudo smbpasswd -a pi
 ```
Add password when prompted.

After setting up Samba, go to Mac/PC computer to access shared drive and upload songs into the "SwitchMusicBox" folder by dragging in ".wav" audio files.

Attach a switch to GPIO pin 13 and GND on Raspberry Pi/Speaker Bonnet.

In Terminal on the Pi, change directories into the directory with musicbox.py:

```
$ cd /home/pi/SwitchMusicBox
```

Test out the switch by running the program.

```
$ sudo python musicbox.py
```

If music plays when you hit the switch, and cycles to new songs, super (make sure you have WAV audio files in the SwitchBoxSongs directory).  Add the script to run on startup by changing the rc.local file found in /etc.  Here we use the "nano" editor:

```
$ sudo nano /etc/rc.local
```
And adding above the "exit 0" line:

```
$ sudo python /home/pi/Desktop/musicbox.py &
```
Reboot the pi and see if script runs on startup.

If it does, edit code and hardware to take on additional switches.
