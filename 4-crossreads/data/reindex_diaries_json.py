import json
import simplejson
from pprint import pprint
import re
to_delete = [100350,100365,100367,100393,100394,100403,100407,100411,115162,115164,115175,115199,115202,115204,115212,115213,115243,115245,281689,308755,318442,318465,338054,365805]



new_diaries=[]
with open('diaries.json') as data_file:
    data = json.load(data_file)
print len(data)
for i,item in enumerate(data):
    item["id"]=i
    if item["nid"] in to_delete:
        data.remove(item)


print len(data)
#for i,item in enumerate(data):
#    print i,item["id"]
new = json.dumps(data)

f = open('diaries_final.json','w+')
f.write(new)
f.close()
