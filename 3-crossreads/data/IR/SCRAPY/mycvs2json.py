import csv
import random

ifile  = open('icml13-clean.csv', "rb")
reader = csv.reader(ifile)

def r():
	return(random.randrange(0,100,10))

rr = random.randrange

path = "http://www.jmlr.org/papers/volume14/"
myjson = "var DATA = [\n\t{\n\t\t"
mynewline = "\n\t\t"
myEOF = "\n\t}\n]"
rownum = 0
mytmp = ""
mytmp2 = ""
c = 0
for row in reader:
	# Save header row.
	if rownum == 0:
		header = row
	else:
		myendnext = '"topic1": %s,\n\t\t"topic2": %s,\n\t\t"topic3": %s,\n\t\t"topic4": %s,\n\t\t"topic5": %s,\n\t\t"axis1": "a%s",\n\t\t"axis2": "b%s",\n\t\t"axis3": "c%s",\n\t\t"axis4": "d%s",\n\t\t"axis5": "e%s"\n\t},\n\t{\n\t\t' % (r(), r(), r(), r(), r(), rr(1,3), rr(1,4), rr(1,3), rr(1,4), rr(1,6))
		colnum = 0
		myjson += "'id':"+str(c)+","+mynewline 
		for col in row:
			#print '%s: %s' % (header[colnum], col)
			if header[colnum] == "Title":
				myjson += "\"title\": \""+col+"\","+mynewline
			elif header[colnum] == "Author":
				mytmp2 = "\"author\": "+"\""+col+"\","+mynewline
			elif header[colnum] == "Identifier":
				mytmp = "\"url\": "+"\""+path+"/"+col+"/"+col+".pdf\","+mynewline
			colnum += 1
		myjson += mytmp2+mytmp+myendnext
	rownum += 1
	c += 1

print myjson+myEOF
ifile.close()

# Just edit the file manually and add the last closing JSON (!)

