import csv
import sys
import operator

# Open csv file and sorted it
def sortFilterPrint(id, num, order):
    file = '6-Mallet-results/crossreads4_compostion.txt'
    #file = '6-Mallet-results/test.csv'
    mycsv = csv.reader(open(file),delimiter=',')
    print "###"
    print type(mycsv)
    setOrder = {"desc":1,"asc":0}
    sortedlist = sorted(mycsv, key=lambda row: float(row[int(id)+2]), reverse=setOrder[order]) 

    # Get every page path/filename
    for item in sortedlist[:int(num)]:
        new = item[1].replace('file:/home/jaume/apps/Mallet/TranscriptionsCLEAN/', '3-Transcriptions/')
        print new+"\t"+item[0]+"\t"+item[int(id)+2]
        page = open(new, 'r')
        print page.read()
        print "......................................"

# Get arguments
arrArg = []
if len(sys.argv) <= 1 or len(sys.argv) > 4:
    print
    print "\tUsage: python 7-TopicMode-CSVbrowser.py [TM id] [Num pages] [desc/asc]"
    print "\tThis script needs three parameters:"
    print "\t* [TM id]: id of the topic model acording to csv files in './6-Mallet-results'"
    print "\t* [Num pages]: Number of pages you want to see"
    print "\t* [desc/asc]: sort descending or ascending"
    print
else:
    for arg in sys.argv:
         arrArg.append(arg)
         print arg,

    sortFilterPrint(arrArg[1], arrArg[2], arrArg[3])




