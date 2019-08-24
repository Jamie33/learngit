# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from login1688.items import Login1688Item
import re,csv,os,json,hashlib
import xlrd

class Tb1688Spider(Spider):
    name = 'tb1688'
    allowed_domains = ['detail.1688.com','test.amazing.com']
    urls = ['https://detail.1688.com/offer/41571718696.html?spm=b26110380.sw1688.mof001/.1.574e396c2GXK4G','https://detail.1688.com/offer/596464478184.html?spm=b26110380.sw1688.mof001/.1.574e396c2GXK4G']


    # 用产品链接 md5 加密成唯一的 ID
    @staticmethod
    def md5(url):
        obj = hashlib.md5()
        obj.update(bytes(url, encoding='utf-8'))
        return obj.hexdigest()

    def start_requests(self):
        for url in self.urls:
            yield Request(url=url,callback=self.parse)

    # def start_requests(self):
    #     file_path = self.settings.get('FILE_PATH')
    #     data = xlrd.open_workbook(file_path)  # 打开表格
    #     sheets = data.nsheets  # 获取表格sheet个数
    #     for i in range(sheets):
    #         sheet_info = data.sheet_by_index(i)  # 获取每个sheet信息
    #         sheet_rows = sheet_info.nrows  # 获取每个sheet行数
    #         for n in range(sheet_rows):
    #             category = sheet_info.row_values(n)[0]
    #             url = sheet_info.row_values(n)[1]  # 获取每个sheet中第二列所有的数据
    #             yield Request(url=url, meta={'category':category},callback=self.parse)

    def parse(self, response):
        item = Login1688Item()
        product = response.xpath('.//div[@id="mod-detail"]')
        item['title'] = product.xpath('.//div[@id="mod-detail-title"]//h1[@class="d-title"]//text()').extract_first()
        try:
            price_info = product.xpath('.//div[@id="mod-detail-price"]//tr[@class="price"]//@data-range').extract()
            item['price'] = float(json.loads(price_info[0])['price'])
        except:
            item['price'] = product.xpath('.//div[@id="mod-detail-price"]//tr[@class="price"]//div[@class="price-discount-sku"]//span[@class="value"]//text()').extract_first()

        item['url'] = response.url
        item['pro_id'] = self.md5(item['url'])
        img_tags = product.xpath('.//div[@class="tab-content-container"]//a[@class="box-img"]')
        item['image_urls'] = []
        for img in img_tags:
            img_link = img.xpath('./img/@src').extract_first()
            image_url = re.sub(r'\.60x60', '', img_link)
            if image_url.startswith('https://cbu01.alicdn.com/img'):
                item['image_urls'].append(image_url)
        item['main_pic'] = item['image_urls'][0]
        desc_images = response.xpath('//div[@id="desc-lazyload-container"]//img')
        item['des_images'] = [img.xpath('./@src').extract_first() for img in desc_images]
        # item['category'] = response.meta['category']
        # item['category'] = ''
        item['pro_des'] = []
        yield item