#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import pymssql

conn = pymssql.connect(host='172.22.42.172',
                       user='sa',
                       password='wcidfyajdog19780417',
                       database='zsqxdb',
                       charset='utf8')

#查看连接是否成功
cursor = conn.cursor()
sql = 'select * from YCZ_Day_Data'
cursor.execute(sql)
#用一个rs变量获取数据
rs = cursor.fetchall()
dt = pd.DataFrame(rs)
print(dt)
