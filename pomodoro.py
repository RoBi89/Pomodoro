#!/usr/bin/python

import time
from gi.repository import Notify

import endTimes
import setter
import variables


# These messages are shown at the beginning of each new phase
workMessage = "Start working! Your Pause begins in {} minutes".format(variables.workDuration)
shortPauseMessage = "Well done! Have a break. It ends in {} minutes".format(variables.shortPauseDuration)
longPauseMessage = "Now you deserve a longer break! Take {} minutes to get some rest".format(variables.longPauseDuration)


# Starts a work phase
def work():
    print(workMessage)
    print(endTimes.workTimeMessage)
    time.sleep(variables.workDuration * 60)  # We have to multiply since workDuration is in minutes, not seconds
    if variables.shortPauseCounter >= 0 and variables.shortPauseCounter <= 2:  # We've had less than 3 short pauses so far
        shortPause()
    elif variables.shortPauseCounter == 3:  # We've had three short pauses, time for a long one
        longPause()
    else:  # If this ever happens, something is very wrong
        print("ERROR! shortPauseCounter outside of range")


# Starts a short pause
def shortPause():
    print(shortPauseMessage)
    print(endTimes.shortPauseTimeMessage)
    time.sleep(variables.shortPauseDuration * 60)  # We have to multiply since shortPauseDuration is in minutes, not seconds
    global shortPauseCounter
    variables.shortPauseCounter += 1
    work()


# Starts a long pause
def longPause():
    print(longPauseMessage)
    print(endTimes.longPauseTimeMessage)
    time.sleep(variables.longPauseDuration * 60)  # We have to multiply since longPauseDuration is in minutes, not seconds
    setter.resetShortPauseCounter()  # The counter needs to reset in order to start a whole new cycle
    work()


# Starts the program
work()
