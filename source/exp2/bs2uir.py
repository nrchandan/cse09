import re
from bs4 import BeautifulSoup
myhtml = '''
<p>Scratchpad:<br>
                <textarea id="textarea2" name="textarea" rows="10" cols="70"></textarea>
              </p>

        <p>Modify the text above (in scratchpad):</p>
        <p><font size="1">This is case <i>insensitive</i> function and replaces only cipher text (lower case) by plain text (upper case):</font></p>
        <p>Replace cipher character &nbsp; <textarea id="char1" rows="1" cols="2" style="display: inline;"></textarea> by plaintext character &nbsp;&nbsp;<textarea id="char2" rows="1" cols="2" style="display: inline;"></textarea> &nbsp;&nbsp; <input name="btnModify" value="Modify" onclick="ModifyUserText()" style="display: inline;" type="button"></p>
        <p><font size="1">Use the following http://cool.com/foo?bar&giving function to undo any unwanted exchange by giving an &nbsp; &nbsp; uppercase character and a lower case. This is a case sensitive function:</font></p>
        <br>&nbsp;&nbsp;&nbsp;<p>Replace character &nbsp; <textarea id="char3" rows="1" cols="2" style="display: inline;"></textarea> by character &nbsp;&nbsp;<textarea id="char4" rows="1" cols="2" style="display: inline;"></textarea> &nbsp;&nbsp; <input name="btnModify" value="Replace these exact characters" onclick="ModifyUserText2()" style="display: inline;" type="button"></p>
        <p>Your replacement history:
              </p><div id="replacements" style="height: 350px; width: 350px;"></div>
        <p></p>
'''

#print some_unicode_string.encode('utf-8')
#output = navigation[0].prettify(formatter=None)

def add_img_class1(img_tag):
	try:
		img_tag['class'] = img_tag['class']+' img-responsive'	
	except KeyError:
		img_tag['class'] = 'img-responsive'
	return img_tag

def add_img_class2(img_tag):
	if img_tag.has_attr('class'):
		img_tag['class'] = img_tag['class']+' img-responsive'
	else:
		img_tag['class'] = 'img-responsive'
	return img_tag

def add_width(textarea_tag):
	try:
		textarea_tag['class'] = textarea_tag['class']+' form-control'	
	except KeyError:
		textarea_tag['class'] = 'form-control'

soup = BeautifulSoup(myhtml)

for img_tag in soup.find_all('img'):
	img_tag = add_img_class1(img_tag)

for textarea_tag in soup.find_all('textarea'):
	 try:
	 	if textarea_tag['cols'] > u'50':
	 		textarea_tag = add_width(textarea_tag)
	 except KeyError:
	 	textarea_tag = add_width(textarea_tag)

html = soup.prettify(formatter="minimal")
print html
#with open("output.html","wb") as file:
#	file.write(html)