# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    cover_url = scrapy.Field()
    cover_url_path = scrapy.Field()
    date = scrapy.Field()
    vote_num = scrapy.Field()
    fav_num = scrapy.Field()
    comments = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
