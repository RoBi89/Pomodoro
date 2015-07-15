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


# This is getting the input from the user and sends it to evaluate() in order to determine what to do with it
def userInput():
    x = input("Enter command: ")
    command = x.split()
    evaluate(command)
    return


# Evaluates the input given by the user
def evaluate(args):
    if len(args) == 1:
        if args[0] == "s":
            print("Starting program")
            work()
            userInput()
        elif args[0] == "e":
            print("Program exiting")
            exit()
        elif args[0] == "p":
            print("Pausing...")
            wait = input("PRESS ENTER TO CONTINUE.")
            userInput()
        elif args[0] == "status":
            print(variables.workDuration)
            userInput()
        else:
            print("Invalid input, please correct!")
            userInput()
    if len(args) == 2:
        if args[0] == "set_work":
            setter.setWorkDuration(args[1])
            userInput()
        elif args[0] == "set_short":
            setter.setShortPauseDuration(args[1])
            userInput()
        elif args[0] == "set_long":
            setter.setLongPauseDuration(args[1])
            userInput()
        else:
            print("Invalid input, please correct!")
            userInput()


# Starts the program
userInput()
