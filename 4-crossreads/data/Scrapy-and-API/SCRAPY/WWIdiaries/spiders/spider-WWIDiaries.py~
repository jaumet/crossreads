from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from InformationR.items import WWIDiaries

class InformationResearch(BaseSpider):
    '''
    This class gets the list of URLs for each issue
    '''
    name = "WWIDiaries"
    allowed_domains = ["transcripts.sl.nsw.gov.au/"]
    start_urls = [
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-narrative-27-august-28-september-1915",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-1-march-11-april-1917",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-1-26-august-1915",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-11-march-6-june-1919",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-12-april-11-may-1917",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-12-may-20-july-1917",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-16-july-27-august-1918",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-16-october-21-november-1917",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-17-march-8-july-1916",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-20-september-15-october-1917",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-21-december-1916-28-february-1917",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-21-july-19-september-1917",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-22-november-1917-28-january-1918",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-23-august-30-october-1918",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-23-december-1918-10-march-1919",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-23-march-24-april-1918",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-25-april-30-may-1918",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-26-july-11-september-1916",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-27-august-28-september-1915",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-28-september-11-december-1915",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-29-january-22-march-1918",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-31-may-15-july-1918",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-31-october-22-december-1918",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-7-june-11-september-1919",
        "http://transcripts.sl.nsw.gov.au/content/arl-wiltshire-diary-8-26-july-1916",
        "http://transcripts.sl.nsw.gov.au/content/alan-langley-pryce-diary-21-december-1914-27-april-1915",
        "http://transcripts.sl.nsw.gov.au/content/alan-langley-pryce-letters-13-august-1914-3-april-1915",
        "http://transcripts.sl.nsw.gov.au/content/alfred-bray-diary-16-august-1915-23-august-1916",
        "http://transcripts.sl.nsw.gov.au/content/alfred-bray-diary-19-june-1918-8-february-1919",
        "http://transcripts.sl.nsw.gov.au/content/alfred-bray-diary-23-august-1916-19-august-1917",
        "http://transcripts.sl.nsw.gov.au/content/alfred-bray-diary-august-1917-20-june-1918",
        "http://transcripts.sl.nsw.gov.au/content/alfred-grinyer-diary-29-january-1917-3-january-1918",
        "http://transcripts.sl.nsw.gov.au/content/alfred-grinyer-diary-29-march-1916-28-january-1917",
        "http://transcripts.sl.nsw.gov.au/content/alfred-prichard-kington-morris-diary-17-october-1915-11-may-1916",
        "http://transcripts.sl.nsw.gov.au/content/ambrose-ohare-war-diary-12-august-1914-15-october-1918",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-14-april-1917-19-may-1917",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-15-december-1918-26-january-1919",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-20-june-30-september-1918",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-21-september-1917-4-march-1918",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-23-july-1916-2-september-1916",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-3-january-1917-26-march-1917",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-3-september-3-october-1916",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-4-october-1916-7-november-1916",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-5-march-12-april-1918",
        "http://transcripts.sl.nsw.gov.au/content/archibald-barwick-diary-7-november-1916-2-january-1917",
        "http://transcripts.sl.nsw.gov.au/content/armstrong-family-papers-1918",
        "http://transcripts.sl.nsw.gov.au/content/arthur-john-moore-diary-1-january-1918-january-7-1919",
        "http://transcripts.sl.nsw.gov.au/content/arthur-john-moore-diary-11-november-1916-11-january-1918",
        "http://transcripts.sl.nsw.gov.au/content/arthur-john-moore-diary-9-november-1915-11-november-1916",
        "http://transcripts.sl.nsw.gov.au/content/australia-army-6th-battalion-order-book-3-september-1916-28-october-1916",
        "http://transcripts.sl.nsw.gov.au/content/bailey-narrative-life-aboard-australian-troopship-22-october-28-december-1918-ernest-bailey",
        "http://transcripts.sl.nsw.gov.au/content/benjamin-alfred-cohen-diary-1-march-23-june-1919",
        "http://transcripts.sl.nsw.gov.au/content/benjamin-alfred-cohen-diary-10-may-17-september-1917",
        "http://transcripts.sl.nsw.gov.au/content/benjamin-alfred-cohen-diary-20-september-20-december-1917",
        "http://transcripts.sl.nsw.gov.au/content/benjamin-alfred-cohen-diary-22-december-1917-10-june-1918",
        "http://transcripts.sl.nsw.gov.au/content/benjamin-alfred-cohen-diary-28-june-12-august-1919",
        "http://transcripts.sl.nsw.gov.au/content/cameron-robertson-war-diary-18-october-20-december-1914",
        "http://transcripts.sl.nsw.gov.au/content/cameron-robertson-war-diary-21-december-1914-16-december-1916",
        "http://transcripts.sl.nsw.gov.au/content/charles-gifford-pryce-letters-28-october-1915-5-september-1918",
        "http://transcripts.sl.nsw.gov.au/content/charles-monaghan-diary-1916",
        "http://transcripts.sl.nsw.gov.au/content/charles-monaghan-diary-1917",
        "http://transcripts.sl.nsw.gov.au/content/charles-monaghan-letter-his-wife-emma-july-21-1920",
        "http://transcripts.sl.nsw.gov.au/content/clarke-war-diary-15-august-1916-14-december-1916",
        "http://transcripts.sl.nsw.gov.au/content/clarke-war-diary-20-may-1916-13-august-1916",
        "http://transcripts.sl.nsw.gov.au/content/clifford-m-geddes-diary-1-august-5-september-1918",
        "http://transcripts.sl.nsw.gov.au/content/crooks-war-diary-11-february-1915-24-may-1918",
        "http://transcripts.sl.nsw.gov.au/content/dene-b-fry-diary-21-august-1916-26-january-1917",
        "http://transcripts.sl.nsw.gov.au/content/donald-e-macdonald-diary-1-february-12-may-1916",
        "http://transcripts.sl.nsw.gov.au/content/donald-e-macdonald-diary-12-may-13-september-1916",
        "http://transcripts.sl.nsw.gov.au/content/donald-e-macdonald-diary-12-may-18-december-1915",
        "http://transcripts.sl.nsw.gov.au/content/donald-e-macdonald-diary-18-december-1915-6-january-1916",
        "http://transcripts.sl.nsw.gov.au/content/frank-hurley-war-diary-21-august-28-october-1917",
        "http://transcripts.sl.nsw.gov.au/content/frank-hurley-war-diary-24-january-13-august-1918",
        "http://transcripts.sl.nsw.gov.au/content/frank-hurley-war-diary-28-october-1917-24-january-1918",
        "http://transcripts.sl.nsw.gov.au/content/frank-smith-diary-8-july-1917-26-february-1919",
        "http://transcripts.sl.nsw.gov.au/content/geoffrey-rose-memoir-based-war-diaries-and-letters-18-august-1919-3-september",
        "http://transcripts.sl.nsw.gov.au/content/george-edward-edmondson-diary-11-may-17-september-1916",
        "http://transcripts.sl.nsw.gov.au/content/george-edward-edmondson-diary-13-july-1917-29-march-1918",
        "http://transcripts.sl.nsw.gov.au/content/george-edward-edmondson-diary-18-september-8-december-1916",
        "http://transcripts.sl.nsw.gov.au/content/george-edward-edmondson-diary-9-december-1916-12-july-1917",
        "http://transcripts.sl.nsw.gov.au/content/george-edward-edmondson-papers-1915",
        "http://transcripts.sl.nsw.gov.au/content/h-v-berry-diary-14-june-1915-27-may-1916",
        "http://transcripts.sl.nsw.gov.au/content/h-v-berry-diary-29-may-1916-5-may-1918",
        "http://transcripts.sl.nsw.gov.au/content/henry-joseph-parsons-war-diary-1-july-1916-30-april-1918",
        "http://transcripts.sl.nsw.gov.au/content/henry-joseph-parsons-war-diary-1-june-2-september-1919",
        "http://transcripts.sl.nsw.gov.au/content/henry-joseph-parsons-war-diary-1-may-1918-31-may-1919",
        "http://transcripts.sl.nsw.gov.au/content/henry-weston-pryce-diary-14-july-1916-1917",
        "http://transcripts.sl.nsw.gov.au/content/jack-sommers-war-letters-and-verses-1914-1916",
        "http://transcripts.sl.nsw.gov.au/content/james-mckenzie-diary-19-september-1917-20-september-1918",
        "http://transcripts.sl.nsw.gov.au/content/james-mckenzie-diary-21-january-1916-19-september-1917",
        "http://transcripts.sl.nsw.gov.au/content/james-mckenzie-diary-21-september-5-december-1918",
        "http://transcripts.sl.nsw.gov.au/content/james-mckenzie-diary-5-july-1915-21-january-1916",
        "http://transcripts.sl.nsw.gov.au/content/james-mckenzie-diary-8-october-1914-4-july-1915",
        "http://transcripts.sl.nsw.gov.au/content/john-h-wheat-narrative-ca-1914-1918",
        "http://transcripts.sl.nsw.gov.au/content/john-h-wheat-papers-ca-1917-1918",
        "http://transcripts.sl.nsw.gov.au/content/john-joyce-diary-10-june-31-july-1916",
        "http://transcripts.sl.nsw.gov.au/content/john-owen-maddox-diary-1-january-31-december-1917",
        "http://transcripts.sl.nsw.gov.au/content/john-owen-maddox-diary-1-january-31-december-1918",
        "http://transcripts.sl.nsw.gov.au/content/john-owen-maddox-diary-2-january-11-june-1919",
        "http://transcripts.sl.nsw.gov.au/content/john-owen-maddox-diary-2-october-1916-20-march-1917",
        "http://transcripts.sl.nsw.gov.au/content/john-owen-maddox-diary-20-september-1915-21-october-1916",
        "http://transcripts.sl.nsw.gov.au/content/joseph-pye-diary-3-december-1915-17-february-1919-and-diary-5th-australian-field-bakery-5",
        "http://transcripts.sl.nsw.gov.au/content/leslie-morris-war-diary-6-january-1916-7-february-1919",
        "http://transcripts.sl.nsw.gov.au/content/leslie-morris-war-diary-8-july-1916-1-january-1918",
        "http://transcripts.sl.nsw.gov.au/content/leslie-william-sutherland-diary-1-january-13-december-1916",
        "http://transcripts.sl.nsw.gov.au/content/leslie-william-sutherland-order-book-1915",
        "http://transcripts.sl.nsw.gov.au/content/letters-smuggled-out-holsworthy-internment-camp-march-1919",
        "http://transcripts.sl.nsw.gov.au/content/norman-lee-pearce-world-war-i-diary-1-january-8-november-1916",
        "http://transcripts.sl.nsw.gov.au/content/oscar-melly-diaries-3-january-1917-12-july-1918",
        "http://transcripts.sl.nsw.gov.au/content/oscar-melly-letters-3-january-1917-27-may-1918",
        "http://transcripts.sl.nsw.gov.au/content/rhodes-diary-26-june-1915-4-april-1916-oscar-rhodes",
        "http://transcripts.sl.nsw.gov.au/content/robert-harris-diary-17-august-1914-3-january-1915",
        "http://transcripts.sl.nsw.gov.au/content/robert-harris-diary-24-july-1915-30-march-1916",
        "http://transcripts.sl.nsw.gov.au/content/robert-harris-diary-30-march-1916-28-march-1917",
        "http://transcripts.sl.nsw.gov.au/content/robert-harris-diary-4-april-1917-27-december-1918",
        "http://transcripts.sl.nsw.gov.au/content/rodda-war-diary-11-october-1918-29-april-1919",
        "http://transcripts.sl.nsw.gov.au/content/rodda-war-diary-20-august-1917-10-october-1918",
        "http://transcripts.sl.nsw.gov.au/content/rodda-war-diary-27-march-18-august-1917",
        "http://transcripts.sl.nsw.gov.au/content/scheidel-letters-received-during-world-war-12-october-1914-10-november-1919-lillian-scheidel",
        "http://transcripts.sl.nsw.gov.au/content/smyth-war-narrative-28-march-12-june-1919-mcvicker-smyth",
        "http://transcripts.sl.nsw.gov.au/content/t-j-cleary-diary-25-august-1918-5-july-1919",
        "http://transcripts.sl.nsw.gov.au/content/vick-letters-1916-1918-frederick-harold-vick",
        "http://transcripts.sl.nsw.gov.au/content/w-j-allsop-diary-1-january-31-december-1917",
        "http://transcripts.sl.nsw.gov.au/content/w-j-allsop-diary-23-november-1916-4-january-1917",
        "http://transcripts.sl.nsw.gov.au/content/william-burrell-diary-1-may-1917-15-june-1918",
        "http://transcripts.sl.nsw.gov.au/content/william-burrell-diary-16-june-1918-1-july-1919",
        "http://transcripts.sl.nsw.gov.au/content/william-burrell-diary-20-december-1915-12-november-1916",
        "http://transcripts.sl.nsw.gov.au/content/william-henry-nicholson-diary-1-january-1917-23-may-1918",
        "http://transcripts.sl.nsw.gov.au/content/william-henry-nicholson-diary-19-august-1915-31-december-1916"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        myShortLink = hxs.select('//link[contains(@rel, "shortlink")]/@href').extract()      
        items = []

	item = WWIDiaries()
	item['shortLink'] = myShortLink

	#p = re.compile('(^http\:\/\/informationr\.net\/ir\/(.*)\-(.*)\/).*\.html$')
	#pp = p.findall(response.url)
	#myurl = pp[0][0]
	#myvolume = int(pp[0][1])
	#myissue = int(pp[0][2])
	#item['title'] = issue.select('a/text()').extract()
	#item['authors'] = issue.select('text()').re(re.compile('(^\w.*|\ .*)'))
	#item['link'] = response.url+str(issue.select('a[contains(@href, "paper")]').extract()) 
	
	#18-1: len(hxs.select('//div[@id="content_inner"]/h5/a[contains(@href, "paper")]'))
	# 1-3 to 13-4: len(hxs.select('//td/h4/a[contains(@href, "paper")]'))
	#if (int(myvolume)>13):
	#	item['numpapers'] = len(hxs.select('//div[@id="content_inner"]/h5/a[contains(@href, "paper")]'))
	#else: 
	#	item['numpapers'] = len(hxs.select('//td/h4/a[contains(@href, "paper")]'))
	
	items.append(item)
	return items

'''
    def parseX(self, response):
        hxs = HtmlXPathSelector(response)
        issuesList = hxs.select('hxs.select('//ul/li/div/span/div/a/@href').extract()
        items = []
        count = 0
        for issue in issuesList:
        	count += 1
        	item = InformationrIR()
        	link = i
		item['link'] = "http://informationr.net/ir/"+issue
		items.append(item)
        return items
'''
