import json
import simplejson
from pprint import pprint
import re, random, os

def gen_simple_topics():
  with open('dataDiaries.json') as data_file:    
	  diaries = json.load(data_file)
	  print diaries[125]["don"]
  new = ''; 
  out = "var DATA = [\n";
  c = 1
  for diary in diaries:
    #if int(diary["id"])>17:
    diary["id"] = c
    c += 1
    #print "id-> "+str(diary["id"]),
    out += '{\n\t"id": '+str(diary["id"])+', \n\t"diary_id": '+str(diary["diary_id"])+', \n\t"don": "'+diary["don"]+'",  \n\t"title": "'
    out += diary["title"]+'", \n\t"author": "'+diary["author"]+'", \n\t"topics": "'+diary["topics"]
    out += '", \n\t"cover": "'+diary["cover"]+'",'
    out += ' \n\t"start_date": [{"start_year": "'+diary["start_date"][0]["start_year"]+'", "start_month": "'+diary["start_date"][0]["start_month"]+'", "start_day": "'+diary["start_date"][0]["start_day"]+'"}],'
    out += ' \n\t"end_date": [{"end_year": "'+diary["end_date"][0]["end_year"]+'", "end_month": "'+diary["end_date"][0]["end_month"]+'", "end_day": "'+diary["end_date"][0]["end_day"]+'"}],'
    out += '\n\t"kind": "'+diary["kind"]+'",\n\t"location": "'+diary["location"]+'", \n\t"page_no": '+str(diary["page_no"])+'\n},\n';
        
    #.encode("ascii")
    #print
    #new += out
  new = out[:-2]+"];"
    
  f = open('XdataDiaries.js','w+')
  f.write(str(new))
  #simplejson.dump(, f)
  f.close()


gen_simple_topics()
