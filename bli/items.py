# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class BiliItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    birthday=Field()
    face=Field()
    jointime=Field()
    url=Field()
    name=Field()
    title=Field()
    sex=Field()
    sign=Field()