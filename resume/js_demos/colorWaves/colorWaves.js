function ColorWave (context, width, height) {
	this.context = context;
	this.width = width;
	this.height = height;
	this.frequency = 0.0;
	this.phaseShift = 0.0;
	this.panelCount = 32;
	this.panelWidth = this.width/this.panelCount;
	this.panelColors = [];
	

}
ColorWave.prototype.recalcColors = function () {
	var redFreq = 0.1 + this.frequency, 
		greenFreq = 0.2 + this.frequency,
		blueFreq = 0.3 + this.frequency;

	for (var i =0; i < this.panelCount; i++) {
		red   = Math.sin(redFreq*i + 0) * 127 + 128;
   		green = Math.sin(greenFreq*i + 2) * 127 + 128;
   		blue  = Math.sin(blueFreq*i + 4) * 127 + 128;

   		this.panelColors[i] = utils.RGB2Color(red, green, blue);
	}
}
ColorWave.prototype.draw = function () {
	//this.context.save();
	this.recalcColors();

	for (var i = 0; i < this.panelCount; i++) {
		this.context.fillStyle = this.panelColors[i];
		this.context.fillRect(this.panelWidth*i, 0, this.panelWidth*i + this.panelWidth, this.height);
		
	}
	//this.context.restore();


}