"""
import using
from vinBase import *
"""

def p(Print=""):
    """1
    print()
    """
    print(Print)
def printNL(textToPrint):
    r"""1
    print() without \n
    """
    print(textToPrint, end="")
def pp(Print):
    r"""1
    print() with an extra \n
    """
    print(Print + "\n")
def i(Input=""):
    """1
    p:
        input()
    o:
        str(userInput)
    """
    return input(Input)
def printElementsInIterator(Iterator):
    for i in Iterator:
        print(i)
def isElementInIterator(Element, Iterator):
    if Element in Iterator:
        return True
    else:
        return False

def convertToGoodPath(Path):
    while Path[-1] == "\\":
        Path = Path[:-1]
    return Path
