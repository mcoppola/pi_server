# Matthew Coppola
# server code for raspberry pi 0.1
# implementation for museyroom album pro tools session repository
import os, time, shutil, zipfile, datetime, subprocess, threading
from bottle import route, run, request, redirect, FlupFCGIServer, static_file
from HTMLwriter import HTMLwriter
from util import zipdir, formatLoc, unzip, unzipReplace, sendEmail


class ZipDir ( threading.Thread ):
	def __init__(self, account, loc, emailTo):
              threading.Thread.__init__(self)
              self.account = account
              self.loc = loc
              self.emailTo = emailTo

	def run (self):
		subprocess.call('site/scripts/zip.sh ' + self.account + ' ' + self.loc, shell=True)
		subject = '%s has been Zipped!' % self.loc
		body = self.loc + ' has been zipped.  You can download the zip file from within the %s directory' % self.loc
		sendEmail('mcoppola832@gmail.com', self.emailTo, subject, body)
		#redirect ('/account/' + self.account + '/' + self.loc)

#-------------------------------------------------------------------------//

@route('/', method='GET')
def index():
	return html.head + html.index + html.loginForm + html.linksFooter

@route('/login', method='GET')
def login():
	redirect('/')

@route('/login', method='POST')
def do_login():
	global user, loggedIn, users, passwords, access
	user = request.forms.get('login')
	password = request.forms.get('password')
	count=0
	for u in users:
		if u == user:
			if passwords[count] == password:
				loggedIn = str(user)
				access = True
				redirect('/home/' + user)
			else:
				return html.head + html.index + html.loginForm + html.linksFooter + '<br><p>Wrong password.  Try again.</p>'
		else:
			count+=1
	return html.head + html.index + html.loginForm + html.linksFooter + '<br><p>Username not found.</p>'


@route('/logout')
def logout():
	global loggedIn, loc
	loggedIn = ''
	loc = ''
	redirect('/')

@route('/about')
def about():
	return html.about

@route('/file/<file>')
def returnFile(file):
	return open(file, 'r')

# RESUME ----------------------------------------------------/
@route('/resume')
def resume():
	return open('resume/index.html', 'r')

@route('/resume/<loc>/<filename:path>', method='GET')
def send_static(loc, filename):
	return static_file(filename, root= './resume/' + loc)

# VitaminME -------------------------------------------------/
@route('/vm')
def vitaminMe():
	out = subprocess.Popen('php vm/public_html/index.php', shell=True, stdout=subprocess.PIPE)
	return out.stdout.read()

@route('/vm/<loc>/<filename:path>')
def send_staticVM(loc, filename):
	return static_file(filename, root= './vm/public_html' + loc)

# USER HOME -------------------------------------------------/
@route('/home/<user>')
def userHome(user):
	# display groups that the user belongs to
	checkLogin(user)
	global groups
	fl = open('site/html_gen.txt', 'w')
	fl.write(html.genHeader(user))
	fl.write('<ul style="list-style-type:circle">')
	for g in groups[user]:
		fl.write('<a href="/account/' + g + '"><li>' + g + '</li></a> \n')
	fl.write('</ul> </ol>')
	fl.write(html.homeFooter(user))
	fl.close()
	txt = open('site/html_gen.txt', 'r')
	return txt

# -----------------------------------------------------------/
@route('/master')
def about():
	return html.addUser

@route('/mc', method='GET')
def mcHome():
	checkLogin('mc')
	return 'welcome matthew'


def printGenDirectory(account, loc):
	global user
	fl = open('site/html_gen.txt', 'w')
	fl.write(html.genHeader(account, formatLoc(loc)))
	fl.write(html.genFolderLinks(account, loc))
	if (loc != ''):
		loca = loc + '/'
	else:
		loca = loc
	for top, dirs, files in os.walk('data/' + account + '/' + loc ):
		count = 0
		fl.write('<ul style="list-style-type:circle">')
		for f in dirs:
			fl.write('<a href="/account/' + account + '/' + loca + f + '"><li>' + f + '</li></a> \n')
		fl.write('</ul> <ol>')
		for f in files:
			count = count + 1
			size = os.path.getsize('data/' + account + '/' + loc + '/' + f)
			date = time.ctime(os.path.getmtime('data/' + account + '/' + loc + '/' + f))
			fl.write('<li>' + '<a href="/' + account + '/down/' + loca + str(count) + '">'
				+ f + '</a>' + ' | '
				+ str(size) + ' bytes' +  ' | '
				+ str(date) + '</li>' + '\n')
		break
	fl.write(html.museyFooter + html.folderLinksFooter(user, account))
	fl.close()
	txt = open('site/html_gen.txt', 'r')
	return txt

