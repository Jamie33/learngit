## LAZADA美妆个护产品爬取需求
### scrapy + mongodb + 代理池

---

> 需求：

- 抓取Lazada越南站下列频道按poparility排行前10页的产品信息
- 抓取字段包括产品名称，URL，价格，评价量/销量

![mXDPO0.jpg](https://s2.ax1x.com/2019/08/30/mXDPO0.jpg)


**注意：由于页面产品会实时变动，抓取到的商品会有重复**

> 数据

导出数据如下：
爬取到 5880条数据, 未去重。7个字段包括 产品类别，页码，页面URL，产品名称，价格，评价量/销量，URL
预览如下：（完整表格烦请参考附件）

![mXDFmV.jpg](https://s2.ax1x.com/2019/08/30/mXDFmV.jpg)