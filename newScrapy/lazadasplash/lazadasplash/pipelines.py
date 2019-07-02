# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo,requests,json

class LazadasplashPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()

class uploaditemPipeline(object):

    '''
    web_from=参数代表：
    nindia  之前的印度站
    tw  台湾站
    mee  meesho越南站
    mee_id  meesho印尼站
    yunji  tinisho
    '''

    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.post_url = 'http://test.amazing.com/api/goods/insertgoods?web_from=yunji'

    def process_item(self,item,spider):
        post_data = {
            "name":item['title'],
            "id":item['pro_id'],
            "price":item['price'],
            "main_pic":item['main_pic'],
            "url":item['url'],
            "images":item['image_urls'],
            "description": item['pro_des'],
            'des_images':item['des_images'],
            "category":item['category'],
            "sales": 0,
            "review": 0,
        }
        print('上传成功')
        return requests.post(url=self.post_url, data=json. dumps(post_data), headers=self.headers)