
import simplejson as json
import glob
from pprint import pprint

#open diaries.json
f = open("diaries.json", "r")
diariesjson = json.loads(f.read())

g = open("topics.json", "r")
topicsjson = json.loads(g.read())

# Set vars:
TGlabels = ["", "per","war","mil","tra","tou"]
TOPIC_THERSHOLD = 0.1;
TOPLIST_NO = 1001;
path0 = "11-diaryID-jsons/"
topics_list = [1, 3, 5, 6, 7, 8, 9, 12, 14, 15, 17, 18, 19, 20, 23, 24, 25, 26, 27, 33, 34, 35, 36, 37, 38, 39, 40, 42, 45, 46, 49, 50, 53, 57, 58, 59, 60, 61, 62, 63, 65, 66, 68, 69, 70, 71, 72, 74, 75, 77, 78, 79, 80, 83, 84, 85, 87, 89, 90, 93, 94, 95, 96, 97] ## 64 topics out of 100. Finally 30 Labels.

## List of available diaries:

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!! MAIN LOOP NEEDS TO BE TOPICSJSON, AND THEN FOR EACH label, loop all diariesID.json and apply rules
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

totals = []
for thetopic in topicsjson:
  top = [[100,"xx"]] ## fake first element. It'll be deleted  
  TGid = int(str(thetopic["tid"])[0])
  print "----------- TGid: "+str(thetopic["mallet_ids_inluded"])
  for d in glob.glob(path0+'*'):
      #print d
      f = open(d, "r")
      mydiary = json.loads(f.read())
      p = 0
      for pages in mydiary[0]["pages"]:
          p+=1
          for topics in pages["topics"]:
            if float(topics[1]) >= TOPIC_THERSHOLD: 
              ## get TG of this mallet_id, topics[0]
              if topics[0] in thetopic["mallet_ids_inluded"]: # and str(thetopic["tid"])[0] == str(TGid):
                ## Add conditions to add page to top list: number of element and score > that minimum.
                if float(topics[1]) > top[-1][0]:
                  del top[-1]
                if len(top) < TOPLIST_NO:
                  top.append([float(topics[1]), "/"+d[17:-5]+"/"+str(p)]);
                  #print p,
                  ## reorder list desc
                  top = sorted(top,key=lambda el: (-el[0]));

  #####################################
  ## Order 1st for label, 2nd by score desc
  ## top = sorted(top,key=lambda el: (el[1],-el[0]));
  #####################################

  print len(top)
  totals.append([str(TGid)+'-'+TGlabels[TGid], str(thetopic["tid"])+'-'+thetopic["label"], len(top)])
  ## write top to file
  if len(top) >0:
    del top[0]
    f = open('14-tops/Topic-'+str(TGid)+'-'+TGlabels[TGid]+'--'+str(thetopic["tid"])+'-'+thetopic["label"].replace(" ","_")+'.json','w+')
    f.write(str(top))
    f.close()
    print '\t>>> Written --> 14-tops/Topic-'+str(TGid)+'-'+TGlabels[TGid]+'--'+str(thetopic["tid"])+'-'+thetopic["label"].replace(" ","_")+'.json'
print "------"
pprint(totals)
