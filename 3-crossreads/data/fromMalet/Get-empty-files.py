import os, re

def listEmptyFilesrecursively(remove):
  path = './diariesPages/'
  diaries = os.listdir(path)
  diaries.sort()
  emptyDiaries = [];p = 0
  print "["

  for diary in diaries:
    pages = os.listdir(path+diary)
    for page in pages:
      #print path+diary+"/"+page
      size = os.path.getsize(path+diary+"/"+page)
      if size == 0:
        p +=1
        if diary not in emptyDiaries:
          emptyDiaries.append(diary)
        print "\""+path+diary+"/"+page+"\",", #+"\t"+str(size)
        if remove == "removeEmptyPages":
          os.remove(path+diary+"/"+page) 
    #print  "------------------"
  print "]"
  print   
  print "Total:"
  print "\tpages:\t\t"+str(p)
  print "\tdiaries:\t"+str(len(emptyDiaries))
  print emptyDiaries

def getTranscriptions_PagesList():
  myTranscripts = ['36', '45', '52', '53', '54', '66', '75', '81', '83', '87', '88', '89', '98', '104', '109', '110', '113']
  myTranscriptsDiaryId = ['100320','100329','100337','100338','100339','100351','100360','100366','100368','100372','100373','100374','100383','100389','100394','100395','100398']

  print "num\tTarget\tPages:\tDiary"
  for num in myTranscripts:
    #print "########################   "+num
    c = 0
    path = './diariesPages/'
    f = open('./DIARIES-tO-RECOVER-FROM-TRANSCRIPTS/diary-'+num+'.txt', 'r')
    p = f.read()
    pages =  re.split("\[Page\ \d*\]", p)
    pages.pop(0)
    targets = os.listdir(path+myTranscriptsDiaryId[myTranscripts.index(num)])
    targets.sort()
    cc = 0
    c += 1
    #pages.pop(0)
    print num+"\t"+str(len(targets))+"\t"+str(len(pages))+"\t"+myTranscriptsDiaryId[myTranscripts.index(num)]
    for target in targets:
      #print str(c)+"\t"+str(cc)+"\t"+myTranscriptsDiaryId[myTranscripts.index(num)]+"/"+target 
      #print "page no: "+str(targets.index(target))
      t = open(path+myTranscriptsDiaryId[myTranscripts.index(num)]+"/"+target, "w")
      try:
###WRITE        t.write(pages[targets.index(target)])
        pass
      except:
        print "Pass: "+str(targets.index(target))

      t.close()
      #print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
      cc += 1

  #print my
  #print str(len(my))
  #print my[89]
#  with open(diaryUrl) as data:  

'''
run defs:
'''
listEmptyFilesrecursively("no")
#listEmptyFilesrecursively("removeEmptyPages")

#getTranscriptions_PagesList()