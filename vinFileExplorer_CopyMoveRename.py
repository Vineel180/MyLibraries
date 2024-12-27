import os
import shutil
import vinFileExplorer_Base
import vinStrings

def reduceFileNameLength(fileName):

def convertToValidFileName(fileName, autoReduceLongFileNames=False):

def convertToValidFolderPath(Path):
    Path = vinFileExplorer_Base.removeTrailingChars(Path, "\\")
    if not Path[0].lower() in vinStrings.listOfAlphabets_small:
        return False
    if Path[1] != ":":
        return False
    if Path[2] != "\\":
        return False

def convertToValidFolderPathAndObjectName(Path, autoReduceLongFileNames=False):
    Path = vinFileExplorer_Base.separatePath(Path)
    Path = convertToValidFolderPath(Path[0])
    if not Path:
        return False
    Name = convertToValidFileName(Path[1])
    if not Name:
        return False
    return os.path.join(Path, Name)

def getUniqueObjectName(Path, preUniqueIdStr=" (", postUniqueIdStr=")", uniqueIdStartValue=2):
    n = uniqueIdStartValue
    while vinFileExplorer_Base.getTargetType(Path) != 0:
        newPathList = vinFileExplorer_Base.separateExtension(Path)
        newPath = newPathList[0] + preUniqueIdStr + str(n) + postUniqueIdStr + "." + newPathList[1]
        n+=1
    return newPath

def renameObject(oldFilePath, newFileName, autoAddExtension=True, convertToValidPath=True, preUniqueIdStr=" (", postUniqueIdStr=")", uniqueIdStartValue=2, autoReduceLongFileNames=False):
    folderPath = ( vinFileExplorer_Base.separatePath(oldFilePath) )[0]
    if autoAddExtension:
        newFilePath = newFilePath + (vinFileExplorer_Base.separateExtension(oldFilePath))[-1]
    newFilePath = os.path.join(folderPath, newFileName)
    newFilePath = getUniqueObjectName(newFilePath, preUniqueIdStr, postUniqueIdStr, uniqueIdStartValue)
    newFilePath = convertToValidFolderPathAndObjectName(newFilePath, autoReduceLongFileNames)
    if newFilePath:
        os.rename(oldFilePath, newFilePath)
        return True
    else:
        return False
