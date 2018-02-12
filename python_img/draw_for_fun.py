#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 17:17
# @Author  : glacier
# @Site    : 
# @File    : draw_for_fun.py
# @Software: PyCharm Edu


import turtle

#画图，边数为sides
def drawShape(sides, length):
    angle = 360.0 / sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)

#移动turtle
def moveTurtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

#正方形
def drawSquare(length):
    chooseColor()
    drawShape(4,length)
    turtle.end_fill()

#三角形
def drawTriangle(length):
    chooseColor()
    drawShape(3,length)
    turtle.end_fill()

#圆形
def drawCircle(length):
    chooseColor()
    drawShape(360,length)
    turtle.end_fill()

def chooseColor():
    index = random.randrange(1,5)
    if index ==1:
        color = "red"
    elif index ==2:
        color = "green"
    elif index ==3:
        color = "black"
    elif index ==4:
        color = "yellow"
    elif index ==5:
        color = "blue"

    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()

#引入random模块
import random

#随机生成图形
def drawRandom():
    x=random.randrange(-200,200)  #生成-200到200之间的随机数
    y=random.randrange(-200,200)
    length = random.randrange(75)  #生成0到75之间的随机数（不包括75）
    shape = random.randrange(1,4)  #生成1到4之间的随机数（不包括4）

    moveTurtle(x,y)

    if shape == 1:
        drawSquare(length)
    elif shape == 2:
        drawTriangle(length)
    elif shape == 3:
        length = length % 4
        drawCircle(length)

for shape in range(20):  #主程序部分，调用100次随机生成图形函数
    drawRandom()
turtle.done()

