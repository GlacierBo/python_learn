## Python 对象

> 封装、继承、多态  —— JAVA

> 对象 —— 属性 + 方法  类——是为了量产

类名 ：大写字母

函数 ：小写字母开头

``` python
self 类似于 this
```

####面向对象小例子：

``` python
class Ball:
    def setName(self,name):
        self.name = name

    def kick(self):
        print("我叫%s,谁敢踢我..."% self.name)
```

``` python
from Ball import *

a = Ball()
a.setName('球A')
a.kick()
```

`__init__(self,param1,param2...)` python 构造函数

####重写`__init__`方法

``` python
class Ball:
  
    def __init__(self,name):
        self.name = name

    def kick(self):
        print("我叫%s,谁敢踢我..."% self.name)
```

``` python
from Ball import *

a = Ball('球a')
a.kick()
```

公有，私有，不过python这里的私有实现是伪私有，通过修改了属性的名字，来实现私有`_类名__属性名`

__name 私有

name 公有

####继承&&多态小例子

``` python
class Parent:
    def hello(self):
        print("正在调用父类的hello...")
```

``` python
from Parent import *

class Child(Parent):
    # 重写hello
    def hello(self):
        print("正在调用子类的方法")

p = Parent()
p.hello()

c = Child()
c.hello()
```

####PS

- 不要试图在一个类里面定义出所有能想到的特性和方法，应该利用继承和组合机制来进行扩展。
- 用不同的词性命名，如属性名用名词，方法名用动词。

####绑定

Python 严格要求方法需要有实例才能被调用，这种限制其实就是Python所谓的绑定





























