from psutil import process_iter

def isAppRunning(appName):
    """1
    o:
        bool
    """
    for i in process_iter(["name"]):
        if i.info["name"] == appName:
            return True
    return False
def stopApp(appName, printError=False):
    """1
    NOTE: returns FALSE if app was not running
    o:
        bool
    """
    for i in process_iter(["pid", "name"]):
        if appName in i.info["name"]:
            try:
                i.terminate()
                return True
            except Exception as e:
                if printError:
                    print(f"Failed to terminate {appName}: {e}")
                return False
    if printError:
        print(f"App {appName} is not running.")
    return False
