#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 9:53
# @Author  : glacier
# @Site    : 
# @File    : baiduApi-anjuke-address.py
# @Software: PyCharm Edu


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv,pymysql,traceback
import requests
import json


#
# data = pd.read_csv('anjuke-tocsv.csv')
# print(data['户型'],data['大小'],data['售价'])


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}

def UserBaiduApi(address):
    ak = '6AFCcQAwMl7wm6ATEcm1z4I1ml4oEXxg'
    city = "昆山市"
    baiduAPI_url = 'http://api.map.baidu.com/geocoder/v2/?address='+str(address)+'&city='+str(city)+'&output=json&pois=1&ak='+ str(ak)
    print(baiduAPI_url)
    try:
        r = requests.get(baiduAPI_url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        traceback.print_exc()
        return ""


if __name__ == '__main__':

    # 打开数据库连接
    db = pymysql.connect(
        "localhost",
        "root",
        "123456",
        "python",
        charset='utf8'
    )

    cursor = db.cursor()
    sql = "SELECT houseName,housePrice FROM anju_ks_community"
    try:
        # 执行SQL语句
        table  = cursor.execute(sql)
        results = cursor.fetchall()
        # result = '水月周庄(别墅)'

        dic = []
        for result in results:
            apiResult = UserBaiduApi(result[0])
            resultJson = json.loads(apiResult)
            if resultJson.get('status') == 0:
                lng = resultJson.get("result").get('location').get('lng')
                lat = resultJson.get("result").get('location').get('lat')
                count = float(result[1])/1000
                dic.append({"lng":lng,"lat":lat,"count":count})
            else:
                print(resultJson.get('msg'))
                pass
        print(dic)
        # 提交到数据库执行
        db.commit()
    except:
        traceback.print_exc()
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()



