# TESTED
# VARIABLES
# Text
Reset = "\033[0m"
Blinking = "\033[5m"
Bright = "\033[1m"
Dim = "\033[2m"
Italic = "\033[3m"
Underline = "\033[4m"
ReverseColours = "\033[7m"
HideText = "\033[8m"

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
    """
    i:
        chain printAttribute using +
    """
    print(f"{printAttribute}{textToPrint}\033[0m", end=endingChar)

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

def setTerminalTitle(terminalTitle="Python Terminal"):
    print(f"\033]0;{terminalTitle}\007", end="")
