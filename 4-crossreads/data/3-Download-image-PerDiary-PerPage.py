import os
import urllib2
import json
from os import listdir
from os.path import isfile, join

mypath = "2-PagesList-forEachDiary"
diaries = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for d in diaries:
    raw = '2-PagesList-forEachDiary/'+d
    # Open a Diary with Page List 
    print raw
    if not os.path.exists('3-Images/'+str(d[:-5])):
        os.makedirs('3-Images/'+str(d[:-5]))
    path, dirs, files = os.walk('3-Images/'+str(d[:-5])).next()
    if len(files) == 0:
        with open(raw) as data_file:
            diary = json.load(data_file)
            myurl = ''
            for page in diary[0]['transcript_pages']:
                if type(page) is dict:
                    myurl =  page['uri']
                    print page['uri']
                elif type(page) is unicode:
                    print "is a "+str(type(page))
                    myurl = diary[0]['transcript_pages'][page]['uri']
                    print diary[0]['transcript_pages'][page]['uri']
                else:
                    print "CHECK THISSSSSSSSSS"            
                response = urllib2.urlopen(myurl)
                myjson = json.load(response)
                newdir = '3-Images/'+str(d[:-5])
                if not os.path.exists(newdir+'/'+myjson['nid']+'.jpg'):
                    try:
                        myurl = myjson['transcript_image']['file']['uri']
                        print "---> "+str(myurl)
                        #if not os.path.exists(newdir): os.makedirs(newdir)
                        response2 = urllib2.urlopen(myurl)
                        myjson2 = json.load(response2)
                        imgurl = myjson2['url']
                    except:
                        imgurl = "http://teatre.com/parts-of-the-leg.jpg"
                    print imgurl
                    #if not os.path.exists(newdir+'/'+myjson['nid']+'.jpg'):
                    img = urllib2.urlopen(imgurl)
                    file = open(newdir+'/'+myjson['nid']+'.jpg', "wb")
                    file.write(img.read())
                    file.close()
                    print "Created --> "+newdir+'/'+myjson['nid']+'.jpg'
                    print "------------"
print
print "This is it"

