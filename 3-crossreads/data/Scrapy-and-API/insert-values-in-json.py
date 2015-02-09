import json
import simplejson
from pprint import pprint
import re

#load list of subjects:
with open('by_subject-FINAL.json') as subjects_file:    
    subjects = json.load(subjects_file)

#pprint(subjects[0])

#print "@@@@@@@@@@@@@@@"

with open('data.json') as data_file:    
    data = json.load(data_file)
for item in data:
	tmp = []
	for subject in subjects:
		if subject["paperid"] == item["paperid"]:
			tmp.append(subject["subject"])
			#print item["paperid"], subject["paperid"], tmp
	item["subject"]= tmp
	#if len(item["subject"]) <1:
	#print item["paperid"], item["subject"]
	#pprint(unicode(item)),

print(data),

#f = open('mydata.json','w+')
#simplejson.dump(data, f)
#f.close()
