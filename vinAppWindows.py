import pygetwindow

def getWindow(windowName, activate=True, maximize=True, restore=True):
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
