#!/usr/bin/python

import time
import datetime

workDuration = 25  # Duration of a work phase, can be changed by the user
shortPauseDuration = 5  # Duration of a short pause, can be changed by the user
longPauseDuration = 20  # Duration of a long pause, can be changed by the user
shortPauseCounter = 0  # Counts how many short pauses have already occured since the last long pause


# Calculates the end time of the current work phase
def calculateEndTimeWork():
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=workDuration)
    t = now.time()
    combined = ((datetime.datetime.combine(datetime.date(1, 1, 1), t) + delta).time())  # Adds workDuration to the current time
    combinedCut = combined.replace(second=0, microsecond=0)  # Cuts out seconds and microseconds for better readibility
    return combinedCut


# Calculates the end time of the current short pause
def calculateEndShortPause():
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=shortPauseDuration)
    t = now.time()
    combined = ((datetime.datetime.combine(datetime.date(1, 1, 1), t) + delta).time())   # Adds shortPauseDuration to the current time
    combinedCut = combined.replace(second=0, microsecond=0)  # Cuts out seconds and microseconds for better readibility
    return combinedCut


# Calculates the end time of the current long pause
def calculateEndLongPause():
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=longPauseDuration)
    t = now.time()
    combined = ((datetime.datetime.combine(datetime.date(1, 1, 1), t) + delta).time())   # Adds longPauseDuration to the current time
    combinedCut = combined.replace(second=0, microsecond=0)  # Cuts out seconds and microseconds for better readibility
    return combinedCut


# Starts a work phase
def work():
    print("Start working! Your Pause begins in {} minutes".format(workDuration))
    print("Your work will end at {}".format(calculateEndTimeWork()))
    time.sleep(workDuration * 60)  # We have to multiply since workDuration is in minutes, not seconds
    if shortPauseCounter >= 0 and shortPauseCounter <= 2:  # We've had less than 3 short pauses so far
        shortPause()
    elif shortPauseCounter == 3:  # We've had three short pauses, time for a long one
        longPause()
    else:  # If this ever happens, something is very wrong
        print("ERROR! shortPauseCounter outside of range")


# Starts a short pause
def shortPause():
    print("Well done! Have a break. It ends in {} minutes".format(shortPauseDuration))
    print("Your pause will end at {}".format(calculateEndShortPause()))
    time.sleep(shortPauseDuration * 60)  # We have to multiply since shortPauseDuration is in minutes, not seconds
    global shortPauseCounter
    shortPauseCounter += 1
    work()


# Starts a long pause
def longPause():
    print("Now you deserve a longer break! Take {} minutes to get some rest".format(longPauseDuration))
    print("Your pause will end at {}".format(calculateEndLongPause()))
    time.sleep(longPauseDuration * 60)  # We have to multiply since longPauseDuration is in minutes, not seconds
    resetShortPauseCounter()  # The counter needs to reset in order to start a whole new cycle
    work()


# Sets the duration of a work phase
def setWorkDuration(x):
    global workDuration
    workDuration = x
    print("Work duration has been set to {}".format(x))


# Sets the duration of a short pause
def setShortPauseDuration(x):
    global pauseDuration
    pauseDuration = x
    print("Pause duration has been set to {}".format(x))


# Sets the duration of a long pause
def setLongPauseDuration(x):
    global longPauseDuration
    longPauseDuration = x
    print("Long pause duration has been set to {}".format(x))


# Used to reset the shortPauseCounter
def resetShortPauseCounter():
    global shortPauseCounter
    shortPauseCounter = 0


# Starts the program
work()
