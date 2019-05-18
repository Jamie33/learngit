# -*- coding: utf-8 -*-
import scrapy,re,json
from lazadaVN.items import LazadavnItem
from urllib.parse import urlencode
from scrapy import Request, Spider

class LazadavnSpider(Spider):
    name = 'lazadavn'
    allowed_domains = ['www.lazada.vn']
    #start_urls = ['https://www.lazada.vn/trang-diem-mat/?spm=a2o4n.searchlistcategory.cate_4_1.1.46663876ChKfhm+&page=1']

    def start_requests(self):
        #url_list = ['https://www.lazada.vn/trang-diem-mat/?spm=a2o4n.searchlistcategory.cate_4_1.1.46663876ChKfhm ','https://www.lazada.vn/mat/?spm=a2o4n.searchlistcategory.cate_4_1.2.539926e0swrjYP','https://www.lazada.vn/moi/?spm=a2o4n.searchlistcategory.cate_4_1.3.4ed3750eubugPZ','https://www.lazada.vn/mong/?spm=a2o4n.searchlistcategory.cate_4_1.4.4e903658Jj03KW','https://www.lazada.vn/phu-kien-trang-diem/?spm=a2o4n.searchlistcategory.cate_4_1.5.6a168ad9eLA9a3','https://www.lazada.vn/tay-trang/?spm=a2o4n.searchlistcategory.cate_4_1.6.2a936e92JeyJfv','https://www.lazada.vn/bo-kit-trang-diem-va-palletes/?spm=a2o4n.searchlistcategory.cate_4_1.7.71ff27c5yPbBCI','https://www.lazada.vn/mat-na-lot-va-hat-tay-te-bao/?spm=a2o4n.searchlistcategory.cate_4_2.8.1c88cf9ewmZHk2 ','https://www.lazada.vn/co-the/?spm=a2o4n.searchlistcategory.cate_4_1.9.3eca2169x9L86I','https://www.lazada.vn/cac-loai-duong-am/?spm=a2o4n.searchlistcategory.cate_4_2.1.1bec6942rVxIIj','https://www.lazada.vn/cham-soc-da-chuyen-sau/?spm=a2o4n.searchlistcategory.cate_4_2.2.c7fb5950pZQeaF','https://www.lazada.vn/cham-soc-da-vung-mat/?spm=a2o4n.searchlistcategory.cate_4_2.3.d2312a04gy26Xm','https://www.lazada.vn/duong-da-va-serum/?spm=a2o4n.searchlistcategory.cate_4_2.4.4ba4412czqpBLe','https://www.lazada.vn/son-duong-va-tri-tham/?spm=a2o4n.searchlistcategory.cate_4_2.5.3e644b5fnm3gDf','https://www.lazada.vn/kem-chong-nang-phuc-hoi-sau-di-nang/?spm=a2o4n.searchlistcategory.cate_4_2.6.66385f66BY6Flj','https://www.lazada.vn/mat-na-dap/?spm=a2o4n.searchlistcategory.cate_4_2.7.54a25a2dlYO8Zl','https://www.lazada.vn/mat-na-lot-va-hat-tay-te-bao/?spm=a2o4n.searchlistcategory.cate_4_2.8.5b3120a4dKZfTH','https://www.lazada.vn/nuoc-hoa-hong-va-xit-khoang/?spm=a2o4n.searchlistcategory.cate_4_2.9.60852169RjHoKU','https://www.lazada.vn/sua-rua-mat/?spm=a2o4n.searchlistcategory.cate_4_2.10.ac596932oyBgu6']
        url_list = ['https://www.lazada.vn/trang-diem-mat/?',
                    'https://www.lazada.vn/mat/?',
                    'https://www.lazada.vn/moi/?',
                    'https://www.lazada.vn/mong/?',
                    'https://www.lazada.vn/phu-kien-trang-diem/?',
                    'https://www.lazada.vn/tay-trang/?',
                    'https://www.lazada.vn/bo-kit-trang-diem-va-palletes/?',
                    'https://www.lazada.vn/mat-na-lot-va-hat-tay-te-bao/?',
                    'https://www.lazada.vn/co-the/?',
                    'https://www.lazada.vn/cac-loai-duong-am/?',
                    'https://www.lazada.vn/cham-soc-da-chuyen-sau/?',
                    'https://www.lazada.vn/cham-soc-da-vung-mat/?',
                    'https://www.lazada.vn/duong-da-va-serum/?',
                    'https://www.lazada.vn/son-duong-va-tri-tham/?',
                    'https://www.lazada.vn/kem-chong-nang-phuc-hoi-sau-di-nang/?',
                    'https://www.lazada.vn/mat-na-dap/?',
                    'https://www.lazada.vn/mat-na-lot-va-hat-tay-te-bao/?',
                    'https://www.lazada.vn/nuoc-hoa-hong-va-xit-khoang/?',
                    'https://www.lazada.vn/sua-rua-mat/?']

        for url in url_list:
            #spm = re.search(r'spm=(.*)', url).group(1)
            #data = {'spm':spm}
            #base_url = re.search(r'(.*)spm=', url).group(1)
            data = {}
            category = re.search(r'https://www.lazada.vn/(.*)/\?', url).group(1)
            for page in range(1,self.settings.get('MAX_PAGE')+1):
                data['page'] = page
                params = urlencode(data)
                form_url = url + params
                yield Request(form_url, self.parse, meta={'category':category,'page':page,'page_url':form_url})

    def parse(self, response):
        html = response.text
        js_content = re.search(r'listItems":(.*),"breadcrumb":',html).group(1)
        item_list = json.loads(js_content, strict=False)
        for i in item_list:
            item = LazadavnItem()
            item['pro_name'] = i['name']
            item['pro_url'] = 'https:'+ i['productUrl']
            item['pro_price'] = i['price']
            item['pro_review'] = i['review']
            item['category'] = response.meta['category']
            item['page'] = response.meta['page']
            item['page_url'] = response.meta['page_url']
            yield item

