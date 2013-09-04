function Room (context, width, height) {
	this.x = 0;
	this.y = 0;
	this.z = 1;
	this.frame = 0;
	this.shiftX = 0.2; //staring conditions
	this.shiftY = 1.6; //
	this.shiftFactor = 20;
	this.context = context;
	this.width = width;
	this.height = height;
	this.color = "#000000";
	this.playing = false;
	this.paused = false;
	this.lineWidth = 1;
	this.areaLines = [];
	this.walls = new Walls (this);
	this.lineCount = 50;
	this.delay = 200;
	this.segmentLength = width/8.5;

}
Room.prototype.play = function () {

//draw gradient
	this.walls.draw();

//AREA LINES
	for(var i = 1; i < this.lineCount; i++) {
		this.areaLines[i] = new AreaLine(this, this.x - (i*this.delay), this.y - (i*this.delay));
		this.areaLines[i].draw(this.context, this.frame - (i*this.delay), this.width, this.height, i);
	}

}

function AreaLine (room, x, y) {
	this.room = room;
	this.x = x;
	this.y = y;
	this.shiftXL = room.shiftX;
	this.shiftXR = 1 + (1 - room.shiftX);
	this.shiftYT = room.shiftY;
	this.shiftYB = 1 + (1 - room.shiftY);
	this.z = room.z;
	this.color = "#000000";
	this.lineWidth = 1;
}
AreaLine.prototype.draw = function (context, frame, width, height, i) {

	context.save();
	context.beginPath();
	context.globalAlpha = (width/2 - (this.x + 30))/(width/2);
	context.lineWidth = this.lineWidth;
	
	seg = this.room.segmentLength - (frame)/3.6;
	if (seg < 0) {
		seg = 0;
	}

	//boxes
	if (i % 2 == 0) {
		if (width/2 > this.x + 30) {
/*			context.shadowBlur = 15;
			context.shadowColor = this.color;*/
			//top
			context.moveTo(this.x*this.shiftXL + seg*this.shiftXL, this.y*this.shiftYT + seg*this.shiftYT);
			context.lineTo(width - this.x*this.shiftXR - seg*this.shiftXR, this.y*this.shiftYT + seg*this.shiftYT);
			//right
			context.moveTo(width - this.x*this.shiftXR - seg*this.shiftXR, this.y*this.shiftYT + seg*this.shiftYT);
			context.lineTo(width - this.x*this.shiftXR - seg*this.shiftXR, height - this.y*this.shiftYB - seg*this.shiftYB);
			//bottom
			context.moveTo(width - this.x*this.shiftXR - seg*this.shiftXR, height - this.y*this.shiftYB - seg*this.shiftYB);
			context.lineTo(this.x*this.shiftXL + seg*this.shiftXL, height - this.y*this.shiftYB - seg*this.shiftYB);
			//left
			context.moveTo(this.x*this.shiftXL + seg*this.shiftXL, height - this.y*this.shiftYB - seg*this.shiftYB);
			context.lineTo(this.x*this.shiftXL + seg*this.shiftXL, this.y*this.shiftYT + seg*this.shiftYT);
			
			context.stroke();
			
		}
	}

	if(width/2 > this.x + 30) {	
		context.beginPath();

		//top left
		context.moveTo(this.x*this.shiftXL, this.y*this.shiftYT);
		context.lineTo(this.x*this.shiftXL + seg*this.shiftXL, this.y*this.shiftYT + seg*this.shiftYT);
		
		//top right
		context.moveTo(width - this.x*this.shiftXR, this.y*this.shiftYT);
		context.lineTo(width - this.x*this.shiftXR - seg*this.shiftXR, this.y*this.shiftYT + seg*this.shiftYT);

		//bottom left
		context.moveTo(this.x*this.shiftXL, height - this.y*this.shiftYB);
		context.lineTo(this.x*this.shiftXL + seg*this.shiftXL, height  - this.y*this.shiftYB - seg*this.shiftYB);

		//bottom right
		context.moveTo(width - this.x*this.shiftXR, height - this.y*this.shiftYB);
		context.lineTo(width - this.x*this.shiftXR - seg*this.shiftXR, height - this.y*this.shiftYB - seg*this.shiftYB);
	}

	context.stroke();
	context.restore();
}

