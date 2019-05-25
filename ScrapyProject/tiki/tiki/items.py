# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TikiItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'health_0522_test_filter'
    pro_name = Field()
    pro_id = Field()
    price = Field()
    main_pic = Field()
    review_num = Field()
    pro_url = Field()
    image_urls = Field()
    rank = Field()
    page = Field()
