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

def sendEmail(From, To, subject, body):
    import smtplib
    from email.mime.text import MIMEText

    msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n%s" % (From,To,subject,body)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mcoppola832@gmail.com','millbrook')
    server.sendmail(From, To, msg)
    server.close()

    