def printProToolsDirectory(account, loc):
	global user
	fl = open('site/html_gen.txt', 'w')
	fl.write(html.genHeader(account, formatLoc(loc)))
	if (loc != ''):
		fl.write(html.proToolsLinks(account, loc))
		loca = loc + '/'
	else:
		loca = loc
	for top, dirs, files in os.walk('data/' + account + '/' + loc ):
		count = 0
		fl.write('<ul style="list-style-type:circle">')
		for f in dirs:
			fl.write('<a href="/account/' + account + '/' + loca + f + '"><li>' + f + '</li></a> \n')
		fl.write('</ul> <ol>')
		for f in files:
			count = count + 1
			size = os.path.getsize('data/' + account + '/' + loc + '/' + f)
			date = time.ctime(os.path.getmtime('data/' + account + '/' + loc + '/' + f))

			if f.endswith('.ptx'):
				fl.write('<li>' + '<a href="/'+ account + '/down/' + loca + str(count) + '">' + '<font color="#66CCFF">'
					+ f + '</a></font>' + ' | '
					+ str(size) + ' bytes' +  ' | '
					+ str(date) + '</li>' + '\n')
			elif f.endswith('.ptf'):
				fl.write('<li>' + '<a href="/'+ account + '/down/' + loca + str(count) + '">' + '<font color="#6699FF">'
					+ f + '</a></font>' + ' | '
					+ str(size) + ' bytes' +  ' | '
					+ str(date) + '</li>' + '\n')
			elif f.endswith('.zip'):
				fl.write('<li>' + '<a href="/'+ account + '/down/' + loca + str(count) + '">' + '<font color="#00CC99">'
					+ f + '</a></font>' + ' | '
					+ str(size) + ' bytes' +  ' | '
					+ str(date) + '</li>' + '\n')
			else:
				fl.write('<li>' + '<a href="/'+ account + '/down/' + loca + str(count) + '">'
					+ f + '</a>' + ' | '
					+ str(size) + ' bytes' +  ' | '
					+ str(date) + '</li>' + '\n')
		break
	
	fl.write(html.museyFooter + html.folderLinksFooter(user, account))
	if( loc == ''):
		log = open('site/' + account + '/log.txt').read()
		links = open('site/' + account + '/links.txt').read()
		fl.write(html.linksHeader(account) + str(links) + html.logHeader + str(log))
	fl.close()
	txt = open('site/html_gen.txt', 'r')
	return txt

# PRO TOOLS FUNCTIONS --------------------------------------------------/

@route('/replace/<account>/<loc>')
def replace(account, loc):
	global user
	checkLogin(user)
	return html.uploadSongZip(account, loc)

@route('/replace/<account>/<loc>', method='POST')
def doReplace(account, loc):
	global user
	checkLogin(user)
	checkAccess()
	upload = request.files.get('upload')
	if(upload.filename and upload.filename.endswith('.zip')):
		fn = os.path.basename(upload.filename)
		open('data/' + account + '/' + fn, 'w').write(upload.file.read())
		print 'file %s was upload' % fn
		#move directory to _previous
		try:
			shutil.move('data/' + account + '/' + loc + '/', 'data/' + account + '/_previous/')
		except:
			shutil.rmtree('data/' + account + '/_previous/' + loc + '/')
			shutil.move('data/' + account + '/' + loc + '/', 'data/' + account + '/_previous/' + loc + '/')
		#zip directory 
		(dirName, fileName) = fn.split('.')
		if not os.path.exists('data/' + account + '/' + dirName):
			os.mkdir('data/' + account + '/' + dirName)
		unzip('data/' + account + '/' + fn, 'data/' + account + '/' + dirName)
		os.remove('data/' + account + '/' + fn)
		redirect('/account/' + account + '/' + dirName)
	else:
		return 'error, directory was not replaced'	


@route('/mkzip_prompt/<account>/<loc>', method='GET')
def makeZipPrompt(account, loc):
	global user
	checkLogin(user)
	checkAccess()
	return html.mkzip_prompt(account, loc)

@route('/mkzip_prompt/<account>/<loc>', method='POST')
def domakeZipPrompt(account, loc):
	email = request.forms.get('email')
	redirect ('/mkzip/'+account+'/'+loc+'/'+email)

@route('/mkzip/<account>/<loc>/<emailTo>')
def makeZip(account, loc, emailTo):
	global user
	checkLogin(user)
	checkAccess()
	#make zip of directory
	ziplog = open('ziplog', 'wb')
	ziplog.close()
	z = ZipDir(account, loc, emailTo)
	z.start()
	#redirect ('/account/' + account + '/' + loc)
	redirect('/mkziplog')

