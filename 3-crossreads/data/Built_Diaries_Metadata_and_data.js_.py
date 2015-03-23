import os, json, requests, urllib2, pprint

diariesUrls = ["Diaries-only-diary_jsons/100307.json",
"Diaries-only-diary_jsons/100325.json",
"Diaries-only-diary_jsons/100324.json",
"Diaries-only-diary_jsons/100312.json",
"Diaries-only-diary_jsons/100325.json",
"Diaries-only-diary_jsons/100309.json",
"Diaries-only-diary_jsons/100307.json",
"Diaries-only-diary_jsons/100324.json",
"Diaries-only-diary_jsons/100308.json",
"Diaries-only-diary_jsons/100318.json",
"Diaries-only-diary_jsons/100322.json",
"Diaries-only-diary_jsons/100311.json",
"Diaries-only-diary_jsons/100302.json",
"Diaries-only-diary_jsons/100306.json",
"Diaries-only-diary_jsons/100310.json",
"Diaries-only-diary_jsons/100313.json",
"Diaries-only-diary_jsons/100315.json",
"Diaries-only-diary_jsons/100319.json",
"Diaries-only-diary_jsons/100321.json",
"Diaries-only-diary_jsons/100316.json",
"Diaries-only-diary_jsons/100304.json",
"Diaries-only-diary_jsons/100327.json",
"Diaries-only-diary_jsons/100314.json",
"Diaries-only-diary_jsons/100317.json",
"Diaries-only-diary_jsons/100326.json",
"Diaries-only-diary_jsons/100323.json",
"Diaries-only-diary_jsons/100320.json",
"Diaries-only-diary_jsons/100303.json",
"Diaries-only-diary_jsons/100395.json",
"Diaries-only-diary_jsons/100396.json",
"Diaries-only-diary_jsons/100382.json",
"Diaries-only-diary_jsons/100371.json",
"Diaries-only-diary_jsons/100384.json",
"Diaries-only-diary_jsons/100383.json",
"Diaries-only-diary_jsons/100385.json",
"Diaries-only-diary_jsons/115137.json",
"Diaries-only-diary_jsons/100301.json",
"Diaries-only-diary_jsons/100275.json",
"Diaries-only-diary_jsons/100404.json",
"Diaries-only-diary_jsons/100280.json",
"Diaries-only-diary_jsons/100287.json",
"Diaries-only-diary_jsons/100285.json",
"Diaries-only-diary_jsons/100282.json",
"Diaries-only-diary_jsons/100276.json",
"Diaries-only-diary_jsons/100277.json",
"Diaries-only-diary_jsons/100411.json",
"Diaries-only-diary_jsons/100283.json",
"Diaries-only-diary_jsons/100278.json",
"Diaries-only-diary_jsons/100360.json",
"Diaries-only-diary_jsons/100361.json",
"Diaries-only-diary_jsons/100279.json",
"Diaries-only-diary_jsons/100359.json",
"Diaries-only-diary_jsons/182325.json",
"Diaries-only-diary_jsons/100331.json",
"Diaries-only-diary_jsons/100334.json",
"Diaries-only-diary_jsons/100330.json",
"Diaries-only-diary_jsons/100367.json",
"Diaries-only-diary_jsons/100332.json",
"Diaries-only-diary_jsons/100335.json",
"Diaries-only-diary_jsons/100388.json",
"Diaries-only-diary_jsons/100292.json",
"Diaries-only-diary_jsons/100397.json",
"Diaries-only-diary_jsons/100290.json",
"Diaries-only-diary_jsons/100366.json",
"Diaries-only-diary_jsons/100365.json",
"Diaries-only-diary_jsons/100362.json",
"Diaries-only-diary_jsons/100291.json",
"Diaries-only-diary_jsons/100350.json",
"Diaries-only-diary_jsons/100344.json",
"Diaries-only-diary_jsons/100358.json",
"Diaries-only-diary_jsons/100343.json",
"Diaries-only-diary_jsons/100342.json",
"Diaries-only-diary_jsons/100341.json",
"Diaries-only-diary_jsons/100295.json",
"Diaries-only-diary_jsons/100364.json",
"Diaries-only-diary_jsons/100363.json",
"Diaries-only-diary_jsons/100372.json",
"Diaries-only-diary_jsons/100377.json",
"Diaries-only-diary_jsons/100380.json",
"Diaries-only-diary_jsons/100378.json",
"Diaries-only-diary_jsons/100405.json",
"Diaries-only-diary_jsons/100379.json",
"Diaries-only-diary_jsons/100288.json",
"Diaries-only-diary_jsons/100389.json",
"Diaries-only-diary_jsons/100337.json",
"Diaries-only-diary_jsons/100338.json",
"Diaries-only-diary_jsons/100390.json",
"Diaries-only-diary_jsons/100375.json",
"Diaries-only-diary_jsons/100398.json",
"Diaries-only-diary_jsons/100289.json",
"Diaries-only-diary_jsons/100381.json",
"Diaries-only-diary_jsons/100374.json",
"Diaries-only-diary_jsons/100376.json",
"Diaries-only-diary_jsons/100368.json",
"Diaries-only-diary_jsons/100336.json",
"Diaries-only-diary_jsons/100373.json",
"Diaries-only-diary_jsons/100387.json",
"Diaries-only-diary_jsons/100351.json",
"Diaries-only-diary_jsons/100401.json",
"Diaries-only-diary_jsons/100402.json",
"Diaries-only-diary_jsons/100403.json",
"Diaries-only-diary_jsons/100399.json",
"Diaries-only-diary_jsons/100386.json",
"Diaries-only-diary_jsons/100400.json",
"Diaries-only-diary_jsons/100370.json",
"Diaries-only-diary_jsons/100356.json",
"Diaries-only-diary_jsons/100369.json",
"Diaries-only-diary_jsons/100328.json",
"Diaries-only-diary_jsons/100394.json",
"Diaries-only-diary_jsons/100357.json",
"Diaries-only-diary_jsons/100391.json",
"Diaries-only-diary_jsons/100339.json",
"Diaries-only-diary_jsons/100392.json",
"Diaries-only-diary_jsons/100329.json",
"Diaries-only-diary_jsons/100352.json",
"Diaries-only-diary_jsons/100353.json",
"Diaries-only-diary_jsons/100355.json",
"Diaries-only-diary_jsons/100408.json",
"Diaries-only-diary_jsons/100354.json",
"Diaries-only-diary_jsons/100409.json",
"Diaries-only-diary_jsons/100407.json",
"Diaries-only-diary_jsons/100393.json",
"Diaries-only-diary_jsons/100410.json",
"Diaries-only-diary_jsons/100299.json",
"Diaries-only-diary_jsons/100300.json",
"Diaries-only-diary_jsons/100406.json",
"Diaries-only-diary_jsons/100346.json",
"Diaries-only-diary_jsons/100347.json",
"Diaries-only-diary_jsons/100345.json",
"Diaries-only-diary_jsons/100340.json",
"Diaries-only-diary_jsons/100348.json",
"Diaries-only-diary_jsons/100349.json"]

