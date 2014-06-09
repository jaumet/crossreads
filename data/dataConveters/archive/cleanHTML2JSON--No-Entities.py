# -*- coding: utf-8 -*-    
import os, fnmatch, re

########################
## Usage:
## initialy do: '/var/www/crossreads/data/dataConveters/' path

path1 = '/var/www/crossreads/data/dataConveters/DOCs-cp/HTMLs'
filePattern= '*.html'
replaceList = {
 r'^(?:.|\n|\r)+?</head>': '',
 r'<body.*?\>': '', 
 '</font>' : '', 
 r'<p\ .*?\>': '<p>', 
 r'</body>[.*|\n*]</html>': '', 
 r'<span.*?\>': '',
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
      print ">>>> "+lastpath
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
        filepath = os.path.join(path, filename)
        print "--> "+filepath
        with open(filepath) as f:
          data = f.read()
          '''Build a list splitting data into "<p>*.</p>" pieces'''
          paragraphsIn = re.compile("(?<!^)\s+(?=\<p\>)(?!.\s)").split(data)

        '''Join paragraphs with len < 1100 characters (including spaces)'''
        paragraphsOut = []          
        for i, p in enumerate(paragraphsIn):
          # Cleaning paragraphs from bad chatarters
          p = re.sub("\n", "", p)
          p = re.sub('\"', '\\\"', p)
          p = re.sub('\t', ' ', p)
          p = re.sub('', ' ', p)
          p = re.sub('', ' ', p)
          p = re.sub('', ' ', p)
          # Remove empty <p> </p> !!!!!!!!!!!!!!!!!
          p = re.sub(r'<p>\s+</p>', '', p)

          print "####"
          print "i -> "+str(i)
          print "len(p) -> "+str(len(p))
          print "----"
          # output builder
          if i==0:
            # Create here the spliter in case len(p) > 700
            paragraphsOut.append(p)
          else:
            if len(p) < 700:
              if len(p) + len(paragraphsOut[-1]) < 700:
                paragraphsOut[-1] += p
                print "[Concatenated] len(paragraphsOut[-1]) -> "+str(len(paragraphsOut[-1])) 
              else:
                paragraphsOut.append(p)
                print "[appendded]"
            else:
              if len(paragraphsOut[-1]) < 100:
                paragraphsOut[-1] += p
              else:
                # split p by "."
                paragraphsOut.append(p)

          print "---> len(paragraphsOut) ->"+str(len(paragraphsOut))

        '''JSON output'''    
        myjson = "[\n"
        for i, p1 in enumerate(paragraphsOut):
          myjson +=  "\n\t{\n\t\t\"pid\" : "+str(i)+",\n\t\t\"p\" : \""+p1+"\"\n\t},"
        myjson = myjson[:-1]
        myjson += "\n]"
        ## CUSTOMIZE split AS THE NAMES OF THE FILES REQUIRE
        filename = filename.split(" ")[0]
        with open(path2+"/"+filename+".json", "w+") as f:
          print ">>>>>>>> "+path2+"/"+filename+".json"
          f.write(myjson)


  #print "####  DEBUG  ########"
  #print "from: "+str(len(paragraphs))
  #print "to: "+str(len(paragraphs1))
  #print "############"


replace(path, filePattern)