@route('/mkziplog')
def mkZiplog():
	return html.mkziplog()
	

@route('/addPTX/<account>/<loc>')
def addPTX(account, loc):
	global user
	checkLogin(user)
	return html.uploadPTX(account, loc)

@route('/addPTX/<account>/<loc>', method='POST')
def doAddPTX(account, loc):
	global user
	checkLogin(user)
	checkAccess()
	upload = request.files.get('upload')
	if upload.filename:
		fn = os.path.basename(upload.filename)
		if not fn.endswith('.ptx') and not fn.endswith('.ptf'):
			return 'please choose a ptx or ptf file'
		try:
			#move existing session file
			split = fn.split('.')
			newName = split[0] + "_" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + split[1]
			shutil.move('data/' + account + '/' + loc + '/' + fn, 'data/' + account + '/' + loc + '/Session File Backups/' + newName)
			#write new session file
			open('data/' + account + "/" + loc + '/' + fn, 'wb').write(upload.file.read())
			logger('addPTX', loc, account)
			redirect('/account/' + account + '/' + loc)
		except:
			open('data/' + account + "/" + loc + '/' + fn, 'wb').write(upload.file.read())
			logger('addPTX', loc, account)
			redirect('/account/' + account + '/' + loc)
	return 'no file was uploaded'

@route('/addSong/<account>')
def addSong(account):
	global user
	checkLogin(user)
	return html.uploadNewSongZip(account)

@route('/addSong/<account>', method='POST')
def doAddSong(account):
	global user
	checkLogin(user)
	checkAccess()
	upload = request.files.get('upload')
	if upload.filename:
		fn = os.path.basename(upload.filename)
		if not fn.endswith('.zip'):
			return 'please choose a .zip file'

		open('data/' + account + '/' + fn, 'wb').write(upload.file.read())
		(dirName, fileName) = fn.split('.')
		if not os.path.exists('data/' + account + '/' + dirName):
			os.mkdir('data/' + account + '/' + dirName)
		unzip('data/' + account + '/' + fn, 'data/' + account + '/' + dirName)
		os.remove('data/' + account + '/' + fn)
		logger('addSong', fn, account)
		redirect('/account/' + account)

@route('/addAudio/<account>/<loc>')
def addAudio(account, loc):
	return 'comming soon'

# GENERIC FUNCTIONS ----------------------------------------------------/

@route('/upload_gen_folder/<account>', method='GET')
def genUpload(account):
	global user
	checkLogin(user)
	return html.uploadGen(account, '')

@route('/upload_gen_folder/<account>', method='POST')
def doGenUpload(account):
	global user
	checkLogin(user)
	upload = request.files.get('upload')
	if upload.filename:
		fn = os.path.basename(upload.filename)
		open('data/' + account + '/' + fn, 'wb').write(upload.file.read())
		redirect('/account/' + account)

@route('/upload_gen_folder/<account>/<loc>', method='GET')
def genUpload(account, loc = ''):
	global user
	checkLogin(user)
	return html.uploadGen(account, loc)

@route('/upload_gen_folder/<account>/<loc>', method='POST')
def doGenUpload(account, loc = ''):
	global user
	checkLogin(user)
	upload = request.files.get('upload')
	if upload.filename:
		fn = os.path.basename(upload.filename)
		open('data/' + account + '/' + loc + '/' + fn, 'wb').write(upload.file.read())
		redirect('/account/' + account + '/' + loc)

#download html link for files in top directory
@route('/<account>/down/<num:int>')
def download(account, num):
	global user
	checkLogin(user)
	checkAccess()
	num = int(num) - 1
	files = [f for f in os.listdir('data/' + account) 
		if os.path.isfile('data/' + account + '/' + f)]
	fn = files[num]
	return static_file(fn, root=('data/' + account), download=fn)

#download html link for files in current directory
@route('/<account>/down/<loc>/<num:int>')
def download(account, loc, num):
	global user
	checkLogin(user)
	checkAccess()
	num = int(num) - 1
	files = [f for f in os.listdir('data/' + account + '/' + loc) 
		if os.path.isfile('data/' + account + '/' + loc + '/' + f)]
	fn = files[num]
	return static_file(fn, root=('data/' + account + '/' + loc), download=fn)

