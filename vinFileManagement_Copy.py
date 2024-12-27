import os
import shutil
import vinFileManagement_Base

def reduceFileNameLength(fileName):

def convertToValidFileName(fileName):

def convertToValidFolderPath(Path):

def convertToValidFolderPathAndObjectName(Path):
    if len(Path)>260:


def renameObject(oldFilePath, newFileName, autoAddExtension=True, convertToValidPath=True, preUniqueIdStr=" (", postUniqueIdStr=")", autoReduceLongFileNames=False):
    folderPath = ( vinFileManagement_Base.separatePath(oldFilePath) )[0]
    if autoAddExtension:
        newFilePath = newFilePath + (vinFileManagement_Base.separateExtension(oldFilePath))[-1]
    newFilePath = os.path.join(folderPath, newFileName)

    newFilePath = 
    os.rename(oldFilePath, newFilePath)

"""
if not os.path.isdir(folderPath):
    os.makedirs(folderPath)
"""
