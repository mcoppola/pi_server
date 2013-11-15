
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

			      <div class="navbar navbar-info">
			        <div class="navbar-header">
			          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			          </button>
			        </div>
			        <div class="navbar-collapse collapse">
			          <ul class="nav navbar-nav">
			           <li class="active home_btn"><a href="/home/%s"><i class="glyphicon glyphicon-home"></i></a></li>
			           <li class="dropdown user_btn">
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

	def proToolsProjectHeader(self, account, loc = '', username= ''):
		# NAVBAR for ProTools Folders
		return '''
				<div class="container">
			      <div class="navbar navbar-info">
			        <div class="navbar-header">
			          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			          </button>
			        </div>
			        <div class="navbar-collapse collapse">
			          <ul class="nav navbar-nav">
			            <li class="home_btn"><a href="/home/%s"><i class="glyphicon glyphicon-home"></i></a></li>
			            <li class="dropdown user_btn">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="glyphicon glyphicon-user"></i>  %s </a>
			              <ul class="dropdown-menu">
			                <li><a href="#">Change Password</a></li>
			                <li><a href="#">Change Email</a></li>
			                <li class="divider"></li>
			                <li><a href="/logout">Logout</a></li>
			              </ul>
			            </li>
			            <li><a class="navbar-brand" href="#">%s / %s </a>
			            <li class="dropdown">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="glyphicon glyphicon-plus"></i></b></a>
			              <ul class="dropdown-menu">
			              	<li role="presentation" class="dropdown-header">Add</li>
			                <li><a data-toggle="modal" href="#newSongForm">Song</a></li>
			                <li><a href="#">Collaborator</a></li>
			              </ul>
			            </li>
			          </ul>
			        </div><!--/.nav-collapse -->
			      </div><!--/.navbar navbar-default -->
				''' % (username, username, account, loc)

	def proToolsSessionHeader(self, group, loc = '', username= ''):
		# NAVBAR for ProTools Folders
		locFull = loc
		if (len(loc.split('/')) == 3):
			locSplit = loc.split('/')
			loc = locSplit[0]
			return '''
				<div class="container">
			      <div class="navbar navbar-info">
			        <div class="navbar-header">
			          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			          </button>
			        </div>
			        <div class="navbar-collapse collapse">
			          <ul class="nav navbar-nav">
			            <li class="home_btn"><a href="/home/%s"><i class="glyphicon glyphicon-home"></i></a></li>
			            <li><a class="navbar-brand" href="/account/%s">%s</a>
			            <a class="navbar-brand" href="/account/%s/%s" style="margin-left:-25px">/ %s</a>
			            <a class="navbar-brand" href="/account/%s/%s/%s" style="margin-left:-25px">/ %s</a></li>  
			          </ul>
			        </div><!--/.nav-collapse -->
			      </div><!--/.navbar navbar-default -->
			      <div style="position:relative; left:0px">
				''' % (username, group, group, group, loc, loc, group, loc, locSplit[1], locSplit[1])
		elif (len(loc.split('/')) > 1):
			locSplit = loc.split('/')
			loc = locSplit[0]

		return '''
				<div class="container">
			      <div class="navbar navbar-info">
				      <div id="addPTXForm" class="modal fade in" role="dialog">
									<div class="modal-dialog">
										<div class="modal-content">
										<div class="modal-header">
											<a class="close" data-dismiss="modal">x</a>
											<h3>Commit Session File</h3>
										</div>
										<div class="modal-body">
											<p>Upload a PTX or PTF file to be commited.  This will become the current session file in this directory 
											and other collaborators will be notified.  The previous PTX or PTF of the same name will be coppied into the "Session File Backups" folder.</p>
											<br>
											<form action="/addPTX/%s/%s" method="post" enctype="multipart/form-data">
												<input type="text" name="message" placeholder="Commit Message"/><br> 
									            <input type="file" name="upload" value="Upload"/>
								              
										</div>
										<div class="modal-footer">
											<input class="btn btn-success" type="submit" value="Commit"/></form>
											<a href="#" class="btn" data-dismiss="modal">Close</a>
										</div>
										</div><!--./modal-content-->
									</div><!--./modal-dialog-->
								</div>
				        <div class="navbar-header">
			          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			            <span class="icon-bar"></span>
			          </button>
			        </div>
			        <div class="navbar-collapse collapse">
			          <ul class="nav navbar-nav">
			            <li class="home_btn"><a href="/home/%s"><i class="glyphicon glyphicon-home"></i></a></li>
			            <li><a class="navbar-brand" href="/account/%s">%s</a>
			            <a class="navbar-brand" href="/account/%s/%s" style="margin-left:-25px">/ %s </a></li>
			            <li class="dropdown">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="glyphicon glyphicon-plus"></i></b></a>
			              <ul class="dropdown-menu">
			              	<li role="presentation" class="dropdown-header">Commit</li>
				                <li><a data-toggle="modal" href="#addPTXForm">PTX</a></li>
				                <li><a data-toggle="modal" href="#addPTXForm">PTF</a></li>
			                <li class="divider"></li>
			                <li role="presentation" class="dropdown-header">Add</li>
			                <li><a href="#">Audio File</a></li>
			                <li><a href="#">Fade File</a></li>
			                <li><a href="#">Session Backup</a></li>
			                <li><a href="#">Zipped Resources</a></li>
			              </ul>
			            </li>
			            <li class="dropdown">
			              <a class="dropdown-toggle" data-toggle="dropdown" href="#"><i class="glyphicon glyphicon-wrench"></i></b></a>
			              <ul class="dropdown-menu">
			                <li><a href="#">Make Zip</a></li>
			                <li><a href="#">Replace Entire Session</a></li>
			                <li><a href="#">Backup PTX</a></li>
			                <li><a href="#">Backup PTF</a></li>
			              </ul>
			            </li>    
			          </ul>
			        </div><!--/.nav-collapse -->
			      </div><!--/.navbar navbar-default -->
			      <div style="position:relative; left:16px">
				''' % (group, loc, username, group, group, group, loc, locFull)
	# Log array = [time, group, song-commited-to, user-who-commited, action, message]
	def notification(self, user, log, time):
		return '''	<div class="panel-body" style="padding:10px">
					<button type="button" class="close" data-dismiss="alert" aria-hidden="true" onclick="removeNotification('%s', '%s');">
					&times;
					</button>
					<p style="font-size:meduim"><a class="alert-link" href="/account/%s"><font color="#3AA4FF">%s</font></a>,     <!--/.group -->
					<a class="alert-link" href="/account/%s/%s"><font color="#1BA68C">%s</font></a> <!--/.song -->
					</p>    <!--/.header -->
					<p style="font-size:small; line-height:0px">
					<span style="color:#999; font-size:small"><medium> %s, %s</medium></span>
					</p>
					<p style="font-size:small">
					<a class="alert-link" href="/user/%s"><font color="#F2522E">%s</font></a>: %s</p><!--/.message -->
					</div>
				''' % (log[0], log[1], log[1], log[1], log[1], log[2], log[2], log[4], time, log[3], log[3], log[5])

	def notificationLatest(self, user, log, time):
		return '''	<div class="panel-body" style="padding:10px">
					<p style="font-size:meduim"><a class="alert-link" href="/account/%s"><font color="#3AA4FF">%s</font></a>,     <!--/.group -->
					<a class="alert-link" href="/account/%s/%s"><font color="#1BA68C">%s</font></a> <!--/.song -->
					</p>    <!--/.header -->
					<p style="font-size:small; line-height:0px">
					<span style="color:#999; font-size:small"><medium> %s, %s</medium></span>
					</p>
					<p style="font-size:small">
					<a class="alert-link" href="/user/%s"><font color="#F2522E">%s</font></a>: %s</p><!--/.message -->
					</div>
				''' % (log[1], log[1], log[1], log[2], log[2], log[4], time, log[3], log[3], log[5])

	def linkItem(self, user, group, link, index):
		return '''
				<a target="_blank" href="%s" class="list-group-item li_link"><b>%s</b>
				<button type="button" class="close" data-dismiss="alert" aria-hidden="true" onclick="removeLink('%s', %d);">
					&times;
					</button>
				</a>
				''' % (link[0], link[1], group, index)

	def folderItem(self, account, loc, dir_name):
		return '''
				<a class="folder" href="/account/%s/%s%s" style="">
				<i class="glyphicon glyphicon-folder-close"></i> %s</a><br>
				''' % (account, loc, dir_name, dir_name)

	# Log array = [time, group, song-commited-to, user-who-commited, action, message]
	def sessionHistoryItem(self, user, log, time):
		return '''	<div class="panel-body" style="padding:10px; margin-left: 18px">
					<p style="font-size:meduim"><a class="alert-link" href="#"><font color="#3AA4FF">%s</font>, <!--/.date -->
					<span style="color:#999; font-size:small"><medium> %s </medium></span>
					</p>    <!--/.header -->
					<p style="font-size:small;">
					<a class="alert-link" href="/user/%s"><font color="#F2522E">%s</font></a>: %s</p><!--/.message -->
					</div>
				''' % (time, log[4], log[3], log[3], log[5])

	def sessionHistoryItemBehind(self, user, log, time):
		return '''	<div class="panel-body" style="padding:10px">
					<p style="font-size:meduim;"><i style="color:#F2522E" class="glyphicon glyphicon-flag"></i>&nbsp;<a class="alert-link" href="#"><font color="#3AA4FF">%s</font>, <!--/.date -->
					<span style="color:#999; font-size:small"><medium> %s </medium></span>
					</p>    <!--/.header -->
					<p style="font-size:small; margin-left: 18px">
					<a class="alert-link" href="/user/%s"><font color="#F2522E">%s</font></a>: %s</p><!--/.message -->
					</div>
				''' % (time, log[4], log[3], log[3], log[5])

	accountListHeader = ''' <div class="row">
  									<div class="col-md-6"> 
									<div class="panel panel-primary">
										<div id="newProjectForm" class="modal fade in" role="dialog">
											<div class="modal-dialog">
												<div class="modal-content">
												<div class="modal-header">
													<a class="close" data-dismiss="modal">x</a>
													<h3>New Project</h3>
												</div>
												<div class="modal-body">
												<p>Feature not available.  Contact matt to add a new project.</p>
													      
												</div>
												<div class="modal-footer">
													<a href="#" class="btn" data-dismiss="modal">Close</a>
												</div>
												</div><!--./modal-content-->
											</div><!--./modal-dialog-->
										</div>
										<div class="panel-heading">Pro Tools Projects
										  <span class="pull-right">
												<a data-toggle="modal" href="#newProjectForm" class="btn btn-default btn-xs" title="New Project">
												<font color="B8B8B8"><i class="glyphicon glyphicon-plus"></i></font></a>
										  </span>

										</div><!--./panel-heading-->
									<div class="list-group">
							
						'''


	accountListFooter = '''
							</div><!--/.list-group -->
							</div><!--/.panel-info -->
							</div><!--/.col-md-5 -->
						'''

	notesListHeader = '''<div class="col-md-6">
								<div class="panel panel-warning">
									<div class="panel-heading">Notifications</div>
											<div class="list-group">

					'''

	notesListFooter = '''
							</div><!--/.list-group -->
							</div><!--/.panel -->
							</div><!--/.col-md-6 -->
							
						'''

	sessionHistoryHeader = '''<br><br>
							<div class="col-md-12">
								<div class="panel panel-default">
									<div class="panel-heading">Session History</div>
											<div class="list-group">

							'''

	sessionHistoryFooter = '''
						</div><!--/.list-group -->
						</div><!--/.panel -->
						</div><!--/.col-md-12 -->
						
					'''
	def linksListHeader(self, account):
		return '''<div class="col-md-6 pull-right">
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
										<input class="btn btn-success" type="submit" value="Add Link"/></form>
										<a href="#" class="btn" data-dismiss="modal">Close</a>
										
									</div>
									</div><!--./modal-content-->
								</div><!--./modal-dialog-->
							</div>
						<div class="panel-heading">Links
							<span class="pull-right">
									<a data-toggle="modal" href="#newLinkForm" class="btn btn-default btn-xs" title="New Link">
									<font color="B8B8B8"><i class="glyphicon glyphicon-plus"></i></font></a>	    
							  </span>
						</div>
							<div class="list-group">
					'''% (account)

	linksListFooter = '''
							</div><!--/.list-group -->
							</div><!--/.panel -->
							</div><!--/.col-md-6 -->
							
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
					<link href="/static/navbar.css" rel="stylesheet">
					<link href="/static/bootstrap.css" rel="stylesheet">
					<link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css" rel="stylesheet">
				    <link href="/static/style.css" rel="stylesheet">
				</head>
			   <body>
			   	'''

	foot = '''		</div>  <!--/.container -->
					<script src="/static/jquery-1.10.2.min.js" type="text/javascript"></script>
					<script type="text/javascript" src="/static/bootstrap.min.js"></script>
				    <script>
						function removeLink(account, i)
						{
						window.location.replace("/removeLink/" + account + "/" + i);
						}
						function removeNotification(date, account)
						{
						window.location.replace("/removeNotification/" + date + "/" + account;
						}
					</script>					
  				</body>
			</html>
			'''

	def songListHeader(self, account):
		return '''
					<div class="row">
  						<div class="col-md-6">
							<div class="panel panel-default">
							<div id="newSongForm" class="modal fade in" role="dialog">
								<div class="modal-dialog">
									<div class="modal-content">
									<div class="modal-header">
										<a class="close" data-dismiss="modal">x</a>
										<h3>New Song</h3>
									</div>
									<div class="modal-body">
										<p>Upload a Zip file of the entire Pro Tools Directory.  It will be extracted into this account.  
										This will take a while depending on the size of the session. Please do not press "back" after the upload has begun. </p>
										<br>
										<form action="/addSong/%s" method="post" enctype="multipart/form-data"> 
								            <input type="file" name="upload" value="Upload"/>
								              
									</div>
									<div class="modal-footer">
										<input class="btn btn-success" type="submit" value="Add Song"/></form>
										<a href="#" class="btn" data-dismiss="modal">Close</a>
									</div>
									</div><!--./modal-content-->
								</div><!--./modal-dialog-->
							</div>
					  			<div class="panel-heading">Songs
					  			<span class="pull-right">
									<a data-toggle="modal" href="#newSongForm" class="btn btn-default btn-xs" title="New Song">
									<font color="B8B8B8"><i class="glyphicon glyphicon-plus"></i></font></a>	    
							    </span>
							    </div>
					  		
					  			<ul class="list-group">
					''' % account

	songListFooter = '''
								</ul><!-- /list-group -->
							</div><!-- /panel -->
						</div><!-- /col-md-6
						 -->
					
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

