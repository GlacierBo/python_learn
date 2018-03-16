### 爬虫

#### 入门

``` python
# 最简单的请求
r = requests.get(url)
```

构造一个向服务器请求资源的`Request`对象，返回的是一个`Response`对象

| 属性                  | 说明                       |
| ------------------- | ------------------------ |
| r.status_code       | 返回的状态                    |
| r.text              | HTTP响应内容的字符串形式，url对应页面内容 |
| r.encoding          | 从HTTP header中猜测相应内容编码方式  |
| r.apparent_encoding | 从内容分析出相应内容编码方式           |
| r.content           | 相应内容的二进制                 |

#### 异常处理

| 异常                        | 说明                     |
| ------------------------- | ---------------------- |
| requests.ConnectionError  | 网络连接错误异常，DNS查询失败、拒绝连接等 |
| requests.HTTPError        | HTTP错误异常               |
| requests.URLRequired      | URL缺失异常                |
| requests.TooManyRedirects | 超过最大定向次数，产生定向异常        |
| requests.ConnectTimeout   | 连接远程服务器超时异常            |
| requests.Timeout          | 请求URL超时，产生超时异常         |

**网络连接有风险，处理异常很重要**

例子：

``` python
try:
  r = requests.get(url,timeout=30)
  r.raise_for_status() #如果状态不是200，引发HTTPError异常
  r.encoding = r.apparent_encoding
  return r.text
except:
  return "产生异常"
```

proxies：字典类型，设定访问代理服务器，可以增加登录认证。

``` python
pxs ={
    'http':'xxx.xxx.xxx.xxx'
  	'https':'xxx.xxxx.xxx.xxx'
}
```

#### 网络爬虫引发的问题

骚扰问题、法律风险、隐私泄露

### 盗亦有道

来源审查、Robots协议

PS: 类人行为可不参考Robots协议，获取的资源不能用于商业用途

### 实例

``` python
import requests
headers = {
    # 'Host': 'i.meizitu.net',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}
if __name__ == '__main__':
    key = input("输入您要查询的内容：")
    kv = {'wd':key}
    url = "https://www.baidu.com/s"
    req = requests.get(url,params=kv,headers=headers).text
    print(req)
```

编写爬虫的时候，必须要考虑代码的**可靠性**和**稳定性**。

``` python
import os
# 爬取图片写入文件
root = "D://pics//"
path = root + url.split('/').[-1]
try:
    if not os.path.exists(root):
      os.mkdir(root)
    if not os.path.exists(path):
      r = requests.get(url)
      with open(path,'wb') as f :
        f.write(r.content)
        f.close()
        print("文件保存成功")
    else:
      print("文件已存在")
except:
     print("爬取失败")
```

### BeautifulSoup

- 使用BeautifulSoup解析网页

`'lxml'` 是解析html用到的库，解析的库有五种，另外四种：`html.parser` ,`lxml HTML` ,`lxml XML` , `html5lib`

```python
soup = BeautifulSoup(html,'lxml')
```

- 描述要爬取的东西在哪

```python
[] = soup.select('???')
# 例1：
contents = soup.select('#post-qiniu > div > div.article-entry > blockquote > p')
imgs = soup.select('img[width="160"]')
```

- 从标签中获得你要的信息

```python
<p>Something</p>
# 例1：
for content in contents:
  	print(content.get_text())
```

- 字典构造

```python
for title,image,desc,rate,cate in zip(title,image,desc,rate,cate):
  	data = {
        'title':title.get_text(),
      	'..':...get_text(),
      	'..':...get_text(),
        'image':image.get('src')
      	...
    }
 .stripped_strings => 获取多个标签 
```

#### 下行遍历

``` python
.contents 子节点列表
.children 子节点的迭代类型
.descendants 子孙节点的迭代类型
```

遍历儿子节点

``` python
for child in soup.body.children:
  print(child)
```

#### 上行遍历

``` python
.parent 节点的父亲标签
.parents 节点的父亲列表
```

标签树的上行遍历

``` python
soup = BeautifulSoup(demo,"html.parser")
for parent in soup.a.parents:
  if parent is None:
    print(parent)
  else:
    print(parent.name)
```

#### `prettify()`方法

在调试`BeautifulSoup`可以讲`html`格式化输出，结构非常清晰，便于调试

``` python
print(soup.a.prettify())
```

### 正则表达式

| 函数            | 说明                                 |
| ------------- | ---------------------------------- |
| re.search()   | 在一个字符串中搜索匹配正则表达式的第一个位置             |
| re.match()    | 从一个字符串的开始位置起匹配正则表达式，返回match对象      |
| re.findall()  | 搜索字符串，以列表类型返回全部能匹配的字符串，返回的是一个列表类型  |
| re.split()    | 将一个字符串按照正则表达式匹配结果进行分割，返回列表类型       |
| re.finditer() | 搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象 |
| re.sub()      | 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串    |

``` python
re.search(pattern,string,flags=0)
# flat: 正则表达式使用时的控制标记
re.I 忽略正则表达式的大小写，[A-Z]能够匹配小写字符
re.M 正则表达式中^操作符能够给定字符串的每行当做匹配开始
re.S 正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符
```

#### 







