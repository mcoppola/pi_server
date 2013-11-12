import zipfile, os, shutil, datetime
from collections import defaultdict

def zipdir(name, path):
	zipper(path, name)
	#shutil.make_archive(name, "zip", path)
	

def formatLoc(loc):
	formated = ''
	locs = loc.split('/')
	for l in locs:
		if l != '':
			formated += l + ' / '
	return formated

def timeSinceNow(date):
    date = date.split('-')
    now = datetime.datetime.now().strftime("%Y,%m,%d,%H,%M,%S").split(',')
    try:
        for i in range(0, len(now)):
            date[i] = int(date[i])
            now[i] = int(now[i])
    except ValueError:
        return 'unknown'

    if (now[0] - date[0] <= 0):
        if (now[1]-date[1] <= 0):
            if (now[2]-date[2] <= 0):
                if (now[3]-date[3] <= 0):
                    if(now[4]-date[4] < 1):
                         return '%d second%s ago'%(now[5]-date[5] + ((now[4]-date[4])*60), sif2(now[5]-date[5] + ((now[4]-date[4])*60)))
                    return '%d minute%s ago'%(now[4]-date[4] + ((now[3]-date[3])*60), sif2(now[4]-date[4] + ((now[3]-date[3])*60)))
                return '%d hour%s ago'%(now[3]-date[3], sif2(now[3]-date[3]))
            return '%d day%s ago'%(now[2]-date[2], sif2(now[2]-date[2]))
        return '%d month%s ago'%(now[1]-date[1], sif2(now[1]-date[1]))
    return '%d year%s ago'%(now[0]-date[0], sif2(now[0]-date[0]))

def niceDate(date):
    months = {
           1 : 'January',
           2 : 'February',
           3 : 'March',
           4 : 'April',
           5 : 'May',
           6 : 'June',
           7 : 'July',
           8 : 'August',
           9 : 'September',
           10 : 'October',
           11 : 'November',
           12 : 'December'
    }
    date = date.split('-')
    return months[int(date[1])] + ' %s, %s' % (date[2], date[0])


def sif2(num):
    if (num > 1):
        return 's'
    else:
        return ''

def noteCountForSongs(user, account):
    notes = defaultdict(lambda: 0)
    commitsBehind = open('site/' + user + '/commits_behind.txt', 'r').read().splitlines()
    for l in commitsBehind:
        if l.startswith(account):
            v = l.split(',')
            for value in v[1:]:
                if not (value.endswith('.ptx') | value.endswith('.ptf')):
                    notes[value] += 1
    return notes

def notesForFile(user, account, loc, filename):
    commitsBehind = open('site/' + user + '/commits_behind.txt', 'r').read().splitlines()
    for l in commitsBehind:
        if l.startswith(account):
            v = l.split(',')
            for value in v:
                if (value == filename):
                    return True
    return False

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

    
