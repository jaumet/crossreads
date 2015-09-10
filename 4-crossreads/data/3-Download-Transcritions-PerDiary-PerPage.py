import os
import urllib2
import json
from os import listdir
from os.path import isfile, join

# Browse dirctory. And for each file do:
mypath = "2-PagesList-forEachDiary"
diaries = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for d in diaries:
    #print "xxxx"
    raw = '2-PagesList-forEachDiary/'+d
    # Open a Diary with Page List 
    print raw
    if not os.path.exists('3-Transcriptions/'+str(d[:-5])):
        with open(raw) as data_file:
            diary = json.load(data_file)
            #print diary[0]['transcript_pages']
            myurl = ''
            for page in diary[0]['transcript_pages']:
                if type(page) is dict:
                    myurl =  page['uri']
                    print page['uri']
                    #print "Is a dict"
                elif type(page) is unicode:
                    print "is a "+str(type(page))
                    #import re
                    myurl = diary[0]['transcript_pages'][page]['uri']
                    print diary[0]['transcript_pages'][page]['uri']
                    #m = re.search('(http\:\/\/.+)\"\,\"id', page)
                    #print m
                else:
                    print "CHECK THISSSSSSSSSS"
                
                #print page["uri"] #["transcript_pages"]["id"] #['id']
                response = urllib2.urlopen(myurl)
                myjson = json.load(response)
                try:
                    transcription = myjson['transcription']['value']
                except:
                    transcription = "ERROR"
                print transcription
                if transcription is not ("<p>[Blank]</p>" and "ERROR"):
                    #check if directory exists and create it
                    newdir = '3-Transcriptions/'+str(d[:-5])
                    if not os.path.exists(newdir): os.makedirs(newdir)
                    if not os.path.exists(newdir+'/'+myjson['nid']+'.json'):
                        file = open(newdir+'/'+myjson['nid']+'.txt', "w")
                        file.write(transcription)
                        file.close()
                        print "Created --> "+newdir+'/'+myjson['nid']+'.json'
                print "------------"
                ## Idemfor the image-file:
                ##image = myjson['transcript_image']['file']['uri']
            
print
print "This is it"

