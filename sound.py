#!/usr/bin/python3

import os


def startSoundWork():
    os.system("/usr/bin/canberra-gtk-play --id='suspend-error'")


def startSoundPause():
    os.system("/usr/bin/canberra-gtk-play --id='complete'")
