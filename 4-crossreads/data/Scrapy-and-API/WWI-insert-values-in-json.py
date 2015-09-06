import json
import simplejson
from pprint import pprint
import re

#load list of subjects:
with open('SCRAPY/InformationR/spiders/Diaries-DigitalOrderNumber.json') as don_file:    
	dons = json.load(don_file)
	#print dons[3]["pageUrl"]

		
with open('dataDiaries.json') as data_file:    
	data = json.load(data_file)
	#print data[4]["id"]

for item in data:
	tmp = []
	for don in dons:
		#print ">>"+str(don["pageUrl"]).strip()+"<< >>"+str(item["diary_id"]).strip()
		if str(don["pageUrl"]).strip() == str(item["diary_id"]).strip():
			print "---"
			print ">>"+str(don["pageUrl"]).strip()+"<< >>"+str(item["diary_id"]).strip()
			#tmp.append(don["pageImage"])
			item["don"] = don["pageImage"]
	#if len(item["subject"]) <1:
	#print item["paperid"], item["subject"]
	#pprint(unicode(item)),

#print(data),

f = open('dataDiaries-don.json','w+')
simplejson.dump(data, f)
f.close()

