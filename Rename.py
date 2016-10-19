#coding=utf-8
import os

def rename():
	path = '/Users/Macx/Downloads/workspace/水浒传/水浒/忠义堂';
	filelist = os.listdir(path);
	for files in filelist:
		Olddir = os.path.join(path,files)
		if os.path.isdir(Olddir):
			continue;
		filename = os.path.splitext(files)[0];
		filetype = os.path.splitext(files)[1];

		fileNameBefore = 'ZHONGYI_DONG';
		fileNameAfter = files.split('_')[1];

		if filename.find('_') >= 0:
			Newdir = os.path.join(path, fileNameBefore+'_'+fileNameAfter);

			if not os.path.isfile(Newdir):
				os.rename(Olddir, Newdir);



rename();