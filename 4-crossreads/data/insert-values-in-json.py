import json
import simplejson
from pprint import pprint
import re

#load list of subjects:
#with open('by_subject-FINAL.json') as subjects_file:
#    subjects = json.load(subjects_file)

#pprint(subjects[0])

#print "@@@@@@@@@@@@@@@"

with open('diaries.json') as data_file:
    data = json.load(data_file)
for i,item in enumerate(data):
	#print item
    #print i,
    print item["nid"],


#f = open('mydata.json','w+')
#simplejson.dump(data, f)
#f.close()
