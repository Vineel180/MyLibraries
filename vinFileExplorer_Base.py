import os

# SEPARATE STRING
def separateExtension(Path):
    """
    o:
        list(str( remainder ), str( Extension ))
    """
    return Path.rsplit(".", 1)
def separatePath(Path):
    """
    o:
        list(str( Path ), str( Target ))
    """
    return Path.rsplit("\\", 1)
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
    return isFileOrFolderOrNone(Path)

def createFolderPath(Path):
    os.makedirs(Path, exist_ok=True)
