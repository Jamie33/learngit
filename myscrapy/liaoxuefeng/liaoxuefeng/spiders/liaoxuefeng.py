import scrapy

class LiaoxufefengSpider(scrapy.Spider):
    #将爬虫定义为scrapy.Spider这个类下的一个实例
    #Spider这个类定义了爬虫的很多基本功能，我们直接实例化就好，省却了很多重写方法的麻烦

    name = 'lxf'
    #爬虫的名字，这个非常重要
    start_urls = ['http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000']
    #这是爬虫开始干活的地址，必须是一个可迭代对象

    def parse(self,response):
    #爬虫收到上面的地址后，就会发送requests请求，在收到服务器返回的内容后，就将内容传递给parse函数。在这里重写函数，到达我们想要的功能。
        titles = response.css("//ul[@class='uk-nav uk-nav-side']//a/text().").extract()
    # 这是廖雪峰老师python教程的标题列表。我们利用xpath解析器对收到的response进行分析，从而提取出我们需要的数据。//XXX表示任何任何目录下的XXX区块，/XXX表示子目录下的XXX区块，XXX[@class=abc]表示带有class=abc属性值的XXX区块，/text()表示获取该区块的文本。最后加上.extract()表示将内容提取出来
    for title in titles:
        print(title)

