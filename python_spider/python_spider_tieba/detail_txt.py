# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     detail_txt
   Description :
   Author :       Glacier
   date：          
-------------------------------------------------
   Change Activity:
                   :
-------------------------------------------------
"""

import random

__author__ = 'Glacier'
file = ""

def init_file_name():
     return random.randint(0, 100000)

def save_file(fileName,txt):
    with open(fileName,"a+",encoding='utf-8') as t:
        t.write(txt)
        t.close()


with open('tieba.txt',encoding='utf-8') as f :
     line = f.readline();
     f.close()
     txt = line.split()

     fileName = str(init_file_name()) + ".txt"
     for i in txt:
         save_file(fileName,str(i)+"\n")

     print("电子书生成完毕！")

