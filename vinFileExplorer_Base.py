import os

# SEPARATE STRING
def separateExtension(Path):
    """
    o:
        list(str( remainder ), str( Extension ))
    """
    x = Path.rsplit(".", 1)
    if len(x) == 1:
        return [ x[0] , "" ]
    else:
        return x
def separatePath(Path):
    """
    o:
        list(str( Path ), str( Target ))
    """
    return Path.rsplit("\\", 1)
def separate_folderPath_objectName_objectExtension_3(Path):
    List = []
    a = separatePath(Path)
    List.append(a[0])
    b = separateExtension(a[1])
    List = List + b
    return List

def removeTrailingChars(String, Char):
    while String[-1] == Char:
        String = String[:-1]
    return String

# MORE
def isFileOrFolderOrNone(Path):
    """
    o: int:
        2 IF object is a folder
        1 IF object is a file
        0 IF object doesn't exist
    """
    if os.path.isdir(Path):
        return 2
    elif os.path.isfile(Path):
        return 1
    else:
        return 0
def getTargetType(Path):
    """
    o: int:
        2 IF object is a folder
        1 IF object is a file
        0 IF object doesn't exist
    """
    return isFileOrFolderOrNone(Path)

def createFolderPath(Path):
    os.makedirs(Path, exist_ok=True)
