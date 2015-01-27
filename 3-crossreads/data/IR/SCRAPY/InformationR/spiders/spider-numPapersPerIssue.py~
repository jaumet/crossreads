from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import re

from InformationR.items import InformationrNumPapersPerIssue

class InformationResearch(BaseSpider):
    '''
    This class gets the list URLs of papers taken from each issue page.
    '''
    name = "numpapers"
    allowed_domains = ["informationr.net/"]
    start_urls = [
        "http://informationr.net/ir/18-1/infres181.html",
	"http://informationr.net/ir/18-2/infres182.html",
	"http://informationr.net/ir/17-1/infres171.html",
	"http://informationr.net/ir/17-2/infres172.html",
	"http://informationr.net/ir/17-3/infres173.html",
	"http://informationr.net/ir/17-4/infres174.html",
	"http://informationr.net/ir/16-1/infres161.html",
	"http://informationr.net/ir/16-2/infres162.html",
	"http://informationr.net/ir/16-3/infres163.html",
	"http://informationr.net/ir/16-4/infres164.html",
	"http://informationr.net/ir/15-1/infres151.html",
	"http://informationr.net/ir/15-2/infres152.html",
	"http://informationr.net/ir/15-3/infres153.html",
	"http://informationr.net/ir/15-4/infres154.html",
	"http://informationr.net/ir/14-1/infres141.html",
	"http://informationr.net/ir/14-2/infres142.html",
	"http://informationr.net/ir/14-3/infres143.html",
	"http://informationr.net/ir/14-4/infres144.html",
	"http://informationr.net/ir/13-1/infres131.html",
	"http://informationr.net/ir/13-2/infres132.html",
	"http://informationr.net/ir/13-3/infres133.html",
	"http://informationr.net/ir/13-4/infres134.html",
	"http://informationr.net/ir/12-1/infres121.html",
	"http://informationr.net/ir/12-2/infres122.html",
	"http://informationr.net/ir/12-3/infres123.html",
	"http://informationr.net/ir/12-4/infres124.html",
	"http://informationr.net/ir/11-1/infres111.html",
	"http://informationr.net/ir/11-2/infres112.html",
	"http://informationr.net/ir/11-3/infres113.html",
	"http://informationr.net/ir/11-4/infres114.html",
	"http://informationr.net/ir/10-1/infres101.html",
	"http://informationr.net/ir/10-2/infres102.html",
	"http://informationr.net/ir/10-3/infres103.html",
	"http://informationr.net/ir/10-4/infres104.html",
	"http://informationr.net/ir/9-1/infres91.html",
	"http://informationr.net/ir/9-2/infres92.html",
	"http://informationr.net/ir/9-3/infres93.html",
	"http://informationr.net/ir/9-4/infres94.html",
	"http://informationr.net/ir/8-1/infres81.html",
	"http://informationr.net/ir/8-2/infres82.html",
	"http://informationr.net/ir/8-3/infres83.html",
	"http://informationr.net/ir/8-4/infres84.html",
	"http://informationr.net/ir/7-1/infres71.html",
	"http://informationr.net/ir/7-2/infres72.html",
	"http://informationr.net/ir/7-3/infres73.html",
	"http://informationr.net/ir/7-4/infres74.html",
	"http://informationr.net/ir/6-1/infres61.html",
	"http://informationr.net/ir/6-2/infres62.html",
	"http://informationr.net/ir/6-3/infres63.html",
	"http://informationr.net/ir/6-4/infres64.html",
	"http://informationr.net/ir/5-1/infres51.html",
	"http://informationr.net/ir/5-2/infres52.html",
	"http://informationr.net/ir/5-3/infres53.html",
	"http://informationr.net/ir/5-4/infres54.html",
	"http://informationr.net/ir/4-1/infres41.html",
	"http://informationr.net/ir/4-2/infres42.html",
	"http://informationr.net/ir/4-3/infres43.html",
	"http://informationr.net/ir/4-4/infres44.html",
	"http://informationr.net/ir/3-1/infres31.html",
	"http://informationr.net/ir/3-2/infres32.html",
	"http://informationr.net/ir/3-3/infres33.html",
	"http://informationr.net/ir/3-4/infres34.html",
	"http://informationr.net/ir/2-1/infres21.html",
	"http://informationr.net/ir/2-2/infres22.html",
	"http://informationr.net/ir/2-3/infres23.html",
	"http://informationr.net/ir/2-4/infres24.html",
	"http://informationr.net/ir/1-1/infres.html",
	"http://informationr.net/ir/1-2/infres2.html",
	"http://informationr.net/ir/1-3/infres3.html"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
      
        items = []
	p = re.compile('(^http\:\/\/informationr\.net\/ir\/(.*)\-(.*)\/).*\.html$')
	pp = p.findall(response.url)
	myurl = pp[0][0]
	myvolume = int(pp[0][1])
	myissue = int(pp[0][2])
			
	item = InformationrNumPapersPerIssue()
	#item['title'] = issue.select('a/text()').extract()
	#item['authors'] = issue.select('text()').re(re.compile('(^\w.*|\ .*)'))
	#item['link'] = response.url+str(issue.select('a[contains(@href, "paper")]').extract()) 
	item['volume'] = myvolume
	item['issue'] = myissue
	
	#18-1: len(hxs.select('//div[@id="content_inner"]/h5/a[contains(@href, "paper")]'))
	# 1-3 to 13-4: len(hxs.select('//td/h4/a[contains(@href, "paper")]'))
	if (int(myvolume)>13):
		item['numpapers'] = len(hxs.select('//div[@id="content_inner"]/h5/a[contains(@href, "paper")]'))
	else: 
		item['numpapers'] = len(hxs.select('//td/h4/a[contains(@href, "paper")]'))
	items.append(item)

	return items
