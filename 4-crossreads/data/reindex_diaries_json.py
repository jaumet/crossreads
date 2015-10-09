import json
import simplejson
from pprint import pprint
import re
#to_delete = [100350,100365,100367,100393,100394,100403,100407,100411,115162,115164,115175,115199,115202,115204,115212,115213,115243,115245,281689,308755,318442,318465,338054,365805]

#to_delete2 = [100365,100394,100407,115164,115213,115245]

'''3 remaping date fields'''
new_diaries=[]
with open('diaries.json') as data_file:
    data = json.load(data_file)
print len(data)
s_start = []
d_end = []
for i,item in enumerate(data):
    d_start = item["date_start"].split(" ")
    if len(d_start) == 1:
        start_y = d_start[0];start_m = '' ; start_d = ''
    elif len(d_start) == 2:
        start_y = d_start[1]; start_m = d_start[0]; start_d = ''
    elif len(d_start) == 3:
        start_y = d_start[2]; start_m = d_start[1]; start_d = d_start[0]
    item["start_date"] = [{"start_year": start_y,"start_month": start_m,"start_day": start_d}]

    d_end = item["date_end"].split(" ")
    if len(d_end) == 1:
        end_y = d_end[0];end_m = '' ; end_d = ''
    elif len(d_end) == 2:
        end_y = d_end[1]; end_m = d_end[0]; end_d = ''
    elif len(d_end) == 3:
        end_y = d_end[2]; end_m = d_end[1]; end_d = d_end[0]
    item["end_date"] = [{"end_year": end_y,"end_month": end_m,"end_day": end_d}]

    del item["date_start"]
    del item["date_end"]

''''2 checking anormalities in dates:
for i,item in enumerate(data):
    if len(item["date_start"].split()) == 0:
        print " No date_start! for id="+str(item["id"])
    elif len(item["date_start"].split()) == 1:
        if len(item["date_end"].split()) == 0:
            item["date_end"] = item["date_start"]
        elif len(item["date_end"].split()) < 0:
            print "Anormality 1! "+str(item["id"])
    elif len(item["date_start"].split()) == 2:
        if len(item["date_end"].split()) == 0:
            pass#print "Anormality 2! "+str(item["id"])
    elif len(item["date_start"].split()) == 3:
        if len(item["date_end"].split()) == 0:
            pass#print "Anormality 3! "+str(item["id"])

'''

'''1 reindexing id's
for i,item in enumerate(data):
    item["id"]=i
    if item["nid"] in to_delete2:
        data.remove(item)
'''

print len(data)
#for i,item in enumerate(data):
#    print i,item["id"]
new = json.dumps(data)

f = open('diaries_final.json','w+')
f.write(new)
f.close()
