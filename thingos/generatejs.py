try:
	random_color_PATH = 'randomcolor.js'
	end_js_PATH = 'end.js'
	end_html_PATH = 'end.html'
	js_for = 'for(var i=0;i<50;i++)\n{'
	with open(random_color_PATH, 'r') as f:
		randomcolor_func = f.read()
	js_program = randomcolor_func
	alltext = []
	text = input('Enter the text you would like to rainbow-ify\n')
	while text!='':
		alltext.append(text)
		text = input()
	for text in alltext:
		js_program += "\nrainbowword(\"{}\");".format(text)
	with open(end_js_PATH, 'w')  as f:
		f.write(js_program)
	htmldoc = '<script type=\"text/javascript\">\n{}\n</script>'.format(js_program)
	with open(end_html_PATH, 'w')  as f:
		f.write(htmldoc)


except Exception as e:
	print(type(e), e)
	input()