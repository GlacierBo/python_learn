#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 17:40
# @Author  : glacier
# @Site    : 
# @File    : zhihu_new.py
# @Software: PyCharm Edu


from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException
import pymysql
client = ZhihuClient()

try:
    client.login('13776390465', '14715912300.mm')
    # 必须在 client 已经处于登录状态时才能使用
    client.save_token('token.pkl')
except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login('13776390465', '14715912300.mm', captcha)

client.load_token('token.pkl')
me = client.me()

import traceback
client = ZhihuClient()
# 登录
client.load_token('token.pkl') # 加载token文件
id = 24400664 # https://www.zhihu.com/question/24400664(长得好看是一种怎么样的体验)

question = client.question(id)
print(u"问题:",question.title)
print(u"回答数量:",question.answer_count)

index = 1 # 图片序号
for answer in question.answers:
    index = index + 1
    print("正在保存第"+str(index)+"个回答")
    content = answer.content # 回答内容
    count = answer.voteup_count

    # 打开数据库连接
    db = pymysql.connect(
        "116.62.66.227",
        "root",
        "123456",
        "pythondb",
        charset='utf8'
    )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "insert into zhihu_question(beautiful,vote) value(%s,%s)"
    try:
        # 执行SQL语句
        cursor.execute(sql,(content,count))
        # 提交到数据库执行
        db.commit()
    except:
        print("出错啦！")
        traceback.print_exc()

        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()




