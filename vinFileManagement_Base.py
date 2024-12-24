import os

# SEPARATE STRING
def separateExtension(Path):
    """1
    o:
        list(str( remainder ), str( Extension ))
    """
    return Path.rsplit(".", 1)
def separatePath(Path):
    """1
    o:
        list(str( remainder ), str( OBJECT))
    """
    return Path.rsplit("\\", 1)
def removeTrailingChars(String, Char):
    while String[-1] == Char:
        String = String[:-1]
    return String

# CHECK IF OBJECT EXISTS
def doesFileExist(path):
    """1
    o:
        bool
    """
    if os.path.isfile(path):
        return True
    else:
        return False
def doesFolderExist(path):
    """1
    o:
        bool
    """
    if os.path.isdir(path):
        return True
    else:
        return False
def doesObjectExist(path):
    """1
    o:
        bool
    """
    if doesFileExist(path):
        return True
    elif doesFolderExist(path):
        return True
    else:
        return False

# FIND OBJECT TYPE
def isFile_ifFileExists(Path):
    """1
    NOTE: returns FALSE if object doesn't exist
        so, use doesObjectExist() beforehand to check if object exists
    o:
        bool
    """
    if os.path.isfile(Path):
        return True
    else:
        return False
def isFolder_ifFileExists(Path):
    """1
    NOTE: returns FALSE if object doesn't exist
        so, use doesObjectExist() beforehand to check if object exists
    o:
        bool
    """
    if os.path.isdir(Path):
        return True
    else:
        return False
