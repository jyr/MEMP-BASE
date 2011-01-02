#
#   MEMPController.py
#
#   Created by Jair Gaxiola on 01/01/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
import os

class MEMPController(NSWindowController):
	path = "/Applications/MEMP/init/"
	
	@objc.IBAction
	def startServers_(self, sender):
		print "start servers"
	
	@objc.IBAction
	def stopServers_(self, sender):
		print "stop servers"
	
	@objc.IBAction
	def openPage_(self, sender):
		print "opan memp page"
	
	@objc.IBAction
	def exit_(self, sender):
		self.stopServers_(self)
		NSApp().terminate_(self)



