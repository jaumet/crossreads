import os, re

def listEmptyFilesrecursively(remove):
  path = './diariesPages-READY/'
  diaries = os.listdir(path)
  diaries.sort()
  emptyDiaries = [];p = 0
  #print "["
  counter = 11587
  for diary in diaries:
    pages = os.listdir(path+diary)
    for page in pages:
      #print path+diary+"/"+page
      size = os.path.getsize(path+diary+"/"+page)
      ########
      #### For empty pages:
      ## if size == 0:
      #### For Pages size = 17:
      if size == 17:
        p +=1
        if diary not in emptyDiaries:
          emptyDiaries.append(diary)
        #print "\""+path+diary+"/"+page+"\",", #+"\t"+str(size)

        counter += 1
        mypath = 'file:/home/jaume/apps/Mallet/diariesPages-noEmptyPages/'
        mypage = diary+"/"+page+".txt"
        myceros = str('0,'*50)[:-1]
        print str(counter)+","+mypath+mypage+","+myceros
#11586 file:/home/jaume/apps/Mallet/diariesPages-noEmptyPages/100376/102740.txt  0.0006456055  0.0024585362  0.0013453475  0.0002059472  0.0027865736  0.2203400464  0.000496083 0.0015031199  0.0011651873  0.0012457385  0.0001442713  0.0005212216  0.0015398681  0.0166908655  0.0013675327  0.0002034517  0.1896686369  0.2107431754  0.0020414579  0.0002415158  0.111763046 0.001098842 0.0797269935  0.0006652298  0.0002407634  0.0012642909  0.0021225831  0.0022031867  0.0019222825  0.0479433888  0.0008788717  0.0164967875  0.0322658993  0.0005471778  0.0003888614  0.0008247721  0.0001878028  4.38651958482058E-005 0.0002636883  0.0005635466  0.0006642886  0.0006825228  0.0202531785  0.0003465737  0.0011421407  0.0006231193  0.0171623467  0.0013967998  0.0001556913  0.0008072772

        if remove == "removeEmptyPages":
	  #################### remove?!
          os.remove(path+diary+"/"+page) 
    #print  "------------------"
  #print "]"
  #print   
  #print "Total:"
  #print "\tpages:\t\t"+str(p)
  #print "\tdiaries:\t"+str(len(emptyDiaries))
  #print emptyDiaries

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
