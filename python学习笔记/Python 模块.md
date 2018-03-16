## Python 模块

``` shell
容器 -> 数据的封装
函数 -> 语句的封装
类   -> 方法和属性的封装
模块 -> 模块就是程序 
```

### 导入模块

- import 模块名
- from 模块名 import 函数名（尽量不要用这种方法，如果引入模块的方法名跟这个类的方法名一样，则会由于冲突出现错误）
- import 模块名 as 新名字（建议使用）



`__name__` 作为主程序调用的时候为真，执行，反之则不执行，可以在你的测试代码上加入以下代码，用以测试

``` python
if __name__ == '__main__'
```

###搜索路径

``` python
# 查看约定的路径
>>> import sys
>>> sys.path
['D:\\object_demo', 'D:\\object_demo', 'C:\\Program Files\\Python36\\python36.zip', 'C:\\Program Files\\Python36\\DLLs', 'C:\\Program Files\\Python36\\lib', 'C:\\Program Files\\Python36', 'C:\\Users\\glacier\\AppData\\Roaming\\Python\\Python36\\site-packages', 'C:\\Program Files\\Python36\\lib\\site-packages', 'C:\\Program Files\\Python36\\lib\\site-packages\\beautifulsoup4-4.4.1-py3.6.egg']
```

推荐存放在`site-packages`这个目录下

### 包（package）

- 创建一个文件夹，用于存放相关的模块，文件夹的名字即报的名字；
- 在文件夹中创建一个`__init__.py`的模块文件，内容可以为空；
- 将相关的模块放入文件夹中



> Python 自己带着电池（Batteries included）

设计哲学：优雅、明确和简单

> 用一种方法，最好是只有一种方法来做一件事！

