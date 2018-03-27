# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 13:56
# @Author  : glacier
# @Email   : 2284711614@qq.com
# @File    : test_down.py
# @Software: PyCharm

import python_spider_wangjin.download_media as download

if __name__ == '__main__':
    url = 'http://apps.xikang.com/u/cms/xikang/vedio1/xkll-0001.flv'
    path = 'D:/Python_Download/test.flv'
    print('正在下载...'+ path)
    download.do_load_media(url,path)



