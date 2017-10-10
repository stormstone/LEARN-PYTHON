#! -*- coding:utf-8 -*-
__author__ = 'storm'

import requests as rq
import re
import time
import datetime
from multiprocessing.dummy import Pool
import pymongo  # 使用数据库负责存取
import urllib.parse  # 用来对URL进行解码

pymongo.MongoClient().drop_database('saikr_com_vs')
tasks = pymongo.MongoClient().saikr_com_vs.tasks  # 将队列存于数据库中
items = pymongo.MongoClient().saikr_com_vs.items  # 存放结果

tasks.create_index([('url', 'hashed')])  # 建立索引，保证查询速度
items.create_index([('url', 'hashed')])

count = items.count()  # 已爬取页面总数
if tasks.count() == 0:  # 如果队列为空，就把该页面作为初始页面，这个页面要尽可能多超链接
    tasks.insert({'url': u'https://www.saikr.com/vs?page=1'})

url_split_re = re.compile('&|\+')


def main():
    global count
    while True:
        url = tasks.find_one_and_delete({})['url']  # 取出一个url，并且在队列中删除掉
        # url = tasks.find_one({})['url']  # 取出一个url，并且在队列中删除掉

        sess = rq.get(url)
        web = sess.content.decode('utf-8', 'ignore')

        urls = re.findall(u'href="(/vs\?page.*?)"', web)  # 查找所有站内链接

        print("2-urls的个数:")
        print(urls.__len__())

        for u in urls:
            try:
                u = urllib.parse.unquote(str(u)).decode('utf-8')
            except:
                pass
            u = 'https://www.saikr.com' + u
            # u = clean_url(u)
            if not items.find_one({'url': u}):  # 把还没有队列过的链接加入队列
                tasks.update({'url': u}, {'$set': {'url': u}}, upsert=True)
                print("加入队列成功")
                print(u)
        text = re.findall('<li class="item clearfix">([\s\S]*?)<li class="item clearfix">', web)
        # 爬取我们所需要的信息，需要正则表达式知识来根据网页源代码而写

        if text:
            for text_item in text:
                # 对爬取的结果做一些简单的处理
                # text = ' '.join([re.sub(u'[ \n\r\t\u3000]+', ' ', re.sub(u'<.*?>|\xa0', ' ', unescape(t))).strip() for t in
                #                  text])
                # title = re.findall(u'(.*?)', web)[0]

                item_url_zz = u'href="(https://www.saikr.com/[^"]+)"'
                item_url = re.findall(item_url_zz, text_item).__getitem__(0)
                item_title = ""
                print("item_url:")
                print(item_url)

                if not items.find_one({'url': item_url}):  # 把还没有队列过的链接加入队列
                    items.update({'url': url}, {'$set': {'item_url': item_url, 'item_title': item_title}}, upsert=True)

                count += 1
                # print u'%s, 爬取《%s》，URL: %s, 已经爬取%s' % (datetime.datetime.now(), title, url, count)


pool = Pool(1, main)  # 多线程爬取，4是线程数
time.sleep(60)
while tasks.count() > 0:
    print("tasks.count()>0")
    time.sleep(60)

pool.terminate()
