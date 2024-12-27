import vinFileManagement_Base
import os
import re

# GET ALL OBJECTS IN FOLDER
def getFilesInFolder_multiLayer(Path):
    """
    o:
        list(object name, with path)
            ie has PATH
    """
    List = []
    for root, folders, files in os.walk(Path):
        for file in files:
            List.append( os.path.join(root, file) )
    return List
def getFoldersInFolder_multiLayer(Path):
    """
    o:
        list(object name, with path)
            ie has PATH
    """
    List = []
    for root, folders, files in os.walk(Path):
        for folder in folders:
            List.append( os.path.join(root, folder) )
    return List
def getFilesAndFoldersInFolder_multiLayer(Path):
    """
    o:
        list(object name, with path)
            ie has PATH
    """
    List = []
    List = List + getFilesInFolder_multiLayer(Path)
    List = List + getFoldersInFolder_multiLayer(Path)
    return List

def getFilesInFolder_singleLayer(Path):
    """
    o:
        list(objects)
            ie has NO PATH
    """
    List = []
    for i in os.listdir(Path):
        if os.path.isfile(os.path.join(Path, i)):
            List.append(i)
    return List
def getFoldersInFolder_singleLayer(Path):
    """
    o:
        list(objects)
            ie has NO PATH
    """
    List = []
    for i in os.listdir(Path):
        if os.path.isdir(os.path.join(Path, i)):
            List.append(i)
    return List
def getFilesAndFoldersInFolder_singleLayer(Path):
    """
    o:
        list(objects)
            ie has NO PATH
    """
    return os.listdir(Path)

# SEARCH
def searchFilesInFolder_withExtensions__multiLayer(Path, extensionList):
    """
    p:
        get files in folder with extensions in extensionList
    o:
        list(file names, with path)
            ie has PATH
    """
    listOfFiles = getFilesInFolder_multiLayer(Path)
    newList = []
    for i in listOfFiles:
        if (vinFileManagement_Base.separateExtension(i))[-1] in extensionList:
            newList.append(i)
    return newList
def searchFilesInFolder_withExtensions__singleLayer(Path, extensionList):
    """
    p:
        get files in folder with extensions in extensionList
    o:
        list(file names)
            ie has NO PATH
    """
    listOfFiles = getFilesInFolder_singleLayer(Path)
    newList = []
    for i in listOfFiles:
        if (vinFileManagement_Base.separateExtension(i))[-1] in extensionList:
            newList.append(i)
    return newList

def searchFiles_Ya_FoldersInFolder_usingRegex__multiLayer(Path, regexPattern, _0IfBoth_1IfFiles_2IfFolders_=0):
    """
    o:
        list(files and/or folders, with path)
            ie has PATH
    """
    if _0IfBoth_1IfFiles_2IfFolders_ == 2:
        listOfObjects = getFoldersInFolder_multiLayer(Path)
    elif _0IfBoth_1IfFiles_2IfFolders_ == 1:
        listOfObjects = getFilesInFolder_multiLayer(Path)
    else:
        listOfObjects = getFilesAndFoldersInFolder_multiLayer(Path)
    newList = []
    for i in listOfObjects:
        if re.search(regexPattern, i):
            newList.append(i)
    return newList
def searchFiles_Ya_FoldersInFolder_usingRegex__singleLayer(Path, regexPattern, _0IfBoth_1IfFiles_2IfFolders_=0):
    """
    o:
        list(file and/or folder names)
            ie has NO PATH
    """
    if _0IfBoth_1IfFiles_2IfFolders_ == 2:
        listOfObjects = getFoldersInFolder_singleLayer(Path)
    elif _0IfBoth_1IfFiles_2IfFolders_ == 1:
        listOfObjects = getFilesInFolder_singleLayer(Path)
    else:
        listOfObjects = getFilesAndFoldersInFolder_singleLayer(Path)
    newList = []
    for i in listOfObjects:
        if re.search(regexPattern, i):
            newList.append(i)
    return newList
