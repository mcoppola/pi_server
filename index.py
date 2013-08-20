# Matthew Coppola
# server code for raspberry pi 0.1
import os, time, shutil, zipfile, datetime
from bottle import route, run, request, redirect, FlupFCGIServer, static_file
from HTMLwriter import HTMLwriter
from util import zipdir, formatLoc


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

@route('/mc', method='GET')
def mcHome():
	checkLogin()
	return 'welcome matthew'

@route('/museyroom', method='GET')
def museyroom():
	checkLogin()
	return printProToolsDirectory('')

@route('/museyroom/<loc>', method='GET')
def museyroomLoc(loc):
	checkLogin()
	return  printProToolsDirectory(str(loc))

#hack (FIX)
@route('/museyroom/<loc>/<loc2>', method='GET')
def museyroomHack(loc, loc2):
	checkLogin()
	return  printProToolsDirectory(str(loc + '/' + loc2))



def printProToolsDirectory(loc):
	global user
	fl = open('site/html_gen.txt', 'w')
	fl.write(html.museyHeader(formatLoc(loc)))
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
			fl.write('<li>' + '<a href="' + '/down/' + loc +'/' + str(count) + '">'
				+ f + '</a>' + ' | '
				+ str(size) + ' bytes' +  ' | '
				+ str(date) + '</li>' + '\n')
		break

	if(loc == ''):
		fl.write(html.addSong(user))
	fl.write(html.museyFooter)
	fl.close()
	txt = open('site/html_gen.txt', 'r')
	return txt

@route('/replace/<loc>')
def replace(loc):
	checkLogin()
	global user
	return html.uploadSongZip(loc)

@route('/replace/<loc>', method='POST')
def doReplace(loc):
	checkLogin()
	global user
	upload = request.files.get('upload')
	if(upload.filename and upload.filename.endswith('.zip')):
		fn = os.path.basename(upload.filename)
		open('data/' + user + '/' + fn, 'w').write(upload.file.read())
		print 'file %s was upload' % fn
		#move directory to _previous
		shutil.move('data/' + user + '/' + loc + '/.', 'data/' + user + '/_previous/' + loc + '/')
		#zip directory 
		zfile = zipfile.ZipFile('data/' + user + '/' + fn, 'r')
		print zfile.getinfo()
		for name in zfile.namelist():
			(dirname, filename) = os.path.split(name)
			print "Decompressing " + filename + " on " + dirname
			if not os.path.exists(dirname):
				os.mkdir(dirname)
			fd = open('data/' + user + '/' + name,"wb")
			fd.write(file.read(name))
			fd.close()

@route('/dwnzip/<loc>')
def downloadZip(loc):
	checkLogin()
	global user
	#make zip of directory
	zipdir(loc, 'data/' + user + '/' + loc)
	return static_file(loc + '.zip', root=('/'), download=(loc+'.zip'))

@route('/addPTX/<loc>')
def addPTX(loc):
	checkLogin()
	global user
	return html.uploadPTX(loc)

@route('/addPTX/<loc>', method='POST')
def doAddPTX(loc):
	checkLogin()
	global user
	upload = request.files.get('upload')
	if upload.filename:
		fn = os.path.basename(upload.filename)
		if not fn.endswith('.ptx') and not fn.endswith('.ptf'):
			return 'please choose a ptx or ptf file'
		#move existing session file
		try:
			split = fn.split('.')
			newName = split[0] + "_" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + split[1]
			shutil.move('data/' + user + '/' + loc + '/' + fn, 'data/' + user + '/' + loc + '/sessionbackups/' + newName)
			open('data/' + user + "/" + loc + '/' + fn, 'wb').write(upload.file.read())
			redirect('/' + user + '/' + loc)
		except:
			open('data/' + user + "/" + loc + '/' + fn, 'wb').write(upload.file.read())
			redirect('/' + user + '/' + loc)
		#write new session file
	return 'no file was uploaded'

#download html link for files in current directory
@route('/down/<loc>/<num>')
def download(loc, num):
	checkLogin()
	global user
	num = int(num) - 1
	files = [f for f in os.listdir('data/' + user + '/' + loc) 
		if os.path.isfile('data/' + user + '/' + loc + '/' + f)]
	fn = files[num]
	return static_file(fn, root=('data/' + user + '/' + loc), download=fn)

#hack FIX 
@route('/down/<loc>/<loc2>/<num>')
def downloadHACK(loc, loc2, num):
	checkLogin()
	global user
	loc = loc+'/'+loc2
	num = int(num) - 1
	files = [f for f in os.listdir('data/' + user + '/' + loc) 
		if os.path.isfile('data/' + user + '/' + loc + '/' + f)]
	fn = files[num]
	return static_file(fn, root=('data/' + user + '/' + loc), download=fn)


def checkLogin():
	if (loggedIn != user):
		redirect('/login')


users = open('site/users.txt', 'r').read().splitlines()
passwords = open('site/passwords.txt', 'r').read().splitlines()
html = HTMLwriter()
user = 'null'
password = ''
loggedIn = ''
#on pi server=FlupFCGIServer
run(host='127.0.0.1', port=8080)