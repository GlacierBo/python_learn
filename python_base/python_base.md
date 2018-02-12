## python base

- 将连续相同的字符或者数字取唯一

``` python
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
```

参考：

``` python
from itertools import groupby
def unique_in_order(iterable):
    return [key for key, value in groupby(iterable)]
```

``` python
def unique_in_order(iterable):
    r = []
    for x in iterable:
      x in r[-1:] or r.append(x)
    return r
```

- 出现多次的字符用`')'`出现一次的字符用`'('`代替

``` python
"din" => "((("
"recede" => "()()()"
"Success" => ")())())"
"(( @" => "))(("
```

参考：

``` python
def duplicate_encode(word):
    return   "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
```

- 计算最短字符

``` shell
"bitcoin take over the world maybe who knows perhaps"
"turns out random test cases are easier than writing out basic ones"
"lets talk about javascript the best language"
```

参考：

``` python
def find_short(s):
    temp = s.split(" ")
    l = len(temp[0])
    for i in temp:
        if l > len(i):
            l = len(i)
    return l 
```

``` python
def find_short(s):
    return min(len(x) for x in s.plit())
```

- 二进制计算

``` python
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
```

参考：

``` python
def binary_array_to_number(arr):
  sum = 0
  index = len(arr)-1
  i = 0
  while(index >= 0):
     sum += mul(arr[i],index)
     i += 1
     index -=1
  return sum
def mul(index,arg2):
    for i in range(arg2):
        index = index * 2
    return index
```

``` python
def binary_array_to_number(arr):
   # 将arr转成string字符串，然后进制装换
    return int("".join(map(str,arr)),2)
```

- 获取`list`中的数字

``` shell
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```

参考：

```python
def filter_list(l):
     ll = []
     for i in l:
         if type(i) == type(1):
             ll.append(i)
     return ll
```

``` python
def filter_list(l):
  return [i for i in l if not isinstance(i, str)]
```

``` python
def filter_list(l):
  return [x for x in l if type(x) is not str]
```

- 获取`list`中最小值

``` python
Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
```

参考：

``` python
def findSmallestInt(arr):
    print(min(arr))
```

- 取中间值

``` shell
Test.assert_equals(get_middle("test"),"es")
Test.assert_equals(get_middle("testing"),"t")
Test.assert_equals(get_middle("middle"),"dd")
Test.assert_equals(get_middle("A"),"A")
Test.assert_equals(get_middle("of"),"of")
```

参考：

``` python
def get_middle(s):
     # 偶数
    if len(s)%2 == 0:
        return s[int(len(s)/2-1)]+s[int(len(s)/2)]
    else:
        # 奇数
        return s[int(len(s)/2)]
```

``` python
def get_middle(s):
    print(s[(len(s)-1)//2:len(s)//2+1])
```

- 统计重复字符个数(不区分大小写)

``` shell
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
```

参考：

``` python
def duplicate_count(text):
    text = text.lower()
    print(text)
    tt = []
    for i in text:
       if text.count(i) != 1:
           i in tt[:] or tt.append(i)
    return len(tt)
```

``` python
def duplicate_count(text):
    return len( [c for c in set(text.lower()) if text.lower().count(c)>1] )
```

- 时间格式化

``` python
Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
```

``` python
import time
def make_readable(seconds):
    return time.strftime("%H:%M:%S",time.localtime(seconds))
```









