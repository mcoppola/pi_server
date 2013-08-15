# Matthew Coppola
# server code for raspberry pi 0.1
from bottle import route, run, request, redirect, FlupFCGIServer
from HTMLwriter import HTMLwriter


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
				return 'Wrong password.  Please refresh the page to try again'
		else:
			count+=1 

@route('/mc', method='GET')
def mcHome():
	checkLogin()
	return 'welcome matthew'

@route('/museyroom', method='GET')
def museyroom():
	checkLogin()




def printProToolsDirectory(loc):
	fl = open('site/html_gen.txt', 'w+')
	fl.write(html.header(user, loc))
	for top, dirs, files in os.walk(user + loc):
		count = 0
		fl.write('<ul style="list-style-type:circle">')
		for f in dirs:
			fl.write('<li>' + f + '</li> \n')
		fl.write('</ul> <ol>')
		for f in files:
			count = count + 1
			size = os.path.getsize(user + loc + f)
			fl.write('<A HREF=' + '/down/' + str(count) + '>'
				+ '<li>' + f + '</A>' + '&nbsp;|&nbsp;'
				+ str(size) + ' bytes' + '</li>' + '\n')
		break

	fl.write(html.OLfooter())
	fl.close()
	txt = open('site/displaydirectory.txt', 'r')
	return txt


def checkLogin():
	if (loggedIn != user):
		redirect('/login')

users = open('site/users.txt', 'r').read().splitlines()
passwords = open('site/passwords.txt', 'r').read().splitlines()
html = HTMLwriter()
user = 'null'
password = ''
loggedIn = ''
run(host='127.0.0.1', port=8080, server=FlupFCGIServer)