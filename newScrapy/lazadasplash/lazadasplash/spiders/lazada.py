# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import quote
from lazadasplash.items import LazadasplashItem
from scrapy_splash import SplashRequest
import re,csv,os,time
import pandas as pd

script = """
function main(splash, args)
  splash:set_viewport_size(1028, 10000)
  assert(splash:go(args.url))
  local scroll_to = splash:jsfunc("window.scrollTo")
  scroll_to(0, 2000)
  assert(splash:wait(args.wait))
  return { html = splash:html(),}
end
"""


class LazadaSpider(Spider):
    name = 'lazada'
    allowed_domains = ['www.lazada.vn']
    urls = ['https://www.lazada.vn/products/ao-thun-nam-the-thao-hang-vnxk-vai-day-min-vai-dom-i265780948-s382816264.html?']

    # def xlsx_to_csv(self,file_name):
    #     print('文件格式转换到 csv ......')
    #     save_name = os.path.splitext(file_name)[0]
    #     data_xls = pd.read_excel(file_name, index_col=0)
    #     save_file = r'{}.csv'.format(save_name)
    #     print(save_file)
    #     data_xls.to_csv(save_file, encoding='utf-8')
    #     return save_file

    # def start_requests(self):
    #     file_path = self.settings.get('FILE_PATH')
    #     file_path = self.xlsx_to_csv(file_path)
    #     with open(file_path,'r',encoding='utf-8-sig') as f:
    #         reader = csv.reader(f)
    #         rows = [row for row in reader]
    #         for row in rows:
    #             url = row[1]
    #             yield SplashRequest(url, callback=self.parse)
    #             #yield SplashRequest(url, callback=self.parse, endpoint = 'execute',args = {'lua_source': script, 'wait': 7})

    FILE_PATH = r'E:\Scarpy_files\test.xls'
    print('文件格式转换到 csv ......')
    save_name = os.path.splitext(FILE_PATH)[0]
    data_xls = pd.read_excel(FILE_PATH, index_col=0)
    save_file = r'{}.csv'.format(save_name)
    data_xls.to_csv(save_file, encoding='utf-8')

    with open(save_file,'r',encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        urls = [ row[1] for row in rows]

    def start_requests(self):
        for url in self.urls:
            #yield SplashRequest(url, callback=self.parse)
            yield SplashRequest(url, callback=self.parse, endpoint='execute', args={'lua_source': script, 'wait': 3})

    def parse(self, response):
        #print(response.text)
        product = response.xpath('.//div[@class="pdp-block"]//div[@class="pdp-block pdp-block__main-information"]')
        item = LazadasplashItem()
        item['title'] = product.xpath('.//div[@class="pdp-product-title"]//text()').extract_first()
        item['price'] = product.xpath('.//div[@class="pdp-product-price"]//text()').extract_first()
        item['url'] = response.url
        img_tags = product.xpath('.//div[@class="item-gallery__image-wrapper"]')
        item['image_urls'] = []
        for img in img_tags:
            img_link = img.xpath('./img/@src').extract_first()
            image_url = re.sub(r'80x80','800x800', img_link)
            image_url = re.sub(r'_.webp', '', image_url)
            item['image_urls'].append('https:'+image_url)
        yield item