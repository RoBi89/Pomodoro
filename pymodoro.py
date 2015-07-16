#!/usr/bin/python3

import time

import endTimes
import setter
import variables
import messages
import notifications
import sound


# Starts a work phase
def work():
    sound.startSoundWork()  # Plays a sound to alert the user
    print(messages.workMessage())  # Shows the message telling the user that the work phase has started
    print(endTimes.workTimeMessage())  # Shows the message telling the user when the current work phase will end
    notifications.workStartNotification()  # Shows a notification with the same info as in the terminal
    userInput()  # Allows the user to enter commands during the ongoing phase
    time.sleep(variables.workDuration * 60)  # We have to multiply since workDuration is in minutes, not seconds
    if variables.shortPauseCounter >= 0 and variables.shortPauseCounter <= 2:  # We've had less than 3 short pauses so far
        shortPause()  # starts a short pause
    elif variables.shortPauseCounter == 3:  # We've had three short pauses, time for a long one
        longPause()  # starts a long pause
    else:  # If this ever happens, something is very wrong
        print("ERROR! shortPauseCounter outside of range")


# Starts a short pause
def shortPause():
    sound.startSoundPause()  # Plays a sound to alert the user
    print(messages.shortPauseMessage())  # Shows the message telling the user that the short pause has started
    print(endTimes.shortPauseTimeMessage)  # Shows the message telling the user when the current short pause will end
    notifications.shortPauseStartNotification.show()  # Shows a notification with the same info as in the terminal
    userInput()  # Allows the user to enter commands during the ongoing phase
    time.sleep(variables.shortPauseDuration * 60)  # We have to multiply since shortPauseDuration is in minutes, not seconds
    global shortPauseCounter
    variables.shortPauseCounter += 1  # we need to increase the counter so we know when to start a long pause instead of a short pause
    work()  # starts the working phase


# Starts a long pause
def longPause():
    sound.startSoundPause()  # Plays a sound to alert the user
    print(messages.longPauseMessage())  # Shows the message telling the user that the long pause has started
    print(endTimes.longPauseTimeMessage)  # Shows the message telling the user when the current long pause will end
    notifications.longPauseStartNotification.show()  # Shows a notification with the same info as in the terminal
    userInput()  # Allows the user to enter commands during the ongoing phase
    time.sleep(variables.longPauseDuration * 60)  # We have to multiply since longPauseDuration is in minutes, not seconds
    setter.resetShortPauseCounter()  # The counter needs to reset in order to start a whole new cycle
    work()


# This is getting the input from the user and sends it to evaluate() in order to determine what to do with it
def userInput():
    print("Welcome to PyModoro, type *help* to see the available commands")
    x = input("Enter command: ")  # Allows user to enter command
    command = x.split()  # Splits the string entered by the user into multiple words so we can use them for evaluate()
    evaluate(command)  # Evaluates the user command to find out what to do with it
    return


# Evaluates the input given by the user
def evaluate(args):
    if len(args) == 1:  # If the length is only one, that means that the user is not trying to use one of the setters
        if args[0] == "s":  # Runs the program normally
            print("Starting program...")
            work()
        elif args[0] == "e":  # Exits the program
            print("Program exiting...")
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
        else:  # User has entered something wrong
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
        else:  # User has entered something wrong
            print("Invalid input, please correct!")
            userInput()


# Starts the program
userInput()
