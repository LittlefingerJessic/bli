# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
from itemadapter import ItemAdapter
class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db):
        self.mongouri=mongo_uri
        self.mongodb=mongo_db
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri= crawler.settings.get('MONGO_URI'),
            mongo_db= crawler.settings.get('MONGO_DB')
        )
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongouri)
        self.db=self.client[self.mongodb]
    def process_item(self, item, spider):
        name=item.__class__.__name__
        self.db[name].insert(dict(item))
        return item
    def close_spider(self,spider):
        self.client.close()