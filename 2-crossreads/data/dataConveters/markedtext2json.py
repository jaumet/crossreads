import re

with open('Quaranta_In_Your_Computer.txt', 'r') as markedText:
  output = markedText.readlines()
path = '/home/jnualart/public_html/crossreads/2-crossreads/data/texts/'
tmp = ''
c = 0
textArray = []
for line in output:
  if (line[0:5]=='#####'):
    if c>0:
      print "counting = "+str(c)
      # Get the title and text
      #title = re.search('(.*?)\\n\%\%\%\%', tmp).group(1),
      #print "title: "+title
      print tmp.split('%%%%')[0][8:].strip()
      text = tmp.split('%%%%')[1].strip()
      print text[0:150]
      textArray = text.split('@@@@')
      print "No of segments: "+str(len(textArray) )
      # Build JSON format
      myjson = '[\n'
      for segment in textArray:
        seg = segment.replace('"', '\\"').replace('\n', '<br />').replace('<br /><br />', '<br />')
        seg = seg.replace('<br /><<<<<br />', '').replace('<br />>>>><br />', '')
        seg = re.sub(r"^\<br \/\>|<br \/\>$", "", seg)
        if (seg.strip() != ""):
          myjson += '\t{\n\t\t"pid" : '+str(textArray.index(segment))+',\n\t	"p" : "'+seg.strip()+'"\n\t},\n' 
      myjson = myjson[:-2]
      myjson += '\n]'
      with open(path+str(c)+".json", "w+") as f:
        print ">>>>>>>> "+path+str(c)+".json"
        f.write(myjson)
      print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"      
      
      # Write output file
      
      # Initialisation
    c += 1
    tmp = ''
    
  tmp += line
