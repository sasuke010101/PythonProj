#coding=utf-8
import os

def GetFileNameAndExt(filename):
	(filepath,tempfilename) = os.path.split(filename);
 	(shotname,extension) = os.path.splitext(tempfilename);
 	return shotname

def GetFileList(dir, fileList):
	newDir = dir
	if os.path.isfile(dir):
		fileList.append('SoundName.'+GetFileNameAndExt(dir)+' = '+'"'+GetFileNameAndExt(dir)+'"')
	elif os.path.isdir(dir):
		for s in os.listdir(dir):
			newDir=os.path.join(dir,s)
			GetFileList(newDir, fileList)
	return fileList

list = GetFileList('/Users/Macx/Downloads/workspace/百家乐配音/百家乐剪辑配音/百家乐标准女', [])
for e in list:
	print e