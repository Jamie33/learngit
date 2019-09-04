##  shopee 印尼站高价位爆款数据抓取
###  动态渲染 selenium，解析库 pyquery，数据库 Mongodb

---

> 运营侧需求：爬取shopee 印尼站高价位爆款数据

- 爬取品类 ：按顺序依次为：鞋，表，包，饰品
- 价位区间：按200-300，及300以上两个价位区间爬取(饰品稍等，待观察各品台基础价位)
- 销量：爬出月销量1500以上的sku


> 注意：

![nVQA3D.png](https://s2.ax1x.com/2019/09/04/nVQA3D.png)

- Shopee平台，在商品集合页需要按销量排名才可以看到月销量，商品页的销量不是月销量。

- 价格中的逗号 price_range = re.sub(r'\,|\n','',price_range)



> 数据：

导出数据如下：爬取到 311 条数据, 无重复数据。

- CSV 文件 
包含品类，小类，商品名称，价格信息，价格，月销量，商品链接，商品主图链接 共 8 个字段，预览如下：（完整表格烦请参考附件）
如果商品有价格区间，price 为价格低点和价格高点的平均值

![nVQk9O.jpg](https://s2.ax1x.com/2019/09/04/nVQk9O.jpg)

- 品类名命名的文件夹：
包含该商品的主图
产品图命名方式：商品名.png

![nVQVjH.png](https://s2.ax1x.com/2019/09/04/nVQVjH.png)



##  shopee 台湾站爆款抓取
###  动态渲染 selenium，解析库 pyquery，数据库 Mongodb

---

> 运营侧需求：爬取Shopee 台湾站爆款数据

- 网站：Shopee 台湾站
- 品类：美妝保健，居家生活，女生配件，寵物，女鞋，男鞋，女生包包-精品，男生包包與配件 （8个品类）
- 筛选标准：月销量超过500、价格800台币【约173人民币】以上（价格高点）


> 注意：

- Shopee平台，在商品集合页需要按销量排名才可以看到月销量，商品页的销量不是月销量。
- 以价格高点筛选价格800台币以上的商品



> 数据：

- 月销量超过500以上的商品有 2473 条数据 （[利用 python 对 shopee TW站 八大品类商品进行数据分析](https://jamie33.github.io/PageDemo/shopee_data_analysis_TW.html)/ Data analysis on eight merchandise categories from shopee Taiwan using python）
- 筛选后，价格800台币以上的商品有 34 条数据

导出数据如下：

包含品类，小类，商品名称，价格信息，价格低点，价格高点，月销量，商品链接，商品主图链接 共 9 个字段，预览如下：（完整表格烦请参考附件）
如果商品无价格区间，价格低点 = 价格高点，(price_min 为价格低点, price_max 为价格高点)















