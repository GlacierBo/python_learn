# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 8:18
# @Author  : glacier
# @Email   : 2284711614@qq.com
# @File    : get_plan_to_md.py
# @Software: PyCharm

import os,time
import pymysql
import datetime


if __name__ == '__main__':
    # 格式化
    # today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    today = '2018-03-23'

    db = pymysql.connect(
        "123.206.84.216",
        "user001",
        "123456",
        "glacier",
        charset='utf8'
    )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "SELECT user_id,plan_content,plan_type FROM plan_list " \
          "WHERE create_time like '%"+ today +"%'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        table = cursor.fetchall()

        # 提交到数据库执行
        db.commit()

        for tt in table:
            with open('C:\\Users\\Administrator\\Desktop\\今日计划.md','a+',encoding='UTF-8') as f:
                if tt[2] == 0:
                    f.write('- [ ] ' + tt[1] + '\n')
                elif tt[2] == 1:
                    f.write('- [ ] ' + tt[1] + ' - 进行中 \n')
                elif tt[2] == 2:
                    f.write('- [x] ' + tt[1] + '\n')

            f.close()
    except:
        print("出错啦！")
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()


    # with open('C:\\Users\\Administrator\\Desktop\\今日计划.md') as f:
    #      pass








