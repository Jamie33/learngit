# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from tiki.items import TikiItem
from urllib.parse import urlencode
import re


class TikivnSpider(Spider):
    name = 'tikiVN'
    allowed_domains = ['sendo.vn']

    def start_requests(self):
        base_url = 'https://www.sendo.vn/my-pham/?'
        data = {'sortType':'norder_30_desc'}
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            data['p'] = page
            params = urlencode(data)
            url = base_url + params
            yield Request(url,self.parse,meta={'page': page})

    def parse(self, response):
        products = response.xpath('//div[@class="item_3AIm"]')
        i = 1
        page = response.meta['page']
        for product in products:
            item = TikiItem()
            item['page'] = page
            item['rank'] = i
            item['pro_name'] = product.xpath('.//span[@class="truncateMedium_3wDG"]//text()').extract_first()
            price_info = product.xpath('.//div[@class="productPrice_1TsR"]//text()').extract_first()
            price = re.sub(r'Đ|,','',price_info)
            item['price'] = price
            review_info = product.xpath('.//span[@class="ratingTotal_3cVd"]//text()').extract_first()
            if review_info:
                review_num = re.search(r'\d+',review_info).group(0)
            item['review_num'] = int(review_num)
            sales_info = product.xpath('.//span[@class="textSmall_2s-0"]//text()').extract_first()
            if 'k' in sales_info:
                item['sales'] = int(float(re.search(r'(.*)k',sales_info).group(1))*1000)
            else:
                item['sales'] = int(sales_info)
            item['pro_url'] = 'https://www.sendo.vn'+product.xpath('./a/@href').extract_first()
            i += 1
            yield item
