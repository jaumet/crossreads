import csv
import sys
import operator

# Get arguments
arrArg = []
for arg in sys.argv:
     arrArg.append(arg)
     print arg
     
# Open csv file and sorted it
def sortFilterPrint(id, num, order):
    mycsv = '6-Mallet-results/topics50/crossreads_compostion.txt'
    #mycsv = '6-Mallet-results/TM-test.csv'
    mycsv = csv.reader(open(mycsv),delimiter='\t')
    sortedlist = sorted(mycsv, key=operator.itemgetter(int(id)+2), reverse=int(order)) 

    # Get every page path/filename
    for item in sortedlist[:int(num)]:
        #print item
        print item[1]
        new = item[1].replace('file:/home/jnualart/apps/Mallet/crossreads4', '3')
        page = open(new, 'r')
        print page.read()
        print "......................................"

sortFilterPrint(arrArg[1], arrArg[2], arrArg[3  ])




