from sys import stdout

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

### ### ### ### ###

# FUNCTIONS
def printSpecial(textToPrint="", printAttribute="", endingChar="\n"):
    """1
    i:
        chain printAttribute using +
    """
    print(f"{printAttribute}{textToPrint}\033[0m", end=endingChar)
def inputSpecial(textToPrint="", printAttribute="", inputAttribute=""):
    """1
    i:
        chain printAttribute/inputAttribute using +
    o:
        str(userInput)
    """
    print(f"{printAttribute}{textToPrint}\033[0m{inputAttribute}", end="")
    userInput = input()
    print("\033[0m", end="")
    return userInput

def getSameLengthNumbers_range(endAtNumber, paddingChar=" ", paddingCharPosition_falseIfPre_trueIfPost=True, 
                               anyNumberExcept_endAtNumber_isNegative__And__endAtNumber_isPositive=False, 
                               startAtNumber=1, stepSize=1, preNumberString="", postNumberString=""):
    """1
    for -ve numbers use anyNumberExcept_endAtNumber_isNegative__And__endAtNumber_isPositive
    """
    listOfNumbers = range(startAtNumber, endAtNumber+1, stepSize)
    if anyNumberExcept_endAtNumber_isNegative__And__endAtNumber_isPositive:
        lenOfLargestNumber = len(str(endAtNumber))+1
    else:
        lenOfLargestNumber = len(str(endAtNumber))
    newListOfNumbers = []
    for i in listOfNumbers:
        i = str(i)
        lenDiff = lenOfLargestNumber - len(i)
        i = preNumberString + i + postNumberString
        if paddingCharPosition_falseIfPre_trueIfPost:
            for j in range(lenDiff):
                i = i + paddingChar
        else:
            for j in range(lenDiff):
                i = paddingChar + i
        newListOfNumbers.append(i)
    return newListOfNumbers

def getSameLengthNumber_instanceIterator(numberToConvert, LargestNumber,
                                         paddingChar=" ", paddingCharPosition_falseIfPre_trueIfPost=True, preNumberString="", postNumberString=""):
    """1
    """
    number = str(numberToConvert)
    if number.startswith("-"):
        len_ofLargestNumber = len(str(LargestNumber))+1
    else:
        len_ofLargestNumber = len(str(LargestNumber))
    lenDiff = len_ofLargestNumber - len(number)
    number = preNumberString + number + postNumberString
    if paddingCharPosition_falseIfPre_trueIfPost:
        for j in range(lenDiff):
            number = number + paddingChar
    else:
        for j in range(lenDiff):
            number = paddingChar + number
    return number

def setTerminalTitle(terminalTitle="Python Terminal"):
    """1
    """
    print(f"\033]0;{terminalTitle}\007", end="")

def setAndPrintSpecialTerminalTitle(terminalTitle="Python Terminal", printAttribute=ReverseColours, endingChar="\n\n", addToPrintOnly_Pre = " ", addToPrintOnly_Post = " "):
    """1
    """
    print(f"\033]0;{terminalTitle}\007", end="")
    printSpecial(addToPrintOnly_Pre+terminalTitle+addToPrintOnly_Post, printAttribute, endingChar)
