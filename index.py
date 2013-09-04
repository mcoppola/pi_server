# Matthew Coppola
# server code for raspberry pi 0.1
# implementation for museyroom album pro tools session repository
import os, time, shutil, zipfile, datetime
from bottle import route, run, request, redirect, FlupFCGIServer, static_file
from HTMLwriter import HTMLwriter
from util import zipdir, formatLoc, unzip, unzipReplace


@route('/', method='GET')
def index():
	return html.head + html.index + html.loginForm + html.linksFooter

@route('/login', method='GET')
def login():
	redirect('/')

@route('/login', method='POST')
def do_login():
	global user, loggedIn, users, passwords
	user = request.forms.get('login')
	password = request.forms.get('password')
	count=0
	for u in users:
		if u == user:
			if passwords[count] == password:
				loggedIn = str(user)
				redirect('/' + user)
			else:
				return 'Wrong password.  Press back to try again'
		else:
			count+=1

@route('/logout')
def logout():
	global loggedIn, loc
	loggedIn = ''
	loc = ''
	redirect('/')

@route('/about')
def about():
	return html.about

# RESUME ----------------------------------------------------/
@route('/resume')
def resume():
	return open('resume/index.html', 'r')

@route('/resume/<loc>/<filename:path>')
def send_static(loc, filename):
	return static_file(filename, root= './resume/' + loc)

# -----------------------------------------------------------/
@route('/master')
def about():
	return html.addUser

@route('/mc', method='GET')
def mcHome():
	checkLogin('mc')
	return 'welcome matthew'

@route('/museyroom', method='GET')
def museyroom():
	checkLogin('museyroom')
	return printProToolsDirectory('')

@route('/museyroom/<loc>', method='GET')
def museyroomLoc(loc):
	checkLogin('museyroom')
	return  printProToolsDirectory(str(loc)) 

#hack (FIX)
@route('/museyroom/<loc>/<loc2>', method='GET')
def museyroomHack(loc, loc2):
	checkLogin('museyroom')
	return  printProToolsDirectory(str(loc + '/' + loc2))

def printProToolsDirectory(loc):
	global user
	fl = open('site/html_gen.txt', 'w')
	fl.write(html.genHeader(user, formatLoc(loc)))
	if (loc != ''):
		fl.write(html.proToolsLinks(user, loc))
		loca = loc + '/'
	else:
		loca = loc
	for top, dirs, files in os.walk('data/' + user + '/' + loc ):
		count = 0
		fl.write('<ul style="list-style-type:circle">')
		for f in dirs:
			fl.write('<a href="/' + user + '/' + loca + f + '"><li>' + f + '</li></a> \n')
		fl.write('</ul> <ol>')
		for f in files:
			count = count + 1
			size = os.path.getsize('data/' + user + '/' + loc + '/' + f)
			date = time.ctime(os.path.getmtime('data/' + user + '/' + loc + '/' + f))

			if f.endswith('.ptx'):
				fl.write('<li>' + '<a href="' + '/down/' + loc +'/' + str(count) + '">' + '<font color="#66CCFF">'
					+ f + '</a></font>' + ' | '
					+ str(size) + ' bytes' +  ' | '
					+ str(date) + '</li>' + '\n')
			elif f.endswith('.ptf'):
				fl.write('<li>' + '<a href="' + '/down/' + loc +'/' + str(count) + '">' + '<font color="#6699FF">'
					+ f + '</a></font>' + ' | '
					+ str(size) + ' bytes' +  ' | '
					+ str(date) + '</li>' + '\n')
			elif f.endswith('.zip'):
				fl.write('<li>' + '<a href="' + '/down/' + loc +'/' + str(count) + '">' + '<font color="#00CC99">'
					+ f + '</a></font>' + ' | '
					+ str(size) + ' bytes' +  ' | '
					+ str(date) + '</li>' + '\n')
			else:
				fl.write('<li>' + '<a href="' + '/down/' + loc +'/' + str(count) + '">'
					+ f + '</a>' + ' | '
					+ str(size) + ' bytes' +  ' | '
					+ str(date) + '</li>' + '\n')
		break
	
	fl.write(html.museyFooter + html.folderLinksFooter(user))
	if( loc == ''):
		log = open('site/' + user + '/log.txt').read()
		fl.write(html.logHeader + str(log))
	fl.close()
	txt = open('site/html_gen.txt', 'r')
	return txt

@route('/replace/<loc>')
def replace(loc):
	global user
	checkLogin(user)
	return html.uploadSongZip(loc)

@route('/replace/<loc>', method='POST')
def doReplace(loc):
	global user
	checkLogin(user)
	checkAccess()
	upload = request.files.get('upload')
	if(upload.filename and upload.filename.endswith('.zip')):
		fn = os.path.basename(upload.filename)
		open('data/' + user + '/' + fn, 'w').write(upload.file.read())
		print 'file %s was upload' % fn
		#move directory to _previous
		try:
			shutil.move('data/' + user + '/' + loc + '/', 'data/' + user + '/_previous/')
		except:
			shutil.rmtree('data/' + user + '/_previous/' + loc + '/')
			shutil.move('data/' + user + '/' + loc + '/', 'data/' + user + '/_previous/' + loc + '/')
		#zip directory 
		(dirName, fileName) = fn.split('.')
		if not os.path.exists('data/' + user + '/' + dirName):
			os.mkdir('data/' + user + '/' + dirName)
		unzip('data/' + user + '/' + fn, 'data/' + user + '/' + dirName)
		os.remove('data/' + user + '/' + fn)
		redirect('/' + user + '/' + dirName)
	else:
		return 'error, directory was not replaced'	

