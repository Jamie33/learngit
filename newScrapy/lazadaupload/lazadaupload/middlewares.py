from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
from selenium.webdriver.common.keys import Keys
import time, random, requests, logging
from selenium.webdriver.chrome.options import Options
from .settings import *
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.spidermiddlewares.httperror import HttpError


class SeleniumMiddleware():
    def __init__(self, timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.chrome_options = Options()
        # 禁止图片和视频的加载，提高网页爬取速度
        #prefs = {"profile.managed_default_content_settings.images": 2}
        #self.chrome_options.add_experimental_option("prefs", prefs)
        self.chrome_options.add_argument('--headless')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()
        print('关闭 selenium')

    def process_request(self, request, spider):
        self.logger.debug('Chromedriver is Starting')
        try:
            if request.url.startswith('https://www.lazada.vn/'):
                self.browser.get(request.url)
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pdp-mod-product-badge-title')))
                #self.logger.debug(self.browser.page_source)
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


class ProxyMiddleware():
    def __init__(self, proxy_url):
        self.logger = logging.getLogger(__name__)
        self.proxy_url = proxy_url

    def get_random_proxy(self):
        try:
            response = requests.get(self.proxy_url)
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except requests.ConnectionError:
            return False

    def process_request(self, request, spider):
        if request.meta.get('retry_times'):
            proxy = self.get_random_proxy()
            if proxy:
                uri = 'https://{proxy}'.format(proxy=proxy)
                self.logger.debug('使用代理 ' + proxy)
                request.meta['proxy'] = uri

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            proxy_url=settings.get('PROXY_URL')
        )


class GetFailedUrl():
    def process_response(self,response,request,spider):
        if response.status != 200:
            print('response status is not 200:{}'.format(response.url))
            return response
        else:
            return response