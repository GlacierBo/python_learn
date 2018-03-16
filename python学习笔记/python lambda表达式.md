## lambda 表达式

使用lambda关键字创建匿名函数

``` python
>>> def ds(x):
  		return 2 * x + 1

>>> ds(5)
11

>>> lambda x : 2 * x + 1

>>> g = lambda x : 2 * x + 1
>>> g(5)
```

``` python
>>> g = lambda x,y : x + y
>>> g(1,3)
```

用lambda就不需要考虑命名的问题了。

### Filter 过滤函数

``` python
>>> list(filter(None,[1,0,False,True]))
[1,True]

def odd(x):
  return x % 2
temp = range(10)
show = filter(odd,temp)
list(show)

# 简化成lambda表达式
>>> print(list(filter(lambda x : x % 2 ,range(10))))
[1, 3, 5, 7, 9]

```

### Map 映射函数

``` python
>>> print(list(map(lambda x : x * 2 , range(10))))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```































