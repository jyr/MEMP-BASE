#
#  main.py
#  memp
#
#  Created by Jair Gaxiola on 01/01/11.
#  Copyright __MyCompanyName__ 2011. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import mempAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
