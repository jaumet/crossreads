import json
import simplejson
from pprint import pprint
import re, random, os

def gen_simple_topics():
  with open('dataDiaries.json') as data_file:    
	  diaries = json.load(data_file)
	  #print data[128]
  out = "["
  for diary in diaries:
    print "\npages: "+str(diary["page_no"])
    out += "["
    for n in range(1, diary["page_no"]):
      #print str(n),
      out += str(random.randint(1, 5))+","
    out += "]"
  out += "]"
  f = open('dummyTopics-real-size.json','w+')
  f.write(out)
  #simplejson.dump(, f)
  f.close()

def gen_only_pages_list():
  # List of Diaries directories
  out = "var pages = [\n"
  path = "diariesPages/"
  diaries = sorted(os.listdir(path))
  # List of pages files per diary 
  # Add random topics
  out += "[\n"
  for diary in diaries:
    out += "["
    pages = sorted(os.listdir(path+diary))
    for page in pages:
      out += "\""+page[:-4]+"\","
    out = out[:-1]
    out +=  "],\n"
  out = out[:-2]
  out +=  "];"
  print out



def gen_topics_with_pages_list_JSON():
  # List of Diaries directories
  out = ""
  path = "diariesPages/"
  diaries = sorted(os.listdir(path))
  # List of pages files per diary 
  # Add random topics
  out += "[\n"
  for diary in diaries:
    out += "{ \"\" :\""+diary+"\": \t{"
    pages = sorted(os.listdir(path+diary))
    for page in pages:
      out += "\""+page[:-4]+"\":"+str(random.randint(1, 5))+","
    out = out[:-1]
    out +=  "}\n},"
  out = out[:-1]
  out +=  "]"

  ## NOTE Get element nth from a dict:
  ## list(dict)
  ## desired key -> k = list(dict)[nth]
  ## value -> dict[k]

  # Write to file
  print out
  
def gen_topics_with_pages_list_ARRAYS():
  # List of Diaries directories
  out = ""
  path = "diariesPages/"
  diaries = sorted(os.listdir(path))
  # List of pages files per diary 
  # Add random topics
  out0 = "var diary = ["
  out = ''
  for diary in diaries:
    out0 += "\""+diary+"\","
    out += "diary[\""+diary+"\"] = ["
    pages = sorted(os.listdir(path+diary))
    for page in pages:
      out += "[\""+page[:-4]+"\","+str(random.randint(1, 5))+"],"
    out = out[:-1]
    out +=  "];\n"
  out0 = out0[:-1]
  out0 +=  "];\n"
  #out = out[:-1]
  #out +=  "]"

  # Write to file
  print out0
  print out
  
gen_only_pages_list()
#gen_topics_with_pages_list_JSON()
#gen_topics_with_pages_list_ARRAYS()
