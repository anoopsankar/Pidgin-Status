#!/usr/bin/env python

import os, sys, dbus, datetime
import weather

sessionBus = dbus.SessionBus()
purpleObj = sessionBus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(purpleObj, "im.pidgin.purple.PurpleInterface")

def pidgin_status(message):
	old_status = purple.PurpleSavedstatusGetCurrent()
	status_type = purple.PurpleSavedstatusGetType(old_status)
	new_status = purple.PurpleSavedstatusNew("", status_type)
	purple.PurpleSavedstatusSetMessage(new_status, message)
	purple.PurpleSavedstatusActivate(new_status)

def format_status():
	symbolLookup = {
	    'clear':u'\u263C',
	    'partly sunny':u'\u2600',
	    'scattered thunderstorms':u'\u2602',
	    'showers':u'\u2602',
	    'scattered showers':u'\u2602',
	    'overcast':u'\u2601',
	    'chance of rain':u'\u2601',
	    'sunny':u'\u2600',
	    'mostly sunny':u'\u2600',
	    'partly cloudy':u'\u2601',
	    'mostly cloudy':u'\u2601',
	    'chance of storm':u'\u2601',
	    'rain':u'\u2602',
	    'chance of snow':u'\u2603',
	    'cloudy':u'\u2601',
	    'mist':u'\u2601',
	    'storm':u'\u2601',
	    'thunderstorm':u'\u2602',
	    'chance of tstorm':u'\u2602',
	    'light rain':u'\u2602'
	}

	weatherString = weather.getWeather("Kochi")
	return symbolLookup[weatherString.lower()]

status = format_status()
pidgin_status(status)

print status
