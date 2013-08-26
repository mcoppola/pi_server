
class HTMLwriter(object):

	def __init__(self):
		super(HTMLwriter, self).__init__()

	# def header(self, user, loc):
 #        return ('''<!DOCTYPE html><html></html><body><h3>%s %s</h3>'''% (user, loc))

 	def locHeader(self, user, loc):
 		return '''<
 					'''

 	def museyHeader(self, loc):
 		return '''<html><head><link rel="stylesheet" href="style.css"></head>
				<body>
				<h id=museyhead>museyroom album / %s </h> <br>
				''' % loc

	def proToolsLinks(self, user, loc):
		return (' <a title="replace this directory with a zip file" href="/replace/' + loc + '" style="text-decoration: none;">replace</a>' + ' | '
					+ '<a title="compress this directory into a .zip file, may take a while" href="/mkzip/' + loc + '" style="text-decoration: none;">make zip</a>' + ' | '
					+ '<a title="upload new audio instead of replacing the entire directory" href="/addAudio/'+ loc + '" style="text-decoration: none;">add audio</a>' + ' | '
					+ '<a title="upload a new ptf or ptx file" href="/addPTX/' + loc + '"  style="text-decoration: none;">add ptx</a>')
		
	def addSong(self, user):
		return ('<br><a href="/addSong" style="text-decoration: none;">add song</a>')		
	
	def uploadSongZip(self, loc):
		return ('''<h>replace pro tools session</h>
				<p>Upload a compressed .zip file of the entire directory 
				to replace the current version on the server</p>
				<form action="/replace/%s" method="post"
				enctype="multipart/form-data"> <small>
				<input type="file" name="upload" />
				<input type="submit" value="Upload" /> </small>
				</form>
				''' % loc)

	def uploadNewSongZip(self):
		return ('''<h>Add Song</h>
				<p>Upload a compressed .zip file of the entire Pro Tools Session
				directory</p>
				<form action="/addSong" method="post"
				enctype="multipart/form-data"> <small>
				<input type="file" name="upload" />
				<input type="submit" value="Upload" /> </small>
				</form>
				''')		

	def uploadPTX(self, loc):
		return ('''<h>add pro tools session file (ptx/ptf)</h>
				<p>if the ptx/ptf matches the name of an existing file it will be replaced in the top of the directory
				and the previous version will be moved to Session File Backups</p>
				<form action="/addPTX/%s" method="post"
				enctype="multipart/form-data"> <small>
				<input type="file" name="upload" />
				<input type="submit" value="Upload" /> </small>
				</form>
				''' % loc)

	head = '''<head>
			  <meta charset = "utf-8">
			    <title>mc</title>
			    <link rel="stylesheet" href="style.css">
			  </head>'''

	index = '''<h id=header></h> </html>'''
	
	loginForm = '''<html>
	            <form action="/login" method="post">
	            user:    <input type="text" name="login" /> 
	            password: <input type="password" name="password" />
	            <input type="submit" value="Login" />
	            </form></small>
	            '''

	linksFooter = '''<small> <a href= /master > add user </a>
				&nbsp;|&nbsp;
				<a href= /about > about  </a> </small>
				'''

	def folderLinksFooter(self, user): 
		return '''<small> <a href= /%s > go up </a>
				&nbsp;|&nbsp;
				<a href= /addSong> add song </a>
				&nbsp;|&nbsp;
				<a href= /logout > logout </a> </small>
				''' % user

	about = loginForm + '''<html> <small> <p> This is a private server hosted by matthew coppola. <br>
                I can be reached at mcoppola832@gmail.com  &nbsp;|&nbsp; <a href= /login > back </a>  </p> </small> </html>'''

	addUser = loginForm + '''<html> <small> <p>feature not available, contact me at mcoppola832@gmail.com &nbsp;|&nbsp; <a href= /login > back </a>  </p> </small> </html>'''

	# museyHeader = '''<html><head><link rel="stylesheet" href="style.css"></head>
	# 			<body>
	# 			<h id=museyhead>museyroom album</h>
	# 			<body>'''

	museyFooter = '''</ol></body></html>'''

