import os
import vinFileExplorer_Base
import vinStrings

def convertToValidFolderPathAndObjectName(filePath):
    if (filePath[0]).lower() not in vinStrings.listOfAlphabets_small:
        return False, 2
    if filePath[1] != ":":
        return False, 2
    if filePath[2] !="\\":
        return False, 2
    filePath_list = filePath.split("\\")
    for i in filePath_list[1:-1]:
        i = i.strip()
        i = vinFileExplorer_Base.removeTrailingChars(i, ".")

    filePath_list[-1] = 

def getUniqueObjectName(filePATH, preUniqueIdStr=" (", postUniqueIdStr=")", startUniqueIdAt=2):
    newFilePath = filePATH
    n = startUniqueIdAt
    while not vinFileExplorer_Base.getTargetType(newFilePath):

        n+=1
    return newFilePath


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
        if not vinFileExplorer_Base.getTargetType(oldFilePath):
            return False, 1
    #done (simple)
    
    #convert newFileName to newFilePath, by adding folderPath and fileExtension
    folderPath = vinFileExplorer_Base.separatePath(oldFilePath)[0]
    if autoAddExtension:
        newFileName = newFileName + "." + vinFileExplorer_Base.separateExtension(oldFilePath)[1]
    newFilePath = os.path.join(folderPath, newFileName)
    #with this, the base newFilePath has been created

    """
    this function family is, relatively speaking, insanely complicated: do not try to edit it without making a backup of this function family (ie file)
    """
    newFilePath = convertToValidFolderPathAndObjectName(newFilePath)

    #create the finalFolderPath, if it doesn't exist --- according to the new newFilePath
    os.makedirs( ( vinFileExplorer_Base.separatePath(newFilePath) )[0] )
    #done

    #do the actual renaming, with the new newFilePath
    os.rename(oldFilePath, newFilePath)
    return newFilePath, 0
    #done (simple)
