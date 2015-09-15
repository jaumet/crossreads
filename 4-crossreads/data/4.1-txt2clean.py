import os, fnmatch
import re

#directory = "/home/jaume/crossreads/crossreads/4-crossreads/data/3-TranscriptionsTXT"
directory = "/home/jnualart/public_html/crossreads/4-crossreads/data/3-TranscriptionsTXT"

for path, dirs, files in os.walk(os.path.abspath(directory)):
    print path
    for filename in files[10:]:
        filepath = os.path.join(path, filename)
        print "-->"+filepath
        myfile = open(filepath, "r")
        html = myfile.read()
        #print html
        print "..............................................."
        txt = re.sub("\[Page.*?\]", "", html)
        #import HTMLParser
        #h = HTMLParser.HTMLParser()
        #txt = h.unescape(txt)
   
        txt = txt.replace("&nbsp;", " ")
        txt = txt.replace("&quot;", "\"")
        txt = txt.replace("&amp;", "&")
        txt = txt.replace("&#39;", "'")
        txt = txt.replace("&ndash;", "-")
        txt = txt.replace("&mdash;", "-")
        txt = txt.replace("&frac12;", "1/2")
        txt = txt.replace("&frac14;", "1/4")
        txt = txt.replace("&frac34;", "3/4")
        txt = txt.replace("&eacute;", "e")
        txt = txt.replace("&hellip;", "...")

        txt = txt.replace("&deg;", "")
        txt = txt.replace("&pound;", "")
        txt = txt.replace("&percnt;", "%")
        txt = txt.replace("&acirc;", "a")
        txt = txt.replace("&amp:", "&")
        txt = txt.replace("&amp;", "&")
        txt = txt.replace("&amp", "&")
        txt = txt.replace("&anp;", "&")
        txt = txt.replace("&mp;", "&")
        txt = txt.replace("&egrave;", "e")
        #txt = txt.replace("", "")
        #txt = txt.replace("", "")
        #txt = txt.replace("", "")
        #txt = txt.replace("", "")

        print txt
        print
        print "## ## ## ## ## ## ## ## ##"
        print
        
        filepath1 = filepath.replace("3-TranscriptionsTXT","3-TranscriptionsCLEAN")
        myfile1 = open(filepath1, "wb+")
        myfile1.write(txt)  
        myfile1.close()
        myfile.close()


