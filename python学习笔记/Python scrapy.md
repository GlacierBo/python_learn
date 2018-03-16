- 使用Scrapy抓取一个网站一共需要四个步骤：
  - 创建一个Scrapy项目
  - 定义Item容器
  - 编写爬虫
  - 存储内容

Spider，是用户编写用于从网站上爬取数据的类，其包含了一个用于下载的初始URL，然后是如何跟进网页中的链接以及如何分析页面中的内容，还有提取生成item的方法。



### XPath

XPath是一门在网页中查找特定信息的语言，所以用XPath来筛选数据，要比正则表达式容易些。

例子：

``` python
>>> response.xpath('//title')
>>> response.xpath('//title').extract() # 序列化
>>> response.xpath('//title/text()').extract() 
```

Scrapy会自动产生一个sel变量，我们直接调用sel.xpath()就行了

