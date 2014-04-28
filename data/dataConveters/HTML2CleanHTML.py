# -*- coding: utf-8 -*-    
import os, fnmatch
import re

path = '/var/www/crossreads/data/dataConveters/DOCs-cp/HTMLs/test'
replaceList = {'^(?:.|\n|\r)+?</head>': '', '</div>' : '', '</font>' : '', '<br>': '', '<body.*>': '','<p.*>': '<p>', '<div.*>': '', '</body>[.*|\n*]</html>': '', '<font[.*|\b+]\">': '', '\<p\>\n+\<\/p\>': '', '<span.*>': '', '</span>': '', '\•': ''} 


def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
                print "-----------> "+filepath
            #s = s.replace(find, replace)
            s = re.sub(find, replace, s)
            with open(filepath, "w") as f:
                f.write(s)

for orig in replaceList:
  print orig+" -> "+replaceList[orig]
  findReplace(path, orig, replaceList[orig], "*.html")

print






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
