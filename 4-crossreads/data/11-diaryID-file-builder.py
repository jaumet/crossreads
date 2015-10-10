import csv, json
import sys
import operator
import glob

file = '6-Mallet-results/crossreads4_compostion-Readu-to-parse.csv'
#file = '6-Mallet-results/test.csv'
mycsv = csv.reader(open(file),delimiter=',')
path = '3-Transcriptions/'

print

## List of silent (not used) topics. Mallet ids are given
silentTopics = [0, 2, 4, 10, 11, 13, 16, 21, 22, 28, 29, 30, 31, 32, 41, 43, 44, 47, 48, 51, 52, 54, 55, 56, 64, 67, 73, 76, 81, 82, 86, 88, 91, 92, 98, 99]
json_base ='[{"page_no": 0,"pages": [{"id": "","topics": []}]}]'

## List of available diaries:
diariesList = []
for d in glob.glob(path+'*'):
    diariesList.append(d.replace(path, ''))
#print diariesList

# Get every page path/filename
countedDiaries = [];
c =0;cc=0
###Slide per diaty:
for diary in diariesList:
    myjson = json.loads(json_base)
    myDiary = dict()
    myTopics = dict()
    l=0
    c+=1
    mycsv = csv.reader(open(file),delimiter=',')
    print "----> "+diary
    for line in mycsv:
        cc+=1
        #print line
        #print type(line[1].split("/")[0]), type(diary)
        if line[1].split("/")[0] == diary:
            scores = line[2:]
            for s in scores:
                myTopics[scores.index(s)] = s
            #print "---> "+diary
            #print "... line: "+str(line[1].split("/"))
            ## filter myTopics dict by silentTopics
            for k, v in myTopics.items():
                if k in silentTopics:
                    del myTopics[k]
            # Sort tpoics by scoresand add them to myjson
            sortedScores =  sorted(myTopics.items(), key=lambda x: float(x[1]), reverse=True)
            # add new page. Set id and define topics
            myjson[0]["pages"].append({"id": line[1].split("/")[1].replace(".txt", ""),"topics": []})
            myjson[0]["pages"][-1]["topics"].extend(sortedScores[:10])

            if diary not in countedDiaries:
                countedDiaries.append(diary)
            l+=1 # number of lines for this diary
    if len(myjson[0]["pages"][-1]["topics"])>0:
        print "      Myjson: "+str(len(myjson[0]["pages"][-1]["topics"]))
        # Set pages_no in myjson:
        myjson[0]["page_no"] = l
        # wrtie the file
        f = open("11-diaryID-jsons/"+diary+".json","w")
        f.write(json.dumps(myjson))



print "#############"
print "countedDiaries = "+str(len(countedDiaries))
print "lines l= "+str(l)
print "diariesList cycles c= "+str(c)
print "mycsv cycles c= "+str(cc)
'''

'''

#    if scores.index(m)   in silentTopics:
#        print myTopics[m]
#        print "##########"

#    mytuple = enumerate(scores)
#    scoresSorted = sorted(mytuple, key=lambda score: score[1], reverse=True)
#    print scoresSorted
#    print len(scoresSorted)
