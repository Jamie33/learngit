# -*- coding: utf-8 -*-
from scrapy import Spider
from splash1688.items import Splash1688Item
from scrapy_splash import SplashRequest
import re,json,hashlib

script = """
function main(splash, args)
  assert(splash:go(args.url))
  splash.resource_timeout = 10
  assert(splash:wait(args.wait))
  return splash:html()
end
"""


class Tb1688Spider(Spider):
    name = 'tb1688'
    allowed_domains = ['detail.1688.com']
    urls = ['https://detail.1688.com/offer/41571718696.html?spm=b26110380.sw1688.mof001/.1.574e396c2GXK4G']

    def start_requests(self):
        for url in self.urls:
            yield SplashRequest(url, callback=self.parse, endpoint='execute', args={'lua_source': script, 'wait': 5,'cookies':'UM_distinctid=169b91a7acb4e3-016f9cab7aa24-b781636-1fa400-169b91a7acce21; cna=OigNFH/QjBkCAXQYQOPEDXSc; lid=priatej; ali_ab=183.14.132.100.1557023611304.9; hng=CN%7Czh-CN%7CCNY%7C156; ali_apache_track=c_mid=b2b-49246855974b25|c_lid=priatej|c_ms=1|c_mt=2; ad_prefer="2019/07/11 16:25:27"; CNZZDATA1253659577=1992458606-1557046010-https%253A%252F%252Fshow.1688.com%252F%7C1564626190; _csrf_token=1564626934091; cookie2=523027bacfffa9a7cd60747976498a09; t=45201858cb4ad17fed2931a54d20e68f; _tb_token_=7e93335be66e7; alicnweb=touch_tb_at%3D1564626939755%7ChomeIdttS%3D09381918207483643134156289714168953034%7ChomeIdttSAction%3Dtrue%7Clastlogonid%3Dpriatej; cookie1=W5tUXo9DyKXYFUGVUte6BthQDscT8L7xCyDRbyU6KBw%3D; cookie17=VyUOVv1wViAm; sg=j98; csg=5e822929; unb=492468559; uc4=nk4=0%40Ea%2BKMc90Sedv%2FhUlfk03Tgxh&id4=0%40VXJ%2FGDvzQeSko%2BV2flDXfEaLPSI%3D; __cn_logon__=true; __cn_logon_id__=priatej; ali_apache_tracktmp=c_w_signed=Y; _nk_=priatej; last_mid=b2b-49246855974b25; _is_show_loginId_change_block_=b2b-49246855974b25_false; _show_force_unbind_div_=b2b-49246855974b25_false; _show_sys_unbind_div_=b2b-49246855974b25_false; _show_user_unbind_div_=b2b-49246855974b25_false; __rn_alert__=false; l=cBMMKS77vAhGScqoBOCN5uI8an7OtIRAguPRwNYvi_5QZTxNn5_OkSkvPnv6cjWd9R8B4z6vzNe9-etusAsZ2i8gi3AV.; isg=BPv7kzgFIkCr7B8vPAJQOYFoit-l-A8mAYE2ke24mvo_TBsudSPeogcGZqyn7GdK',})

    # 用产品链接 md5 加密成唯一的 ID
    @staticmethod
    def md5(url):
        obj = hashlib.md5()
        obj.update(bytes(url, encoding='utf-8'))
        return obj.hexdigest()

    def parse(self, response):
        item = Splash1688Item()
        #print(response.html)
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
        item['pro_des'] = []
        yield item