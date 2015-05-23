#!/usr/bin/python

import time
import datetime

workDuration = 25
shortPauseDuration = 5
longPauseDuration = 20
shortPauseCounter = 0


def calculateEndTimeWork():
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=workDuration)
    t = now.time()
    combined = ((datetime.datetime.combine(datetime.date(1, 1, 1), t) + delta).time())
    combinedCut = combined.replace(second=0, microsecond=0)
    return combinedCut


def calculateEndShortPause():
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=shortPauseDuration)
    t = now.time()
    combined = ((datetime.datetime.combine(datetime.date(1, 1, 1), t) + delta).time())
    combinedCut = combined.replace(second=0, microsecond=0)
    return combinedCut


def calculateEndLongPause():
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=longPauseDuration)
    t = now.time()
    combined = ((datetime.datetime.combine(datetime.date(1, 1, 1), t) + delta).time())
    combinedCut = combined.replace(second=0, microsecond=0)
    return combinedCut


def startWork():
    print("Start working! Your Pause begins in {} minutes".format(workDuration))
    print("Your work will end at {}".format(calculateEndTimeWork()))
    time.sleep(workDuration * 60)
    if shortPauseCounter <= 2:
        startShortPause()
    elif shortPauseCounter == 3:
        startLongPause()
    else:
        print("ERROR! shortPauseCounter is too high")


def startShortPause():
    print("Well done! Have a break. It ends in {} minutes".format(shortPauseDuration))
    print("Your pause will end at {}".format(calculateEndShortPause()))
    time.sleep(shortPauseDuration * 60)
    global shortPauseCounter
    shortPauseCounter += 1
    startWork()


def startLongPause():
    print("Now you deserve a longer break! Take {} minutes to get some rest".format(longPauseDuration))
    print("Your pause will end at {}".format(calculateEndLongPause()))
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
