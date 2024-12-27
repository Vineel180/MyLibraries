"""
import using
from vinBase import *
"""

def p(Print=""):
    """
    print()
    """
    print(Print)

def pNL0(Print=" "):
    r"""
    print() without \n
    """
    print(Print, end="")

def pNL2(Print=""):
    r"""
    print() with an extra \n
    """
    print(Print + "\n")

def i(Input=""):
    """
    p:
        input()
    o:
        str(userInput)
    """
    return input(Input)

def pIterator(Iterator):
    """
    """
    for i in Iterator:
        print(i)