function Walls (room) {
	this.room = room;
	this.color1 = "white";
	this.color2 = "#EDEDED";
	this.color3 = "#344152";
}
Walls.prototype.draw = function () {
//GRADIENT
	//top
	var grd=this.room.context.createLinearGradient(0,0,0,(this.room.height/2)*this.room.shiftY);
	grd.addColorStop(.8,this.color1);
	grd.addColorStop(0,this.color3);
	grd.addColorStop(.6, this.color2);
	var top=[0,0, this.room.width,0, (this.room.width/2)*this.room.shiftX,(this.room.height/2)*this.room.shiftY];
	this.room.context.fillStyle = grd;
	this.room.context.beginPath();
	this.room.context.moveTo(top[0], top[1]);
	for( item=2 ; item < top.length-1 ; item+=2 ){this.room.context.lineTo( top[item] , top[item+1] )}
	this.room.context.closePath();
	this.room.context.fill();

	//left
	grd=this.room.context.createLinearGradient(0,(this.room.height/2)*this.room.shiftY,(this.room.width/2)*this.room.shiftX,(this.room.height/2)*this.room.shiftY);
	grd.addColorStop(.8,this.color1);
	grd.addColorStop(0,this.color3);
	grd.addColorStop(.6, this.color2);
	this.room.context.fillStyle = grd;
	this.room.context.beginPath();
	var left=[0,0, (this.room.width/2)*this.room.shiftX,(this.room.height/2)*this.room.shiftY, 0,this.room.height];
	this.room.context.moveTo(left[0], left[1]);
	for( item=2 ; item < left.length-1 ; item+=2 ){this.room.context.lineTo( left[item] , left[item+1] )}
	this.room.context.closePath();
	this.room.context.fill();


	//bottom
	grd=this.room.context.createLinearGradient(0,(this.room.height/2)*this.room.shiftY,0,this.room.height);
	grd.addColorStop(.2,this.color1);
	grd.addColorStop(1,this.color3);
	grd.addColorStop(.4, this.color2);
	this.room.context.fillStyle = grd;
	this.room.context.beginPath();
	var bottom=[0,this.room.height, (this.room.width/2)*this.room.shiftX,(this.room.height/2)*this.room.shiftY, this.room.width,this.room.height];
	this.room.context.moveTo(bottom[0], bottom[1]);
	for( item=2 ; item < bottom.length-1 ; item+=2 ){this.room.context.lineTo( bottom[item] , bottom[item+1] )}
	this.room.context.closePath();
	this.room.context.fill();

	//right
	grd=this.room.context.createLinearGradient((this.room.width/2)*this.room.shiftX,0,this.room.width,0);
	grd.addColorStop(.2,this.color1);
	grd.addColorStop(1,this.color3);
	grd.addColorStop(.4, this.color2);
	this.room.context.beginPath();
	var right=[this.room.width,this.room.height, (this.room.width/2)*this.room.shiftX,(this.room.height/2)*this.room.shiftY, this.room.width,0];
	this.room.context.moveTo(right[0], right[1]);
	for( item=2 ; item < right.length-1 ; item+=2 ){this.room.context.lineTo( right[item] , right[item+1] )}
	this.room.context.closePath();
	this.room.context.fillStyle = grd;
	this.room.context.fill();

}


function SnowFlake (x, y, width, height, size) {
	if (size === undefined) { size = 4; }
	colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF",
		"#FF00FF", "#C0C0C0"];
	this.x = x;
	this.y = y;
	this.z = 1;
	this.size = size;
	this.delay = 100;
	this.color = colors[Math.floor(Math.random()*colors.length)];
	this.lineWidth = 3;

	this.dx = Math.abs(x - (width/2));
	this.dxu = x - width/2;
	this.dy = Math.abs(y - height/2);
	this.dyu = y - height/2;
	this.rate = (Math.sqrt(Math.pow(this.dx, 2)+Math.pow(this.dy, 2))/Math.sqrt(Math.pow(width/2, 2)+Math.pow(height/2, 2)))*3;
	if (this.dx > this.dy){
		this.xScale = this.dx/this.dy;
		this.yScale = 1;
	}
	else {
		this.xScale = 1;
		this.yScale = this.dy/this.dx;
	}

