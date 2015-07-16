#!/usr/bin/python

import variables


# These messages are shown at the beginning of each new phase
def workMessage():
    return("Start working! Your Pause begins in {} minutes".format(variables.workDuration))


def shortPauseMessage():
    return("Well done! Have a break. It ends in {} minutes".format(variables.shortPauseDuration))


def longPauseMessage():
    return("Now you deserve a longer break! Take {} minutes to get some rest".format(variables.longPauseDuration))
