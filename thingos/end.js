function rainbowword(word2rainbow){

	var htmlstuff = '';
	for(var j=0;j<word2rainbow.length;j++)
	{
		color = '';
		for(var i=0;i<4;i++)
		{
			decnumber = Math.floor(Math.random()*8+8);
			hex = decnumber.toString(16);
			color = color +hex;
		}
		color = '00' + color;
		htmlstuff = htmlstuff + '<font size="'+Math.floor((Math.random())*0+7)+'", color="'+color+'">'+word2rainbow[j]+'</font>'
	}
	document.write(htmlstuff);
}
rainbowword("penis");