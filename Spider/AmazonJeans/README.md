## amazon 牛仔裤品类爬虫
###  动态渲染 selenium，解析库 pyquery，数据库 Mongodb

---

> 运营侧需求：爬取 amazon 牛仔裤品类

爬20页所有商品的部分信息，字段包括商品名、现价、评价数、商品链接

> 链接：
https://www.amazon.com/s/ref=sr_st_featured-rank?rh=n%3A7141123011%2Cn%3A7147441011%2Cn%3A1040658%2Cn%3A1045564&qid=1548214701&sort=featured-rank&ajr=3

![运营侧需求](https://s2.ax1x.com/2019/09/03/nA5lCt.jpg)

> 结果：

由于基本每页有48个商品，部分页数只有47个商品，所以20页共爬取到 957 条商品数据。
爬取数据预览如下：完整表格烦请参考 page20_item_details.csv

![文档预览](https://s2.ax1x.com/2019/09/03/nA518P.jpg)





