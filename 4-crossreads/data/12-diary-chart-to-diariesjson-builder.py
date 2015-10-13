import csv
import simplejson as json
import sys
import operator
import glob

#file = '6-Mallet-results/crossreads4_compostion-Readu-to-parse.csv'
#file = '6-Mallet-results/test.csv'
#mycsv = csv.reader(open(file),delimiter=',')
#path = '3-Transcriptions/'

print

## List of silent (not used) topics. Mallet ids are given
#silentTopics = [0, 2, 4, 10, 11, 13, 16, 21, 22, 28, 29, 30, 31, 32, 41, 43, 44, 47, 48, 51, 52, 54, 55, 56, 64, 67, 73, 76, 81, 82, 86, 88, 91, 92, 98, 99]
json_base ='[{"diary_chart": [{"mallet_id": "","score": []}]}]'
path = "11-diaryID-jsons/"

## List of available diaries:
for d in glob.glob(path+'*'):
    print d
    f = open(d, "r")
    mydiary = json.loads(f.read())
    myscore = {}; myscore_sorted = {}
    p = 0
    for diary in mydiary:
        print type(diary)
        for page in diary["pages"]:
            p+=1
            for i in page["topics"]:
                #print i[0], i[1]
                #print type(i[0]), type(float(i[1]))
                #i[0] = str(i[0])
                i[1] = float(i[1])
                if i[0] not in myscore:
                    myscore[i[0]] = i[1]
                else:
                    #print myscore
                    myscore[i[0]] += i[1]
    ## Normalize score to numpber of pahes
    print "number of pages: "+str(len(diary["pages"]))+" | pages cycles: "+str(p)
    ## Sort the diary scores by scores:
    myscore_sorted = sorted(myscore.items(), key=operator.itemgetter(1), reverse=True)
    print max(myscore.iteritems(), key=operator.itemgetter(1))
    chart_json = json.dumps(myscore_sorted)
    #print chart_json
    ## Add the scores in this loop to [mydiaryID].json
    diary["chart"] = myscore_sorted
    #print diary
    f = open("11-diaryID-jsons-charts/"+d.split("/")[1],"w")
    f.write(json.dumps(diary))
    f.close()
    print "######################"



'''
countedDiaries = [];
c =0;cc=0
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
        if line[1].split("/")[0] == diary:
            scores = line[2:]
            for s in scores:
                myTopics[scores.index(s)] = s
            ## filter myTopics dict by silentTopics
            for k, v in myTopics.items():
                if k in silentTopics:
                    del myTopics[k]
            # Sort tpoics by scoresand add them to myjson
            sortedScores =  sorted(myTopics.items(), key=lambda x: float(x[1]), reverse=True)
            # Add new page. Set id and define topics
            myjson[0]["pages"].append({"id": line[1].split("/")[1].replace(".txt", ""),"topics": []})
            myjson[0]["pages"][-1]["topics"].extend(sortedScores[:10])
            if diary not in countedDiaries:
                countedDiaries.append(diary)
            l+=1 # number of lines for this diary
    if len(myjson[0]["pages"][-1]["topics"])>0:
        print "      Myjson: "+str(len(myjson[0]["pages"][-1]["topics"]))
        # Set nunmber of pages for this diary:
        myjson[0]["page_no"] = l
        f = open("11-diaryID-jsons/"+diary+".json","w")
        f.write(json.dumps(myjson))

print "countedDiaries = "+str(len(countedDiaries))
print "lines l= "+str(l)
print "diariesList cycles c= "+str(c)
print "mycsv cycles c= "+str(cc)
'''
