import urllib2
import json
from pprint import pprint


# 1 open data-diaries-list.json
with open('data-diaries-list.json') as data_file:    
    data = json.load(data_file)
# 2 iterate through diaries, and get entity_node and the list of pages for each diary. Write each one in 2-getPagesList-forEachDiary/[nid].json

for item in data:
    nid = str(item['nid'])
    url = 'http://transcripts.sl.nsw.gov.au/api/entity_node/'+nid+'/?fields=nid,title,record_number,percentage_unlocked,transcript_pages'
    print url
    response = urllib2.urlopen(url)
    myjson = response.read()
    #915317
    #http://transcripts.sl.nsw.gov.au/api/entity_node/915317/?fields=nid,title,record_number,percentage_unlocked,transcript_pages
    file = open('2-getPagesList-forEachDiary/'+nid+'.json', "w")
    file.write("["+myjson+"]")
    file.close()


