## 速卖通 aliexpress 牛仔裤品类爬虫
###  动态渲染 selenium，解析库 pyquery，数据库 Mongodb

---

> 运营侧需求：爬取速卖通 aliexpress 平台牛仔裤品类

按销量排行20页内所有商品的部分信息，字段包括商品名、价格区间、价格低点、价格高点、订单数、评价数、商品链接

- 该订单数为近6个月的订单数；
- 商品如无价格区间，价格低点=价格高点；

> 链接：
https://www.aliexpress.com/category/100003086/jeans/1.html?site=glo&g=y&SortType=total_tranpro_desc&needQuery=n&tag=

![运营侧需求](![nA4Ewj.jpg](https://s2.ax1x.com/2019/09/03/nA4Ewj.jpg))

> 结果：

每页有48个商品，所以20页共爬取到 960 条商品数据。
爬取数据预览如下：完整表格烦请参考 aliexpress_jean_20page_item_details.csv

![文档预览](![nA4VTs.jpg](https://s2.ax1x.com/2019/09/03/nA4VTs.jpg))





