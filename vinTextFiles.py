def readFile(filePath):
    """1
    o:
        str(fileData)
    """
    with open(filePath, "r") as file:
        fileData = file.read()
        return fileData
def writeFile(filePath, dataToWrite=""):
    """1
    """
    with open(filePath, "w") as file:
        file.write(dataToWrite)
