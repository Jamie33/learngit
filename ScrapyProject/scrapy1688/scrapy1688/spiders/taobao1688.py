# -*- coding: utf-8 -*-
from scrapy import Request, Spider, FormRequest
from scrapy1688.items import Scrapy1688Item
import re,json

class Taobao1688Spider(Spider):
    name = 'taobao1688'
    allowed_domains = ['1688.com','test.amazing.com']
    start_urls = ['https://show.1688.com/pinlei/industry/pllist.html?spm=a260j.12536140.jr60szx6.7.5cb12da8vQKyBr&sceneSetId=840&sceneId=7237&bizId=9944']

    # def parse(self, response):
    #     products = response.xpath('//div[@class="cate1688-offer b2b-ocms-fusion-comp"]')
    #     for product in products:
    #         item = Scrapy1688Item()
    #         item['pro_name'] = product.xpath('.//div[@class="offer-title"]//text()').extract_first()
    #         item['price'] = float(product.xpath('.//span[@class="price-num"]//text()').extract_first())
    #         item['main_pic'] = product.xpath('.//div[@class="offer-img"]//img/@src').extract_first()
    #         item['pro_url'] = product.xpath('./a/@href').extract_first()
    #         item['pro_id'] = re.search(r'offer/(\d+).html?',item['pro_url']).group(1)
    #         sold_info = product.xpath('.//div[@class="alife-bc-uc-textLine offer-vol single-line"]//text()').extract_first()
    #         item['sold_num'] = re.search(r'成交(.+)件', sold_info).group(1)
    #         if '万' in item['sold_num']:
    #             item['sold_num'] = float(re.search(r'(.+)万', item['sold_num']).group(1))
    #             if item['sold_num'] >= 0.3:
    #                 if item['price'] <= 20:
    #                     yield item

    def parse(self, response):
        products = response.xpath('//div[@class="cate1688-offer b2b-ocms-fusion-comp"]')
        for product in products:
            item = Scrapy1688Item()
            item['pro_name'] = product.xpath('.//div[@class="offer-title"]//text()').extract_first()
            item['price'] = float(product.xpath('.//span[@class="price-num"]//text()').extract_first())
            main_pic_info = product.xpath('.//div[@class="offer-img"]//img/@src').extract_first()
            item['main_pic'] = re.sub(r'.\d+x\d+', '', main_pic_info)
            item['pro_url'] = product.xpath('./a/@href').extract_first()
            item['pro_id'] = re.search(r'offer/(\d+).html?',item['pro_url']).group(1)
            sold_info = product.xpath('.//div[@class="alife-bc-uc-textLine offer-vol single-line"]//text()').extract_first()
            item['sold_num'] = re.search(r'成交(.+)件', sold_info).group(1)
            if '万' in item['sold_num']:
                item['sold_num'] = float(re.search(r'(.+)万', item['sold_num']).group(1))
                if item['sold_num'] >= 0.3:
                    item['sold_num'] = item['sold_num'] * 10000
                    if item['price'] <= 20:
                        yield Request(item['pro_url'],callback=self.parse_detail, meta = {'item':item})

    def parse_detail(self, response):
        item = response.meta['item']
        item['image_urls'] = []
        img_tags = response.xpath('//div[@class="content"]//a[@class="box-img"]')
        for img in img_tags:
            img_link = img.xpath('./img/@src').extract_first()
            image_url = re.sub(r'.\d+x\d+','',img_link)
            if image_url != 'https://cbu01.alicdn.com/cms/upload/other/lazyload.png':
                item['image_urls'].append(image_url)
        # yield item
        headers = {'Content-Type': 'application/json'}
        post_url = 'http://test.amazing.com/api/goods/insertgoods?web_from=mee_id'
        '''
        web_from=参数代表：
        nindia  之前的印度站
        tw  台湾站
        mee  meesho越南站
        mee_id  meesho印尼站
        '''
        post_data = {
            "name":item['pro_name'],
            "id":item['pro_id'],
            "price":item['price'],
            "main_pic":item['main_pic'],
            "url":item['pro_url'],
            "sales":item['sold_num'],
            "images":item['image_urls']
        }
        return Request(url=post_url, method="POST", body=json.dumps(post_data), headers=headers)