def readFile(filePath):
    """
    o:
        str(fileData)
    """
    with open(filePath, "r") as file:
        fileData = file.read()
        return fileData

def writeFile(filePath, dataToWrite=""):
    """
    """
    with open(filePath, "w") as file:
        file.write(dataToWrite)
