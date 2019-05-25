# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
from selenium.webdriver.common.keys import Keys
import time, random, requests
from selenium.webdriver.chrome.options import Options


class ShopeeMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    
    def __init__(self, timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.chrome_options = Options()
        # 禁止图片和视频的加载，提高网页爬取速度
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.chrome_options.add_experimental_option("prefs", prefs)
        self.chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.wait = WebDriverWait(self.browser, self.timeout)
    
    def __del__(self):
        self.browser.close()

    def process_request(self,request,spider):
        self.logger.debug('Chromedriver is Starting')
        try:
            self.browser.get(request.url)
            item_num = len(self.browser.find_elements_by_css_selector('.c5TXIP'))
            self.logger.debug(' load {} items...'.format(item_num))
            while True:
                if item_num == 40:
                    break
                if item_num < 40:
                    self.browser.find_element_by_xpath("/html/body").send_keys(Keys.PAGE_DOWN)
                    self.logger.debug('page down...'.format(item_num))
                    time.sleep(random.uniform(1, 5))
                    item_num = len(self.browser.find_elements_by_css_selector('.c5TXIP'))
                    self.logger.debug('loading {} items...'.format(item_num))

            #self.logger.debug(self.browser.page_source)
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)        

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'))


class ProxypoolMiddleware(object):
    # 定义一个请求之前的方法
    def process_request(self, request, spider):
        PROXY_POOL_URL = 'http://localhost:5555/random'
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            return None
