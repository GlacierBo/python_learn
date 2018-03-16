### Scrapy

scrapy不是一个函数功能库，而是一个爬虫框架

- 爬虫框架是实现爬虫功能的一个软件结构和功能组件集合。
- 爬虫框架是一个半成品，能够帮助用户实现专业网络爬虫




### `5 + 2`结构

#### Engine 

- 控制所有模块之间的数据流
- 根据条件触发事件

#### Downloader

根据请求下载网页

#### Scheduler

对所有爬取请求进行调度管理

#### Downloader

目的：实施`Engine`、`Scheduler`和`Downloader`之间进行用户可配置的控制

功能：修改、丢弃、新增请求或响应

#### Spider

- 解析Downloader返回的响应（Response）
- 产生爬取项（scraped item）
- 产生额外的爬取请求（Request）

#### Item Pipelines

- 以流水线方式处理`Spider`产生的爬取项。
- 由一组操作顺序组成，类似流水线，每个操作是一个`Item Pipeline`类型。
- 可能操作包括：清理、检验和查重爬取项中的`HTML`数据、将数据存储到数据库。

###Scrapy命令行

| 命令           | 说明         | 格式                                       |
| ------------ | ---------- | ---------------------------------------- |
| startproject | 创建一个新工程    | scrapy startproject <name> [dir]         |
| genspider    | 创建一个爬虫     | scrapy genspider [options] <name> <domain> |
| settings     | 获取爬虫配置信息   | scrapy settings [options]                |
| crawl        | 运行一个爬虫     | scrapy crawl <spider>                    |
| list         | 列出工程中所有爬虫  | scrapy list                              |
| shell        | 启动url调试命令行 | scrapy shell [url]                       |



### 产生爬虫

#### 建立一个Scrapy爬虫

``` shell
scrapy startproject python123demo
```

``` shell
python123demo/ --------->  外层目录
	scrapy.cfg     ----->  部署Scrapy爬虫的配置文件
	python123demo/ ----->  Scrapy框架的用户自定义python代码
		__init__.py   ---> 初始化脚本
		items.py      ---> Items代码模板
		middlewares.py---> Middlewares代码模板
		pipelines.py  ---> Pipelines代码模板
		settings.py   ---> Scrapy爬虫的配置文件
		spiders/      ---> Spiders代码模板目录
```

#### 在工程中产生一个Scrapy爬虫

``` shell
scrapy genspider demo pyshon123.io
```

``` python
# -*- coding: utf-8 -*-
import scrapy
class DemoSpider(scrapy.Spider):
    name = 'small fire'
    allowed_domains = ['pyshon123.io']
    start_urls = ['http://pyshon123.io/']
    
    def parse(self, response):
        pass
```

**parse()**用于处理响应，解析内容形成字典，发现新的`url`爬取请求

#### 配置产生的spider爬虫

``` python
# -*- coding: utf-8 -*-
import scrapy
class DemoSpider(scrapy.Spider):
    name = "smallfire"
    # allowed_domains = ['pyshon123.io']
    start_urls = ['http://pyshon123.io/ws/demo.html']

    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname,'wb') as f:
            f.write(response.body)
```

#### 运行爬虫，获取网页

``` python
scrapy crawl demo
```

### yield关键字  yield ==生成器

- 生成器是一个不断产生值的函数
- 包含yield语句的函数式一个生成器
- 生成器每次产生一个值（yield语句），函数被冻结，被唤醒后再产生一个值

生成器的写法：

``` python
def gen(n):
  for i in  range(n):
    yield i**2
    
for i in gen(5):
  print(i," ",end="")

=> 0 1 4 9 16
```

优点：（相比一次列出所有内容）

- 更节省存储空间
- 响应更迅速
- 使用更灵活

``` python
import scrapy
class DemoSpider(scrapy.Spider):
  name = "dmeo"
  
  def start_requests(self):
     urls =[
         'http://python123.io/ws/demo.html'
     ]
     for url in urls:
          yield scrapy.Request(url=url,callback=self.parse)
        
  def parse(self, response):
     fname = response.url.split('/')[-1]
     with open(fname,'wb') as f:
          f.write(response.body)
```

#### Scrapy 爬虫的使用步骤

- 创建一个工程和Spider模板
- 编写Spider
- 编写Item Pipeline
- 优化配置策略

#### Scrapy 爬虫的数据类型

- Request类


- Response类
- Item类

#### Scrapy 提取信息的方法

- Beautiful Soup
- lxml
- re
- XPath Selector
- CSS Selector


### Scrapy爬虫应用展望

- 普通价值

``` shell
- 基于Linux,7*24，稳定爬取输出
- 商业级部署和应用（scrapyd-*）
- 千万规模内URL爬取、内容分析和存储
```

- 高阶价值

```shell
- 基于 docker，虚拟化部署
- 中间件扩展，增加调度和监控
- 各种反扒应对技术
```








