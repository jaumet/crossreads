import csv


file1 = 'dataPages.js'
file2 = 'dataTopics.js'
#file3 = 'data.js'

f1 = open(file1)

f2 = open(file2)


with open(file1) as f1:
  list1 = f1.readlines()
with open(file2) as f2:
  list2 = f2.readlines()

print len(list1)
print len(list2)
print len(list1[17].split(","))
print len(list2[18].split(","))

if len(list1) != len(list2):
  print "WRANING!!!!"
  print "\tNo diaries in dataPages "+file1+"\t"+str(len(list1))
  print "\tNo diaries in dataTopics "+file2+"\t"+str(len(list2))
#else:
print "\tID\tPages\tTopics"
for c in range(1, len(list1)):
  print "\t"+str(c)+"\t"+str(len(list1[c].split(",")))+"\t"+str(len(list2[c].split(",")))
  if len(list1[c].split(",")) != len(list2[c].split(",")):
    print "WARNING!!!!" 
  #print "\t"+str(c)+"\t"+str(list1.split(",")[c])+"\t"+str(list2.split(",")[c])

