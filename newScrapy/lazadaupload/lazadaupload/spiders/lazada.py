# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from lazadaupload.items import LazadauploadItem
import re,csv,os,json,hashlib
import pandas as pd
import xlrd


class LazadaSpider(Spider):
    name = 'lazadaupload'
    allowed_domains = ['www.lazada.vn','test.amazing.com']
    # urls = ['https://www.lazada.vn/products/ao-thun-nam-the-thao-hang-vnxk-vai-day-min-vai-dom-i265780948-s382816264.html?']
    # urls = ['https://www.lazada.vn/products/ke-mat-nuoc-eyeliner-maycreate-i216263143-s270998286.html?spm=a2o4n.searchlistcategory.list.59.5d283876kaUygS&search=1','https://www.lazada.vn/products/ao-thun-nam-the-thao-hang-vnxk-vai-day-min-vai-dom-i265780948-s382816264.html?']

    # 用产品链接 md5 加密成唯一的 ID
    @staticmethod
    def md5(url):
        obj = hashlib.md5()
        obj.update(bytes(url, encoding='utf-8'))
        return obj.hexdigest()

    # # 文件 xls 转成 csv 格式
    # @staticmethod
    # def xlsx_to_csv(file_name):
    #     save_name = os.path.splitext(file_name)[0]
    #     data_xls = pd.read_excel(file_name, index_col=0)
    #     save_file = r'{}.csv'.format(save_name)
    #     data_xls.to_csv(save_file, encoding='utf-8')
    #     return save_file
    #
    # # 从文件取出  url
    # def start_requests(self):
    #     file_path = self.settings.get('FILE_PATH')
    #     file_path = self.xlsx_to_csv(file_path)
    #     with open(file_path,'r',encoding='utf-8-sig') as f:
    #         reader = csv.reader(f)
    #         rows = [row for row in reader]
    #         for row in rows:
    #             url = row[1]
    #             yield Request(url=url, callback=self.parse)

    def start_requests(self):
        file_path = self.settings.get('FILE_PATH')
        data = xlrd.open_workbook(file_path)  # 打开表格
        sheets = data.nsheets  # 获取表格sheet个数
        for i in range(sheets):
            sheet_info = data.sheet_by_index(i)  # 获取每个sheet信息
            sheet_rows = sheet_info.nrows  # 获取每个sheet行数
            for n in range(sheet_rows):
                category = sheet_info.row_values(n)[0]
                url = sheet_info.row_values(n)[1]  # 获取每个sheet中第二列所有的数据
                yield Request(url=url, meta={'category':category},callback=self.parse)


    # #从配置取出 url
    # def start_requests(self):
    #     for url in self.urls:
    #         yield Request(url=url, callback=self.parse)

    def parse(self, response):
        product = response.xpath('.//div[@class="pdp-block"]//div[@class="pdp-block pdp-block__main-information"]')
        item = LazadauploadItem()
        item['title'] = product.xpath('.//div[@class="pdp-product-title"]//text()').extract_first()
        price_info = product.xpath('.//div[@class="pdp-product-price"]//text()').extract_first()
        item['price'] = re.sub(r'₫|\.','',price_info).strip()
        item['url'] = response.url
        item['pro_id'] = self.md5(item['url'])
        img_tags = product.xpath('.//div[@class="item-gallery__image-wrapper"]')
        item['image_urls'] = []
        for img in img_tags:
            img_link = img.xpath('./img/@src').extract_first()
            image_url = re.sub(r'80x80','800x800', img_link)
            image_url = re.sub(r'_.webp', '', image_url)
            if image_url.startswith('//vn-test-11'):
                item['image_urls'].append('https:'+image_url)
        item['main_pic'] = item['image_urls'][0]
        #desc_text = product.xpath('//div[@class="pdp-product-desc "]//text()').extract() 内容高度限制
        desc_text = product.xpath('//div[contains(@class,"pdp-product-desc")]//text()').extract()
        desc_images = product.xpath('//div[contains(@class,"pdp-product-desc")]//img')
        item['des_images'] = [img.xpath('./@src').extract_first() for img in desc_images]
        item['pro_des'] = [x.strip() for x in [i.strip() for i in desc_text] if x != '']
        item['category'] = response.meta['category']
        yield item

