#!/usr/bin/python
from gi.repository import Notify

import messages
import endTimes

Notify.init("Hello World")


def workStartNotification():
    wsn = Notify.Notification.new(messages.workMessage(), endTimes.workTimeMessage(), "dialog-information")
    wsn.show()


def shortPauseStartNotification():
    spsn = Notify.Notification.new(messages.shortPauseMessage(), endTimes.shortPauseTimeMessage(), "dialog-information")
    spsn.show()


def longPauseStartNotification():
    lpsn = Notify.Notification.new(messages.longPauseMessage(), endTimes.longPauseTimeMessage(), "dialog-information")
    lpsn.show()
