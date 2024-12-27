import os
import shutil
import vinFileExplorer_Core


def copyObject(oldFilePath, newFilePath, autoAddExtension=True, preUniqueIdStr=" (", postUniqueIdStr=")"):
    oldFilePath = 
    if not vinFileExplorer_Core.getTargetType(oldFilePath):
        
    newFolderPath = vinFileExplorer_Core.separatePath(newFilePath)[0]
    if not vinFileExplorer_Core.createFolderPath(newFolderPath):
    if autoAddExtension:
        newFilePath = newFilePath + vinFileExplorer_Core.separateExtension(oldFilePath)[1]

    shutil.copy2(oldFilePath, newFilePath)

def moveObject():
def renameObject():