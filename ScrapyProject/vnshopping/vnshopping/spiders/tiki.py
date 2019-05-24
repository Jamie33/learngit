# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from vnshopping.items import VnshoppingItem
import re


class TikiSpider(CrawlSpider):
    name = 'tiki'
    allowed_domains = ['tiki.vn']
    start_urls = ['https://tiki.vn/lam-dep-suc-khoe/c20908?src=tree&brand_country=Trung%20Qu%E1%BB%91c']

    rules = (
        #Rule(LinkExtractor(allow=r'https://tiki.vn/.*', restrict_xpaths='//div[@class="product-box-list"]//div[contains(@class,"product-item")]'),callback='parse_detail'),
        Rule(LinkExtractor(allow=r'https://salt.tikicdn.com/.*',
                           restrict_xpaths='//span[@class="flx"]'),
             callback='parse_item')
    )

    def parse(self, response):
        products = response.xpath('//div[@class="product-box-list"]//div[contains(@class,"product-item")]')
        print('item number', len(products))
        rank = 1
        for product in products:
            item = VnshoppingItem()
            item['rank'] = rank
            item['pro_name'] = product.xpath('@data-title').extract_first()
            item['pro_id'] = product.xpath('@data-id').extract_first()
            item['pro_url'] = product.xpath('./a/@href').extract_first()
            price_info = product.xpath('.//span[@class="final-price"]/text()').extract_first().strip()
            price = re.sub(r'₫|\.','',price_info).strip()
            item['price'] = price
            review_info = product.xpath('.//p[@class="review"]/text()').extract_first()
            item['main_pic'] = re.sub(r'cache/\d+x\d+/', '', product.xpath('.//span[@class="image"]/img/@src').extract_first())
            if review_info:
                review_num = re.search(r'\d+',review_info).group(0)
                item['review_num'] = int(review_num)
            else:
                item['review_num'] = 0
            rank += 1
            yield item

    def parse_item(self, response):
        item = VnshoppingItem()
        item['image_urls'] = []
        img_tags = response.xpath('//span[@class="flx"]')
        if len(img_tags) == 0:
            img_link = response.xpath('//img[@id="product-magiczoom"]/@src').extract_first()
            image_url = re.sub(r'cache/\d+x\d+/', '', img_link)
            item['image_urls'].append(image_url)
        else:
            for img in img_tags:
                img_link = img.xpath('./img/@src').extract_first()
                image_url = re.sub(r'cache/\d+x\d+/','',img_link)
                item['image_urls'].append(image_url)
        yield item