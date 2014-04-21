#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib,urllib2
import json

API_URL="http://www.scurtu.it/apis/documentSimilarity"


#####################################################################################
##### 		callApi 
#####################################################################################
def callApi(url,inputObject):
  params = urllib.urlencode(inputDict)    
  f = urllib2.urlopen(url, params)
  response= f.read()
  responseObject=json.loads(response)  
  return responseObject
  

  
if __name__ == "__main__":  


  inputDict={}
  inputDict['doc1']='Text of the first document)'
  inputDict['doc2']='Text of the second document'


  finalResponse = callApi(API_URL,inputDict)


  print finalResponse

      



