#
#   PreferencesController.py
#
#   Created by Jair Gaxiola on 15/01/11.
#   Copyright 2011 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
class PreferencesController (NSViewController):	
	def show(self):
		#print dir(PreferencesController)
		self.PreferencesController = PreferencesController.alloc().initWithNibName_bundle_("Preferences", None)
		#print dir(self.PreferencesController)
		self.PreferencesController.view()
		self.PreferencesController.retain()
	show = classmethod(show)


