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

def stopApp(appName):
    """
    o:
        0: App was terminated
        1: Failed to terminate app
        2: App was not running
    """
    for i in process_iter(["pid", "name"]):
        if appName == i.info["name"]:
            try:
                i.terminate()
                return 0
            except Exception:
                return 1
    return 2
