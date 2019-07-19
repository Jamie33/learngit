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
import time, random
from selenium.webdriver.chrome.options import Options


class Login1688SpiderMiddleware(object):
    def __init__(self, timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.chrome_options = Options()
        # 禁止图片和视频的加载，提高网页爬取速度
        #prefs = {"profile.managed_default_content_settings.images": 2}
        #self.chrome_options.add_experimental_option("prefs", prefs)
        # self.chrome_options.add_argument('--headless')]
        # self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        # 允许浏览器重定向，Framebusting requires same-origin or a user gesture
        self.chrome_options.add_argument("disable-web-security")
        #self.chrome_options.add_argument(r"--user-data-dir=C:\Users\win7\AppData\Local\Google\Chrome\User Data")  # 设置成用户自己的数据目录
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()
        print('关闭 selenium')

    def process_request(self, request, spider):
        # self.logger.debug('Chromedriver is Starting')
        # login_url = 'https://login.1688.com/member/signin.htm'
        # self.browser.get(login_url)
        # print("请在10秒内完成扫码登录")
        # time.sleep(10)

        self.logger.debug('Chromedriver is Starting')
        self.browser.get(request.url)
        time.sleep(random.randint(3, 6))
        print(self.browser.current_url)
        try:
            if self.browser.current_url.startswith('https://login.1688.com'):
                print('需要登陆')
                self.logger.debug('Chromedriver is Starting')
                login_url = 'https://login.1688.com/member/signin.htm'
                self.browser.get(login_url)
                print("请在10秒内完成扫码登录")
                time.sleep(10)
                self.browser.get(request.url)
                # self.browser.execute_script("""
                #     (function () {
                #         var y = document.body.scrollTop;
                #         var step = 500;
                #         window.scroll(0, y);
                #         function f() {
                #             if (y < document.body.scrollHeight) {
                #                 y += step;
                #                 window.scroll(0, y);
                #                 setTimeout(f, 50);
                #             }
                #             else {
                #                 window.scroll(0, y);
                #                 document.title += "scroll-done";
                #             }
                #         }
                #         setTimeout(f, 1000);
                #     })();
                # """)
                time.sleep(random.randint(30, 60))
                return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',status=200)

            elif self.browser.current_url.startswith('https://detail.1688.com/'):
                print('不需要登陆')
                # self.browser.execute_script("""
                #     (function () {
                #         var y = document.body.scrollTop;
                #         var step = 2000;
                #         window.scroll(0, y);
                #         function f() {
                #             if (y < document.body.scrollHeight) {
                #                 y += step;
                #                 window.scroll(0, y);
                #                 setTimeout(f, 50);
                #             }
                #             else {
                #                 window.scroll(0, y);
                #                 document.title += "scroll-done";
                #             }
                #         }
                #         setTimeout(f, 1000);
                #     })();
                # """)
                time.sleep(random.randint(30, 60))
                return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',status=200)
            else:
                return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                    status=200)
        except TimeoutException:
            print('selenium request timeout exception:{}'.format(request.url))
            return HtmlResponse(url=request.url, status=500, request=request)


    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'))