from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from InformationR.items import WWIDiariesToPages

class InformationResearch(BaseSpider):
    '''
    This class gets the list of URLs for each issue
    '''
    name = "WWIDiariesToPages"
    allowed_domains = ["transcripts.sl.nsw.gov.au/"]
    start_urlsTEST = [
        "http://transcripts.sl.nsw.gov.au/node/100307",
        "http://transcripts.sl.nsw.gov.au/node/100325",
        "http://transcripts.sl.nsw.gov.au/node/100324"
    ]
    start_urls = [
    	"http://transcripts.sl.nsw.gov.au/node/100307",
			"http://transcripts.sl.nsw.gov.au/node/100325",
			"http://transcripts.sl.nsw.gov.au/node/100324",
			"http://transcripts.sl.nsw.gov.au/node/100312",
			"http://transcripts.sl.nsw.gov.au/node/100325",
			"http://transcripts.sl.nsw.gov.au/node/100309",
			"http://transcripts.sl.nsw.gov.au/node/100307",
			"http://transcripts.sl.nsw.gov.au/node/100324",
			"http://transcripts.sl.nsw.gov.au/node/100308",
			"http://transcripts.sl.nsw.gov.au/node/100318",
			"http://transcripts.sl.nsw.gov.au/node/100322",
			"http://transcripts.sl.nsw.gov.au/node/100311",
			"http://transcripts.sl.nsw.gov.au/node/100302",
			"http://transcripts.sl.nsw.gov.au/node/100306",
			"http://transcripts.sl.nsw.gov.au/node/100310",
			"http://transcripts.sl.nsw.gov.au/node/100313",
			"http://transcripts.sl.nsw.gov.au/node/100315",
			"http://transcripts.sl.nsw.gov.au/node/100319",
			"http://transcripts.sl.nsw.gov.au/node/100321",
			"http://transcripts.sl.nsw.gov.au/node/100316",
			"http://transcripts.sl.nsw.gov.au/node/100304",
			"http://transcripts.sl.nsw.gov.au/node/100327",
			"http://transcripts.sl.nsw.gov.au/node/100314",
			"http://transcripts.sl.nsw.gov.au/node/100317",
			"http://transcripts.sl.nsw.gov.au/node/100326",
			"http://transcripts.sl.nsw.gov.au/node/100323",
			"http://transcripts.sl.nsw.gov.au/node/100320",
			"http://transcripts.sl.nsw.gov.au/node/100303",
			"http://transcripts.sl.nsw.gov.au/node/100395",
			"http://transcripts.sl.nsw.gov.au/node/100396",
			"http://transcripts.sl.nsw.gov.au/node/100382",
			"http://transcripts.sl.nsw.gov.au/node/100371",
			"http://transcripts.sl.nsw.gov.au/node/100384",
			"http://transcripts.sl.nsw.gov.au/node/100383",
			"http://transcripts.sl.nsw.gov.au/node/100385",
			"http://transcripts.sl.nsw.gov.au/node/115137",
			"http://transcripts.sl.nsw.gov.au/node/100301",
			"http://transcripts.sl.nsw.gov.au/node/100275",
			"http://transcripts.sl.nsw.gov.au/node/100404",
			"http://transcripts.sl.nsw.gov.au/node/100280",
			"http://transcripts.sl.nsw.gov.au/node/100287",
			"http://transcripts.sl.nsw.gov.au/node/100285",
			"http://transcripts.sl.nsw.gov.au/node/100282",
			"http://transcripts.sl.nsw.gov.au/node/100276",
			"http://transcripts.sl.nsw.gov.au/node/100277",
			"http://transcripts.sl.nsw.gov.au/node/100411",
			"http://transcripts.sl.nsw.gov.au/node/100283",
			"http://transcripts.sl.nsw.gov.au/node/100278",
			"http://transcripts.sl.nsw.gov.au/node/100360",
			"http://transcripts.sl.nsw.gov.au/node/100361",
			"http://transcripts.sl.nsw.gov.au/node/100279",
			"http://transcripts.sl.nsw.gov.au/node/100359",
			"http://transcripts.sl.nsw.gov.au/node/182325",
			"http://transcripts.sl.nsw.gov.au/node/100331",
			"http://transcripts.sl.nsw.gov.au/node/100334",
			"http://transcripts.sl.nsw.gov.au/node/100330",
			"http://transcripts.sl.nsw.gov.au/node/100367",
			"http://transcripts.sl.nsw.gov.au/node/100332",
			"http://transcripts.sl.nsw.gov.au/node/100335",
			"http://transcripts.sl.nsw.gov.au/node/100388",
			"http://transcripts.sl.nsw.gov.au/node/100292",
			"http://transcripts.sl.nsw.gov.au/node/100397",
			"http://transcripts.sl.nsw.gov.au/node/100290",
			"http://transcripts.sl.nsw.gov.au/node/100366",
			"http://transcripts.sl.nsw.gov.au/node/100365",
			"http://transcripts.sl.nsw.gov.au/node/100362",
			"http://transcripts.sl.nsw.gov.au/node/100291",
			"http://transcripts.sl.nsw.gov.au/node/100350",
			"http://transcripts.sl.nsw.gov.au/node/100344",
			"http://transcripts.sl.nsw.gov.au/node/100358",
			"http://transcripts.sl.nsw.gov.au/node/100343",
			"http://transcripts.sl.nsw.gov.au/node/100342",
			"http://transcripts.sl.nsw.gov.au/node/100341",
			"http://transcripts.sl.nsw.gov.au/node/100295",
			"http://transcripts.sl.nsw.gov.au/node/100364",
			"http://transcripts.sl.nsw.gov.au/node/100363",
			"http://transcripts.sl.nsw.gov.au/node/100372",
			"http://transcripts.sl.nsw.gov.au/node/100377",
			"http://transcripts.sl.nsw.gov.au/node/100380",
			"http://transcripts.sl.nsw.gov.au/node/100378",
			"http://transcripts.sl.nsw.gov.au/node/100405",
			"http://transcripts.sl.nsw.gov.au/node/100379",
			"http://transcripts.sl.nsw.gov.au/node/100288",
			"http://transcripts.sl.nsw.gov.au/node/100389",
			"http://transcripts.sl.nsw.gov.au/node/100337",
			"http://transcripts.sl.nsw.gov.au/node/100338",
			"http://transcripts.sl.nsw.gov.au/node/100390",
			"http://transcripts.sl.nsw.gov.au/node/100375",
			"http://transcripts.sl.nsw.gov.au/node/100398",
			"http://transcripts.sl.nsw.gov.au/node/100289",
			"http://transcripts.sl.nsw.gov.au/node/100381",
			"http://transcripts.sl.nsw.gov.au/node/100374",
			"http://transcripts.sl.nsw.gov.au/node/100376",
			"http://transcripts.sl.nsw.gov.au/node/100368",
			"http://transcripts.sl.nsw.gov.au/node/100336",
			"http://transcripts.sl.nsw.gov.au/node/100373",
			"http://transcripts.sl.nsw.gov.au/node/100387",
			"http://transcripts.sl.nsw.gov.au/node/100351",
			"http://transcripts.sl.nsw.gov.au/node/100401",
			"http://transcripts.sl.nsw.gov.au/node/100402",
			"http://transcripts.sl.nsw.gov.au/node/100403",
			"http://transcripts.sl.nsw.gov.au/node/100399",
			"http://transcripts.sl.nsw.gov.au/node/100386",
			"http://transcripts.sl.nsw.gov.au/node/100400",
			"http://transcripts.sl.nsw.gov.au/node/100370",
			"http://transcripts.sl.nsw.gov.au/node/100356",
			"http://transcripts.sl.nsw.gov.au/node/100369",
			"http://transcripts.sl.nsw.gov.au/node/100328",
			"http://transcripts.sl.nsw.gov.au/node/100394",
			"http://transcripts.sl.nsw.gov.au/node/100357",
			"http://transcripts.sl.nsw.gov.au/node/100391",
			"http://transcripts.sl.nsw.gov.au/node/100339",
			"http://transcripts.sl.nsw.gov.au/node/100392",
			"http://transcripts.sl.nsw.gov.au/node/100329",
			"http://transcripts.sl.nsw.gov.au/node/100352",
			"http://transcripts.sl.nsw.gov.au/node/100353",
			"http://transcripts.sl.nsw.gov.au/node/100355",
			"http://transcripts.sl.nsw.gov.au/node/100408",
			"http://transcripts.sl.nsw.gov.au/node/100354",
			"http://transcripts.sl.nsw.gov.au/node/100409",
			"http://transcripts.sl.nsw.gov.au/node/100407",
			"http://transcripts.sl.nsw.gov.au/node/100393",
			"http://transcripts.sl.nsw.gov.au/node/100410",
			"http://transcripts.sl.nsw.gov.au/node/100299",
			"http://transcripts.sl.nsw.gov.au/node/100300",
			"http://transcripts.sl.nsw.gov.au/node/100406",
			"http://transcripts.sl.nsw.gov.au/node/100346",
			"http://transcripts.sl.nsw.gov.au/node/100347",
			"http://transcripts.sl.nsw.gov.au/node/100345",
			"http://transcripts.sl.nsw.gov.au/node/100340",
			"http://transcripts.sl.nstr(response)[-7:][:-1]sw.gov.au/node/100348",
			"http://transcripts.sl.nsw.gov.au/node/100349"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        mypageUrl = ''   
        items = []

	item = WWIDiariesToPages()
	item['pageUrl'] = str(response)[-7:][:-1]
	item['diariesDigitalOrderNumber'] = hxs.select('//p/text()').extract()[1]
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
