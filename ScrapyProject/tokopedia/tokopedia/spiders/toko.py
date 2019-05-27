# -*- coding: utf-8 -*-
import scrapy,re,json
from tokopedia.items import TokopediaItem
from urllib.parse import urlencode
from scrapy import Request, Spider
import hashlib


class TokoSpider(scrapy.Spider):
    name = 'toko'
    allowed_domains = ['www.tokopedia.com','test.amazing.com']
    start_urls = ['https://www.tokopedia.com/p/kecantikan/make-up-tools?fcity=174,175,176,177,178&rt=4,5&official=true']

    @staticmethod
    def md5(url):
        obj = hashlib.md5()
        obj.update(bytes(url, encoding='utf-8'))
        return obj.hexdigest()

    def start_requests(self):
        base_url = 'https://www.tokopedia.com/p/kecantikan/make-up-tools?'
        data = {'fcity': '174,175,176,177,178', 'rt':'4,5','official':'true'}
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            data['page'] = page
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        # html = response.text
        # print(html)
        products = response.xpath('//div[@class="_2p2-wGqG"]//div[@class="_33JN2R1i"]')
        print('item number', len(products))
        for product in products:
            item = TokopediaItem()
            item['pro_name'] = product.xpath('.//h3[@class="_18f-69Qp"]/text()').extract_first().strip()
            item['pro_url'] = product.xpath('.//div[@class="_27sG_y4O"]/a/@href').extract_first()
            item['pro_id'] = self.md5(item['pro_url'])
            #item['pro_url'] = re.sub(r'src=.*', '', product.xpath('./a/@href').extract_first())
            price_info = product.xpath('.//span[@class="_3PlXink_"]/span/text()').extract_first()
            price = re.sub(r'Rp|\.','',price_info).strip()
            item['price'] = price
            review_info = product.xpath('.//span[@class="_2wY6y7fV"]/text()')[1].extract()
            if review_info:
                item['review_num'] = int(review_info)
            else:
                item['review_num'] = 0
            yield Request(item['pro_url'], callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        item['image_urls'] = []
        img_tags = response.xpath('.//div[@class="content-img-relative"]')
        for img in img_tags:
            img_link = img.xpath('./img/@src').extract_first()
            image_url = re.sub(r'cache/\d+/','',img_link)
            item['image_urls'].append(image_url)
        yield item

        headers = {'Content-Type': 'application/json'}
        post_url = 'http://test.amazing.com/api/goods/insertgoods?web_from=mee_id'

        # web_from=参数代表：
        # nindia  之前的印度站
        # tw  台湾站
        # mee  meesho越南站
        # mee_id  meesho印尼站
        #
        # post_data = {
        #     "name": item['pro_name'],
        #     "id": item['pro_id'],
        #     "price": item['price'],
        #     "main_pic": item['main_pic'],
        #     "url": item['pro_url'],
        #     "sales": 0,
        #     "review": item['review_num'],
        #     "images": item['image_urls']
        # }
        # return Request(url=post_url, method="POST", body=json.dumps(post_data), headers=headers)