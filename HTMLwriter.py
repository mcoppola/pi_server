
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

	def userHomeHeader(self, user, loc = '', username= ''):
		return '''
				<div class="container">

			      <div class="navbar navbar-default">
			        <div class="navbar-header">
			          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			          </button>
			        </div>
			        <div class="navbar-collapse collapse">
			          <ul class="nav navbar-nav">
			            <li class="active"><a href="/home/%s"><i class="glyphicon glyphicon-home"></i></a></li>
			          </ul>
			          <ul class="nav navbar-nav navbar-right">
			          	<li class="dropdown">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="glyphicon glyphicon-user"></i>  %s </a>
			              <ul class="dropdown-menu">
			                <li><a href="#">Change Password</a></li>
			                <li><a href="#">Change Email</a></li>
			                <li class="divider"></li>
			                <li><a href="/logout">Logout</a></li>
			              </ul>
			            </li>
			          </ul>
			        </div><!--/.nav-collapse -->
			      </div><!--/.navbar navbar-default -->
				''' % (username, username)

	def proToolsProjectHeader(self, user, loc = '', username= ''):
		# NAVBAR for ProTools Folders
		return '''
				<div class="container">
			      <div class="navbar navbar-default">
			        <div class="navbar-header">
			          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			          </button>
			        </div>
			        <div class="navbar-collapse collapse">
			          <ul class="nav navbar-nav">
			            <li><a href="/home/%s"><i class="glyphicon glyphicon-home"></i></a></li>
			            <li><a class="navbar-brand" href="#">%s / %s </a>
			            <li class="dropdown">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="glyphicon glyphicon-plus"></i></b></a>
			              <ul class="dropdown-menu">
			              	<li role="presentation" class="dropdown-header">Add</li>
			                <li><a href="#">Song</a></li>
			                <li><a href="#">Collaborator</a></li>
			              </ul>
			            </li>
			          </ul>
			          <ul class="nav navbar-nav navbar-right">
			          	<li class="dropdown">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="glyphicon glyphicon-user"></i>  %s </a>
			              <ul class="dropdown-menu">
			                <li><a href="#">Change Password</a></li>
			                <li><a href="#">Change Email</a></li>
			                <li class="divider"></li>
			                <li><a href="/logout">Logout</a></li>
			              </ul>
			            </li>
			          </ul>
			        </div><!--/.nav-collapse -->
			      </div><!--/.navbar navbar-default -->
				''' % (username, user, loc, username)

	def proToolsSessionHeader(self, group, loc = '', username= ''):
		# NAVBAR for ProTools Folders
		return '''
				<div class="container">
			      <div class="navbar navbar-default">
			        <div class="navbar-header">
			          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			          </button>
			        </div>
			        <div class="navbar-collapse collapse">
			          <ul class="nav navbar-nav">
			            <li><a href="/home/%s"><i class="glyphicon glyphicon-home"></i></a></li>
			            <li><a class="navbar-brand" href="/account/%s">%s</a>
			            <a class="navbar-brand" href="#" style="right:25px">/ %s </a></li>
			            <li class="dropdown">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#" style="right:25px"><i class="glyphicon glyphicon-plus"></i></b></a>
			              <ul class="dropdown-menu">
			              	<li role="presentation" class="dropdown-header">Commit</li>
			                <li><a href="#">PTF</a></li>
			                <li><a href="#">PTX</a></li>
			                <li class="divider"></li>
			                <li role="presentation" class="dropdown-header">Add</li>
			                <li><a href="#">Audio File</a></li>
			                <li><a href="#">Fade File</a></li>
			                <li><a href="#">Session Backup</a></li>
			                <li><a href="#">Zipped Resources</a></li>
			              </ul>
			            </li>
			            <li class="dropdown">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#" style="right:25px"><i class="glyphicon glyphicon-file"></i></b></a>
			              <ul class="dropdown-menu">
			                <li><a href="#">Make Zip</a></li>
			                <li><a href="#">Replace Entire Session</a></li>
			                <li><a href="#">Backup PTX</a></li>
			                <li><a href="#">Backup PTF</a></li>
			              </ul>
			            </li>    
			          </ul>
			          <ul class="nav navbar-nav navbar-right">
			          	<li class="dropdown">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="glyphicon glyphicon-user"></i>  %s </a>
			              <ul class="dropdown-menu">
			                <li><a href="#">Change Password</a></li>
			                <li><a href="#">Change Email</a></li>
			                <li class="divider"></li>
			                <li><a href="/logout">Logout</a></li>
			              </ul>
			            </li>
			          </ul>
			        </div><!--/.nav-collapse -->
			      </div><!--/.navbar navbar-default -->
				''' % (username, group, group, loc, username)
	# Log array = [time, song-commited-to, user-who-commited, action, message]
	def notification(self, user, group, log):
		return '''<div class="alert alert-dismissable">
					<button type="button" class="close" data-dismiss="alert" aria-hidden="true">
					&times;
					</button>
					<p style="font-size:meduim"><a class="alert-link" href="/account/%s" class="list-group-item">%s</a>,     <!--/.group -->
					<a class="alert-link" href="/account/%s/%s" class="list-group-item">%s</a>,  <!--/.song -->
					<span style="color:#999; font-size:small"><medium> %s</medium></span>
					</p>    <!--/.action -->
					<p style="font-size:small">
					<a class="alert-link" href="/user/%s" class="list-group-item">%s</a>: %s</p><!--/.message -->
					</div>
				''' % (group, group, group, log[1], log[1], log[3], log[2], log[2], log[4])

	accountListHeader = ''' <div class="row">
  									<div class="col-md-7">
									<div class="panel panel-info">
										<div id="newProjectForm" class="modal fade in" role="dialog">
											<div class="modal-dialog">
												<div class="modal-content">
												<div class="modal-header">
													<a class="close" data-dismiss="modal">x</a>
													<h3>New Project</h3>
												</div>
												<div class="modal-dialog">
													<form action="/newProject" method="post">
											            <input type="text" name="projectName" placeholder="Project Name" style="width:80%"/> <br>
											            <input type="text" name="collaborators" placeholder="Add Collaborator" style="width:80%"/> <br>
											        </form>	        
												</div>
												<div class="modal-footer">
													<a href="#" class="btn btn-success">Create</a>
													<a href="#" class="btn" data-dismiss="modal">Close</a>
												</div>
												</div><!--./modal-content-->
											</div><!--./modal-dialog-->
										</div>
										<div class="panel-heading">Pro Tools Projects
										  <span class="pull-right">
												<a data-toggle="modal" href="#newProjectForm" class="btn btn-default btn-xs" title="New Project">
												<i class="glyphicon glyphicon-plus"></i></a>
													    
													    
										  </span>

										</div><!--./panel-heading-->
									<div class="list-group">
							
						'''


	accountListFooter = '''
							</div><!--/.list-group -->
							</div><!--/.panel-info -->
							</div><!--/.col-md-7 -->
						'''

	notesListHeader = '''<div class="col-md-5">
								<div class="panel panel-warning">
									<div class="panel-heading">Notifications</div>
										<div class="list-group">
					'''

	notesListFooter = '''
							</div><!--/.list-group -->
							</div><!--/.panel -->
							</div><!--/.col-md-5 -->
							
						'''
	def linksListHeader(self, account):
		return '''<div class="col-md-5 pull-right">
					<div class="panel panel-success">
					<div id="newLinkForm" class="modal fade in" role="dialog">
								<div class="modal-dialog">
									<div class="modal-content">
									<div class="modal-header">
										<a class="close" data-dismiss="modal">x</a>
										<h3>New Link</h3>
									</div>
									<div class="modal-dialog">
										<form action="/addlink/%s" method="post">
								            <input type="text" name="title" placeholder="Title"/> 
								            <input type="text" name="url" placeholder="URL"/>
								               
									</div>
									<div class="modal-footer">
										<a href="/addlink/%s" class="btn btn-success"><input type="submit" value="Add Link"/></a>
										</form>
										<a href="#" class="btn" data-dismiss="modal">Close</a>
									</div>
									</div><!--./modal-content-->
								</div><!--./modal-dialog-->
							</div>
						<div class="panel-heading">Links
							<span class="pull-right">
									<a data-toggle="modal" href="#newLinkForm" class="btn btn-success btn-xs" title="New Link">
									<i class="glyphicon glyphicon-plus"></i></a>	    
							  </span>
						</div>
							<div class="list-group">
					'''% (account, account)

	linksListFooter = '''
							</div><!--/.list-group -->
							</div><!--/.panel -->
							</div><!--/.col-md-5 -->
							
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
								$('#stdout').load('/static/ziplog');
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
			<!DOCTYPE html>
			<html lang="en">
			<head>
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			  <meta charset = "utf-8">
					<title>mc</title>
					<link href="/static/style.css" rel="stylesheet">
					<link href="/static/navbar.css" rel="stylesheet">
					<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.1/css/bootstrap.min.css" rel="stylesheet">
					<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css" rel="stylesheet">
					<link href="select2.css" rel="stylesheet"/>
				    
				</head>
			   <body>
			   	'''

	foot = '''		</div>  <!--/.container -->
					<script src="http://code.jquery.com/jquery-1.9.1.min.js" type="text/javascript"></script>
					<script type="text/javascript" src="//netdna.bootstrapcdn.com/bootstrap/3.0.1/js/bootstrap.min.js"></script>
					<script src="select2.js"></script>
				    <script>
				        $(document).ready(function() { $("#collabForm").select2({
				        	placeholder: "Add Collaborators",
				        	data:["mc", "ben", "david"]}); });
				    </script>						
  				</body>
			</html>
			'''

	songListHeader = '''
					<div class="row">
  						<div class="col-md-7">
							<div class="panel panel-default">
							<div id="newSongForm" class="modal fade in" role="dialog">
								<div class="modal-dialog">
									<div class="modal-content">
									<div class="modal-header">
										<a class="close" data-dismiss="modal">x</a>
										<h3>New Song</h3>
									</div>
									<div class="modal-dialog">
										<form action="/addlink/%s" method="post">
								            <input type="text" name="title" placeholder="Song Name"/> 
								            <input type="file" name="zip" placeholder="Zip"/>
								        </form>       
									</div>
									<div class="modal-footer">
										<a href="#" class="btn btn-success">Add Song</a>
										<a href="#" class="btn" data-dismiss="modal">Close</a>
									</div>
									</div><!--./modal-content-->
								</div><!--./modal-dialog-->
							</div>
					  			<div class="panel-heading">Songs
					  			<span class="pull-right">
									<a data-toggle="modal" href="#newSongForm" class="btn btn-default btn-xs" title="New Song">
									<i class="glyphicon glyphicon-plus"></i></a>	    
							    </span>
							    </div>
					  		
					  			<ul class="list-group">
					'''
	songListFooter = '''
								</ul><!-- /list-group -->
							</div><!-- /panel -->
						</div><!-- /col-md-7 -->
					
					'''

	noAccess = head + 'You do not have access to this page. ' + '<a href="/login">home</a>'

	index = '''<h id=header></h> </html>'''
	
	loginForm = '''<html>
				<div class="center_login">
				<img src="/static/churdump.jpg" width="150" height="240">
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
	
	homeFooter ='''
					</div><!--/.row -->
				'''

	about = head + loginForm + '''</div> <div class="center_links"><html> <small> <p> This is a private server hosted by matthew coppola. <br>
                I can be reached at mcoppola832@gmail.com  &nbsp;|&nbsp; <a href= /login > back </a>  </p> </small></div></html> '''

	addUser = head + loginForm + '''</div> <div class="center_links"> <small> <p>feature not available, contact me at mcoppola832@gmail.com &nbsp;|&nbsp; <a href= /login > back </a>  </p> </small></div> </html>'''

	# museyHeader = '''<html><head><link rel="stylesheet" href="style.css"></head>
	# 			<body>
	# 			<h id=museyhead>museyroom album</h>
	# 			<body>'''

	olFooter = '''</ol>'''
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

