import csv

topics = ['Analysis & family', 'Cities & landscapes', 'Travelling', 'War', 'Militar life']

f = open('results/20topics/my_compostion.csv')
my20 = csv.reader(f)
t0 = 0;t1=0;t2=0;t3=0;t4=0;co=0
out='var topicMatrix = [\n['
# Transform 20 topics to 5
c = [[],[],[],[],[]]
current = ''
for row20x in my20:
  co+=1;row5 = [];tmp = []
  #out += '['
  # in mycsv topics go from column 2 to 22 
  # out put is 5 columns: (6, 9, 10, 20), (2, 11, 13, 17, 18), (12, 14, 16), (7, 19, 21), (3, 4, 5, 8) NOT included: 15 +float(row20x[15]))
  row5.append(row20x[1].replace('file:/home/jaume/apps/Mallet/Diaries-superclean-text/',''))
  tmp.append(float(row20x[6])+float(row20x[9])+float(row20x[10])+float(row20x[20]))
  tmp.append(float(row20x[2])+float(row20x[11])+float(row20x[13])+float(row20x[17])+float(row20x[18]))
  tmp.append(float(row20x[12])+float(row20x[14])+float(row20x[16]))
  tmp.append(float(row20x[7])+float(row20x[19])+float(row20x[21]))
  tmp.append(float(row20x[3])+float(row20x[4])+float(row20x[5])+float(row20x[8]))
  m = max(tmp)
  mymax = [i for i, j in enumerate(tmp) if j == m]
  #row5.extend(mymax)
  mymax[0] += 1
  if str(mymax[0]) != '':
    diary = row20x[1].replace('file:/home/jaume/apps/Mallet/Diaries-superclean-text/','').split('/')[0]
    if current == str(diary):
      out += str(mymax[0])+','
    else:
      out = out[:-1]      
      current = str(diary)
      out += '], \n[0,'+str(mymax[0])+', ' ##+current
  


  #    print len(row20x)
  #     print tmp
  #print row5
  #print
  #  print mymax[0],
  #  print tmp[mymax[0]],

  # result:
  
  
  if int(mymax[0]) == 1:
    t0 += 1
  if int(mymax[0]) == 2:
    t1 += 1
  if int(mymax[0]) == 3:
    t2 += 1
  if int(mymax[0]) == 4:
    t3 += 1
  if int(mymax[0]) == 5:
    t4 += 1
out = out[:-1]
out += ']\n];'

print out

#print t0, t1, t2, t3 , t4
# write it out as pagesTopic.json

