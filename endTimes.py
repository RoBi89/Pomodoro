#!/usr/bin/python

import datetime
import variables


# Calculates the end time of the current work phase
def endTimeWork():
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=variables.workDuration)
    t = now.time()
    combined = ((datetime.datetime.combine(datetime.date(1, 1, 1), t) + delta).time())  # Adds workDuration to the current time
    combinedCut = combined.replace(second=0, microsecond=0)  # Cuts out seconds and microseconds for better readibility
    return combinedCut


# Calculates the end time of the current short pause
def endTimeShortPause():
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=variables.shortPauseDuration)
    t = now.time()
    combined = ((datetime.datetime.combine(datetime.date(1, 1, 1), t) + delta).time())   # Adds shortPauseDuration to the current time
    combinedCut = combined.replace(second=0, microsecond=0)  # Cuts out seconds and microseconds for better readibility
    return combinedCut


# Calculates the end time of the current long pause
def endTimeLongPause():
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=variables.longPauseDuration)
    t = now.time()
    combined = ((datetime.datetime.combine(datetime.date(1, 1, 1), t) + delta).time())   # Adds longPauseDuration to the current time
    combinedCut = combined.replace(second=0, microsecond=0)  # Cuts out seconds and microseconds for better readibility
    return combinedCut


# These Messages are displayed in pomodoro.py
workTimeMessage = "This work phase will end at {}".format(endTimeWork())
shortPauseTimeMessage = "Your pause will end at {}".format(endTimeShortPause())
longPauseTimeMessage = "Your pause will end at {}".format(endTimeLongPause())
