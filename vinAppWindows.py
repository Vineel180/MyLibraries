import pygetwindow
import re

def showWindow(windowName, restore=True, activate=True, maximize=True):
    """
    o:
        bool
    """
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

def showWindow_regex(windowName_regex, restore=True, activate=True, maximize=True):
    """
    o:
        bool
    """
    allWindows = pygetwindow.getAllTitles()
    for i in allWindows:
        if re.search(windowName_regex, i):
            return showWindow(i, restore, activate, maximize)
    return False
