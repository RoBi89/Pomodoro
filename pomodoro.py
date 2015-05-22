#!/usr/bin/python

import time

workDuration = 25
pauseDuration = 5
longPauseDuration = 20


def startWork():
    print("Start working! Your Pause begins in %d minutes" % (workDuration))
    time.sleep(workDuration * 60)
    startPause()


def startPause():
    print("Well done! Have a break. It ends in %d minutes" % (pauseDuration))
    time.sleep(pauseDuration * 60)
    startWork()


def startLongPause():
    print("Now you deserve a longer break! "
          "Take %d minutes to get some rest" % (longPauseDuration))
    time.sleep(longPauseDuration * 60)
    startWork()


def setWorkDuration(x):
    global workDuration
    workDuration = x
    print("Work duration has been set to %d" % (x))


def setPauseDuration(x):
    global pauseDuration
    pauseDuration = x
    print("Pause duration has been set to %d" % (x))


def setLongPauseDuration(x):
    global longPauseDuration
    longPauseDuration = x
    print("Long pause duration has been set to %d" % (x))
