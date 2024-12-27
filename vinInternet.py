from socket import create_connection
from time import sleep

def checkInternetConnection(maxResponseWaitTime=3):
    """
    o:
        bool
    """
    try:
        create_connection(("8.8.8.8", 53), timeout=maxResponseWaitTime)
        return True
    except OSError:
        return False

def waitForInternetConnection(retryEveryXSecs = 3, maxResponseWaitTime_perCycle = 3):
    """
    """
    while not checkInternetConnection(maxResponseWaitTime_perCycle):
        sleep(retryEveryXSecs)
