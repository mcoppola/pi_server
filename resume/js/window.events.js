var divID = 'pop1';

window.onload = function() 
{
	//var divID = 'pop1';
	var url = document.URL;
	hashPresent = url.substring(url.lastIndexOf('#')+1);
	
	if(hashPresent == 'PersonalStatement')
	{ 
		showPopOver(divID);
	}
	
	// SET EVENT LISTENERS TO CLOSE WHEN CLICKED OUTSIDE OF DIV OR PRESSING ESCAPE
	d = document.getElementById(divID);
	d.addEventListener("click", function(e){e.stopPropagation()}, true);
	addEventListener("click", function() {closePopOver(divID)},false);
	addEventListener("keyup", function(e){e.keyCode == 27 && (closePopOver(divID))}, false);
}
window.onresize = function()
{
	if (document.getElementById(divID).style.display == "block")
	{
		closePopOver(divID);
		showPopOver(divID);
	}
}