/*	this.trails = [];
	for (var i = 1; i < Math.random()*10; i++) {
		if(this.dxu < 0 && this.dyu < 0){
			this.trails.push(new SnowFlakeTrails(this.x - (i*this.delay*(this.dx/(width/2))), this.y - (i*(this.delay*(this.dy/(height/2)))), width, this.rate));
		}
		else if(this.dxu > 0 && this.dyu < 0){
			this.trails.push(new SnowFlakeTrails(this.x + (i*this.delay*(this.dx/(width/2))), this.y - (i*(this.delay*(this.dy/(height/2)))), width, this.rate));
		}
		else if(this.dxu < 0 && this.dyu > 0){
			this.trails.push(new SnowFlakeTrails(this.x - (i*this.delay*(this.dx/(width/2))), this.y + (i*(this.delay*(this.dy/(height/2)))), width, this.rate));
		}
		else if(this.dxu > 0 && this.dyu > 0){
			this.trails.push(new SnowFlakeTrails(this.x + (i*this.delay*(this.dx/(width/2))), this.y + (i*(this.delay*(this.dy/(height/2)))), width, this.rate));
		}
	}*/

}
SnowFlake.prototype.draw = function (context, frame, width, height, shiftX, shiftY) {
	
	context.save();
	context.lineWidth = this.lineWidth;
	context.beginPath();
	context.shadowBlur = 1;
	context.shadowColor = this.color;
	
	context.moveTo(this.x, this.y);
	context.lineTo(this.x + this.size*this.z, this.y + this.size*this.z);
	context.moveTo(this.x, this.y);
	context.lineTo(this.x - this.size*this.z, this.y + this.size*this.z);
	context.moveTo(this.x, this.y);
	context.lineTo(this.x + this.size*this.z, this.y - this.size*this.z);
	context.moveTo(this.x, this.y);
	context.lineTo(this.x - this.size*this.z, this.y - this.size*this.z);

	//context.strokeStyle = this.color;
	context.stroke();
	context.restore();


	/*for(var i = 0; i <this.trails.length; i++) {
		this.trails[i].draw(context, frame, width, height);
	}*/

	
	this.dx = Math.abs(this.x - (width/2)*shiftX);
	this.dy = Math.abs(this.y - (height/2)*shiftY);
	this.rate = (Math.sqrt(Math.pow(this.dx, 2)+Math.pow(this.dy, 2))/Math.sqrt(Math.pow((width/2)*shiftX, 2)+Math.pow((height/2)*shiftY, 2)))*3;
	if (this.dx > this.dy){
		this.xScale = this.dx/this.dy;
		this.yScale = 1;
	}
	else {
		this.xScale = 1;
		this.yScale = this.dy/this.dx;
	}

	rate = Math.max(this.z, 0.3)*this.rate;

	if(this.x > (width/2)*shiftX) {
		this.x -= 1/this.yScale*rate;
	}
	else if (this.x < (width/2)*shiftX) {
		this.x += 1/this.yScale*rate;
	}
	if(this.y > (height/2)*shiftY) {
		this.y -= 1/this.xScale*rate;
	}
	else if (this.y < (height/2)*shiftY) {
		this.y += 1/this.xScale*rate;
	}

}

/*function SnowFlakeTrails (x, y, width, height, rate) {
	colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF",
		"#FF00FF", "#C0C0C0"];
	this.x = x - 50;
	this.y = y - 50;
	this.z = 1;
	this.color = colors[Math.floor(Math.random()*colors.length)];
	this.lineWidth = 2;


	this.dx = Math.abs(x - width/2);
	this.dy = Math.abs(y - height/2);
	this.rate = rate;
	if (this.dx > this.dy){
		this.xScale = this.dx/this.dy;
		this.yScale = 1;
	}
	else {
		this.xScale = 1;
		this.yScale = this.dy/this.dx;
	}

}

SnowFlakeTrails.prototype.draw = function (context, frame, width, height) {
	
	context.save();
	context.translate(this.x, this.y);
	context.rotate(Math.PI*z);
	context.lineWidth = this.lineWidth;
	context.beginPath();
	
	context.moveTo(this.x, this.y);
	context.lineTo(this.x + 4*this.z, this.y + 4*this.z);
	context.moveTo(this.x, this.y);
	context.lineTo(this.x - 4*this.z, this.y + 4*this.z);
	context.moveTo(this.x, this.y);
	context.lineTo(this.x + 4*this.z, this.y - 4*this.z);
	context.moveTo(this.x, this.y);
	context.lineTo(this.x - 4*this.z, this.y - 4*this.z);

	context.strokeStyle = this.color;
	context.stroke();
	context.restore();

	rate = Math.max(this.z, 0.3)*this.rate;

	if(this.x > width/2) {
		this.x -= 1/this.yScale*rate;
	}
	else if (this.x < width/2) {
		this.x += 1/this.yScale*rate;
	}
	if(this.y > height/2) {
		this.y -= 1/this.xScale*rate;
	}
	else if (this.y < height/2) {
		this.y += 1/this.xScale*rate;
	}

}*/