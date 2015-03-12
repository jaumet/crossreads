'''
explore.py ~ this is a console program that helps to explore the collection of WWI-Diaries
'''
from os import walk

## main class 
class Explore():
	def __init__(self):
		self.path = "./Diaries"

	## my console
	def console(self):
		keep_going = True
		count = 0
		while keep_going:
			command = raw_input('I\'m the data: ['+str(count)+']? ').strip()
			if command == 'r': # 
				count += 1
				self.walkDirectory(self.path, 'report')
			elif command == 's': # search
				kindOf = raw_input('Simple search (s), Visualize (v), Detail text (d)? ').strip()
				query = raw_input('your query: ').strip()
				if kindOf == 'ss':
					# search through the pages transcripts and print out results
					self.searchSimple(query, 'ss')
				elif kindOf == 'v':
					self.searchSimple(query, 'v')
				elif kindOf == 'd':
					self.searchSimple(query, 'd')
				count += 1

			elif command == 'h':
				self.printHelp()
				count += 1
			elif command == 'q':
				print ('bye!')
				print 
				keep_going = False
			else:
				print('Invalid Command. ("h" for help)')
				count += 1

	def searchSimple(self, query, out):
		'''
			Search in each page for case-insensitive query
		'''
		import simplejson, re
		# Get list of diaries
		diaryPages = self.walkDirectory(self.path, 'allPages') 
		print "Searching in "+str(len(diaryPages))+" ..." 
		totalFound = 0
		totalPages = 0
		vis = ''; tmp = ''
		details = ''
		for diaryPage in diaryPages:
			#print diaryPage.split('/')[2]
			if tmp != diaryPage.split('/')[2]:
				#print tmp
				vis += '\n'+diaryPage[9:]+'> '
				tmp = diaryPage.split('/')[2]
			data = simplejson.loads(open(diaryPage).read())
			text = data["field_transcription"]["und"][0]["safe_value"]
			result =  re.findall(query, text, re.IGNORECASE)
			if len(result) > 0:
				totalPages += 1
				totalFound += len(result)
				vis += '<'+str(len(result))+'>'
				# Details:
				pos = text.find(query)
				# set detail lentgh
				detail_len = 80
				details += '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
				details += diaryPage[9:]+'> ...'+text[pos-detail_len:pos]+'\033[1m\033[0;31m'+query+'\033[0m\033[39m'+text[pos+len(query):pos+len(query)+detail_len]
			else:
				vis += '.'
		if out == 'v':
			print vis
		elif out == 'd':
			print details
		print "- Total found: "+str(totalFound)+" times."
		print "- Found in "+str(totalPages)+" pages."

	def printHelp(self):
		print
		print ('Options:')
		print ('\tr : report about the data in ./Diaries directory')
		print ('\ts : search query in the data, and print out report of results ')
		print ('\t\tsub-menu search: ')
		print ('\t\tss: Simple report ')
		print ('\t\tv: with Visualization')
		print ('\t\td: with text Detail')
		
	def walkDirectory(self, path, output):
		''' Get the list of direcctories in pathDiaries '''
		# Number of DIaries
		dirs = []
		allPages = []
		report = ''
		for (dirpath, dirnames, filenames) in walk(path):
			dirs.extend(dirnames)
		ndiaries = str(len(dirs))
		report += "\tTotal Diaries: \t"+ndiaries
		# Total numer of pages
		files = []
		for dir in dirs:
			for (dirpath, dirnames, filenames) in walk(path+"/"+dir):
				files.extend(filenames)
				break
			for f in files:
				allPages.append(path+"/"+dir+"/"+f)
			files = []
		npages = str(len(allPages))
		report += "\tTotal Pages: \t"+npages
		# Number of pages per Diary (average)
		report += "\tPages/Diary: \t"+str(len(allPages)/len(dirs))

		## Output selector:
		if output == 'printReport':
			print report
		elif output == 'diariesList':
			return dirs
		elif output == 'allPages':
			return allPages
		else:
			print report

explorer = Explore()
explorer.console()

#path = "./Diaries"
#explorer.walkDirectory(path, 'allPages')
