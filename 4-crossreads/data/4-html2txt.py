import os, fnmatch
import re

directory = "/home/jaume/crossreads/crossreads/4-crossreads/data/3-TranscriptionsHTML"
for path, dirs, files in os.walk(os.path.abspath(directory)):
    print path
    for filename in files:
        filepath = os.path.join(path, filename)
        print "-->"+filepath
        myfile = open(filepath, "r")
        html = myfile.read()
        print html
        txt = re.sub("<.*?>", "", html)
        print "## ## ## ## ## ## ## ## ##"
        print txt
        filepath1 = filepath.replace("3-TranscriptionsHTML","3-TranscriptionsTXT")
        myfile1 = open(filepath1, "wb+")
        myfile1.write(txt)  
        myfile1.close()
        myfile.close()

                
