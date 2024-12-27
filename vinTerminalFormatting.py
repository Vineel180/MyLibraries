from sys import stdout
#
try:
    from vinBase_IO import *
except ImportError:
    importError = True

# VARIABLES
# Text
Reset = "\033[0m"
Blinking = "\033[5m"
Bright=Bold = "\033[1m"
Dim = "\033[2m"
Italic = "\033[3m"
Underline = "\033[4m"
ReverseColours=ReverseTextAndBgColours = "\033[7m"
HideText=ConcealText = "\033[8m"
# More
def clearScreen():
    stdout.write("\033[3J")
    stdout.flush()
def sendCursorToHome():
    stdout.write("\033[H")
    stdout.flush()
def clearScreen_And_sendCursorToHome():
    clearScreen()
    sendCursorToHome()

# Text Colours
Black = "\033[30m"
Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
Cyan = "\033[36m"
White = "\033[37m"
# Background Colours (Normal)
bgBlack = "\033[40m"
bgRed = "\033[41m"
bgGreen = "\033[42m"
bgYellow = "\033[43m"
bgBlue = "\033[44m"
bgMagenta = "\033[45m"
bgCyan = "\033[46m"
bgWhite = "\033[47m"
# Background Colours (Bright)
bgBlackBright = "\033[100m"
bgRedBright = "\033[101m"
bgGreenBright = "\033[102m"
bgYellowBright = "\033[103m"
bgBlueBright = "\033[104m"
bgMagentaBright = "\033[105m"
bgCyanBright = "\033[106m"
bgWhiteBright = "\033[107m"

### ### ### ### ### ### ### ### ### ###

# FUNCTIONS
def printSpecial(textToPrint="", printAttribute="", endingChar="\n"):
    """
    i:
        chain printAttribute using +
    """
    print(f"{printAttribute}{textToPrint}\033[0m", end=endingChar)
def pSpecial(textToPrint="", printAttribute="", endingChar="\n"):
    """
    i:
        chain printAttribute using +
    """
    printSpecial(textToPrint, printAttribute, endingChar)

def inputSpecial(textToPrint="", printAttribute="", inputAttribute=""):
    """
    i:
        chain printAttribute/inputAttribute using +
    o:
        str(userInput)
    """
    print(f"{printAttribute}{textToPrint}\033[0m{inputAttribute}", end="")
    userInput = input()
    print("\033[0m", end="")
    return userInput
def iSpecial(textToPrint="", printAttribute="", inputAttribute=""):
    """
    i:
        chain printAttribute/inputAttribute using +
    o:
        str(userInput)
    """
    return inputSpecial(textToPrint, printAttribute, inputAttribute)

def setTerminalTitle(terminalTitle="Python Terminal"):
    """
    """
    print(f"\033]0;{terminalTitle}\007", end="")

def setAndPrintTerminalTitle(terminalTitle="Python Terminal", printAttribute=ReverseColours, endingChar="\n\n", addToPrintOnly_Pre = " ", addToPrintOnly_Post = " "):
    """
    NOTE: read default settings
    """
    print(f"\033]0;{terminalTitle}\007", end="")
    printSpecial(addToPrintOnly_Pre + terminalTitle + addToPrintOnly_Post, printAttribute, endingChar)

def getSameLengthNumbers_iterator(numberToConvert, largestNumber, paddingChar=" ", paddingCharPosition_falseIfPre_trueIfPost=False, preNumStr="", postNumStr=""):
    """
    p:
        An iterator (ie a single number/time)
    o:
        str(customized number)
    """
    number = str(numberToConvert)
    lenDiff = len(str(largestNumber)) - len(number)
    number = preNumStr + number + postNumStr
    if paddingCharPosition_falseIfPre_trueIfPost:
        for i in range(lenDiff):
            number = number + paddingChar
    else:
        for i in range(lenDiff):
            number = paddingChar + number
    return number
