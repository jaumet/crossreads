import os, fnmatch, re

path = '/var/www/crossreads/data/dataConveters/DOCs-cp/HTMLs'
filePattern= '*.html'
print "INITIAL"

def replace(directory, filePattern):
  path1 = directory+'/cleanHTML'
  path2 = directory+'/JSON'
  for path, dirs, files in os.walk(os.path.abspath(path1)):
      for filename in fnmatch.filter(files, filePattern):
        print "#########"+filename
        filepath = os.path.join(path, filename)
        print "--> "+filepath
        with open(filepath) as f:
          data = f.read()
          '''Build a list splitting data into "<p>*.</p>" pieces'''
          paragraphs = re.compile("(?<!^)\s+(?=\<p\>)(?!.\s)").split(data)

        '''Join paragraphs with len < 1100 characters (including spaces)'''
        paragraphs1 = []
        for i, p in enumerate(paragraphs):
          p = re.sub("\n", "", p)
          p = re.sub('\"', '\\\"', p)
          p = re.sub('\t', ' ', p)
          p = re.sub('', ' ', p)
          p = re.sub('', ' ', p)
          p = re.sub('', ' ', p)          
          
          if i==0:
            paragraphs1.append(p)
          else:
            if len(paragraphs[i-1]) + len(paragraphs[i])<1100:
              paragraphs1[-1] += p
            else:
              paragraphs1.append(p)

        '''JSON output'''    
        myjson = "[\n"
        for i, p1 in enumerate(paragraphs1):
          myjson +=  "\n\t{\n\t\t\"pid\" : "+str(i)+",\n\t\t\"p\" : \""+p1+"\"\n\t},"
        ## FIXME remove last ","
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


