class Scripts(object):
	
Scripts.prototype.stdoutDisplay = function (canvas) {
	window.onload = function () {(

		var canvas = document.getElementById('canvas'),
        context = canvas.getContext('2d');


		function drawFrame () {
	        utils.getAnimationFrame();
	        window.requestAnimationFrame(drawFrame, canvas);

	        var fso = new ActiveXObject('Scripting.FileSystemObject'),
	        iStream=fso.OpenTextFile('site/scripts/ziplog', 1, false);
		    while(!iStream.AtEndOfStream) {
		        document.body.innerHTML += iStream.ReadLine() + '<br/>';
		    }        
		    iStream.Close();


      }());
    };
}

Scripts.prototype.makeZipStdout = function () {
	var fso = new ActiveXObject('Scripting.FileSystemObject'),
    iStream=fso.OpenTextFile('site/scripts/ziplog', 1, false);
    while(!iStream.AtEndOfStream) {
        document.body.innerHTML += iStream.ReadLine() + '<br/>';
    }        
    iStream.Close();
}

Scripts.prototype.setCanvas = function (window) {
	window.addEventListener(
		'load',
		function () {
			var canvas = document.getElementsByTagName('canvas')[0];

			//fullscreenify(canvas);
		},
		false
		);

Scripts.prototype.fullscreenify = function (canvas) {
		var style = canvas.getAttribute('style') || '';
		window.addEventListener('resize', function () {resize(canvas);}, false);

		resize(canvas);

		function resize(canvas) {

			if(window.innerWidth > window.innerHeight) {
				canvas.width  = Math.min(600, window.innerHeight - 60);
				canvas.height = Math.min(600, window.innerHeight - 60);
			}
			else {
				canvas.width = Math.min(600, window.innerWidth - 60);
				canvas.height = Math.min(600, window.innerWidth - 60);
			}

		}
	}
}