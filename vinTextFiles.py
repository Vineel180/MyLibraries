# FUNCTIONS
def readFile(filePath):
    """tested"""
    with open(filePath, "r") as file:
        fileData = file.read()
        return fileData

def writeFile(filePath, dataToWrite):
    """tested"""
    with open(filePath, "w") as file:
        file.write(dataToWrite)
