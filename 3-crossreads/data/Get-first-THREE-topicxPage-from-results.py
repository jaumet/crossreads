import csv, json
from pprint import pprint
import heapq

#topics = ['Analysis & family', 'Cities & landscapes', 'Travelling', 'War', 'Militar life']
################################################################################
topicGroups=["Personal", "War", "Military life", "Traveling", "The accidental tourist"]

with open('topics.json') as json_file:    
    topics = json.load(json_file)

#pprint(data)
#print 
#print topics[46]["topic"]

f = open('50topics/crossreads_compostion-WITH-EMPTY-PAGES.csv')
###f = open('xxx.csv')
my = csv.reader(f)
tnul = 0;t0 = 0;t1=0;t2=0;t3=0;t4=0;co=0
out='var topicMatrix = [\n'
# Transform 20 topics to 5
c = [[],[],[],[],[]]
numDiaries = 0
current = ''
cero = 0
tmp = []
lines = 0
for row20x in my:
  co += 1; 
  # in mycsv topics go from column 2 to 22 
  # out put is 5 columns: (1,25,14,30,29,19,3,37),(4,7,46,44,13,2,23),(28,20,33,6,11),(47,9,49,45,34  ),(22,35,41,0)
  i = 2
  tmp = row20x[2:]
  dd = 0
  for t in tmp:
    tmp[dd]= float(t)
    dd+=1

  m = max(tmp)
  #print m
  #print tmp.index(m)
  code = "0-0"
  #print ">>>>>>>>>> "+str(co)
  notUsedTopics = [17,42,27,26,18,12,8,21,32,31,40,5,39,43,38,24,15,36,10,]
  
  
  r = 0;g="no"
  #print str(tmp.index(m))+" | "+str(tmp)
  while tmp.index(m) in notUsedTopics:
    #### Get the second or third topics if score is > 0.5
    r+=1
    m = heapq.nlargest(r+1, tmp)[r]
    g = "yes"

  if m>0.25 and g == "yes":
    cero+=1
    diary = row20x[1].replace('file:/home/jaume/apps/Mallet/diariesPages-noEmptyPages/','')
    for item in topics:
      if item["topicNo"] == int(tmp.index(m)):
        code = item["code"]
    print str(cero)+") num: "+str(51-r)+" | score: "+str("%.2f" % m)+" >"+diary+" | TM: "+str(code)
'''

  if tmp.index(m) in notUsedTopics or m == 0:
    code = "0-0"
    cero += 1
  else:
    # get the code and topic for that max score
    for item in topics:
      if item["topicNo"] == int(tmp.index(m)):
        code = item["code"]
        #print code
  codeList = code.split("-")

  #pageInfo = str(code)+"-"+str(m)
  pageInfo = str(codeList[0])+"-"+str(codeList[1])+"-"+str("%.2f" % m)

  #print ">>> "+str(tmp.index(m))+"\t"+"\tMYvar:"+str(code)+"-"+str(m)

  #print
  #print " TOTAL: "+str(co)
  #print "No topic: "+str(cero)

  diary = row20x[1].replace('file:/home/jaume/apps/Mallet/diariesPages-noEmptyPages/','').split('/')[0]
  if current == str(diary):
    out += '"'+str(pageInfo)+'",'
  else:
    numDiaries += 1
    #print "----------- New diary: "+
    #print str(diary)+"\t",  
    out = out[:-1]      
    current = str(diary)
    out += '], \n["'+str(pageInfo)+'", ' ##+current
    lines += 1
  #print len(row20x)
  
  # result:
  if int(codeList[0]) == 0:
    tnul += 1
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
out = out[:-1]
out += ']\n];'


print out
print "//lines "+str(lines)
#print "numDiaries: "+str(numDiaries)
#print "No of pages: "+str(co)
#print tnul, t0, t1, t2, t3 , t4
# write it out as pagesTopic.json
#print "Diaries to delete completely: they are mainly printed books, and they are not transcribed: 100300,  100299 (id=17). 115137 (id=127)"
'''
