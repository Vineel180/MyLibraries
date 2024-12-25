""" UNFIN
def isValidPath_wfe():
def isValidName_wfe():
def moveTarget():
def copyTarget():
def renameTarget():
"""

import vinFileManagement_Base
import os

def reduceFileNameLength(fileName, newLength):

def convertToValidName_wfe(Name, preUniqueIdString=" (", postUniqueIdString=")"):

def convertToValidPath_wfe(Path, preUniqueIdString=" (", postUniqueIdString=")"):
    Path = vinFileManagement_Base.separatePath(Path)
    folderPath = Path[0]
    fileName = convertToValidName_wfe(Path[1], preUniqueIdString, postUniqueIdString)

def renameObject(oldFilePath, newFileName, addExtension=True, preUniqueIdString=" (", postUniqueIdString=")"):
    """
    i:
        addExtension = addExtension, if object is file
        convertToValidPath = convertToValidPath, and object name
    """

    oldFilePath = convertToValidPath_wfe(oldFilePath, preUniqueIdString, postUniqueIdString)
    folderPath = vinFileManagement_Base.separatePath(oldFilePath)[0]
    newFilePath = convertToValidPath_wfe( os.path.join(folderPath, newFileName) , preUniqueIdString, postUniqueIdString)
    os.rename(oldFilePath, newFilePath)


def createFolderPath(Path):
    os.makedirs(Path, exist_ok=True)
