# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class DBmoiveSpiderPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['dbmoive']
        self.collection  = db.get_collection('Moives')

    def process_item(self, item, spider):
        result = self.collection.insert_one(item)
        return item
