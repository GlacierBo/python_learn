## Python 函数

``` python
def func():
  print('11')
```

给参数默认值（可以防止调用函数的时候，发生莫名其妙的错误，参数多的时候，非常好用）

``` python
#demo1 
def SaySome(name,words):
  print(name + '->' + words)

#demo2
def SaySome(words='让编程改变世界',name='glacier'):
  print(name + '->' + words)
  
#demo3 给参数标识
SaySome(words="让编程改变世界",name="glacier")
```

不定长度的函数

``` python
#demo1 收集参数
def test(*params):
  print('参数的长度是：',len(params))
  print('参数的长度是：',params[1])

#demo2 
def test(*params,time):
  print('参数的长度是：',len(params))
  print('参数的长度是：',params[1])
  print(time)

test(1,'glaicer',2,3,5,time=12)
```



### 内嵌函数和闭包

global关键字  全局变量

``` python
# 内嵌函数
def fun1():
  print("fun1()正在被调用...")
  def fun2():
    print('fun2()正在被调用...')
  fun2()
```

闭包

``` python
def FunX(x):
  def FunY(y):
    return x * y
  return FunY

>>> i = FunX(8)
>>> type(i)
<class 'function'>
# 调用
>>> FunX(8)(5)
40
```

``` python
def fun1():
  x = 5
  def fun2():
    x *= x
    return x
  return fun2()

# 会报错，因为这里的x不是一个全局变量
```

``` python
# 我们可以把这里的x 赋值成一个列表
def fun1():
  x = [5]
  def fun2():
    x[0] *= x[0]
    return x[0]
  return fun2()
```

nonlocal 关键字

``` python
def fun1():
  x = 5
  def fun2():
    nonlocal x
    x *= x
    return x
  return fun2()
```













