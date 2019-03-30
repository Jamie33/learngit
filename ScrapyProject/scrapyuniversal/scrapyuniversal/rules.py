from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules ={
    'china': (
        Rule(LinkExtractor(allow=r'article\/.*\.html', restrict_xpaths='//div[@id="left_side"]//div[@class="con_item"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageStyle"]//a[contains(.,"下一页")]'))
    )
}
