#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 16:18
# @Author  : glacier
# @Site    : 
# @File    : urls.py
# @Software: PyCharm Edu

from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello)
]
