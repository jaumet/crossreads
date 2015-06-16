import csv, json
from pprint import pprint
import heapq

topicGroups=["Personal", "War", "Military life", "Traveling", "The accidental tourist"]

with open('topics.json') as json_file:    
  topics = json.load(json_file)

def getTopics(topics, my):
  # get the code and topic for that max score
  for item in topics:
    if item["topicNo"] == int(my):
      code = item["code"]
      #print "lala"+str(code)
  return code

f = open('50topics/crossreads_compostion-WITH-EMPTY-PAGES-ONLY-Named-Topics.csv')
###f = open('xxx.csv')
mycsv = csv.reader(f)
t0 = 0;t1=0;t2=0;t3=0;t4=0;co=0
out='var topicMatrix = [\n'
numDiaries = 0
current = ''
tmp = []
lines = 0
for row20x in mycsv:
  i = 2
  tmp = row20x[2:]
  dd = 0
  for t in tmp:
    tmp[dd]= float(t)
    dd+=1
  #topicsOrdered = sorted(enumerate(tmp), key=lambda x: x[1])
  topicsOrdered = heapq.nlargest(len(tmp), enumerate(tmp), key=lambda x: x[1])

  pageInfo = "["
  myline = ""
  for t in topicsOrdered:
    code = getTopics(topics, t[0])
    pageInfo += '"'+str(code)+"-"+str("%.2f" % t[1])+'",'
  pageInfo = pageInfo[:-1]
  pageInfo += ']'
  
  diary = row20x[1].replace('file:/home/jaume/apps/Mallet/diariesPages-noEmptyPages/','').split('/')[0]
  if current == str(diary):
    out += str(pageInfo)+','
  else:
    numDiaries += 1
    out = out[:-1]      
    current = str(diary)
    out += '], \n['+str(pageInfo)+', ' ##+current
    lines += 1

'''  
  # result:
  if int(codeList[0]) == 1:
    t0 += 1
  if int(codeList[0]) == 2:
    t1 += 1
  if int(codeList[0]) == 3:
    t2 += 1
  if int(codeList[0]) == 4:
    t3 += 1
  if int(codeList[0]) == 5:
    t4 += 1
'''

out = out[:-1]
out += ']\n];'


print out
#print "//lines "+str(lines)
#print "numDiaries: "+str(numDiaries)
#print "No of pages: "+str(co)
#print t0, t1, t2, t3 , t4
# write it out as pagesTopic.json
#print "Diaries to delete completely: they are mainly printed books, and they are not transcribed: 100300,  100299 (id=17). 115137 (id=127)"




