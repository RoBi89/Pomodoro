#!/usr/bin/python

import time

workDuration = 10
shortPauseDuration = 5
longPauseDuration = 8
shortPauseCounter = 0


def startWork():
    print("Start working! Your Pause begins in %d minutes" % (workDuration))
    time.sleep(workDuration * 60)
    if shortPauseCounter <= 2:
        startShortPause()
    elif shortPauseCounter == 3:
        startLongPause()
    else:
        print("ERROR! shortPauseCounter is too high")


def startShortPause():
    print("Well done! Have a break. "
          "It ends in %d minutes" % (shortPauseDuration))
    time.sleep(shortPauseDuration * 60)
    global shortPauseCounter
    shortPauseCounter += 1
    startWork()


def startLongPause():
    print("Now you deserve a longer break! "
          "Take %d minutes to get some rest" % (longPauseDuration))
    setShortPauseCounter(0)
    time.sleep(longPauseDuration * 60)
    startWork()


def setWorkDuration(x):
    global workDuration
    workDuration = x
    print("Work duration has been set to %d" % (x))


def setShortPauseDuration(x):
    global pauseDuration
    pauseDuration = x
    print("Pause duration has been set to %d" % (x))


def setLongPauseDuration(x):
    global longPauseDuration
    longPauseDuration = x
    print("Long pause duration has been set to %d" % (x))


def setShortPauseCounter(x):
    global shortPauseCounter
    shortPauseCounter = x

startWork()
