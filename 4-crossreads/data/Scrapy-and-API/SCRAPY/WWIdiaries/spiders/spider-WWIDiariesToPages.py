from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from WWIdiaries.items import WDiariesToPages

class GetDiariesURLs(BaseSpider):
    '''
    This class gets the list of URLs for each issue
    '''
    name = "WWIDiariesToPages"
    allowed_domains = ["transcripts.sl.nsw.gov.au/"]
    start_urls = [
        "http://transcripts.sl.nsw.gov.au/node/100307",
        "http://transcripts.sl.nsw.gov.au/node/100325",
        "http://transcripts.sl.nsw.gov.au/node/100324"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        mypageUrl = ''   
        items = []

	item = WWIDiariesToPages()
	item['pageUrl'] = str(response)[-7:][:-1]
	item['diariesDigitalOrderNumber'] = hxs.select('//p/text()').extract()[1]
	
	#EXAMPLES:
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
