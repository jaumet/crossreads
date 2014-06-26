# -*- coding: utf-8 -*-    
'''
This script clean HTML tags except for <p>, <b>, <i> and <a>
(with or without HTML entities)
'''


import os, fnmatch
import re

# FIRST Set the path and file pattern
#path = '/var/www/crossreads/data/dataConveters/DOCs-cp-35-57/HTMLs'
path = '/home/jnualart/public_html/crossreads/data/dataConveters/DOCs-cp-35-57/HTMLs'
filePattern = '*.html'

# SECOND do you want to convert special characters to HTML entities? "yes" or something else
#entities = 'yes'
entities = 'no'

# THIRD Set the directory were to save the cleaned files (must be inside "path")\
saveDir = 'cleanHTML--no-entities'
#saveDir = 'cleanHTML'

replaceList = {
 r'^(?:.|\n|\r)+?</head>': '',
 r'<body.*?\>': '', 
 '</font>' : '', 
 r'<p\ .*?\>': '<p>', 
 r'\<\/body\>.*?\<\/html\>': '', 
 '</body>':'',
 '</html>':'',
 r'<span\ .*?\>': '',
 r'<\/span>': '',
 '</div>' : '', 
 '<sup>': '[', 
 '</sup>': ']',
 r'([0-9a-zA-Z])\n([0-9a-zA-Z])': r'\1 \2', 
 r'<font\ .*?\"\>': '',
 r'<a\ .*?\">': '[',
 '</a>': ']',
 '\n\n': '\n',
 '<br>': '',
 r'([0-9a-zA-Z])\n([0-9a-zA-Z])': r'\1 \2',
 r'(\,|\:|\>|\])\n([0-9a-zA-Z])': r'\1 \2',
 r'(\,|\:|\>|\|\)]|\;)\n(\,|\:|\<|\]|\;|[0-9a-zA-Z])': r'\1 \2',
 r'</p>\s+<p>': '</p>\n<p>',
 r'^\<\p\>\s+\<\/\p\>\n$': '',
 r'<p>\n+</p>': '',
 "<p>  </p>": ""
}

def replace(directory, filePattern, entities, saveDir):
  for path, dirs, files in os.walk(os.path.abspath(directory)):
    for filename in fnmatch.filter(files, filePattern):
      filepath = os.path.join(path, filename)
      print "FILEPATH --> "+filepath
      s = open(filepath).read()
      for a,b in replaceList.items():
        s = re.sub(a, b, s)
        print a
      if entities=="yes":
        s = s.decode("utf-8").encode("ascii", "xmlcharrefreplace")
      path = directory
      lastpath = path+"/"+saveDir+"/"+filename
      print "PATH >>>"+path
      print "LASTPATH *** "+lastpath
      with open(lastpath, "w+") as f:
        f.write(s)

print replace(path, filePattern, entities, saveDir)
