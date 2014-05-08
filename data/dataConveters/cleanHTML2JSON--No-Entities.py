# -*- coding: utf-8 -*-    
import os, fnmatch, re

########################
## Usage:
## initialy do: '/var/www/crossreads/data/dataConveters/' path

path1 = '/var/www/crossreads/data/dataConveters/DOCs-cp/HTMLs'
filePattern= '*.html'
replaceList = { r'^(?:.|\n|\r)+?</head>': '', r'<body.*>': '', '</font>' : '', r'<font face\=\"Calibri\, sans-serif\"\>': '', r'<p\ .*\">': '<p>', r'</body>[.*|\n*]</html>': '', r'<span.*>': '', '<br>': '', '</div>' : '', r'<p>\n+</p>': '', '<sup>': '', '</sup>': '', r'([0-9a-zA-Z])\n([0-9a-zA-Z])': r'\1 \2', r'(\,)\n([0-9a-zA-Z])': r'\1 \2', '\n\n': '\n', '</p>\n<p>': '</p>\n\n<p>', r'<font\ .*\"\>': '', r'\.</p>': r'\n</p>'}

def replace1(directory, filePattern):
  for path, dirs, files in os.walk(os.path.abspath(directory)):
    for filename in fnmatch.filter(files, filePattern):
      filepath = os.path.join(directory, filename)
      print "--> "+filepath
      s = open(filepath).read()
      for a,b in replaceList.items():
        s = re.sub(a, b, s)
      #### No- entities
      ## s = s.decode("utf-8").encode("ascii", "xmlcharrefreplace")
      lastpath = path1+"/cleanHTML--no-entities/"+filename
      print "*** "+lastpath
      with open(lastpath, "w+") as f:
        f.write(s)


print replace1(path1, filePattern)

print
print "####################################################"
print

####################################################
#### cleanHTML2JSON

path = '/var/www/crossreads/data/dataConveters/DOCs-cp/HTMLs'
filePattern= '*.html'
print "INITIAL"

def replace(directory, filePattern):
  path1 = directory+'/cleanHTML--no-entities'
  path2 = directory+'/JSON--no-entities'
  for path, dirs, files in os.walk(os.path.abspath(path1)):
      for filename in fnmatch.filter(files, filePattern):
        print "#########"+filename
        filepath = os.path.join(path1, filename)
        print "--> "+filepath
        with open(filepath) as f:
          data = f.read()
          '''Build a list splitting data into "<p>*.</p>" pieces'''
          paragraphs = re.compile("(?<!^)\s+(?=\<p\>)(?!.\s)").split(data)

        '''Join paragraphs with len < 1100 characters (including spaces)'''
        paragraphs1 = []
        for i, p in enumerate(paragraphs):
          p = re.sub("\n", "", p)
          p = re.sub('\"', '\\\"', p)
          if i==0:
            paragraphs1.append(p)
          else:
            if len(paragraphs[-1]) + len(p)<1100:
              paragraphs1[-1] += p
            else:
              paragraphs1.append(p)

        '''JSON output'''    
        myjson = "[\n"
        for i, p1 in enumerate(paragraphs1):
          myjson +=  "\t{\n\t\t\"pid\" : "+str(i)+",\n\t\t\"p\" : \""+p1+"\"\n\t},\n"
        myjson += "\n]"

        with open(path2+"/"+filename+".json", "w+") as f:
          print ">>>>>>>> "+path2+"/"+filename+".json"
          f.write(myjson)

  #print "####  DEBUG  ########"
  #print "from: "+str(len(paragraphs))
  #print "to: "+str(len(paragraphs1))
  #print "############"


replace(path, filePattern)


