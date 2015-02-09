from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from InformationR.items import InformationrIR

class InformationResearch(BaseSpider):
    '''
    This class gets the list of URLs for each issue
    '''
    name = "ir"
    allowed_domains = ["informationr.net/"]
    start_urls = [
        "http://informationr.net/ir/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        issuesList = hxs.select('//table/tbody/tr/td/table/tbody/tr/td/a/@href').extract()
        items = []
        count = 0
        for issue in issuesList:
        	count += 1
        	item = InformationrIR()
        	link = issue
		item['link'] = "http://informationr.net/ir/"+issue
		items.append(item)
        return items

