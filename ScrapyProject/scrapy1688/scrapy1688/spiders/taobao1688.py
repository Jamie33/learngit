# -*- coding: utf-8 -*-
from scrapy import Request, Spider, FormRequest
from scrapy1688.items import Scrapy1688Item
import re,json

class Taobao1688Spider(Spider):
    name = 'taobao1688'
    allowed_domains = ['1688.com','test.amazing.com']
    start_urls = ['https://detail.1688.com/offer/41571718696.html?spm=b26110380.sw1688.mof001/.1.574e396c2GXK4G']

    def parse(self, response):
        products = response.xpath('//div[@class="cate1688-offer b2b-ocms-fusion-comp"]')
        for product in products:
            item = Scrapy1688Item()
            item['pro_name'] = product.xpath('.//div[@class="offer-title"]//text()').extract_first()
            item['price'] = float(product.xpath('.//span[@class="price-num"]//text()').extract_first())
            item['main_pic'] = product.xpath('.//div[@class="offer-img"]//img/@src').extract_first()
            item['pro_url'] = product.xpath('./a/@href').extract_first()
            item['pro_id'] = re.search(r'offer/(\d+).html?',item['pro_url']).group(1)
            sold_info = product.xpath('.//div[@class="alife-bc-uc-textLine offer-vol single-line"]//text()').extract_first()
            item['sold_num'] = re.search(r'成交(.+)件', sold_info).group(1)
            if '万' in item['sold_num']:
                item['sold_num'] = float(re.search(r'(.+)万', item['sold_num']).group(1))
                if item['sold_num'] >= 0.3:
                    if item['price'] <= 20:
                        yield item


