# -*- coding: utf-8 -*-    
import os
import re, fnmatch
import HTMLParser

########################
## Usage:
## initialy do: cd path

path = '/var/www/crossreads/data/dataConveters/DOCs-cp/HTMLs'
filePattern= '*.html'
#replaceList = { r'^(?:.|\n|\r)+?</head>': '', r'<body.*>': '', '</font>' : '', r'<font face\=\"Calibri\, sans-serif\"\>': '', r'<p\ .*\">': '<p>', r'</body>[.*|\n*]</html>': '', r'<span.*>': '', '<br>': '', '</div>' : '', r'<p>\n+</p>': '', '<sup>': '', '</sup>': '', r'([0-9a-zA-Z])\n([0-9a-zA-Z])': r'\1 \2', r'(\,)\n([0-9a-zA-Z])': r'\1 \2', '\n\n': '\n', '</p>\n<p>': '</p>\n\n<p>', r'<font\ .*\"\>': '', r'\.</p>': r'\n</p>'}

def replace(directory, filePattern):
  for path, dirs, files in os.walk(os.path.abspath(directory)):
    for filename in fnmatch.filter(files, filePattern):
      pars = HTMLParser.HTMLParser()
      filepath = os.path.join(path, filename)
      print "--> "+filepath
      with open(filepath) as f:
        s = f.readlines()
      #s = open(filepath).read()
      #s = s.decode("utf-8").encode("ascii", "xmlcharrefreplace")
        s = pars.unescape(s)
      lastpath = path+"/cleanHTML--no/"+filename
      print "*** "+lastpath
      with open(lastpath, "w+") as f:
        f.write(s)

print replace(path, filePattern)
