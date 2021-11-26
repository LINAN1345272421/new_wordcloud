
import pandas as pd
import jieba

import string
import time
import traceback

import pymysql
import requests
import re

from bs4 import BeautifulSoup
from flask import json
import nltk
from nltk.corpus import brown

#数据库的连接与查询


def get_conn_mysql():
    """
    :return: 连接，游标192.168.1.102
    """
    # 创建连接
    conn = pymysql.connect(host="127.0.0.1",
                    user="root",
                    password="123456",
                    db="new_class",
                    charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor
def close_conn_mysql(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
def query_mysql(sql,*args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询结果以((),(),)形式
    """
    conn,cursor = get_conn_mysql();
    cursor.execute(sql)
    res=cursor.fetchall()
    close_conn_mysql(conn,cursor)
    return res

#插入数据库
def insert_into_mysql(content,channelName,title):
    conn,cursor=get_conn_mysql()
    sql="insert into newdata (content,channelName,title) values(%s,%s,%s)"
    cursor.execute(sql,[content,channelName,title])
    conn.commit()
    close_conn_mysql(conn,cursor)
#pandas读取分批插入数据库
def pandas_read():
    file_path = "data/xlsx/财经.xlsx"
    df = pd.read_excel(file_path)
    print(df.shape[0])
    print(df.iloc[0, :]["content"])
    for i in range(df.shape[0]):
        try:
            insert_into_mysql(df.iloc[i, :]["content"], df.iloc[i, :]["channelName"], df.iloc[i, :]["title"])
        except:
            print("NO")
#各类文章数统计
def class_text_num():
    sql="SELECT count(channelName) as num,channelName FROM new_class.newdata group by channelName;"
    res=query_mysql(sql)
    return res
#最深层
def deep_2(type):
    sql="select title from new_class.newdata where channelName='"+type+"'"
    res=query_mysql(sql)
    return res
#按题目查询文章内容
def find_content_by_title(title):
    sql="select content from new_class.newdata where title='"+title+"'"
    res=query_mysql(sql)
    return res
#查询所有文章
def find_all_new():
    sql="select content from new_class.newdata "
    res = query_mysql(sql)
    return res
#查询各类的文章
def find_type(type):
    sql="select content from new_class.newdata where channelName='"+type+"'"
    res = query_mysql(sql)
    return res

if __name__ == '__main__':
    pass