"""
import using
from vinBase import *
"""

def p(Print=""):
    """1
    print()
    """
    print(Print)

def i(Input=""):
    """1
    input()
    """
    input(Input)

def printElementsInIterator(Iterator):
    for i in Iterator:
        print(i)

def convertToGoodPath(Path):
    while Path[-1] == "\\":
        Path = Path[:-1]
    return Path
