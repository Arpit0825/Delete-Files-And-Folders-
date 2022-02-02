from msilib.schema import RemoveFile
import os
import shutil
import time

path = 'C:/Users/hp/Desktop/whitehat/Python Projects/project99'

def removeFolder(path):
    if not shutil.rmtree(path):
        print(f'"{path}"is removed successfully')
    else:
        print(f'"{path}"cannot be deleted')

def removeFile(path):
    if not os.remove(path):
        print(f'"{path}"is removed successfully')
    else:
        print(f'"{path}"cannot be deleted')

def getFileOrFolder(path):
    cttime = os.stat(path).st_ctime
    return cttime

def main():
    deletedFolderCount = 0
    deletedFilesCount = 0

    
    days = 30
    seconds = time.time() - (days*24*60*60)
    if os.path.exists(path):
        for rootFolder,folder,files in os.walk(path):
            if seconds >= getFileOrFolder(rootFolder):
                removeFolder(rootFolder)
                deletedFolderCount = deletedFolderCount + 1
                break
            else:
                for f in folder:
                    folderPath = os.path.join(rootFolder,f)
                    if seconds >= getFileOrFolder(folderPath):
                        removeFolder(folderPath)
                        deletedFolderCount = deletedFolderCount + 1
                for file in files:
                    filePath = os.path.join(rootFolder,file)
                    if seconds >= getFileOrFolder(filePath):
                        removeFile(filePath)
                        deletedFilesCount = deletedFilesCount + 1
        else:
            if seconds >= getFileOrFolder(path):
                removeFile(path)
                deletedFilesCount = deletedFilesCount + 1
    else:
        print(f'"{path}" is not found')
        deletedFilesCount += 1
    print("Deleted Files Count: ",deletedFilesCount)
    print("Deleted Folders Conut: ",deletedFolderCount)

main()


    
