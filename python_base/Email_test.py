#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 13:46
# @Author  : glacier
# @Site    : 
# @File    : Email_test.py
# @Software: PyCharm Edu



import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import re,requests



# 收件人列表
mail_namelist = ["heyglacier@139.com"]
# 发送方信息
mail_user = "2284711614@qq.com"
#口令
mail_pass = "vwptpiiutdbyeadc"

#发送邮件
#title：标题
#conen：内容
def send_qq_email(title,conen):
    try:
        msg = MIMEText(str(conen))
        #设置标题
        msg["Subject"] = title
        # 发件邮箱
        msg["From"] = mail_user
        #收件邮箱
        msg["To"] = ";".join(mail_namelist)
        # 设置服务器、端口
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        #登录邮箱
        s.login(mail_user, mail_pass)
        # 发送邮件
        s.sendmail(mail_user, mail_namelist, msg.as_string())
        s.quit()
        print("邮件发送成功!")
        return True
    except smtplib.SMTPException:
        print("邮件发送失败！")
        return False


def bs_text(text):
    soup = BeautifulSoup(text,"lxml")
    contents = soup.find_all('li',{'class':'week-detail-now'})
    return contents

def re_text(text):
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('',text)
    s = s.replace("judgeDayNightStr('','');","").strip().replace("[","").replace("]","")\
        .replace("查看今日天气详情","").replace("查看明日天气详情","").replace("\n","")
    return s

headers = {
    # 'Host': 'i.meizitu.net',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding':'gzip, deflate',
    'Upgrade-Insecure-Requests':'1'
}  # 请求头，蛇无头不行，带上吧，后面会讲到用Cookie实现单账号免密登录

s = requests.session()  # 保留会话

def get_weather():

    url = "http://tianqi.2345.com/kunshan/60037.htm"
    req_text = s.get(url).text

    bsText = bs_text(req_text)
    reText = re_text(str(bsText))
    reText = reText.split(",")
    result = ""
    for i in reText :
        result = i.strip()+"\n"
    return result

def get_text():

    result = "昆山天气："+ get_weather()
    # result += "段子："+ get_duanzi()
    return result;

def dz_bs_text(text):
    soup = BeautifulSoup(text,"lxml")
    content = soup.find_all('p',{'class':''})
    digg = soup.find_all('span',{'class':'digg'})

    content = dz_re_text(content)
    digg = dz_re_text(digg)

    content = content.split(',')
    digg = digg.split(',')

    max_happy_content = ""
    max_digg = 0

    for i in range(0,len(digg)):
        if int(digg[i]) >= max_digg:
            max_digg = int(digg[i])
            max_happy_content = content[i]

    return max_happy_content.strip()

def dz_re_text(html):

    strs = str(html).split(',')
    re_h = re.compile('</?\w+[^>]*>')
    s = re_h.sub('',str(strs).replace("[","").replace("]","").replace("'",""))
    return s

def get_duanzi():
    url = 'http://neihanshequ.com/'
    req_text = s.get(url).text;
    bsText = dz_bs_text(req_text)
    return bsText


send_qq_email("galcier推送",get_text())
