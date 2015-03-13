from random import randint
import os 

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


