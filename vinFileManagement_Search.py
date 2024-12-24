import vinFileManagement_Base
import os
import re

# GET OBJECTS IN FOLDER
def getFilesInFolder_osWalk(Path):
    """1
    o:
        list(object name with path)
    """
    List = []
    for root, folders, files in os.walk(Path):
        for file in files:
            List.append( os.path.join(root, file) )
    return List
def getFoldersInFolder_osWalk(Path):
    """1
    o:
        list(object name with path)
    """
    List = []
    for root, folders, files in os.walk(Path):
        for folder in folders:
            List.append( os.path.join(root, folder) )
    return List
def getFilesAndFoldersInFolder_osWalk(Path):
    """1
    o:
        list(object name with path)
    """
    List = []
    for i in getFilesInFolder_osWalk(Path):
        List.append(i)
    for i in getFoldersInFolder_osWalk(Path):
        List.append(i)
    return List

# SEARCH
def searchFilesInFolder_withExtensions__osWalk(Path, extensionList):
    """1
    p:
        get files in folder with extensions in extensionList
    o:
        list(file names with path)
    """
    listOfFiles = getFilesInFolder_osWalk(Path)
    newList = []
    for i in listOfFiles:
        if (vinFileManagement_Base.separateExtension(i))[-1] in extensionList:
            newList.append(i)
    return newList
def searchFiles_Ya_FoldersInFolder_usingRegex__osWalk(Path, regexPattern, BothIs0_FilesIs1_FoldersIs2=0):
    """1
    o:
        list(files and/or folders with path)
    """
    if BothIs0_FilesIs1_FoldersIs2 == 2:
        listOfObjects = getFoldersInFolder_osWalk(Path)
    elif BothIs0_FilesIs1_FoldersIs2 == 1:
        listOfObjects = getFilesInFolder_osWalk(Path)
    else:
        listOfObjects = getFilesAndFoldersInFolder_osWalk(Path)
    newList = []
    for i in listOfObjects:
        if re.search(regexPattern, i):
            newList.append(i)
    return newList
