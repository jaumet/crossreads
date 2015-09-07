from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from WWIDiaries.items import WwidiariesItem



# -*- coding: utf-8 -*-


class WwidSpider(scrapy.Spider):
	name = "wwid"
	allowed_domains = ["transcripts.sl.nsw.gov.au"]
	start_urls = (
		'http://transcripts.sl.nsw.gov.au/',
	)

	def parse(self, response):
		# URL http://transcripts.sl.nsw.gov.au/project/World%20War%201%20Diaries?title=&sort_by=field_percentage_unlocked_value&sort_order=ASC&page=1
		# scrapy shell http://transcripts.sl.nsw.gov.au/project/World%20War%201%20Diaries?title=\&sort_by=field_percentage_unlocked_value&sort_order=ASC\&page=1
		hxs = HtmlXPathSelector(response)
		myShortLink = hxs.select('//link[contains(@rel, "shortlink")]/@href').extract()	  
		items = []

	item = WwidiariesItem()
	item['urlDiari'] = urlDiari

	items.append(item)
  	return items


