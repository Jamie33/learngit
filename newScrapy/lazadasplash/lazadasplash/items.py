# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class LazadasplashItem(Item):
    collection = 'products_0701'
    title = Field()
    url = Field()
    image_urls = Field()
    price = Field()
    spec_images = Field()
    main_pic = Field()
    pro_des = Field()
    des_images = Field()
    category = Field()

