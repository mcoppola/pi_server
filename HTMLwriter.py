
class HTMLwriter(object):

	def __init__(self):
		super(HTMLwriter, self).__init__()

	head = '''<head>
			  <meta charset = "utf-8">
			    <title>mc</title>
			    <link rel="stylesheet" href="style.css">
			  </head>'''

	index = '''<h id=header>mc's server</h> </html>'''
	
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

	museyHeader = '''<html><head><link rel="stylesheet" href="style.css"></head>
				<body>
				<h>museyroom album</h>
				<body>'''

