from os import path as osPath

def readFile(filePath):
    """
    o:
        str(fileData)
    """
    with open(filePath, "r") as file:
        fileData = file.read()
        return fileData

def writeFile_withOverwriteEnabled(filePath, dataToWrite=""):
    with open(filePath, "w") as file:
        file.write(dataToWrite)
    return True
def writeFile(filePath, dataToWrite="", overwriteIfFileAlreadyExists=False):
    if overwriteIfFileAlreadyExists:
        if osPath.isfile(filePath):
            return False
        else:
            return writeFile_withOverwriteEnabled(filePath, dataToWrite)
    else:
        return writeFile_withOverwriteEnabled(filePath, dataToWrite)
