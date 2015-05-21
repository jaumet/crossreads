import json
import simplejson
from pprint import pprint
import re, random
		
with open('dataDiaries-don.json') as data_file:    
	diaries = json.load(data_file)
	#print data[128]
out = "["
for diary in diaries:
  print "\npages: "+str(diary["page_no"])
  out += "["
  for n in range(1, diary["page_no"]):
    #print str(n),
    out += str(random.randint(1, 5))+","
  out += "]"
out += "]"
f = open('dummyTopics-real-size.json','w+')
f.write(out)
#simplejson.dump(, f)
f.close()

