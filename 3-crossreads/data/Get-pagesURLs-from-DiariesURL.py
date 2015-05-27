import urllib2
import simplejson
import os


diariesUrls = ["http://transcripts.sl.nsw.gov.au/api/node/100275.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100276.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100277.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100278.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100279.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100280.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100282.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100283.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100285.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100287.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100288.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100289.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100290.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100291.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100292.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100295.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100299.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100300.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100301.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100302.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100303.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100304.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100306.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100307.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100308.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100309.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100310.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100311.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100312.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100313.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100314.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100315.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100316.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100317.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100318.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100319.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100320.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100321.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100322.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100323.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100324.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100325.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100326.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100327.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100328.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100329.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100330.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100331.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100332.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100334.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100335.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100336.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100337.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100338.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100339.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100340.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100341.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100342.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100343.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100344.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100345.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100346.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100347.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100348.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100349.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100350.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100351.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100352.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100353.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100354.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100355.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100356.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100357.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100358.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100359.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100360.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100361.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100362.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100363.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100364.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100365.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100366.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100367.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100368.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100369.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100370.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100371.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100372.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100373.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100374.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100375.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100376.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100377.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100378.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100379.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100380.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100381.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100382.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100383.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100384.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100385.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100386.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100387.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100388.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100389.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100390.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100391.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100392.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100393.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100394.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100395.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100396.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100397.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100398.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100399.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100400.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100401.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100402.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100403.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100404.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100405.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100406.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100407.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100408.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100409.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100410.json", 
"http://transcripts.sl.nsw.gov.au/api/node/100411.json", 
"http://transcripts.sl.nsw.gov.au/api/node/115137.json", 
"http://transcripts.sl.nsw.gov.au/api/node/182325.json"]

diariesUrlsXX = ["http://transcripts.sl.nsw.gov.au/api/node/182325.json"]

def getDiaries():
  ''' 
    For each Diary:save diaryID.json file in .Diaries/
  '''
  totalPages = 0; c = 0
  for diaryUrl in diariesUrls:
    #print diaryUrl
    response = urllib2.urlopen(diaryUrl)
    #print response.info()
    myjson = simplejson.load(response)
    pagesList = myjson["field_transcript_pages"]["und"]
    noPages = len(pagesList)
    print noPages
    totalPages += noPages
    c += 1
    
    file = open("Diaries/"+diaryUrl[42:-5]+".json", 'w+')
    file.write(str(myjson))
    file.close()
    print "page: Diaries/"+diaryUrl[42:-5]+".json"
  print "------------------"
  print "Total Diaries:"
  print c
  print "Total pages"
  print totalPages


#################
# Total DIaries
# 132
# Total pages
# 12584
#################


def getPages():
  '''
    For each page of the diary: get the json and save in ./Diaries/diaryID/pageID.json
  '''
  path = "Diaries/"
  urlBase = "http://transcripts.sl.nsw.gov.au/api/node/"
  errorsList = []
  c = 0
  for diaryUrl in diariesUrls:
    print diaryUrl
    response = urllib2.urlopen(diaryUrl)
    #print response.info()
    myjson = simplejson.load(response)
    pagesList = myjson["field_transcript_pages"]["und"]
    ## Create folder if it doesn't exist 
    directory = path+diaryUrl[42:-5]
    if not os.path.exists(directory):
      os.makedirs(directory)
    ## Get each page in json
    for page in pagesList:
      print page["nid"]
      mypage = urlBase+page["nid"]+".json"
      print "-->"+str(c)
      print directory+"/"+page["nid"]
      c+=1
      try:
        response = urllib2.urlopen(mypage)
        #print response.info()
	
	###################################
	#from json import dumps
        #myjson = dumps(response)
	r = response.read()
        #myjson = simplejson.loads(r)
	
	file = open(directory+"/"+page["nid"]+".json", 'w+')
        file.write(r)
        file.close()
      except urllib2.HTTPError, e:
        print 'We failed with error code - %s.' % e.code
        print mypage
        print "$$$$$$$$$$$$"
        errorsList.append("diary:"+diaryUrl[42:-5]+": page "+mypage)
  print "END -----------------"
  print "List of errors:"
  print errorsList
  
#getDiaries()
getPages()

