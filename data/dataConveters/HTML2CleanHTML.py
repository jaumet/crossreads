# -*- coding: utf-8 -*-    
import os, fnmatch
import re

########################
## Usage:
## initialy do: cd path

path = '/var/www/crossreads/data/dataConveters/DOCs-cp/HTMLs'
filePattern= '*.html'
replaceList = { r'^(?:.|\n|\r)+?</head>': '', r'<body.*>': '', '</font>' : '', r'<font face\=\"Calibri\, sans-serif\"\>': '', r'<p\ .*\">': '<p>', r'</body>[.*|\n*]</html>': '', r'<span.*>': '', '<br>': '', '</div>' : '', r'<p>\n+</p>': '', '<sup>': '', '</sup>': '', r'([0-9a-zA-Z])\n([0-9a-zA-Z])': r'\1 \2', r'(\,)\n([0-9a-zA-Z])': r'\1 \2', '\n\n': '\n', '</p>\n<p>': '</p>\n\n<p>', r'<font\ .*\"\>': '', r'\.</p>': r'\n</p>'}

def replace(directory, filePattern):
  for path, dirs, files in os.walk(os.path.abspath(directory)):
    for filename in fnmatch.filter(files, filePattern):
      filepath = os.path.join(path, filename)
      print "--> "+filepath
      s = open(filepath).read()
      for a,b in replaceList.items():
        s = re.sub(a, b, s)
      s = s.decode("utf-8").encode("ascii", "xmlcharrefreplace")
      lastpath = path+"/test/"+filename
      print "*** "+lastpath
      with open(lastpath, "w+") as f:
        f.write(s)

print replace(path, filePattern)

###################################################################
###################################################################
#def findReplace(directory, find, replace, filePattern):
#    for path, dirs, files in os.walk(os.path.abspath(directory)):
#        for filename in fnmatch.filter(files, filePattern):
#            filepath = os.path.join(path, filename)
#            with open(filepath) as f:
#                s = f.read()
#                print "-----------> "+filepath
#            s = re.sub(find, replace, s)
#            s.decode("utf-8").encode("ascii", "xmlcharrefreplace")
#            with open(path+"/test/"+file, "w") as f:
#                f.write(s)
#
#def replace(filename):
#    s = open(filename).read()
#    for a,b in replaceList.items():
#        s = re.sub(a, b, s)
#    return s.decode("utf-8").encode("ascii", "xmlcharrefreplace")
#print replace(path+"/5_cine_nekes_def.html")

#for orig in replaceList:
#  print orig+" -> "+replaceList[orig]
#  findReplace(path, orig, replaceList[orig], "my.html")
#
#print



####################################################
# 
#      > List of replacements:
#D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
#tags = ('<HTML>*.<BODY> -> ''


#, '': '', '': '', '': '', '': '', '': ''

#        </B> -> </b>
#        <(*.)> -> <>
#        <(*.)> -> <>

#        <P>[only bspc]</P> -> ''

#      > Add options to convert also special characters
#        á -> &aacute;
#        é -> &eacute;
#        í -> &iacute;
#        ó -> &oacute;
#        ú -> &uacute;
#        à -> &agrave;
#        è -> &egrave;
#        ò -> &ograve;
#        Á -> &Aacute;
#        É -> &Eacute;
#        Í -> &Iacute;
#        Ó -> &Oacute;
#        Ú -> &Uacute;
#        À -> &Agrave;
#        È -> &Egrave;
#        Ò -> &Ograve;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
#         -> &;
