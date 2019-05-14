# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from shopeeTW.items import ShopeetwItem
from urllib.parse import urlencode
import re

class ShopeeSpider(Spider):
    name = 'shopee'
    allowed_domains = ['lazada.vn']
    #start_urls = ["https://www.lazada.vn/cham-soc-suc-khoe-va-lam-dep/"]

    def start_requests(self):
        url_list = ['https://www.lazada.vn/trang-diem-mat/?spm=a2o4n.searchlistcategory.cate_4_1.1.46663876ChKfhm ','https://www.lazada.vn/mat/?spm=a2o4n.searchlistcategory.cate_4_1.2.539926e0swrjYP','https://www.lazada.vn/moi/?spm=a2o4n.searchlistcategory.cate_4_1.3.4ed3750eubugPZ','https://www.lazada.vn/mong/?spm=a2o4n.searchlistcategory.cate_4_1.4.4e903658Jj03KW','https://www.lazada.vn/phu-kien-trang-diem/?spm=a2o4n.searchlistcategory.cate_4_1.5.6a168ad9eLA9a3','https://www.lazada.vn/tay-trang/?spm=a2o4n.searchlistcategory.cate_4_1.6.2a936e92JeyJfv','https://www.lazada.vn/bo-kit-trang-diem-va-palletes/?spm=a2o4n.searchlistcategory.cate_4_1.7.71ff27c5yPbBCI','https://www.lazada.vn/mat-na-lot-va-hat-tay-te-bao/?spm=a2o4n.searchlistcategory.cate_4_2.8.1c88cf9ewmZHk2 ','https://www.lazada.vn/co-the/?spm=a2o4n.searchlistcategory.cate_4_1.9.3eca2169x9L86I','https://www.lazada.vn/cac-loai-duong-am/?spm=a2o4n.searchlistcategory.cate_4_2.1.1bec6942rVxIIj','https://www.lazada.vn/cham-soc-da-chuyen-sau/?spm=a2o4n.searchlistcategory.cate_4_2.2.c7fb5950pZQeaF','https://www.lazada.vn/cham-soc-da-vung-mat/?spm=a2o4n.searchlistcategory.cate_4_2.3.d2312a04gy26Xm','https://www.lazada.vn/duong-da-va-serum/?spm=a2o4n.searchlistcategory.cate_4_2.4.4ba4412czqpBLe','https://www.lazada.vn/son-duong-va-tri-tham/?spm=a2o4n.searchlistcategory.cate_4_2.5.3e644b5fnm3gDf','https://www.lazada.vn/kem-chong-nang-phuc-hoi-sau-di-nang/?spm=a2o4n.searchlistcategory.cate_4_2.6.66385f66BY6Flj','https://www.lazada.vn/mat-na-dap/?spm=a2o4n.searchlistcategory.cate_4_2.7.54a25a2dlYO8Zl','https://www.lazada.vn/mat-na-lot-va-hat-tay-te-bao/?spm=a2o4n.searchlistcategory.cate_4_2.8.5b3120a4dKZfTH','https://www.lazada.vn/nuoc-hoa-hong-va-xit-khoang/?spm=a2o4n.searchlistcategory.cate_4_2.9.60852169RjHoKU','https://www.lazada.vn/sua-rua-mat/?spm=a2o4n.searchlistcategory.cate_4_2.10.ac596932oyBgu6']
        for url in url_list:
            base_url = re.search(r'(.*)spm=', url).group(1)
            spm = re.search(r'spm=(.*)', url).group(1)
            data = {'spm':spm}
            base_url = re.search(r'(.*)spm=', url).group(1)
            category = re.search(r'https://www.lazada.vn/(.*)/\?spm=', url).group(1)
            for page in range(1,self.settings.get('MAX_PAGE')+1):
                data['page'] = page
                params = urlencode(data)
                url = base_url + params
                yield Request(url, self.parse, meta={'category':category})

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
            item['category'] = response.meta['category']
            yield item