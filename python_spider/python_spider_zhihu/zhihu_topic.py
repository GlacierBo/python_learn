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
import traceback

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
id = 19553298 # 19550994 游戏 19591985 动漫 19551077 历史 19551075 中国历史 19555513 生活方式
# 19553176 教育 # 19551388 摄影 19552266 文化 19609455　金融  19554825 职业发展 19552079 面试
# 19560170 经济学 19554569 房价
# 19551404 投资 19555939 理财 19550714 摇滚乐 19550453 音乐
# 19550874 法律 19553298 自然科学 19552192 健身 19551557 设计
topic = client.topic(id)
best_answers = topic.best_answers

index = 1 # 图片序号
for best_answer in best_answers:

    print("正在保存第"+str(index)+"个话题")
    index = index + 1

    # 记录下标
    # if index < 410:
    #     continue

    question_title = best_answer.question.title
    question_id = best_answer.id
    best_answer_author = best_answer.author.name
    best_answer_comment_count = best_answer.comment_count

    best_answer_content = best_answer.content
    best_voteup_count = best_answer.voteup_count

    topic_name = topic.name
    topic_id = topic.id

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

    sql = "insert into zhihu_topic(question_title,question_id,best_answer_author,best_answer_comment_count," \
          "best_answer_content,best_voteup_count,topic_name,topic_id) value(%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        # 执行SQL语句
        cursor.execute(sql,(question_title,question_id,best_answer_author,best_answer_comment_count,
                            best_answer_content,best_voteup_count,topic_name,topic_id))
        # 提交到数据库执行
        db.commit()
    except:
        print("出错啦！")
        traceback.print_exc()

        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()




