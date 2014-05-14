# -*- coding: utf-8 -*-    
import os, fnmatch
import re

########################
## Usage:
## initialy do: cd path

path = '/var/www/crossreads/data/dataConveters/DOCs-cp/HTMLs'
filePattern= '*.html'

replaceList = {
 r'^(?:.|\n|\r)+?</head>': '',
 r'<body.*?\>': '', 
 '</font>' : '', 
 r'<p\ .*?\>': '<p>', 
 r'</body>[.*|\n*]</html>': '', 
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
 '<p>\n</p>': '',
 '<p>\n\n</p>': '',
 '<p>\n\n\n</p>': '',
 '<br>': '',
 r'([0-9a-zA-Z])\n([0-9a-zA-Z])': r'\1 \2',
 r'(\,|\:|\>|\])\n([0-9a-zA-Z])': r'\1 \2',
 r'(\,|\:|\>|\|\)]|\;)\n(\,|\:|\<|\]|\;|[0-9a-zA-Z])': r'\1 \2',
 r'</p>\s+<p>': '</p>\n<p>'
}

def replace(directory, filePattern):
  for path, dirs, files in os.walk(os.path.abspath(directory)):
    for filename in fnmatch.filter(files, filePattern):
      filepath = os.path.join(path, filename)
      print "--> "+filepath
      s = open(filepath).read()
      for a,b in replaceList.items():
        s = re.sub(a, b, s)
      s = s.decode("utf-8").encode("ascii", "xmlcharrefreplace")
      lastpath = path+"/cleanHTML/"+filename
      print "*** "+lastpath
      with open(lastpath, "w+") as f:
        f.write(s)

print replace(path, filePattern)

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
