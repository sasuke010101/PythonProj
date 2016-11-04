import os.path
import shutil

def copyFiles(sourceDir,targetDir):
    for files in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,files)
        targetFile = os.path.join(targetDir,files)
        if os.path.isfile(sourceFile) and sourceFile.find('.txt')>0:
           shutil.copy(sourceFile,targetDir)

source = '/Users/Macx/Downloads/git/PythonProj/fileOperation/source'
target = '/Users/Macx/Downloads/git/PythonProj/fileOperation/target'
copyFiles(source,target)
