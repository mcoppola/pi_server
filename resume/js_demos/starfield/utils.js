var utils = {};


utils.captureMouse = function (element) {
	var mouse = {x: 0, y: 0};

	element.addEventListener('mousemove', function (event) {
		var x, y;
		if (event.pageX || event.pageY){
			x = event.pageX;
			y = event.pageY;
		} else {
			x = event.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
			y = event.clientY + document.body.scrollTop + document.documentElement.scrollTop;
		}
		x -= element.offsetLeft;
		y -= element.offsetTop;

		mouse.x = x;
		mouse.y = y;
	}, false);

	return mouse;
};

utils.captureTouch = function (element) {
	var touch = {x: null, y: null, ispressed: false};

	element.addEventListener('touchstart', function (event) {
		touch.ispressed = true;
	}, false);

	element.addEventListener('touchend', function (event) {
		var x, y, 
			touch_event = event.touches[0]; 

		if(touch_event.pageX || touch_event.pageY) {
			x = touch_event.pageX;
			y = touch_event.pageY;
		} else {
			x = touch_event.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
			y = touch_event.clientY + document.body.scrollTop + document.documentElement.scrollTop;		
		}
		x -= offsetLeft;
		y -= offsetTop;

		touch.x = x;
		touch.y = y;
	}, false);
	return touch;
};

utils.getAnimationFrame = function () {
	if(!window.requestAnimationFrame){
		window.requestAnimationFrame = (window.webkitRequestAnimationFrame ||
										window.mozRequestAnimationFrame ||
										window.oRequestAnimationFrame ||
										window.msRequestAnimationFrame ||
										function (callback) {
											return window.setTimeout(callback, 1000/60)
										});
	}
};