import zipfile, os, shutil

def zipdir(name, path):
	shutil.make_archive(name, "zip", path)
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

