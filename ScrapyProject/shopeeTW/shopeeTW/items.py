# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ShopeetwItem(Item):
    # define the fields for your item here like:

    collection = 'cosmetics'
    pro_name = Field()
    price = Field()
    review_num = Field()
    pro_url = Field()


    #category = Field()
    #class_name = Field()
    #price_range = Field()
    #price_min = Field()
    #price_max = Field()
    #monthly_sales = Field()
    #pro_url = Field()
    #pic_url = Field()
