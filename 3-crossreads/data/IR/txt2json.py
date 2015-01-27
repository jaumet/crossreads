import re

'''
var DATA = [
{"paperid": "509", "subject": "XXXX"},

<strong>abstracting</strong>
<a href="3-4/paper47.html">Human creation of abstracts with selected computer assistance tools</a>
'''

f = open("by_subject.txt",'r')
myjson = '['
paperid = ''; subject = ''; count = 0;
for line in f:
	#if len(line) > 4:
	if re.match(r'\<strong\>', line):
		# replacements
		subjects = re.sub(r'\<strong\>(.*)?\<\/strong\>.*?\n', r'\1', line)
		##subjects = re.sub(r'\<\/a><a\ .*\>$', '', line)
	elif re.match(r'\<a href\=\"', line):
		paperid = re.sub(r'\<a href\=\"\d+\-\d+\/paper(\d+)?\.html.*?\n', r'\1', line)
	if not re.match(r'\D', paperid) and paperid != '' and not re.match(r'\<a\ href', subject):
		#print "@@@@@@@@@@@@@@@"+line
		#print "paperid: "+paperid
		#print "subject: "+subjects	
		count = count + 1
		myjson += '{"paperid": "'+paperid+'", "subject": "'+subjects+'"},\n'
		paperid = ''
	#else:
		#print "!!!!!!!!!!!!!!!!  "+line
		#print "paperid: "+paperid
		#print "subject: "+subjects
myjson = myjson[:-2]
myjson += ']'
print myjson

