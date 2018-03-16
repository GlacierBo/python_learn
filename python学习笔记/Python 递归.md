## python 递归

> 普通的程序员使用迭代，天才程序员使用递归

``` python
# 死循环
def recursion()
	return recursion()
```

python 3 默认递归深度 100层

``` python
# 修改递归深度
import sys
sys.setrecursionlimit(1000000)
```

简单的一个递归：（栈操作是非常消耗时间的，递归递归，归去来兮，出来混总是要还的）

``` python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input('请输入一个正整数：'))
result = factorial(number)
print('%d 的阶乘是: %d'%(number,result))
```



#### Fibonacci 数列

> 蒙娜丽莎的微笑，黄金分割比例  0.618/1 分支思想

```
1, 当 n=1
1, 当 n=2
F(n-1)+F(n-2), 当 n>2
```

``` python
# 迭代算法
def rabbit(n):
    n1 = 1
    n2 = 1
    n3 = 1

    if n < 1:
        print('输入有误!')
        return -1;

    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return n3

result = rabbit(20)
print(result)
```

``` python
# 递归算法
def rabbit(n):
    if n <= 2:
        return 1;
    else:
        return rabbit(n-1) + rabbit(n-2)

result = rabbit(20)
print(result)
```

