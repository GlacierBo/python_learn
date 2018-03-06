#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 12:32
# @Author  : glacier
# @Site    : 
# @File    : zhihu_story.py
# @Software: PyCharm Edu


from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException
import pymysql
import traceback
from bs4 import BeautifulSoup
import re

client = ZhihuClient()

try:
    client.login('13776390465', '14715912300.mm')
    # 必须在 client 已经处于登录状态时才能使用
    client.save_token('token.pkl')

except NeedCaptchaException:
    traceback.print_exc()
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login('13776390465', '14715912300.mm', captcha)

# 登录
client.load_token('token.pkl') # 加载token文件


def searchQuestion(id):

    question = client.question(id)
    print(u"问题:",question.title)
    print(u"回答数量:",question.answer_count)

    index = 1 # 图片序号
    for answer in question.answers:

        content = answer.content # 回答内容
        count = answer.voteup_count
        print("已经循环到第"+str(index)+"条")
        # 过滤小于1000赞的内容
        if count < 3000 :
            continue
        index = index + 1
        print("正在保存第"+str(index)+"个回答"+"，点赞数量："+ str(count))


        # 这边对内容进行了 一些处理
        soup = BeautifulSoup(content,"html.parser")
        imglist = soup.find_all('img')  #发现html中带img标签的数据，输出格式为<img xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx，存入集合
        imgs = []
        for i in range(len(imglist)):
            imgs.append(imglist[i].attrs['src'])
        imgs = ','.join(imgs)

        contentinfo = soup.get_text(strip=True)[:400]
        content = content.replace("<p>","").replace("</p>","\n").replace("<br><br>","\n").replace("<br>","\n")
        # 获取图片时做处理 将所有图片替换成 <img>
        content = re.sub('<figure>.*?</figure>', "<img>", content)

        # 打开数据库连接
        db = pymysql.connect(
            "116.62.66.227",
            "root",
            "123456",
            "homedb",
            charset='utf8'
        )
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        sql1 = "INSERT INTO wx_artile_a(title,introduction,userid,sweet) value(%s,%s,1,%s)"
        sql2 = "INSERT INTO wx_artile_b(content,imgs) value(%s,%s)"
        try:
            # 执行SQL语句
            cursor.execute(sql1,(question.title,contentinfo,count))
            cursor.execute(sql2,(content,imgs))
            # 提交到数据库执行
            db.commit()
        except:
            traceback.print_exc()
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()


if __name__ == '__main__':

    id = 62920125
    searchQuestion(id)









