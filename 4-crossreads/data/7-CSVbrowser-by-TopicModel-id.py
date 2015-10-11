import csv
import sys
import operator

# Open csv file and sorted it
def sortFilterPrint(id, num, order, output):
    file = '6-Mallet-results/crossreads4_compostion.txt'
    #file = '6-Mallet-results/test.csv'
    mycsv = csv.reader(open(file),delimiter=',')
    setOrder = {"desc":1,"asc":0}
    sortedlist = sorted(mycsv, key=lambda row: float(row[int(id)+2]), reverse=setOrder[order])
    print

    # Get every page path/filename
    c = 1;json_main = '\n[\n\t{\n\t'+output+'-'+id+': ['
    for item in sortedlist[:int(num)]:
        new = item[1].replace('file:/home/jaume/apps/Mallet/TranscriptionsCLEAN/', '3-Transcriptions/')
        if output == "detail":
            print "#"+str(c)
            print " -> "+new+"\t"+item[0]+"\t"+item[int(id)+2]
            page = open(new, 'r')
            print page.read()
            print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
            c += 1
        elif output == "top":
            json_main += new.replace('3-Transcriptions/', '')[:-4]+"\", "
    print "["+json_main[:-2]+"]\n\t}\n]\n]"
# Get arguments
arrArg = []
if len(sys.argv) != 5:
    print
    print "\tUsage: python 7-TopicMode-CSVbrowser.py [TM id] [Num pages] [desc/asc] [detail/top]"
    print
    print "\tThis script needs four parameters:"
    print "\t* [TM id]: id of the topic model acording to csv files in './6-Mallet-results'"
    print "\t* [Num pages]: Number of pages you want to see"
    print "\t* [desc/asc]: sort descending or ascending. [Defaul] is desc."
    print "\t* [detail/top]:"
    print "\t\t 'detail' shows the text"
    print "\t\t 'top' shows [diaryID]/[pageID] for this TM id"
    print
    print "(note: this script is for internal use. It does not check arguments, and it throws out standard python errors)"
else:
    for arg in sys.argv:
         arrArg.append(arg)
    if len(arrArg) == 3:
        arrArg.append("desc") # default value
        arrArg.append("detail")
    sortFilterPrint(arrArg[1], arrArg[2], arrArg[3], arrArg[4])
