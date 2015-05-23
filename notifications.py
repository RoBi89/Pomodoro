#!/usr/bin/python
from gi.repository import Notify

import messages
import endTimes

Notify.init("Hello World")


workStartNotification = Notify.Notification.new((messages.workMessage), (endTimes.workTimeMessage), "dialog-information")
shortPauseStartNotification = Notify.Notification.new((messages.workMessage), (endTimes.workTimeMessage), "dialog-information")
longPauseStartNotification = Notify.Notification.new((messages.workMessage), (endTimes.workTimeMessage), "dialog-information")
