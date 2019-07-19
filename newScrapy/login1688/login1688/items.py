# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class Login1688Item(Item):
    collection = 'products_1688_0711'
    title = Field()
    url = Field()
    image_urls = Field()
    price = Field()
    spec_images = Field()
    pro_id = Field()
    main_pic = Field()
    pro_des = Field()
    des_images = Field()
    category = Field()
