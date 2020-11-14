import json
import requests
import scrapy
from scrapy import Request,Spider
import re
from bli.items import BiliItem
class BlSpider(scrapy.Spider):
    name = 'bl'
    allowed_domains = ['space.bilibili.com/']
    start_urls = ['http ://space.bilibili.com/ ']
    def start_requests(self):
        for n in range(0,700000000):
            self_url = f'https://api.bilibili.com/x/space/acc/info?mid={n}&jsonp=jsonp'.format(n)
            yield Request(self_url,callback=self.parse_self)
    def parse_self(self,response):
        result=response.text
        item=BiliItem()
        pattern=re.compile('"name":"(.*?)".*?"sex":"(.*?)".*?"face":"(.*?)".*?"sign":"(.*?)".*?"jointime":(.*?),.*?"birthday":"(.*?)".*?"title":"(.*?)".*?"url":"(.*?)"',re.S)
        need=re.findall(pattern,result)
        for x in need:
            item['name'] = x[0]
            item['birthday'] = x[5]
            item['url'] = x[7]
            item['face'] = x[2]
            item['title'] = x[6]
            item['sex'] = x[1]
            item['sign'] = x[3]
            item['jointime'] = x[4]
        yield item
        print(type(item))