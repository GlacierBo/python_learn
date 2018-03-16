## python编写爬虫

python  2.7

### 最基本的抓站

```
import urllib2
content = urllib2.urlopen('http://XXXX').read()
```

### 模拟登陆

```python
import urllib
import urllib2

values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values) 
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
```

```python
# agent就是请求的身份，如果没有写入请求身份，那么服务器不一定会响应，所以可以在headers中设置agent,例如下面的例子，这个例子只是说明了怎样设置的headers，

import urllib  
import urllib2  

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
request = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(request)  
page = response.read() 
```

```python
# 对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer

headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
                        'Referer':'http://www.zhihu.com/articles' }  
```

python 3.6

###BeautifulSoup4

```python
# 格式化页面
soup.prettify()
```

```python
# 获取url
links = [a.attrs.get('href') for a in soup.select('a')]
```



### 论一只爬虫的自我修养

#### python如何访问互联网



#### 修改header

- 通过Request的headers参数修改
- 通过Request.add_header()方法修改

#### 代理

- 参数是一个字典{'类型'：'代理ip：端口'}

proxy_support = urllib.request.ProxyHandler({})

- 定制、创建一个opener

opener = urllib.request.build_opener(proxy_support)

- 安装opener

urllib.request.install_opener(opener)

- 调用opener

opener.open(url)





























