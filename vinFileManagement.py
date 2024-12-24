from dynFileManagement_Settings import listOfPrimaryDrives_inWindowsFileExplorer
import os

# SEPARATE STRING
def separatePath(Path):
    return Path.rsplit("\\", 1)
def separateExtension(Path):
    return Path.rsplit(".", 1)

# FIND OBJECT TYPE
def isFile(Path):
    """
    returns FALSE if object doesn't exist
    """
    if os.path.isfile(Path):
        return True
    else:
        return False
def isFolder(Path):
    """
    returns FALSE if object doesn't exist
    """
    if os.path.isdir(Path):
        return True
    else:
        return False

# CHECK IF OBJECT EXISTS
def doesFileExist(path):
    if os.path.isfile(path):
        return True
    else:
        return False
def doesFolderExist(path):
    if os.path.isdir(path):
        return True
    else:
        return False

# GET LIST OF OBJECTS IN FOLDER
def getFilesAndFoldersInFolder_std(folderPath, appendRootFolder=False):
    List = []
    #
    if appendRootFolder:
        for i in os.listdir(folderPath):
            List.append(os.path.join(folderPath, i))
    else:
        for i in os.listdir(folderPath):
            List.append(i)
    #
    return List
def getFilesInFolder_std(folderPath, appendRootFolder=False):
    List = getFilesAndFoldersInFolder_std(folderPath, True)
    newList = []
    if appendRootFolder:
        for i in List:
            if os.path.isfile(i):
                newList.append(i)
    else:
        for i in List:
            if os.path.isfile(i):
                newList.append(separatePath(i)[1])
    return newList
def getFoldersInFolder_std(folderPath, appendRootFolder=False):
    List = getFilesAndFoldersInFolder_std(folderPath, True)
    newList = []
    if appendRootFolder:
        for i in List:
            if os.path.isdir(i):
                newList.append(i)
    else:
        for i in List:
            if os.path.isdir(i):
                newList.append(separatePath(i)[1])
    return newList

# RENAME
def isValidExplorerPath(Path):
    if len(Path) > 260:
        return False

def renameFull(oldFilePATH, newFileNAME, convertToValidFileName=True, convertToValidFolderPath=False, fileExtensionAutoAdd=True, preUniqueId=" (", postUniqueId=")"):
    folderPath = separatePath(oldFilePATH)[0]
    os.rename(oldFilePATH, os.path.join(folderPath, newFileNAME))
