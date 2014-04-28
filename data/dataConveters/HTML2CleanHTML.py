# -*- coding: utf-8 -*-    
import os, fnmatch
import re
import cgi

path = '/var/www/crossreads/data/dataConveters/DOCs-cp/HTMLs/test'

replaceList = { '^(?:.|\n|\r)+?</head>': '', '<body.*>': '', '<\/font>' : '', '<font face\=\"Calibri\, sans-serif\"\>': '', '<p\ .*\">': '<p>', '</body>[.*|\n*]</html>': '', '<span.*>': '', '<br>': '', '</div>' : '', '<p>\n+</p>': '', '<sup>': '', '<\/sup>': '', r'([0-9a-zA-Z])\n([0-9a-zA-Z])': r'\1 \2', r'(\,)\n([0-9a-zA-Z])': r'\1 \2', '\n\n': '\n', '</p>\n<p>': '</p>\n\n<p>', '<font\ .*>': '', '[\d|\.|>]</p>': '\n</p>'}

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
                print "-----------> "+filepath
            s = re.sub(find, replace, s)
            ## not working:
            #s = cgi.escape(s)
            s = unicode(eval(s))
            s.encode("ascii", "xmlcharrefreplace")
            with open(filepath, "w") as f:
                f.write(s)

for orig in replaceList:
  print orig+" -> "+replaceList[orig]
  findReplace(path, orig, replaceList[orig], "my.html")

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
