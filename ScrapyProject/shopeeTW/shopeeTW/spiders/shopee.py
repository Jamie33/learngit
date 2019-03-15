# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from shopeeTW.items import ShopeetwItem


class ShopeeSpider(Spider):
    name = 'shopee'
    allowed_domains = ['shopee.tw']
    #start_urls = ["https://shopee.co.id/Sepatu-Pria-cat.35?page=0&sortBy=sales"]
    start_urls = ["https://shopee.tw/女生配件-cat.2580?page=0&sortBy=sales"]

    def parse(self, response):
        products = response.xpath('//div[@id="main"]//div[@class="shopee-search-item-result"]//div[contains(@class, "col-xs-2-4")]')
        for product in products:
            item = ShopeetwItem()
            #item['category'] = 
            #item['class_name'] = 
            item['pro_name'] = product.xpath('.//div[@class="_1JAmkB"]//text()').extract_first()
            #item['price_range'] = ''.join(product.xpath('.//div[contains(@class, "price")]//text()').extract()).stri
            #item['price_min'] = product.xpath('.//div[contains(@class, "deal-cnt")]//text()').extract_first()
            #item['price_max'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()
            #item['monthly_sales'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()
            #item['pro_url'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()
            #item['pic_url'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()
            yield item