#!/usr/bin/python

import time

import endTimes
import setter
import variables
import messages
import notifications


# Starts a work phase
def work():
    print(messages.workMessage())
    print(endTimes.workTimeMessage())
    notifications.workStartNotification.show()
    userInput()
    time.sleep(variables.workDuration * 60)  # We have to multiply since workDuration is in minutes, not seconds
    if variables.shortPauseCounter >= 0 and variables.shortPauseCounter <= 2:  # We've had less than 3 short pauses so far
        shortPause()
    elif variables.shortPauseCounter == 3:  # We've had three short pauses, time for a long one
        longPause()
    else:  # If this ever happens, something is very wrong
        print("ERROR! shortPauseCounter outside of range")


# Starts a short pause
def shortPause():
    print(messages.shortPauseMessage())
    print(endTimes.shortPauseTimeMessage)
    notifications.shortPauseStartNotification.show()
    time.sleep(variables.shortPauseDuration * 60)  # We have to multiply since shortPauseDuration is in minutes, not seconds
    global shortPauseCounter
    variables.shortPauseCounter += 1
    work()


# Starts a long pause
def longPause():
    print(messages.longPauseMessage())
    print(endTimes.longPauseTimeMessage)
    notifications.longPauseStartNotification.show()
    time.sleep(variables.longPauseDuration * 60)  # We have to multiply since longPauseDuration is in minutes, not seconds
    setter.resetShortPauseCounter()  # The counter needs to reset in order to start a whole new cycle
    work()


# This is getting the input from the user and sends it to evaluate() in order to determine what to do with it
def userInput():
    print("Welcome to PyModoro, type *help* to see the available commands")
    x = input("Enter command: ")
    command = x.split()
    evaluate(command)
    return


# Evaluates the input given by the user
def evaluate(args):
    if len(args) == 1:  # If the length is only one, that means that the user is not trying to use one of the setters
        if args[0] == "s":  # Runs the program normally
            print("Starting program")
            work()
        elif args[0] == "e":  # Exits the program
            print("Program exiting")
            exit()
        elif args[0] == "p":  # Pauses the program
            print("Pausing...")
            input("PRESS ENTER TO CONTINUE.")
            userInput()
        elif args[0] == "help":  # Shows the available commands
            print("The following commands are available:")
            print("s         -> starts the program")
            print("e         -> exits the program")
            print("p         -> pauses the program")
            print("status    -> Shows the current times for the different phases")
            print("set_work  -> Sets the duration of working phases")
            print("set_short -> Sets the duration of short pauses")
            print("set_long  -> Sets the duration of long pauses")
            userInput()
        elif args[0] == "status":  # Shows the variable values
            print("Working phase length : {} minutes".format(variables.workDuration))
            print("Short pause length : {} minutes".format(variables.shortPauseDuration))
            print("Long pause length length : {} minutes".format(variables.longPauseDuration))
            userInput()
        else:
            print("Invalid input, please correct!")
            userInput()
    if len(args) == 2:  # User wants to change the setters (obviously, since that requires both tha command and the value)
        if args[0] == "set_work":  # Changes the duration of a working phase
            setter.setWorkDuration(args[1])
            userInput()
        elif args[0] == "set_short":  # Changes the duration of a short pause
            setter.setShortPauseDuration(args[1])
            userInput()
        elif args[0] == "set_long":  # Changes the duration of a long pause
            setter.setLongPauseDuration(args[1])
            userInput()
        else:
            print("Invalid input, please correct!")
            userInput()


# Starts the program
userInput()
