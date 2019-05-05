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




class Scrapy1688SpiderMiddleware(object):
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
        # 启用headless模式：无浏览器界面，提高速度与稳定性
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        # if request.url.startswith('http://img.china.alibaba.com'):
        #     return HtmlResponse(url=request.url, body=self.browser.page_source, request=request,
        #                         status=200)
        if request.url.startswith('https://show.1688.com'):
            self.logger.debug('Chromedriver is Starting')
            try:
                self.browser.get(request.url)
                #self.browser.maximize_window()
                item_num = len(self.browser.find_elements_by_css_selector('.cate1688-offer.b2b-ocms-fusion-comp'))
                while True:
                    # self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                    # self.logger.debug('scroll to bottom...'.format(item_num))
                    self.browser.find_element_by_xpath("/html/body").send_keys(Keys.PAGE_DOWN)
                    self.logger.debug('page down...'.format(item_num))
                    time.sleep(random.uniform(1, 5))
                    item_num = len(self.browser.find_elements_by_css_selector('.cate1688-offer.b2b-ocms-fusion-comp'))
                    self.logger.debug('loading {} items...'.format(item_num))
                    if item_num == 200:
                        break

                self.logger.debug('loaded {} items...'.format(item_num))
                # self.logger.debug(self.browser.page_source)
                return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                    status=200)
            except TimeoutException:
                return HtmlResponse(url=request.url, status=500, request=request)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'))
