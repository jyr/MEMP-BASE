#
#   PreferencesController.py
#
#   Created by Jair Gaxiola on 15/01/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *

import objc

class PreferencesController (NSWindowController):
#class PreferencesController (NSViewController):
	start = objc.IBOutlet()
	stop = objc.IBOutlet()
	open = objc.IBOutlet()
	nginxPort = objc.IBOutlet()
	mysqlPort = objc.IBOutlet()
	phpPort = objc.IBOutlet()

	def init(self):
		#self.setSettings(self.start, "start")
		self.initWithWindowNibName_("Preferences")
		#print dir(self.window())
		return self
	#def awakeFromNib(self):
		#print dir(self.start)
		#self.setSettings(self.start, "start")
		#settings = NSUserDefaults.standardUserDefaults()
		#startMEMP = settings.boolForKey_("start")
		#print startMEMP
		#print dir(self)
		#if startMEMP:
		#	self.start.setState_(NSOnState)
		#else:
		#	self.start.setState_(NSOffState)
	
	def windowDidLoad(self):
		#super(PreferencesController, self).windowDidLoad()
		#print dir(self.start)
		self.setSettings(self.start, "start")
		#return self

	def show(self):
		#print dir(self.preferencesController)
		#if self.preferencesController == None:
		self.preferencesController = PreferencesController.alloc().init()
		self.preferencesController.showWindow_(self)
		#self.PreferencesController.window().makeKeyAndOrderFront_(self)
	#	self.PreferencesController = PreferencesController.alloc().initWithNibName_bundle_("Preferences", None)
	#	self.PreferencesController.view().window().makeKeyAndOrderFront_(self)
		#print dir(self.PreferencesController)
		#print dir(self.preferencesController.start)
	#	self.setSettings(self.start, "start")
		#return self.preferencesController
		#pass
	show = classmethod(show)
	
	def setSettings(self, field, name):
		settings = NSUserDefaults.standardUserDefaults()
		startMEMP = settings.boolForKey_(name)
		print startMEMP
		#print dir(self.start)
		if startMEMP:
			field.setState_(NSOnState)
		else:
			field.setState_(NSOffState)

	@objc.IBAction
	def savePreferences_(self, sender):
		settings = NSUserDefaults.standardUserDefaults()
		
		if self.start.state():
			print "On"
			settings.setObject_forKey_("On", 'start')
		else:
			print "Off"
			settings.setObject_forKey_("Off", 'start')
		
		if self.stop.state():
			print "On"
			settings.setObject_forKey_("On", 'stop')
		else:
			print "Off"
			settings.setObject_forKey_("Off", 'stop')
		
		if self.open.state():
			print "On"
			settings.setObject_forKey_("On", 'open')
		else:
			print "Off"
			settings.setObject_forKey_("Off", 'open')
		
		if self.nginxPort.stringValue():
			print "On nginx"
			settings.setObject_forKey_(self.nginxPort.stringValue(), 'nginxPort')
		else:
			print "Off"
			settings.setObject_forKey_("80", 'nginxPort')
		
		if self.mysqlPort.stringValue():
			print "On"
			settings.setObject_forKey_(self.mysqlPort.stringValue(), 'mysqlPort')
		else:
			print "Off"
			settings.setObject_forKey_("3306", 'mysqlPort')
		
		if self.phpPort.stringValue():
			print "On"
			settings.setObject_forKey_(self.phpPort.stringValue(), 'phpPort')
		else:
			print "Off"
			settings.setObject_forKey_("9000", 'phpPort')
			
		settings.synchronize()
		

