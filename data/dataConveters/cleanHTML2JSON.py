import os, re

with open("my.html") as f:
    data = f.read()
    '''Build a list splitting data into "<p>*.</p>" pieces'''
    paragraphs = re.compile("(?<!^)\s+(?=\<p\>)(?!.\s)").split(data)

'''Join paragraphs with len < 1100 characters (including spaces)'''
paragraphs1 = []
for i, p in enumerate(paragraphs):
  p = re.sub("\n", "", p)
  if i==0:
    paragraphs1.append(p)
  else:
    ### FIXME: don't append in case a paragraph is too short. It could be a section title.
    if len(paragraphs[i-1]) + len(paragraphs[i])<1100:
      paragraphs1[-1] += p
    else:
      paragraphs1.append(p)

'''JSON output'''    
myjson = "[\n"
for i, p1 in enumerate(paragraphs1):
  myjson +=  "\t{\n\t\t\"pid\" : "+str(i)+",\n\t\t\"p\" : \""+p1+"\"\n\t},\n"

myjson += "\n]"
print myjson

#print "############"
#print "from: "+str(len(paragraphs))
#print "to: "+str(len(paragraphs1))
#print "############"
