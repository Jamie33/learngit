# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from lazadaVN.items import lazadaVNItem
from urllib.parse import urlencode
import re

class ShopeeSpider(Spider):
    name = 'lazada'
    allowed_domains = ['lazada.vn']
    start_urls = ["https://www.lazada.vn/trang-diem-mat/?spm=a2o4n.searchlistcategory.cate_4_1.1.46663876ChKfhm"]

    # def start_requests(self):
    #     data = {'spm':'a2o4n.searchlistcategory.breadcrumb.2.40643876XeEWix'}
    #     base_url = "https://www.lazada.vn/cham-soc-suc-khoe-va-lam-dep/?"
    #     for page in range(1,self.settings.get('MAX_PAGE')+1):
    #         data['page'] = page
    #         params = urlencode(data)
    #         url = base_url + params
    #         yield Request(url, self.parse)

    def parse(self, response):
        products = response.xpath('//div[@class="c2prKC"]')
        for product in products:
            item = ShopeetwItem()
            item['pro_name'] = product.xpath('.//div[@class="c16H9d"]//text()').extract_first()
            price_info = product.xpath('.//span[@class="c13VH6"]//text()').extract_first()
            price = re.sub(r'₫|\.','',price_info)
            item['price'] = price
            review_info = product.xpath('.//span[@class="c3XbGJ"]//text()').extract_first()
            if review_info:
                review_num = re.search(r'\d+',review_info).group(0)
            item['review_num'] = int(review_num)
            item['pro_url'] = 'https:'+product.xpath('.//div[@class="c16H9d"]//a/@href').extract_first()
            yield item