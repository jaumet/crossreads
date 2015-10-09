import csv
import sys
import operator

#file = '6-Mallet-results/crossreads4_compostion.csv'
file = '6-Mallet-results/test.csv'
mycsv = csv.reader(open(file),delimiter=',')
print

## List of silent (not used) topics. Mallet ids are given
silentTopics = [0, 2, 4, 10, 11, 13, 16, 21, 22, 28, 29, 30, 31, 32, 41, 43, 44, 47, 48, 51, 52, 54, 55, 56, 64, 67, 73, 76, 81, 82, 86, 88, 91, 92, 98, 99]

# Get every page path/filename
c = 1
myDiary = dict()
###Slide per diaty:

myList = dict()
for line in mycsv:
    scores = line[2:]
    for s in scores:
        myList[scores.index(s)] = s
    print myList
    m = max(scores)
    print "========"

    ## iterate through myList dict and delete elements where index in silentTopics
    for k, v in myList.items():
        #print v
        if k in silentTopics:
            del myList[k]
    #print sorted(myList, key=lambda score: score[0], reverse=True)
    print  sorted(myList.items(), key=operator.itemgetter(1), reverse=True)
    print "XXXXXXXXXXXXXXXXXXXXXXXXX"


#    if scores.index(m)   in silentTopics:
#        print myList[m]
#        print "##########"

#    mytuple = enumerate(scores)
#    scoresSorted = sorted(mytuple, key=lambda score: score[1], reverse=True)
#    print scoresSorted
#    print len(scoresSorted)