diariesUrlsX = ["Diaries-only-diary_jsons/100348.json", "Diaries-only-diary_jsons/100349.json"]

covers=["a3380001h.jpg","a3363001h.jpg","a3446001h.jpg","a3378001h.jpg","a3364001h.jpg","a3365001h.jpg","a3374001h.jpg","a3368001h.jpg","a3358001h.jpg","a3367001h.jpg","a3362001h.jpg","a3366001h.jpg","a3369001h.jpg","a3375001h.jpg","a3377001h.jpg","a3371001h.jpg","a3372001h.jpg","a3360002h.jpg","a3447001h.jpg","a3448001h.jpg","a3370001h.jpg","a3373001h.jpg","a3376001h.jpg","a3379001h.jpg","a3359001h.jpg","a6369001h.jpg","a6372001h.jpg","a5851001h.jpg","a5854002h.jpg","a5852001h.jpg","a5853001h.jpg","a5731001h.jpg","a5730001h.jpg","a6470001h.jpg","a3314001h.jpg","a2557001h.jpg","a2564001h.jpg","a2562001h.jpg","a2559001h.jpg","a2552001h.jpg","a2556002h.jpg","a2553001h.jpg","a2554001h.jpg","a2560001h.jpg","a2555001h.jpg","a7172001h.jpg","a5301001h.jpg","a5300001h.jpg","a5299001h.jpg","a9494002h.jpg","a5676001h.jpg","a3867001h.jpg","a3862001h.jpg","a3863001h.jpg","a3864001h.jpg","a3868001h.jpg","a5986001h.jpg","a5987001h.jpg","a6373001h.jpg","a2737001h.jpg","a2738001h.jpg","a2739001h.jpg","a5634001h.jpg","a5633001h.jpg","a5328001h.jpg","a4630001h.jpg","a4969001h.jpg","a3959001h.jpg","a3960001h.jpg","a3957001h.jpg","a3958001h.jpg","a2826001h.jpg","a5464001h.jpg","a5463001h.jpg","a5738001h.jpg","a6565001h.jpg","a5839001h.jpg","a5842001h.jpg","a5840001h.jpg","a5841001h.jpg","a5843001h.jpg","a2567001h.jpg","a2568001h.jpg","a3925002h.jpg","a3927002h.jpg","a3926002h.jpg","a6375001h.jpg","a6059002h.jpg","a5770001h.jpg","a5769001h.jpg","a5771001h.jpg","a5678001h.jpg","a5767001h.jpg","a3901001h.jpg","a5983001h.jpg","a4714001h.jpg","a6399001h.jpg","a6400001h.jpg","a6401001h.jpg","a6398001h.jpg","a6397001h.jpg","a5877001h.jpg","a5692001h.jpg","a5691001h.jpg","a4891001h.jpg","a4892001h.jpg","a3545001h.jpg","a6301001h.jpg","a6178001h.jpg","a6179001h.jpg","a3565001h.jpg","a4745001h.jpg","a4746001h.jpg","a4747001h.jpg","a4748001h.jpg","a6703001h.jpg","a6702001h.jpg","a6701001h.jpg","a6719001h.jpg","a6201001h.jpg","a6699001h.jpg","a3955001h.jpg","a3149001h.jpg","a3148001h.jpg","a4032001h.jpg","a4033001h.jpg","a4031001h.jpg","a4391001h.jpg","a4390001h.jpg"]



