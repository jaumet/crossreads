# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class WWIDiaries(Item):
    shortLink = Field()
    #pageUrl = Field()
    #pageImage = Field()
    pass

class WWIDiariesToPages(Item):
    pageUrl = Field()
    #pageUrl = Field()
    diariesDigitalOrderNumber = Field()
    pass

class WWIGetPagesFromDiary(Item):
    pageUrl = Field()
    #pageUrl = Field()
    transcription = Field()
    pass



