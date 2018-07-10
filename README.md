# SwitchMusicBox

Simple code for creating a music player with variable switches.  Each switch (door knob, squeeze mechanism, etc.) will trigger a different song.

A Samba file server allows user to upload songs to the Pi.

After installing Raspian OS, add the musicbox.py code to /home/pi/Desktop.  Create a directory `mkdir /home/pi/Desktop/SwitchBoxSongs`. Install Samba and edit the config file to link to this directory.

Step 1: Install Samba

```
$ sudo apt install -y samba
```

Step 2: Edit Config File

```
$ sudo nano /etc/samba/smb.conf
```

ADD at the END:

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