def buildDiariesJson():
  start_json = "DATA =\n["
  fromTitles = []
  titletxt = ""
  id = 0
  diff = ""
  for diaryUrl in diariesUrls:
    #print "\t\t"+diaryUrl
    start_json += "\n\t{"
    with open(diaryUrl) as data:
      myjson = json.load(data)
      title = myjson["title"]
      #print "\n->"+title
      ## Define fields to save
      id += 1
      diary_id = int(diaryUrl.split("/")[1][:-5])
      noPages = len(myjson["field_transcript_pages"]["und"])
      mycover = myjson["field_digital_order_number"]["und"][0]["value"]

      thiscover = [cover for cover in covers if cover[:-8] == mycover]

      fromTitles.append(diaryUrl.split("/")[1])
      fromTitles.append(parseTitle(title, diaryUrl))
    #print fromTitles
    #print
    ## Build json
    start_json += "\n\t\tid:"+str(id)+","
    start_json += "\n\t\tdiaty_id:"+str(diary_id)+","
    start_json += "\n\t\ttitle:\""+str(title)+"\","
    if len(fromTitles[1])>=3:
      start_json += "\n\t\tstart_date:\""+str(fromTitles[1][2])+"\","
    if len(fromTitles[1])==4:
      start_json += "\n\t\tend_date:\""+str(fromTitles[1][3])+"\","
    start_json += "\n\t\tno_pages:"+str(noPages)+","
    start_json += "\n\t\tlocation:\"location\","
    start_json += "\n\t\ttopics:\"topics\","
    start_json += "\n\t\tkind:\""+str(fromTitles[1][0])+"\","
    if len(fromTitles[1])>=2:
      start_json += "\n\t\tauthor:\""+str(fromTitles[1][1])+"\","
    start_json += "\n\t\tcover:\""+str(thiscover[0])+"\""

    fromTitles = []
    start_json += "\n\t},"
  start_json += "\n];"
  #pprint.pprint(start_json)
  text_file = open("data.js", "w")
  text_file.write(start_json)
  text_file.close()

