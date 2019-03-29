# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from tiki.items import TikiItem
from urllib.parse import urlencode
import re


class TikivnSpider(Spider):
    name = 'tikiVN'
    allowed_domains = ['tiki.vn']

    def start_requests(self):
        base_url = 'https://tiki.vn/lam-dep-suc-khoe/c1520?'
        data = {'src':'mega-menu','order':'top_seller'}
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            data['page'] = page
            params = urlencode(data)
            url = base_url + params
            yield Request(url,self.parse)

    def parse(self, response):
        products = response.xpath('//div[@class="product-item    "]')
        for product in products:
            item = TikiItem()
            item['pro_name'] = product.xpath('.//span[@class="title"]//text()').extract_first().strip()
            price_info = product.xpath('.//span[@class="final-price"]//text()').extract_first()
            price = re.sub(r'₫|/.','',price_info).strip()
            item['price'] = price
            review_info = product.xpath('.//p[@class="review"]//text()').extract_first()
            if review_info:
                review_num = re.search(r'\d+',review_info).group(0)
            item['review_num'] = int(review_num)
            item['pro_url'] = 'https:'+product.xpath('./a/@href').extract_first()
            yield item
