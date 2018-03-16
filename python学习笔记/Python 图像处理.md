## Python 图像处理

可以使用python自带的PIL

下面这个例子对图片进行50%的压缩处理

``` python
from PIL import Image

im = Image.open('imgage.png')
w,h = im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//2, h//2))
im.save('test.png','png')
```

