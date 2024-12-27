from psutil import process_iter

def isAppRunning(appName):
    """
    o:
        bool
    """
    for i in process_iter(["name"]):
        if appName == i.info["name"]:
            return True
    return False

def stopApp(appName, return_ifRunning=False):
    """
    NOTE: returns FALSE if app was not running
    o:
        bool(ifSuccessful)
        bool(ifRunning) is OFF by default
    """
    for i in process_iter(["pid", "name"]):
        if appName == i.info["name"]:
            try:
                i.terminate()
                #
                if return_ifRunning:
                    return True, True
                else:
                    return True
                #
            except Exception:
                #
                if return_ifRunning:
                    return False, True
                else:
                    return False
                #
    if return_ifRunning:
        return False, False
    else:
        return False
