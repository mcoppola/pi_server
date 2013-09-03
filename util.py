import zipfile, os, shutil

def zipdir(name, path):
	zipper(path, name)
	#shutil.make_archive(name, "zip", path)
	
	# zip = zipfile.ZipFile(name, 'w')
	# for root, dirs, files in os.walk(path):
	# 	for file in files:
	# 		zip.write(os.path.join(root, file))
	# zip.close()

def formatLoc(loc):
	formated = ''
	locs = loc.split('/')
	for l in locs:
		if l != '':
			formated += l + ' / '
	return formated

def unzip(zipFilePath, destDir):
    zfile = zipfile.ZipFile(zipFilePath)
    for name in zfile.namelist():
    	print 'name = ' + name
        (dirName, fileName) = os.path.split(name)
        print 'dirName = ' + dirName + ' fileName = ' + fileName
        if dirName != '':
            # directory
            newDir = destDir + '/' + dirName
            print newDir
            if not os.path.exists(newDir):
                os.mkdir(newDir)
            if fileName != '':
	            fd = open(newDir + '/' + fileName, 'wb')
	            fd.write(zfile.read(name))
	            fd.close()
        else:
            # file
            fd = open(destDir + '/' + name, 'wb')
            fd.write(zfile.read(name))
            fd.close()
    zfile.close()

def unzipReplace(zipFilePath, destDir):
    zfile = zipfile.ZipFile(zipFilePath)
    for name in zfile.namelist():
        (dirName, fileName) = os.path.split(name)
        print 'dirName = ' + dirName + ' fileName = ' + fileName
        if fileName == '':
            # directory
            newDir = destDir + '/' + dirName
            print newDir
            if not os.path.exists(newDir):
                os.mkdir(newDir)
        else:
            # file
            fd = open(destDir + '/' + name, 'wb')
            fd.write(zfile.read(name))
            fd.close()
    zfile.close()

def zipper(dir, zip_file):
	zip = zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_STORED)
	root_len = len(os.path.abspath(dir))
	for root, dirs, files in os.walk(dir):
		archive_root = os.path.abspath(root)[root_len:]
		for f in files:
			if not f.endswith('.zip'):
				fullpath = os.path.join(root, f)
				archive_name = os.path.join(archive_root, f)
				print f
				zip.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
	zip.close()
	#return zip_file