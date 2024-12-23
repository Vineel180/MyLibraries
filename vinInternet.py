from socket import create_connection
from time import sleep

def checkInternetConnection(responseWaitTime = 3):
    try:
        create_connection(("8.8.8.8", 53), timeout=responseWaitTime)
        return True
    except OSError:
        return False

def waitForInternetConnection(retryEveryXSecs = 3, responseWaitTime = 3):
    while not checkInternetConnection(responseWaitTime):
        sleep(retryEveryXSecs)
