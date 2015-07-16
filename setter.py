#!/usr/bin/python

import variables

# The methods here are used to change the variables according to user input and to reset the shortPauseCounter


# Sets the duration of a work phase
def setWorkDuration(x):
    variables.workDuration = int(x)  # int() is needed here since otherwise python interprets it as a string
    print("Work duration has been set to {}".format(x))


# Sets the duration of a short pause
def setShortPauseDuration(x):
    variables.shortPauseDuration = int(x)  # int() is needed here since otherwise python interprets it as a string
    print("Pause duration has been set to {}".format(x))


# Sets the duration of a long pause
def setLongPauseDuration(x):
    variables.longPauseDuration = int(x)  # int() is needed here since otherwise python interprets it as a string
    print("Long pause duration has been set to {}".format(x))


# Used to reset the shortPauseCounter
def resetShortPauseCounter():
    variables.shortPauseCounter = 0
