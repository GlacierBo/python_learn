## python数据库操作

### 环境

- python 3.6
- pymysql

简单插入实例：

``` python
   # 打开数据库连接
    db = pymysql.connect(
            "localhost",
            "root",
            "123456",
            "python",
            charset='utf8'
    )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "SELECT id,title,title_url,vote_count FROM p_zhihu_topic_flim"
    try:
       # 执行SQL语句
       table  = cursor.execute(sql)
       print(table)
       # 提交到数据库执行
       db.commit()
    except:
       print("出错啦！")
       # 发生错误时回滚
       db.rollback()

    # 关闭数据库连接
    db.close()
```

插入语句实例：

``` python
sql = 'insert into zhilian_info_javascript (positionname, company, salary, city,info_type,info,persent) value(%s, %s, %s, %s,%s,%s,%s)'
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
try:
	# 执行SQL语句
    cursor.execute(sql, (positionname, company, salary, city,info_type,info,persent))
    # 提交到数据库执行
    db.commit()
except:
    print("出错了")
    traceback.print_exc()
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
```