def parseTitle(raw, diaryUrl):
  raw = raw.strip()
  fromTitles = []
  kind = ''; author = ''
  diff = ""
  tmp = []
  tmp = raw.split(",")
  tmp1 = []
  tmp2 = []
  end = []; start = []
  if len(tmp) == 2 and tmp[1][-4:-2] == '19':
    #print "\tfirst: "+tmp[0]  
    #print "\tsecond: "+tmp[1]
    #print "\t->"+tmp[1][-4:]
    ## Author + kind
    tmp1 = tmp[0].strip().split(" ")
    go = 1
    #print tmp1
    for t in tmp1:
      if t[0].isupper():
        author += t+" "
      else:
        go = 0
        kind += t+" "
    
    fromTitles.append(author.strip())
    fromTitles.append(kind.strip())

    ## Dates
    tmp2 = tmp[1].strip().split("-")
    if len(tmp2)==2:
      ## end date
      end_date = tmp2[1].split(" ")
      if len(end_date) == 3:
        end_year = end_date[0]
        end_month = end_date[1]
        end_day = end_date[2]
        end.append(end_year)
        end.append(end_month)
        end.append(end_day)
      else:
        end.append(end_date)
      ##start date
      start_date = tmp2[0].split(" ")
      if len(start_date)==3:
        start_year = start_date[0]
        start_month = start_date[1]
        start_day = start_date[2]
        start.append(start_year)
        start.append(start_month)
        start.append(start_day)
      else:
        start.append(start_date)
        
      fromTitles.append(start)
      fromTitles.append(end)
    else:
      my = "$$$$ DATES: "+str(tmp2)
      fromTitles.append(my)
      
  else:
    diff +=  "#### "+diaryUrl.split("/")[1]+" --> "+str(tmp)
    diff += " >>>> "+tmp[1][-4:]
    #print "########## "+diaryUrl+" --> "+str(tmp)
    #print "\t->"+tmp[1][-4:]
    fromTitles.append(diff)
  return fromTitles

  #kind = "kind"
  #start_date = "start_date"
  #start_year = "y"
  #start_month = "m"
  #start_day = "d"


'''
OK		"title": "A.R.L. Wiltshire diary, 12 May-20 July 1917", :: from json ===> ["title"]

EASY    "kind":"diary", :: From parsing "title"

EASY		"start_date":
          {
            "year":1918, "month": 1, "day": 28 
          }, 
:: From parsing "title"

EASY		"end_date":
          {
            "year":1918, "month": 1, "day": 28 
          }, 
:: From parsing "title"


EntityRecog		"locations": ["London","Gallipoli"]  ===> List of locations in the diary sort by relevance (number of words?)  

Mallet		"topics":["militar","", "", "", ""]  ===> List of topics sort by relevance (Mallet per page)

		"author":"", ===> 

OK		"cover":"a6565001h.jpg" :: "list-of-url.txt" file and Get-coversjpg-from-urls.py
'''

buildDiariesJson()
