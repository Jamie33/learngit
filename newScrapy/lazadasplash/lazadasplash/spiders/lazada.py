# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from lazadasplash.items import LazadasplashItem
from scrapy_splash import SplashRequest
import re,requests
import xlrd

script = """
function main(splash, args)
  assert(splash:go(args.url))
  splash.resource_timeout = 10
  splash:select("#pdp-block")
  assert(splash:wait(args.wait))
  return splash:html()
end
"""

class LazadaSpider(Spider):
    name = 'lazada'
    allowed_domains = ['www.lazada.vn']
    #urls = ['https://www.lazada.vn/products/ao-thun-nam-the-thao-hang-vnxk-vai-day-min-vai-dom-i265780948-s382816264.html?','https://www.lazada.vn/products/ao-so-mi-nam-trang-cuc-trang-dai-tay-thuong-hieu-dang-cap-i227491113-s332531173.html?spm=a2o4n.searchlistcategory.list.71.4c3534bdGagnUo&search=1','https://www.lazada.vn/products/so-mi-mem-min-khong-nhan-kingman-dang-cap-i102635930-s103187546.html?spm=a2o4n.searchlistcategory.list.94.4c3534bdGagnUo&search=1','https://www.lazada.vn/products/quan-tay-nam-kieu-dang-han-quoc-quan-au-thoi-trang-cong-so-anh-that-100-i265416451-s381928839.html?spm=a2o4n.searchlistcategory.list.35.4c3534bdGagnUo&search=1','https://www.lazada.vn/products/quan-au-nam-han-quoc-quan-tay-nam-den-dang-om-vai-co-gian-khong-nhan-i246256015-s359826960.html?spm=a2o4n.searchlistcategory.list.59.4c3534bdGagnUo&search=1']

    # # 从配置取出 url
    # def start_requests(self):
    #     for url in self.urls:
    #         yield SplashRequest(url, callback=self.parse, endpoint='execute', args={'lua_source': script, 'wait': 5})

    def start_requests(self):
        file_path = self.settings.get('FILE_PATH')
        data = xlrd.open_workbook(file_path)  # 打开表格
        sheets = data.nsheets  # 获取表格sheet个数
        url_list = []
        for i in range(sheets):
            sheet_info = data.sheet_by_index(i)  # 获取每个sheet信息
            sheet_rows = sheet_info.nrows  # 获取每个sheet行数
            for n in range(sheet_rows):
                category = sheet_info.row_values(n)[0]
                url = sheet_info.row_values(n)[1]  # 获取每个sheet中第二列所有的数据
                yield SplashRequest(url, callback=self.parse, endpoint='execute',args={'lua_source': script, 'wait': 10,}, meta={'category': category})


    def parse(self, response):
        product = response.xpath('.//div[@class="pdp-block"]//div[@class="pdp-block pdp-block__main-information"]')
        item = LazadasplashItem()
        item['title'] = product.xpath('.//div[@class="pdp-product-title"]//text()').extract_first()
        price_info = product.xpath('.//div[@class="pdp-product-price"]//text()').extract_first()
        item['price'] = re.sub(r'₫|\.','',price_info).strip()
        item['url'] = response.url
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