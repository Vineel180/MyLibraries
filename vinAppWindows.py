# TESTED
import pygetwindow
import re

def getWindow(windowName, restore=True, activate=True, maximize=True):
    window = pygetwindow.getWindowsWithTitle(windowName)
    if window:
        window = window[0]
        #
        if restore:
            window.restore()
        if activate:
            window.activate()
        if maximize:
            window.maximize()
        #
        return True
    else:
        return False

def getWindow_regex(windowName_regex, restore=True, activate=True, maximize=True):
    allWindows = pygetwindow.getAllTitles()
    for i in allWindows:
        if re.search(windowName_regex, i):
            return getWindow(i, restore, activate, maximize)
    return False
