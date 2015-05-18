from random import randint
import os 


def generate_pages():
  loc = ['Australia', 'London', 'Gallipolly']
  my_topics = ['family', 'peace', 'militar']
  destdir = '/home/jnualart/public_html/crossreads/3-crossreads/interface/data/covers/'
  covers = [f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f))]
  for my_diary_id in range(1,130):
    mydata = 'DATA =\n['
    y = randint(1914, 1919)
    id = 0
    print 'my_diary_id: '+str(my_diary_id)
    print 'covers len: '+str(len(covers))
    for my_page_no in range(1,randint(70,140)):
      id += 1
      diary_id = my_diary_id
      page_no = my_page_no
      title = "title"
      date = str(y)+'/'+str(randint(1,12))+'/'+str(randint(1,30))
      location = loc[randint(0,2)]
      topics = my_topics[randint(0,2)]
      transcript = 'transcript'
      cover = str(covers[my_diary_id-1])
      mydata += "\n\t{\n\t\t\"id\":"+str(id)+",\n\t\t\"diary_id\":\""+str(diary_id)+"\",\n\t\t\"page_no\":\""+str(page_no)+"\",\n\t\t\"title\":\""+title+"\",\n\t\t\"date\":\""+date+"\",\n\t\t\"location\":\""+location+"\",\n\t\t\"topics\":\""+topics+"\",\n\t\t\"transcript\":\""+transcript+"\",\n\t\t\"cover\":\""+cover+"\"\n\t},"
    mydata = mydata[:-1]
    mydata += '\n]'
    file = open("dummyDiaries/"+str(diary_id)+'.js', "w")
    print("dummyDiaries/"+str(diary_id)+'.js')
    file.write(mydata)
    file.close

def generate_diaries_file():
  loc = ['Australia', 'London', 'Gallipolly']
  my_topics = ['family', 'peace', 'militar']
  #destdir = '/home/jnualart/public_html/crossreads/3-crossreads/interface/data/covers/'
  destdir = './covers/'
  covers = [f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f))]
  mydata = 'DATA =\n['
  id = 0
  for my_diary_id in range(1,130):
    page_no = randint(70,140)
    y = randint(1914, 1919)
    print 'my_diary_id: '+str(my_diary_id)
    print 'covers len: '+str(len(covers))
    #for my_page_no in range(1,randint(70,140)):
    id += 1
    diary_id = my_diary_id
    title = "D "+str(my_diary_id-1)
    date = str(y)+'/'+str(randint(1,12))+'/'+str(randint(1,30))
    location = loc[randint(0,2)]
    topics = my_topics[randint(0,2)]
    transcript = 'transcript'
    cover = str(covers[my_diary_id-1])
    mydata += "\n\t{\n\t\t\"id\":"+str(id)+",\n\t\t\"diary_id\":\""+str(diary_id)+"\",\n\t\t\"title\":\""+title+"\",\n\t\t\"date\":\""+date+"\",\n\t\t\"page_no\":\""+str(page_no)+"\",\n\t\t\"location\":\""+location+"\",\n\t\t\"topics\":\""+topics+"\",\n\t\t\"transcript\":\""+transcript+"\",\n\t\t\"cover\":\""+cover+"\"\n\t},"
  mydata = mydata[:-1]
  mydata += '\n]'
  file = open('dataDiaries.js', "w")
  #print("dataDiaries/"+str(diary_id)+'.js')
  file.write(mydata)
  file.close

def generate_topicsDummy():
  mydata = 'var topicMatrix = [\n'
  for my_diary_id in range(1,130): 
    tmp = '['
    for page_no in range(1,randint(70,140)):
      tmp += str(randint(1,5))+','
    print tmp
    mydata += tmp[:-1]+'],\n'
  mydata += '];'
  file = open('topicsDummy.js', "w")
  file.write(mydata)
  file.close
  
############################
#generate_pages()
#generate_diaries_file()
generate_topicsDummy()