@route('/mkzip/<loc>')
def makeZip(loc):
	global user
	checkLogin(user)
	checkAccess()
	#make zip of directory
	zipdir('data/' + user + '/' + loc + '/' + loc + '.zip', 'data/' + user + '/' + loc)
	redirect ('/' + user + '/' + loc)

@route('/addPTX/<loc>')
def addPTX(loc):
	global user
	checkLogin(user)
	return html.uploadPTX(loc)

@route('/addPTX/<loc>', method='POST')
def doAddPTX(loc):
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
			shutil.move('data/' + user + '/' + loc + '/' + fn, 'data/' + user + '/' + loc + '/Session File Backups/' + newName)
			#write new session file
			open('data/' + user + "/" + loc + '/' + fn, 'wb').write(upload.file.read())
			logger('addPTX', loc)
			redirect('/' + user + '/' + loc)
		except:
			open('data/' + user + "/" + loc + '/' + fn, 'wb').write(upload.file.read())
			logger('addPTX', loc)
			redirect('/' + user + '/' + loc)
	return 'no file was uploaded'

@route('/addSong')
def addSong():
	global user
	checkLogin(user)
	return html.uploadNewSongZip()

@route('/addSong', method='POST')
def doAddSong():
	global user
	checkLogin(user)
	checkAccess()
	upload = request.files.get('upload')
	if upload.filename:
		fn = os.path.basename(upload.filename)
		if not fn.endswith('.zip'):
			return 'please choose a .zip file'

		open('data/' + user + '/' + fn, 'wb').write(upload.file.read())
		(dirName, fileName) = fn.split('.')
		if not os.path.exists('data/' + user + '/' + dirName):
			os.mkdir('data/' + user + '/' + dirName)
		unzip('data/' + user + '/' + fn, 'data/' + user + '/' + dirName)
		os.remove('data/' + user + '/' + fn)
		logger('addSong', fn)
		redirect('/' + user)

@route('/addAudio/<loc>')
def addAudio(loc):
	return 'comming soon'

#download html link for files in current directory
@route('/down/<loc>/<num:int>')
def download(loc, num):
	global user
	checkLogin(user)
	checkAccess()
	num = int(num) - 1
	files = [f for f in os.listdir('data/' + user + '/' + loc) 
		if os.path.isfile('data/' + user + '/' + loc + '/' + f)]
	fn = files[num]
	return static_file(fn, root=('data/' + user + '/' + loc), download=fn)

#hack FIX 
@route('/down/<loc>/<loc2>/<num:int>')
def downloadHACK(loc, loc2, num):
	global user
	checkLogin(user)
	checkAccess()
	loc = loc+'/'+loc2
	num = int(num) - 1
	files = [f for f in os.listdir('data/' + user + '/' + loc) 
		if os.path.isfile('data/' + user + '/' + loc + '/' + f)]
	fn = files[num]
	return static_file(fn, root=('data/' + user + '/' + loc), download=fn)

@route('/ptkeeper_demo/<num:int>')
def ptKeeperDemo(num):
	if num == 8320620:
		global loggedIn, user, access
		loggedIn = 'museyroom'
		user = 'museyroom'
		access = False
		redirect('/museyroom')
	else:
		redirect('/noaccess')

#keep generic at bottom of file
@route('/<user>', method='GET')
def userGeneric(user):
	checkLogin(user)
	return printProToolsDirectory('')

@route('/<user>/<dir>', method='GET')
def userGenericLoc(user, dir):
	checkLogin(user)
	return printProToolsDirectory(dir)

@route('/<user>/<dir>/<loc2>', method='GET')
def userGenericLocHack(user, dir, loc):
	checkLogin(user)
	return printProToolsDirectory(str(dir + '/' + loc))

@route('/<user>/<dir>/<loc>/<loc2>', method='GET')
def userGenericLocHack(user):
	checkLogin(user)
	return printProToolsDirectory(str(dir + '/' + loc + '/' + loc2))

@route('/noaccess')
def noAccess():
	return html.noAccess

def checkLogin(user = 'null'):
	global loggedIn
	if (loggedIn != user):
		redirect('/login')

def checkAccess():
	global access
	if not access:
		redirect('/noaccess')

def logger(action, loc):
	global user
	log = open('site/' + user + '/log.text').read()
	newlog = '<li>' + str(datetime.datetime.now()) + ' : ' + user + logActions[action] + loc + '</li><br>'
	log = str(newlog) + str(log)
	open('site/' + user + '/log.txt', 'wb').write(log)


logActions = {'addPTX': ' added a session file to ', 'addSong': ' added the song '}
users = open('site/users.txt', 'r').read().splitlines()
passwords = open('site/passwords.txt', 'r').read().splitlines()
html = HTMLwriter()
user = 'null'
access = True
password = ''
loggedIn = ''
#on pi server=FlupFCGIServer
run(host='127.0.0.1', port=8080)