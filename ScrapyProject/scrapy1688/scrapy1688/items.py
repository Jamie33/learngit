# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Scrapy1688Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'Taobao1688'
    pro_name = Field()
    pro_id = Field()
    price = Field()
    main_pic = Field()
    pro_url = Field()
    sold_num = Field()
    image_urls = Field()