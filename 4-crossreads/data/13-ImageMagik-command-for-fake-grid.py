
''' 
building a command to generate image-grid for each diary

convert -size 200x200 xc:skyblue -fill '#ffffbf' -stroke '#ffffbf' -draw "rectangle 20,10 30,30" -fill '#d7191c' -stroke '#d7191c' -draw "rectangle 50,50 70,70"  draw_rect.gif

montage square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif square.gif -geometry +2+2   montage_geom.jpg

.c4  {background-color: #9966cc;}
.c5  {background-color: #66cccc;}
.c3  {background-color: #99cc66;}
.c2  {background-color: #cc6666;}
.c1  {background-color: #E78F39;}

How to run this cript and generate the images:
$: python 13-ImageMagik-command-for-fake-grid.py>ImageMagick-0.20-1Personal.im
$: mkdir topicGroup-0.2-all # example
$: cat ImageMagick-0.20-all.im |bash

'''

import random
import simplejson as json
import glob

#open diaries.json
f = open("diaries.json", "r")
diariesjson = json.loads(f.read())

g = open("topics.json", "r")
topicsjson = json.loads(g.read())

# Set vars:
IMAGES_PER_ROW = "120" 
# image width = IMAGES_PER_ROW x 10px
#TARGET_DIRECTORY_PATH = "img/topicGroup-0.02-1Personal/"
#TARGET_DIRECTORY_PATH = "img/topicGroup-0.02-2War/"
#TARGET_DIRECTORY_PATH = "img/topicGroup-0.02-3Mil/"
TARGET_DIRECTORY_PATH = "img/topicGroup-0.02-5Tourist/"

TGid = "5"

start = "montage "
end = " -geometry +0+0 -tile "+IMAGES_PER_ROW+"x "+TARGET_DIRECTORY_PATH
imgs = " "
path = "img/"

path0 = "11-diaryID-jsons/"

# ramdon set
#for n in range(1,380):
#    imgs += path+str(random.randrange(1, 5))+".gif " 

## List of available diaries:
output = ""
for d in glob.glob(path0+'*'):
    #print d
    f = open(d, "r")
    mydiary = json.loads(f.read())
    p = 0
    #print type(mydiary[0])
    #print mydiary[0][0]
    #print "<< pages no:"+str(len(mydiary[0]["pages"]))
    imgs = " "
    for diary in mydiary[0]["pages"]:
        p+=1
        #print str(p)+") "+str(diary["topics"][0][0]) ## mallet id     
        mallet_id = diary["topics"][0][0]
        for  topic in topicsjson:
            if mallet_id in  topic["mallet_ids_inluded"]:
                #print "--> "+ str(diary["topics"][0][1])
                ## if float(diary["topics"][0][1]) > 0.20 and topic["tid"] == Tid: ## for Topics 
                if float(diary["topics"][0][1]) > 0.20 and str(topic["tid"])[0] == TGid: # for Topic Groups
                    #print "This page is TG = "+str(topic["tid"])[0]
                    imgs += path+str(topic["tid"])[0]+".gif " 
                else:
                    imgs += path+"0.gif "
                    #print "this is 0.gif"
                    

    output += start+imgs+end+d.split("/")[1][:-5]+'.gif &&'

print output[:-2]
