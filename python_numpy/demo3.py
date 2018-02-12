#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 14:09
# @Author  : glacier
# @Site    : 
# @File    : demo3.py
# @Software: PyCharm Edu

import numpy as np
import pandas as pd
import holoviews as hv
hv.extension('bokeh')

macro_df = pd.read_csv('http://assets.holoviews.org/macro.csv', '\t')
key_dimensions   = [('year', 'Year'), ('country', 'Country')]
value_dimensions = [('unem', 'Unemployment'), ('capmob', 'Capital Mobility'),
                    ('gdp', 'GDP Growth'), ('trade', 'Trade')]
macro = hv.Table(macro_df, key_dimensions, value_dimensions)



gdp_unem_scatter = macro.to.scatter('Year', ['GDP Growth', 'Unemployment'])
gdp_unem_scatter.overlay('Country')