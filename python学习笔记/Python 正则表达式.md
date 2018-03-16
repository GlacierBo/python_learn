Python 正则表达式

``` python
import re
re.search(r'love','I love you!')
```



[] 字符类

``` python
re.search(r'[aeiou]','I love you!')
```

{}限定出现的次数

``` python
re.search(r'ab{3,10}c','abbbbbbbbc')
```

^确定匹配开始的位置（即第一个字符为指定位置）

$确定匹配结束位置（即最后一个字符为指定位置）