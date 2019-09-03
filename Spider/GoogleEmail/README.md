## Google 搜索引擎相关邮箱爬取
###  动态渲染 selenium，解析库 pyquery，数据库 Mongodb

---

> 运营侧需求：抓取 Google 搜索引擎相关邮箱用于EDM

![运营侧需求](![nAWVT1.jpg](https://s2.ax1x.com/2019/09/03/nAWVT1.jpg))


> 进度：(70%) 

脚本基本完成，测试暂时能通过

> 问题：

- google 搜索引擎会省略相关相似的条目，重新搜索以显示省略的结果后，极易出现 google 验证

![google 搜索引擎省略](https://s2.ax1x.com/2019/09/03/nAWeFx.jpg)

- 检测到异常请求后，需要 google 验证，暂时无法解决。

![google 验证](https://s2.ax1x.com/2019/09/03/nAWEwR.jpg)

目前设置的随机间隔时间是40-60s, google 验证出现过一次

> 测试：

以24个关键词组合为样本：['jeans site:amazon.com "@gmail.com"','jeans site:wish.com "@gmail.com"','jeans site:ebay.com "@gmail.com"','jeans site:facebook.com "@gmail.com"','jeans site:Instagram.com "@gmail.com"','jeans site:twitter.com "@gmail.com"','jeans site:tumblr.com "@gmail.com"','jeans site:linkedin.com "@gmail.com"','Jeans site:amazon.com @hotmail.com','Jeans site:wish.com @hotmail.com','Jeans site:ebay.com @hotmail.com','Jeans site:facebook.com @hotmail.com','Jeans site:Instagram.com @hotmail.com','Jeans site:twitter.com @hotmail.com','Jeans site:tumblr.com @hotmail.com','Jeans site:linkedin.com @hotmail.com','Jeans site:amazon.com @yahoo.com','Jeans site:wish.com @yahoo.com','Jeans site:ebay.com @yahoo.com','Jeans site:facebook.com @yahoo.com','Jeans site:Instagram.com @yahoo.com','Jeans site:twitter.com @yahoo.com','Jeans site:tumblr.com @yahoo.com','Jeans site:linkedin.com @yahoo.com']

> 测试结果和导出数据如下：

爬取到 2711 条和 jeans 相关的邮箱, 此数据已去重。
CSV 文件 包含品类和邮箱两个字段，预览如下：（完整表格烦请参考gmails_jeans.csv）

![文档预览](![nAWmY6.jpg](https://s2.ax1x.com/2019/09/03/nAWmY6.jpg)))

