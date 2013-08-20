
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
		return (' <a href="/replace/' + loc + '" style="text-decoration: none;">replace</a>' + ' | '
					+ '<a href="/dwnzip/' + loc + '" style="text-decoration: none;">download</a>' + ' | '
					+ '<a href="/addAudio/'+ loc + '" style="text-decoration: none;">add audio</a>' + ' | '
					+ '<a href="/addPTX/' + loc + '"  style="text-decoration: none;">add ptx</a>')
		
	def addSong(self, user):
		return ('<br><a href="/addSong/' + user + '" style="text-decoration: none;">add song</a>')		
	
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

	def uploadPTX(self, loc):
		return ('''<h>add pro tools session file (ptx/ptf)</h>
				<p>if the ptx/ptf matches the name of an existing file it will be replaced in the top of the directory
				and the previous version will be moved to SessionBackups</p>
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


	# museyHeader = '''<html><head><link rel="stylesheet" href="style.css"></head>
	# 			<body>
	# 			<h id=museyhead>museyroom album</h>
	# 			<body>'''

	museyFooter = '''</ol></body></html>'''

