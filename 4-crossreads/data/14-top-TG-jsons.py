
''' 
building a command to generate image-grid for each diary

convert -size 200x200 xc:skyblue -fill '#ffffbf' -stroke '#ffffbf' -draw "rectangle 20,10 30,30" -fill '#d7191c' -stroke '#d7191c' -draw "rectangle 50,50 70,70"  draw_rect.gif

IMAGE MAGIK command
montage square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif -geometry +2+2   montage_geom.jpg

COLORS
.c4  {background-color: #9966cc;}
.c5  {background-color: #66cccc;}
.c3  {background-color: #99cc66;}
.c2  {background-color: #cc6666;}
.c1  {background-color: #E78F39;}

USAGE
How to run this script and generate the images:
$: python 13-ImageMagik-command-for-fake-grid.py>ImageMagick-0.20-1Personal.im
$: mkdir img/topicGroup-0.2-all # example
$: cat ImageMagick-0.20-all.im |bash

'''

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
## List of available diaries:
output = ""
for TGid in range(1,6):
  top = [[100,"xx"]] ## fake first element. It'll be deleted
  print "----------- TGid: "+str(TGid)
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
              for thetopic in topicsjson:
                if topics[0] in  thetopic["mallet_ids_inluded"] and str(thetopic["tid"])[0] == str(TGid):
                  ## Add conditions to add page to top list: number of element and score > that minimum.
                  if float(topics[1]) > top[-1][0]:
                    del top[-1]
                  if len(top) < TOPLIST_NO:
                    top.append([float(topics[1]),thetopic["label"] ,"/"+d[17:-5]+"/"+str(p)]);
                    print p,
                    ## reorder list desc
                    top = sorted(top,key=lambda el: (-el[0]));

  #####################################
  ## Order 1st for label, 2nd by score desc
  ## top = sorted(top,key=lambda el: (el[1],-el[0]));
  #####################################

  print len(top)
  ## write top to file
  if len(top) >0:
    del top[0]
    f = open('14-tops/TG-'+str(TGid)+'-'+TGlabels[TGid]+'.json','w+')
    f.write(str(top))
    f.close()
    print "\t>>> Written --> tops/TG-"+str(TGid)+"-"+TGlabels[TGid]+".json"

