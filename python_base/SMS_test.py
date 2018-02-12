#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 12:46
# @Author  : glacier
# @Site    : 
# @File    : SMS_test.py
# @Software: PyCharm Edu




#接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
#账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
#注意事项：
#（1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
#（2）请使用 用户名 及 APIkey来调用接口，APIkey在会员中心可以获取；
#（3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

#!/usr/local/bin/python
#-*- coding:utf-8 -*-

import urllib.parse
import  http.client

host  = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

#用户名是登录ihuyi.com账号名（例如：cf_demo123）
account  = "C97073293"
#密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "eae74e4b777f0e1a4ebad7d26691440e"

def send_sms(text, mobile):
    params = urllib.parse.urlencode({'account': account, 'password' : password, 'content': text, 'mobile':mobile,'format':'json' })
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

if __name__ == '__main__':

    mobile = "13086691295"
    text = "您的验证码是：555555。请不要把验证码泄露给其他人。"

    print(send_sms(text, mobile))