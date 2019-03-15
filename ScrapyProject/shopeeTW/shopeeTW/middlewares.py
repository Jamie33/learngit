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
import time


class ShopeeMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    
    def __init__(self, timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, self.timeout)
    
    def __del__(self):
        self.browser.close()

    def process_request(self,request,spider):
        self.logger.debug('Chromedriver is Starting')
        try:
            self.browser.get(request.url)
            for i in range(6):
                self.browser.find_element_by_xpath("/html/body").send_keys(Keys.PAGE_DOWN)
                time.sleep(2)            
            #self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '._1T9dHf._3XaILN')))
            pic_num = len(self.browser.find_elements_by_css_selector('._1T9dHf._3XaILN'))
            self.logger.debug('picture load {}/50...'.format(pic_num))
            while (pic_num<49):
                self.browser.refresh()
                for i in range(6):
                    self.browser.find_element_by_xpath("/html/body").send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
                for i in range(6):
                    self.browser.find_element_by_xpath("/html/body").send_keys(Keys.PAGE_UP)
                    time.sleep(1)
                pic_num = len(self.browser.find_elements_by_css_selector('._1T9dHf._3XaILN'))
                self.logger.debug('picture load again {}/50...'.format(pic_num))                

            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)        

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'))

