from socket import create_connection
from time import sleep

def checkInternetConnection(tryForXSecsMax = 3):
    """1
    o:
        bool
    """
    try:
        create_connection(("8.8.8.8", 53), timeout=tryForXSecsMax)
        return True
    except OSError:
        return False

def waitForInternetConnection(retryEveryXSecs = 3, tryForXSecsMax_perCycle = 3):
    """1
    """
    while not checkInternetConnection(tryForXSecsMax_perCycle):
        sleep(retryEveryXSecs)
