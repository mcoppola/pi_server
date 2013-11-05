
class HTMLwriter(object):
	

	def __init__(self):
		super(HTMLwriter, self).__init__()


	# def header(self, user, loc):
 #        return ('''<!DOCTYPE html><html></html><body><h3>%s %s</h3>'''% (user, loc))

 	def locHeader(self, user, loc):
 		return '''<
 					'''

 	def museyHeader(self, loc):
 		return '''
 				<html><head></head>
				<body>
				<h >museyroom album / %s </h> <br>
				''' % loc

	def genHeader(self, user, loc = '', username= ''):
		return '''
				<div class="container">

			      <div class="navbar navbar-default">
			        <div class="navbar-header">
			          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			          </button>
			          <a class="navbar-brand" href="#">%s / %s </a>
			        </div>
			        <div class="navbar-collapse collapse">
			          <ul class="nav navbar-nav">
			            <li class="active"><a href="#">Link</a></li>
			            <li><a href="#">Link</a></li>
			            <li><a href="#">Link</a></li>
			            <li class="dropdown">
			              <a data-target="#" href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
			              <ul class="dropdown-menu">
			                <li><a href="#">Action</a></li>
			                <li><a href="#">Another action</a></li>
			                <li><a href="#">Something else here</a></li>
			                <li class="divider"></li>
			                <li class="dropdown-header">Nav header</li>
			                <li><a href="#">Separated link</a></li>
			                <li><a href="#">One more separated link</a></li>
			              </ul>
			            </li>
			          </ul>
			          <ul class="nav navbar-nav navbar-right">
			            <li><a href= /logout > logout </a> </small></li>
			          </ul>
			        </div><!--/.nav-collapse -->
			      </div><!--/.navbar navbar-default -->
				''' % (user, loc)

	accountListHeader = ''' <div class="accountList">
							<ul style="list-style-type:circle">
						'''

	def proToolsLinks(self, account, loc):
		return (' <small><a title="replace this directory with a zip file" href="/replace/' + account + '/' + loc + '" style="text-decoration: none;">replace</a>' + ' | '
					+ '<a title="compress this directory into a .zip file" href="/mkzip_prompt/' + account + '/' + loc + '" style="text-decoration: none;">make zip</a>' + ' | '
					+ '<a title="upload new audio instead of replacing the entire directory" href="/addAudio/' + account + '/' + loc + '" style="text-decoration: none;">add audio</a>' + ' | '
					+ '<a title="upload a new ptf or ptx file" href="/addPTX/' + account + '/' + loc + '"  style="text-decoration: none;">add ptx</a> </small>')


	def mkzip_prompt(self, account, loc):
		return ('''
				<!DOCTYPE html>
				<html>
				<head>
				  <meta charset = "utf-8">
				    <title>mc</title>
				    <link rel="stylesheet" href="style.css">
				  </head>
				  <body>
				<h>Zip directory: %s / %s</h>
				<p>Compress directory into a .zip file.  This will take a while.  
				Enter your email below to be notified when the zip is complete.
				Once you press "ZIP" please do not press back.</p>
				<form action="/mkzip_prompt/%s/%s" method="post"
				enctype="multipart/form-data"> <small>
				<input type="text" name="email" placeholder="email" />
				<input type="submit" value="ZIP" /> </small>
				</form>
				</body>
				</html>''' %(account, loc, account, loc))

	def mkziplog(self):
		return ('''
				<!DOCTYPE html>
				<html>
				<head>
				  <meta charset = "utf-8">
				    <title>mc</title>
				    <link rel="stylesheet" href="style.css">
				    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
				  	<script>
						$(document).ready(function(){
							setInterval(function() {
								$('#stdout').load('/file/ziplog');
							}, 1000);

						});
					</script>
				  </head>
				  <body>
				<p>
				<div id="stdout">log</div>
				</p>
				</body>
				</html>''')


	def genFolderLinks(self, account, loc):
		if (loc == ''):
			return (' <small><a title="upload files" href="/upload_gen_folder/' + account +'" style="text-decoration: none;">upload</a></small>' )
		else:
			return (' <small><a title="upload files" href="/upload_gen_folder/' + account + '/' + loc +'" style="text-decoration: none;">upload</a></small>' )


	def addSong(self, account, user):
		return ('<br><a href="/addSong/%s" style="text-decoration: none;">add song</a>' % account)		
	
	def uploadSongZip(self, account, loc):
		return ('''<h>replace pro tools session</h>
				<p>Upload a compressed .zip file of the entire directory 
				to replace the current version on the server.  This will take a while to upload.  After you press upload, please do not press back.
				After it is done uploading, it will still take a few minutes to unzip.</p>
				<form action="/replace/%s/%s" method="post"
				enctype="multipart/form-data"> <small>
				<input type="file" name="upload" />
				<input type="submit" value="Upload" /> </small>
				</form>
				''' %(account, loc))

	def uploadGen(self, account, loc):
		if (loc == ''):
			return ('''<p>Upload a file to add to the current directory</p>
					<form action="/upload_gen_folder/%s" method="post"
					enctype="multipart/form-data"> <small>
					<input type="file" name="upload" />
					<input type="submit" value="Upload" /> </small>
					</form>
					''' % account)
		else:
			return ('''<p>Upload a file to add to the current directory</p>
					<form action="/upload_gen_folder/%s/%s" method="post"
					enctype="multipart/form-data"> <small>
					<input type="file" name="upload" />
					<input type="submit" value="Upload" /> </small>
					</form>
					''' %(account, loc))

	def uploadNewSongZip(self, account):
		return ('''<h>Add Song</h>
				<p>Upload a compressed .zip file of the entire Pro Tools Session
				directory.  This will take a while to upload.  After you press upload, please do not press back.
				After it is done uploading, it will still take a few minutes to unzip.  
				When this is complete it will be located in your home directory.</p>
				<form action="/addSong/%s" method="post"
				enctype="multipart/form-data"> <small>
				<input type="file" name="upload" />
				<input type="submit" value="Upload" /> </small>
				</form>
				'''% account)		

	def uploadPTX(self, account, loc):
		return ('''<h>add pro tools session file (ptx/ptf)</h>
				<p>if the ptx/ptf matches the name of an existing file it will be replaced in the top of the directory
				and the previous version will be moved to Session File Backups</p>
				<form action="/addPTX/%s/%s" method="post"
				enctype="multipart/form-data"> <small>
				<input type="file" name="upload" />
				<input type="submit" value="Upload" /> </small>
				</form>
				''' %(account, loc))

	head = '''
			<html lang="en">
			<head>
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			  <meta charset = "utf-8">
					<title>mc</title>
						<script>
						(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
						(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
						m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
						})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
						ga('create', 'UA-43748849-1', 'no-ip.biz');
						ga('send', 'pageview');
						</script>

					<link href="/file/navbar.css" rel="stylesheet">	
					<link href="/file/bootstrap.css" rel="stylesheet">
					<link rel="stylesheet" type="text/css" href="/file/style.css">
				</head>
			   <body>
			   	'''

	foot = '''		</div>  <!--/.container -->
					<script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    				<script href="/file/bootstrap.min.js"></script>
  				</body>
			</html>
			'''

	noAccess = head + 'You do not have access to this page. ' + '<a href="/login">home</a>'

	index = '''<h id=header></h> </html>'''
	
	loginForm = '''<html>
				<div class="center_login">
				<img src="file/churdump.jpg" width="150" height="240">
	            <form action="/login" method="post">
	            <input type="text" name="login" placeholder="username" style="width: 100%"/> <br>
	            <input type="password" name="password" placeholder="password" style="width: 100%"/> <br>
	            <input type="submit" value="Login" style="width: 100%"/>
	            </form></small>
	            '''

	linksFooter = '''<small> <a href= /master > new user </a>
				&nbsp;|&nbsp;
				<a href= /about > about  </a> </small></div>
				'''

	def folderLinksFooter(self, user, account): 
		return '''<small> <a href= /home/%s > home </a>
				&nbsp;|&nbsp;
				<a href= /account/%s > go up </a>
				&nbsp;|&nbsp;
				<a href= /addSong/%s> add song </a>
				&nbsp;|&nbsp;
				<a href= /logout > logout </a> </small>
				''' % (user, account, account)
	
	def homeFooter(self, user):
		return '''<small> <a href= pass/%s > change password </a>
				&nbsp;|&nbsp;
				<a href= /logout > logout </a> </small>
				''' % user

	about = head + loginForm + '''</div> <div class="center_links"><html> <small> <p> This is a private server hosted by matthew coppola. <br>
                I can be reached at mcoppola832@gmail.com  &nbsp;|&nbsp; <a href= /login > back </a>  </p> </small></div></html> '''

	addUser = head + loginForm + '''</div> <div class="center_links"> <small> <p>feature not available, contact me at mcoppola832@gmail.com &nbsp;|&nbsp; <a href= /login > back </a>  </p> </small></div> </html>'''

	# museyHeader = '''<html><head><link rel="stylesheet" href="style.css"></head>
	# 			<body>
	# 			<h id=museyhead>museyroom album</h>
	# 			<body>'''

	museyFooter = '''</ol></body></html>'''
	#linksHeader = '''<br><br><h>links /</h><ul>'''
	def linksHeader(self, account):
		return '''
			<br><br><h>links / <a href= /addlink/%s title="add link">+</a></h><ul>
			''' % account
	def addLinkForm(self, account):
		return '''<html>
				<h>Add link</h>
	            <form action="/addlink/%s" method="post">
	            title:    <input type="text" name="title" /> 
	            url: <input type="text" name="url" />
	            <input type="submit" value="Add Link" />
	            </form></small>
	            ''' % account

	logHeader = '''</ul><br><h>activity log /</h><small><ul>'''

