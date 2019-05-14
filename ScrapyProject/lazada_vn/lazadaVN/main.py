from scrapy.cmdline import execute  # 调用此函数可以执行scrapy的脚本

import sys
import os

# 用来设置工程目录，有了它才可以让命令行生效
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# os.path.abspath(__file__)  用来获取当前py文件的路径
# os.path.dirname()    用来获取文件的父亲的路径

# 调用execute()函数执行scarpy的命令 scary crawl 爬虫文件名字
execute(['scrapy', 'crawl', 'lazada','-o','lazadaVN_cosmetics_0514.csv'])