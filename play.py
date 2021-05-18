#!/usr/bin/env python3

from os import listdir, system, environ
from os.path import join, splitext
from time import sleep
import signal
from pyfiglet import Figlet

if environ['AUDIO_PATH'] != '':
    AUDIO_PATH = environ['AUDIO_PATH']
else:
    AUDIO_PATH = '/opt/audio'

if environ['AUDIO_EXT'] != '':
    AUDIO_EXT = environ['AUDIO_EXT']
else:
    AUDIO_EXT = '.mp3'

if environ['AUDIO_VOLUME'] != '':
    AUDIO_VOLUME = environ['AUDIO_VOLUME']
else:
    AUDIO_VOLUME = '0'

if environ['AUDIO_DEVICE'] != '':
    AUDIO_DEVICE = environ['AUDIO_DEVICE']
else:
    AUDIO_DEVICE = 'alsa' # options: alsa, hdmi

if environ['AUDIO_LAYOUT'] != '':
    AUDIO_LAYOUT = environ['AUDIO_LAYOUT']
else:
    AUDIO_LAYOUT = '2.1' # options: 2.1, 5.1, 7.1

def main():
    files = listdir(AUDIO_PATH)

    figl = Figlet(font='standard')
    print(figl.renderText('Garden Player'))
    
    while True:
        for f in files:
            ext = splitext(f)[1]
            if ext.lower() == AUDIO_EXT:
                filename = join(AUDIO_PATH,f)
                print("Playing file:", filename)
                system('omxplayer -r -b -o %s --vol %s --layout %s "%s"' % (AUDIO_DEVICE, str(AUDIO_VOLUME), str(AUDIO_LAYOUT), filename))

if __name__ == '__main__':
    main()
