#!/usr/bin/env python

import os, sys, dbus, datetime

sessionBus = dbus.SessionBus()
purpleObj = sessionBus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(purpleObj, "im.pidgin.purple.PurpleInterface")

def pidgin_status(message):
	old_status = purple.PurpleSavedstatusGetCurrent()
	status_type = purple.PurpleSavedstatusGetType(old_status)
	new_status = purple.PurpleSavedstatusNew("", status_type)
	purple.PurpleSavedstatusSetMessage(new_status, message)
	purple.PurpleSavedstatusActivate(new_status)

date1 = datetime.datetime(2010,3,1,8,30,00)
date2 = datetime.datetime.now()
ddiff = date2 - date1

pidgin_status(str(ddiff.days) + ":" + str(ddiff.seconds / 3600))

#Log
print "Status changed at " + str(datetime.datetime.now())
