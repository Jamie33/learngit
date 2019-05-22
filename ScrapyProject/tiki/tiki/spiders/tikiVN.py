# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from tiki.items import TikiItem
from urllib.parse import urlencode
import re,json
from logging import getLogger

class TikivnSpider(Spider):
    name = 'tikiVN'
    allowed_domains = ['tiki.vn','salt.tikicdn.com','test.amazing.com']

    def start_requests(self):
        base_url = 'https://tiki.vn/lam-dep-suc-khoe/c20908?'
        data = {'src': 'tree','brand_country':'Trung%20Quốc'}
        for page in range(1, self.settings.get('MAX_PAGE')+1):
            data['page'] = page
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse, meta = {'page':page})

    def parse(self, response):
        products = response.xpath('//div[@class="product-box-list"]//div[contains(@class,"product-item")]')
        print('item number',len(products))
        rank = 1
        for product in products:
            item = TikiItem()
            item['page'] = response.meta['page']
            item['rank'] = rank
            #item['pro_name'] = product.xpath('.//p[@class="title"]/text()').extract_first().strip()
            item['pro_name'] = product.xpath('@data-title').extract_first()
            item['pro_id'] = product.xpath('@data-id').extract_first()
            #item['pro_id'] = re.search(r'p(\d+).html',item['pro_url']).group(1)
            item['pro_url'] = product.xpath('./a/@href').extract_first()
            #item['pro_url'] = re.sub(r'src=.*', '', product.xpath('./a/@href').extract_first())
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
            yield Request(item['pro_url'], callback=self.parse_detail, meta={'item': item})

    def parse_detail(self,response):
        item = response.meta['item']
        item['image_urls'] = []
        #img_tags = response.xpath('//div[@class="product-feature-images vertical"]//span[@class="flx"]')
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
        # yield item

        headers = {'Content-Type': 'application/json'}
        post_url = 'http://test.amazing.com/api/goods/insertgoods?web_from=mee_id'
        
        # web_from=参数代表：
        # nindia  之前的印度站
        # tw  台湾站
        # mee  meesho越南站
        # mee_id  meesho印尼站
        # 
        post_data = {
            "name":item['pro_name'],
            "id":item['pro_id'],
            "price":item['price'],
            "main_pic":item['main_pic'],
            "url":item['pro_url'],
            "sales":0,
            "review":item['review_num'],
            "images":item['image_urls']
        }
        return Request(url=post_url, method="POST", body=json.dumps(post_data), headers=headers)
