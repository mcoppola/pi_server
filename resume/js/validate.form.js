String.prototype.trim = function() 
{
	return this.replace(/^\s+|\s+$/g,"");
} 

function validateForm()
{
	if (document.getElementById("Message").value.trim() == '')
	{
		alert("Message cannot be left blank");
		return false;
	}

	var name = document.forms["contactForm"]["Name"].value;
	if (name == null || name == "")
	{
		alert("Name cannot be left blank");
		return false;
	}
	
	var email = document.forms["contactForm"]["Email"].value;
	if (email == null || email == "")
	{
		alert("Email cannot be left blank");
		return false;
	}
	var atpos = email.indexOf("@");
	var dotpos = email.lastIndexOf(".");
	if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length)
	{
		alert("Not a valid e-mail address");
		return false;
	}  		
}