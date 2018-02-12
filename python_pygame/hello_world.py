#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 17:16
# @Author  : glacier
# @Site    : 
# @File    : hello_world.py
# @Software: PyCharm Edu


import pygame,sys


pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('兴趣是最好的老师')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()