#hack FIX 
@route('/<account>/down/<loc>/<loc2>/<num:int>')
def downloadHACK(account, loc, loc2, num):
	global user
	checkLogin(user)
	checkAccess()
	loc = loc+'/'+loc2
	num = int(num) - 1
	files = [f for f in os.listdir('data/' + account + '/' + loc) 
		if os.path.isfile('data/' + account + '/' + loc + '/'+ f)]
	fn = files[num]
	return static_file(fn, root=('data/' + account + '/' + loc), download=fn)

@route('/ptkeeper_demo/<num:int>')
def ptKeeperDemo(num):
	if num == 8320620:
		global loggedIn, user, access
		loggedIn = 'museyroom'
		user = 'museyroom'
		access = False
		redirect('/account/museyroom')
	else:
		redirect('/noaccess')

#keep generic at bottom of file
@route('/account/<account>', method='GET')
def accountGeneric(account):
	global user
	checkLogin(user)
	settings = open('site/' + account + '/settings.txt', 'r').read().splitlines()
	if (settings[0] == 'p'):
		return printProToolsDirectory(account, '')
	elif (settings[0] == 'a'):
		return printGenDirectory(account, '')

@route('/account/<account>/<dir>', method='GET')
def accountGenericLoc(account, dir):
	global user
	checkLogin(user)
	settings = open('site/' + account + '/settings.txt', 'r').read().splitlines()
	if (settings[0] == 'p'):
		return printProToolsDirectory(account, dir)
	elif (settings[0] == 'a'):
		return printGenDirectory(account, dir)


@route('/account/<account>/<dir>/<loc>', method='GET')
def accountGenericLocHack(account, dir, loc):
	global user
	checkLogin(user)
	settings = open('site/' + account + '/settings.txt', 'r').read().splitlines()
	if (settings[0] == 'p'):
		return printProToolsDirectory(account, str(dir + '/' + loc))
	elif (settings[0] == 'a'):
		return printGenDirectory(account, str(dir + '/' + loc))

@route('/account/<account>/<dir>/<loc>/<loc2>', method='GET')
def accountGenericLoc2Hack(account, dir, loc, loc2):
	global user
	checkLogin(user)
	settings = open('site/' + account + '/settings.txt', 'r').read().splitlines()
	if (settings[0] == 'p'):
		return printProToolsDirectory(account, str(dir + '/' + loc + '/' + loc2))
	elif (settings[0] == 'a'):
		return printGenDirectory(account, str(dir + '/' + loc + '/' + loc2))

# CHANGE PASSWORD ------------------------------------------------/
@route('/pass/<user>', method='GET')
def changePassword(user):
	return 'not available'

# ADD LINK ------------------------------------------------/
@route('/addlink/<account>', method='GET')
def addLink(account):
	global user
	checkLogin(user)
	return html.addLinkForm(account)

@route('/addlink/<account>', method='POST')
def doAddLink(account):
	global user
	checkLogin(user)
	title = request.forms.get('title')
	url = request.forms.get('url')
	if url.startswith('https://'):
		url = url[7:]
	with open("site/%s/links.txt" % account, "a") as linksFile:
		linksFile.write('<br><a href="https://%s" target="_blank">%s</a>' %(url, title))
	redirect('/account/%s' % account)

@route('/noaccess')
def noAccess():
	return html.noAccess

def checkLogin(user = 'null'):
	global loggedIn, groups
	verified = False
	if (loggedIn == user):
		for g in groups[loggedIn]:
			if (g == loggedIn):
				verified = True
	if (not verified):
		redirect('/login')

def checkAccess():
	global access
	if not access:
		redirect('/noaccess')

def logger(action, loc, account):
	global user
	log = open('site/' + account + '/log.txt').read()
	newlog = '<li>' + str(datetime.datetime.now()) + ' : ' + user + logActions[action] + loc + '</li><br>'
	log = str(newlog) + str(log)
	open('site/' + account + '/log.txt', 'wb').write(log)

#locActions (action: description)
logActions = {'addPTX': ' added a session file to ', 'addSong': ' added the song '}
#groups (user: [groups])
groups = {'null':[], 'ben':['ben', 'museyroom'], 'mc':['mc','wellboys','museyroom', 'caddy', 'drunken_bear'], 'david':['david', 'drunken_bear', 'caddy'], 'museyroom':['museyroom'], 'owen':['owen', 'drunken_bear', 'wellboys'], 'caddy':['caddy']}
users = open('site/users.txt', 'r').read().splitlines()
passwords = open('site/passwords.txt', 'r').read().splitlines()
html = HTMLwriter()
user = 'null'
access = True
password = ''
loggedIn = ''
#on pi server=FlupFCGIServer
run(host='127.0.0.1', port=8080, server=FlupFCGIServer)
