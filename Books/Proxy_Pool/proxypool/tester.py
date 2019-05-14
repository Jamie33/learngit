import asyncio, aiohttp, time
from proxypool.setting import *
from proxypool.db import RedisClient
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError


class Tester(object):
    def __init__(self):
        self.redis = RedisClient()
    
    async def test_single_proxy(self,proxy):
        """
       测试单个代理
       :param proxy: 单个代理
       :return: None
       """
        # 定义了连接器并取消ssl安全验证，使用 ssl使其等于False，默认是True的。因为有的网站请求的时候会验证ssl证书,如果是自签名的ssl证书会出错。
        conn = aiohttp.TCPConnector(ssl = False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                # string = b'xxxxxx'.decode() 直接以默认的utf-8编码解码bytes成string
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://'+ proxy
                print('正在测试',proxy)
                async with session.get(TEST_URL,proxy=real_proxy,timeout=15) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.setmax(proxy)
                        print('代理可用',proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不合法',proxy)
            except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                self.redis.decrease(proxy)
                print('代理请求失败',proxy)
                
    def run(self):
        print('测试开始运行')
        try:
            proxies = self.redis.viewall()
            if proxies:
                loop = asyncio.get_event_loop()
                for i in range(0,len(proxies),BATCH_TEST_SIZE):
                    test_proxies = proxies[i:i+BATCH_TEST_SIZE]
                    tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                    loop.run_until_complete(asyncio.wait(tasks))
                    time.sleep(5)
            else:
                print('proxies 为空')
        except Exception as e:
            print('测试器发生错误',e.args)