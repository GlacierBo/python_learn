## Python 列表&元组

> 设计到逻辑比较复杂的部分，我们可以用流程图

python 内置函数

``` python
dir(__bulitins__)
```



#### python的数据类型

获取变量的数据类型：

``` python
type(a)
# true 两个参数类型一致  false 两个参数类型不一致
isinstance(a,str)
```

#### 常用操作符

`/`

python 3 用了真正的除法代替地板除法（python 3 `//`地板除）

python 2 用的是地板除法

`**`

幂运算

``` python
>>> 3 ** 2
9
```

```python
>>> -3 * 2 + 5 / -2 - 4
-12.5
```

```python
>>> -3 ** 2
-9
>>> -(3 ** 2)
-9
>>> 3 ** -2
0.1111111111
```

#### 分支控制语句

```python
if

if
elif
else

while
```

#### 三元操作符

``` python
x if 条件 else y
```

####for循环

``` python
for 目标 in 表达式 :
  	循环体
```

``` python
for i in favourite :
  print(i,end=' ')
```

``` python
# range([start,]stop[,step=1])
for i in range(1,10,2):
  print(i)
```

###列表

- append() 添加一个元素


- extend() 添加一个列表
- insert() 插入一个列表

``` python
>>> member = ['a','b']
>>> member.append('c')
>>> member.extend(['d','e'])
a,b,c,d,e
>>> members.insert(1,'f')
a,f,b,c,d,e
```

- remove() 删除一个元素
- del 删除
- pop() 也可以加个索引

```python
>>> member.remove('a')
>>> del member[1]
>>> del member #删除整个列表
>>> member.pop() #会返回删除的值
```

- reverse() 逆序
- sort() 从小到大

``` python
sort(func,key,reverse=False) # 默认归并排序    ----数据结构和算法
```



#### 关于分片

分片： 分片的拷贝是重新分配的空间，直接赋值则指向之前的空间。

```python
list1 = [4,3,2,1]
list2 = list1 
list3 = list1[:]
>>> list1.sort()
>>> list1
1,2,3,4
>>> list2
1,2,3,4
>>> list3
4,3,2,1
```

### 元组

> 戴上了枷锁的列表

``` python
>>> tuple1 = (1,2,3,4,5,6)
>>> tuple1
(1,2,3,4,5,6)
>>> tuple1[1]
2
>>> tuple2 = tuple1[:]
# 创建一个空元组可以
>>> temp = 1,2,3
>>> type(temp)
<class 'tuple'>
```















