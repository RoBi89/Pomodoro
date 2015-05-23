#!/usr/bin/python

import time

import endTimes
import setter
import variables
import messages
import notifications


# Starts a work phase
def work():
    print(messages.workMessage)
    print(endTimes.workTimeMessage)
    notifications.workStartNotification.show()
    time.sleep(variables.workDuration * 60)  # We have to multiply since workDuration is in minutes, not seconds
    if variables.shortPauseCounter >= 0 and variables.shortPauseCounter <= 2:  # We've had less than 3 short pauses so far
        shortPause()
    elif variables.shortPauseCounter == 3:  # We've had three short pauses, time for a long one
        longPause()
    else:  # If this ever happens, something is very wrong
        print("ERROR! shortPauseCounter outside of range")


# Starts a short pause
def shortPause():
    print(messages.shortPauseMessage)
    print(endTimes.shortPauseTimeMessage)
    notifications.shortPauseStartNotification.show()
    time.sleep(variables.shortPauseDuration * 60)  # We have to multiply since shortPauseDuration is in minutes, not seconds
    global shortPauseCounter
    variables.shortPauseCounter += 1
    work()


# Starts a long pause
def longPause():
    print(messages.longPauseMessage)
    print(endTimes.longPauseTimeMessage)
    notifications.longPauseStartNotification.show()
    time.sleep(variables.longPauseDuration * 60)  # We have to multiply since longPauseDuration is in minutes, not seconds
    setter.resetShortPauseCounter()  # The counter needs to reset in order to start a whole new cycle
    work()


# Starts the program
work()
