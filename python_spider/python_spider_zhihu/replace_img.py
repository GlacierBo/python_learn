#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 11:01
# @Author  : glacier
# @Site    : 
# @File    : replace_img.py
# @Software: PyCharm Edu

import re

if __name__ == '__main__':
    str1 = '在英国很多地方，都能看到这样一个抱着炮弹的熊的形象。<br><figure><img src="https://pic4.zhimg.com/50/cefdb034c96ac5acbe3b919d59e94189_hd.jpg" data-rawwidth="3456" data-rawheight="4607" class="origin_image zh-lightbox-thumb" width="3456" data-original="https://pic4.zhimg.com/cefdb034c96ac5acbe3b919d59e94189_r.jpg"></figure><br><figure><img src="https://pic1.zhimg.com/50/a4271653c6ff83e2b39710a1235194ef_hd.jpg" data-rawwidth="499" data-rawheight="601" class="origin_image zh-lightbox-thumb" width="499" data-original="https://pic1.zhimg.com/a4271653c6ff83e2b39710a1235194ef_r.jpg"></figure>或许你很早就在《读者》或者别的什么读物上读过这个故事，并对它的真实性表示怀疑。的确，很久以前，我也是这么以为的。<br>......<br>1942年4月8日，伊朗的哈马丹附近，一批驻扎于此的波兰士兵，遇到了一个牵着个小熊的伊朗小男孩......'


    str2 = re.sub('<figure>.*?</figure>', "<img>", str1)

    print(str2)

