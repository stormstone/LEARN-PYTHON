#! -*- coding:utf-8 -*-
__author__ = 'storm'
'''
抓取https://www.saikr.com/vs?page=1，最近更新
得到所有分页（tasks）和每一页具体每一项的链接（items）。
成功，待爬取每一项具体的内容
'''

import requests as rq
import re
import time
import datetime
from multiprocessing.dummy import Pool
import pymongo  # 使用数据库负责存取
from urllib import unquote  # 用来对URL进行解码
from urlparse import urlparse, urlunparse  # 对长的URL进行拆分
import HTMLParser

pymongo.MongoClient().drop_database('saikr_com_vs2')
tasks = pymongo.MongoClient().saikr_com_vs2.tasks  # 将队列存于数据库中
items = pymongo.MongoClient().saikr_com_vs2.items  # 存放结果
specific_items = pymongo.MongoClient().saikr_com_vs2.specific_items  # 存放每一条具体结果

# 将第一页设置为未爬取，爬取第一页最新的数据
# firstpageurl = 'https://www.saikr.com/vs/0/0/1?page=1'
# tasks.update({'item_url': firstpageurl}, {'$set': {'item_url': firstpageurl, "isCrawled": "no"}}, upsert=True)

tasks.create_index([('url', 'hashed')])  # 建立索引，保证查询速度
items.create_index([('item_url', 'hashed')])
specific_items.create_index([('sp_item_url', 'hashed')])

count = items.count()  # 已爬取页面总数
if tasks.count() == 0:  # 如果队列为空，就把第一页作为初始页面
    tasks.insert({'url': u'https://www.saikr.com//vs/0/0/1?page=1', 'isCrawled': 'no'})

url_split_re = re.compile('&|\+')


def main():
    global count

    while True:
        url = tasks.find_one({"isCrawled": "no"})['url']  # 取出一个还未爬取过的url
        print "取出的URL:",
        print url
        tasks.update({'url': url}, {'$set': {"isCrawled": "yes"}}, upsert=True)  # 设置为已爬取

        sess = rq.get(url)
        web = sess.content.decode('utf-8', 'ignore')

        # 查找所有分页链接
        urls = re.findall(u'href="(/vs/0/0/1\?page.*?)"', web)

        for u in urls:
            try:
                u = unquote(str(u)).decode('utf-8')
            except:
                pass
            u = 'https://www.saikr.com' + u

            if not tasks.find_one({'url': u}):  # 把还没有队列过的链接加入队列
                tasks.update({'url': u}, {'$set': {'url': u, "isCrawled": "no"}}, upsert=True)

        # 得到具体每一项的链接列表
        text = re.findall('<div class="fl event4-1-detail-box">([\s\S]*?)<div class="fr event-detail-btn-box">', web)
        print '本页有' + str(len(text)) + '条比赛链接\n'
        if text:
            for text_item in text:
                # 对爬取的结果做一些简单的处理
                item_url_zz = u'href="(https://www.saikr.com/[^"]+)"'
                item_url = re.findall(item_url_zz, text_item).__getitem__(0)
                item_title_zz = u'target="_blank" title="([^"]+)" class="link"'
                item_title = re.findall(item_title_zz, text_item).__getitem__(0)

                if not items.find_one({'item_url': item_url}):  # 把还没有队列过的链接加入队列
                    items.update({'item_url': item_url},
                                 {'$set': {'item_url': item_url, 'item_title': item_title, "isCrawled": "no"}},
                                 upsert=True)

                count += 1


pool = Pool(1, main)  # 多线程爬取，4是线程数
time.sleep(60)
while tasks.count() > 0:
    print "tasks.count()>0"
    time.sleep(60)

pool.terminate()
