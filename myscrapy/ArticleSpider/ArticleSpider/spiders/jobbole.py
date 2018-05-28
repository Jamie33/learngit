# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse

from ArticleSpider.items import ArticlespiderItem

from ArticleSpider.utils.common import get_md5


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        '''

        1. 获取文章列表页中的文章URL，并交给scrapy下载后并进行解析
        2. 获取下一页的URL并交给scrapy进行下载，下载完成后交给parse

        '''

        #解析列表页中的所有文章URL，并交给scrapy下载后并进行解析

        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            cover_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url = parse.urljoin(response.url, post_url),meta={"cover_url":cover_url},callback=self.parse_detail)

        #提取下一页，并交给scrapy下载后并进行解析

        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse)


    def parse_detail(self, response):
        article_item = ArticlespiderItem()


        # 提取文章的具体字段
        re_selector = response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1')
        cover_url = response.meta.get("cover_url","")
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].replace('·','').strip()
        vote_num = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        fav = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        fav_num = re.search(r'(\d+)',fav)
        if fav_num:
            fav = int(fav_num.group(1))
        else:
            fav = 0
        comments = response.xpath("//a[@href='#article-comment']/text()").extract_first("")
        comment_num = re.search(r'(\d+)',comments)
        if comment_num:
            comments = int(comment_num.group(1))
        else:
            comments = 0
        content = response.xpath("//div[@class='entry']")[0].xpath('string(.)').extract()[0].strip()
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tags = ",".join([element for element in tag_list if not element.strip().endswith('评论')])

        #css
        #title1 = response.css(".entry-header h1::text").extract()[0]
        #date2 = response.css(".entry-meta-hide-on-mobile::text").extract()[0].strip().replace('·', '')
        #vote = response.css(".vote-post-up h10::text").extract()[0]
        #fav2 = response.css(".bookmark-btn::text").extract()[0]
        #fav_num2 = re.search(r'(\d+)', fav2)
        #if fav_num2:
        #    fav_num2 = fav_num2.group(1)
        #comment2 = response.css("a[href='#article-comment'] span::text").extract()[0]
        #comment_num2 = re.search(r'(\d+)', comment2)
        #if comment_num2:
        #    comment_num2 = comment_num2.group(1)
        #content2 = response.css("div.entry").extract()[0]
        #tag_list2= response.css("p.entry-meta-hide-on-mobile a::text").extract()
        #tags2 = ",".join([element for element in tag_list2 if not element.strip().endswith('评论')])

        article_item['url_object_id'] = get_md5(response.url)
        article_item['title'] = title
        article_item['url'] = response.url
        article_item['cover_url'] = [cover_url]
        article_item['date'] = date
        article_item['vote_num'] = vote_num
        article_item['fav_num'] = fav_num
        article_item['comments'] = comments
        article_item['content'] = content
        article_item['tags'] = tags

        yield article_item
