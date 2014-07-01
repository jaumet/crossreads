import os, fnmatch, re
'''
This script segments cleanHTML files in paragraphs and then converts it to a JSON format
'''


# FIRST Set the path ans the file name pattern
#path = '/var/www/crossreads/data/dataConveters/DOCs-cp-35-57/HTMLs'
path = '/home/jnualart/public_html/crossreads/data/dataConveters/DOCs-cp-35-57/HTMLs'
filePattern= '*.html'

# SECOND Set the directory from were to cleanedHTML files
#getDir = 'cleanHTML--no-entities'
getDir = 'cleanHTML'

# THIRD Set the directory were to save the JSON files
#saveDir = 'JSON--no-entities'
saveDir = 'JSON'



def replace(directory, filePattern, getDir, saveDir):
  path1 = directory+'/'+getDir
  path2 = directory+'/'+saveDir
  for path, dirs, files in os.walk(os.path.abspath(path1)):
      for filename in fnmatch.filter(files, filePattern):
        print "#########"+filename
        filepath = os.path.join(path, filename)
        print "--> "+filepath
        with open(filepath) as f:
          data = f.read()
          '''Build a list splitting data into "<p>.*</p>" pieces'''
          paragraphsIn = re.compile("(?<!^)\s+(?=\<p\>)(?!.\s)").split(data)

        '''Join paragraphs with len < 700 characters (including spaces)'''
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
          #p = re.sub(r'<p>\s+</p>', '', p)
          
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
              if len(p) + len(paragraphsOut[-1]) < 700 or len(p) < 200:
                paragraphsOut[-1] += p
                print "[Concatenated] len(paragraphsOut[-1]) -> "+str(len(paragraphsOut[-1])) 
              else:
                paragraphsOut.append(p)
                print "[appendded]"
            else:
              if len(paragraphsOut[-1]) < 200:
                paragraphsOut[-1] += p
              else:
                # FIXME split p by "."
                paragraphsOut.append(p)

          print "---> len(paragraphsOut) ->"+str(len(paragraphsOut))
        '''JSON output'''    
        myjson = "["
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


replace(path, filePattern, getDir, saveDir)


