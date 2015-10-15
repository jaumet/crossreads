import csv
import simplejson as json
import sys
import operator
import glob

#file = '6-Mallet-results/crossreads4_compostion-Readu-to-parse.csv'
file = open('diaries_final.json',"r")
diariesjson = json.loads(file.read())
file.close()

## List of silent (not used) topics. Mallet ids are given
path = "11-diaryID-jsons/"

## List of available diaries:
for d in glob.glob(path+'*'):
    print d
    f = open(d, "r")
    mydiary = json.loads(f.read())
    myscore = {}; myscore_sorted = {}
    p = 0
    print type(mydiary)
    for diary in mydiary["pages"]:
        p+=1
        for i in diary["topics"]:
            i[1] = float(i[1])
            if i[0] not in myscore:
                myscore[i[0]] = i[1]
            else:
                myscore[i[0]] += i[1]
    ## Normalize score to numpber of pahes
    print "number of pages: "+str(len(mydiary["pages"]))+" | pages cycles: "+str(p)
    ## Sort the diary scores by scores:
    myscore_sorted = sorted(myscore.items(), key=operator.itemgetter(1), reverse=True)
    print max(myscore.iteritems(), key=operator.itemgetter(1))
    chart_json = json.dumps(myscore_sorted)
    for _diary in  diariesjson:
        if int(_diary["nid"]) == int(d.split("/")[1][:-5]):
            print "********************************> "+str(diary["id"])
            ## Add the scores in this loop to [mydiaryID].json
            _diary["chart"] = myscore_sorted

#f = open("11-diaryID-jsons-charts/"+d.split("/")[1],"w")
#f.write(json.dumps(diary))

f = open("diaries_final.json","w")
f.write(json.dumps(diariesjson))

f.close()
print "######################"
