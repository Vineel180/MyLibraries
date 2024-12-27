import os
import vinFileExplorer_Core
import vinStrings

# VARIABLES
osReservedFileNames = [
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
]

# FUNCTIONS
def getUniqueObjectName(filePATH, preUniqueIdStr=" (", postUniqueIdStr=")", startUniqueIdAt=2):
    filePATH_list = vinFileExplorer_Core.separateExtension(filePATH_list)
    while vinFileExplorer_Core.getTargetType(filePATH):
        filePATH = filePATH_list[0] + preUniqueIdStr + str(startUniqueIdAt) + postUniqueIdStr + "." + filePATH_list[1]
        startUniqueIdAt+=1
    return filePATH

def convertIllegalChars(String):
    inputList  = ["\\", ""]
    outputList = []
    for i in range(len(String)):
        if String[i] in inputList:
            String[i] = outputList[ inputList.index( String[i] ) ]
    return String

def convertToValidFolderPathAndObjectName_forThisInstance(filePath):
    global osReservedFileNames

    # for "C:\" only
    if (filePath[0]).lower() not in vinStrings.listOfAlphabets_small:
        return False, 2
    if filePath[1] != ":":
        return False, 2
    if filePath[2] !="\\":
        return False, 2
    #done

    #checking if all folders and files (in the path) are valid
    filePath = filePath.split("\\")
    for i in filePath[1:]:
        if i:
            i = i.strip()
            i = vinFileExplorer_Core.removeTrailingChars(i, ".")
            if i in osReservedFileNames:
                i = i + "_"
            i = convertIllegalChars(i)

    filePath_list[-1] = 

def renameObject(oldFilePath, newFileName, autoAddExtension, checkIf_oldFilePath_exists=True):

    """
    o:
        output 1:
            str(newPath) | success
            False        | invalid path/s as input
        output 2 (int):
            0 | success
            1 | oldFilePath does not exist
    """

    #check if oldFilePath exists
    if checkIf_oldFilePath_exists:
        if not vinFileExplorer_Core.getTargetType(oldFilePath):
            return False, 1
    #done (simple)
    
    #convert newFileName to newFilePath, by adding folderPath and fileExtension
    folderPath = vinFileExplorer_Core.separatePath(oldFilePath)[0]
    if autoAddExtension:
        newFileName = newFileName + "." + vinFileExplorer_Core.separateExtension(oldFilePath)[1]
    newFilePath = os.path.join(folderPath, newFileName)
    #with this, the base newFilePath has been created

    """ this function family is, relatively speaking, insanely complicated: do not try to edit it without making a backup of this function family (ie file) """
    """ this segment of the function is for generating the new newFilePath"""
    newFilePath = convertToValidFolderPathAndObjectName_forThisInstance(newFilePath)

    #create the finalFolderPath, if it doesn't exist --- according to the new newFilePath
    os.makedirs( ( vinFileExplorer_Core.separatePath(newFilePath) )[0] )
    #done

    #do the actual renaming, with the new newFilePath
    os.rename(oldFilePath, newFilePath)
    return newFilePath, 0
    #done (simple)
