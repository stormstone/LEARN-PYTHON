#! -*- coding:utf-8 -*-
__author__ = 'storm'
'''
不清空数据库：把第一页设置为未爬取，爬取最新的内容
每一项具体信息保存：匹配有问题，级别、参赛对象、报名时间、比赛时间等待处理
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

unescape = HTMLParser.HTMLParser().unescape  # 用来实现对HTML字符的转移

# pymongo.MongoClient().drop_database('saikr_com_vs')
tasks = pymongo.MongoClient().saikr_com_vs.tasks  # 将队列存于数据库中
items = pymongo.MongoClient().saikr_com_vs.items  # 存放结果
specific_items = pymongo.MongoClient().saikr_com_vs.specific_items  # 存放每一条具体结果

# 将第一页设置为未爬取，爬取第一页最新的数据
firstpageurl = 'https://www.saikr.com/vs?page=1'
tasks.update({'item_url': firstpageurl}, {'$set': {'item_url': firstpageurl, "isCrawled": "no"}}, upsert=True)

tasks.create_index([('url', 'hashed')])  # 建立索引，保证查询速度
items.create_index([('item_url', 'hashed')])
specific_items.create_index([('sp_item_url', 'hashed')])

count = items.count()  # 已爬取页面总数
if tasks.count() == 0:  # 如果队列为空，就把该页面作为初始页面，这个页面要尽可能多超链接
    tasks.insert({'url': u'https://www.saikr.com/vs?page=1', 'isCrawled': 'no'})

url_split_re = re.compile('&|\+')


def clean_url(url):
    url = urlparse(url)
    return url_split_re.split(urlunparse((url.scheme, url.netloc, url.path, '', '', '')))[0]


def main():
    global count

    while True:
        url = tasks.find_one({"isCrawled": "no"})['url']  # 取出一个还未爬取过的url
        print "取出的URL:"
        print url
        tasks.update({'url': url}, {'$set': {"isCrawled": "yes"}}, upsert=True)

        sess = rq.get(url)
        web = sess.content.decode('utf-8', 'ignore')

        urls = re.findall(u'href="(/vs\?page.*?)"', web)  # 查找所有站内链接

        for u in urls:
            try:
                u = unquote(str(u)).decode('utf-8')
            except:
                pass
            u = 'https://www.saikr.com' + u
            # u = clean_url(u)

            if not tasks.find_one({'url': u}):  # 把还没有队列过的链接加入队列
                tasks.update({'url': u}, {'$set': {'url': u, "isCrawled": "no"}}, upsert=True)
        text = re.findall('<div class="fl event4-1-detail-box">([\s\S]*?)<div class="fr event-detail-btn-box">', web)
        # 爬取我们所需要的信息，需要正则表达式知识来根据网页源代码而写

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
                # print u'%s, 爬取《%s》，URL: %s, 已经爬取%s' % (datetime.datetime.now(), item_title, item_url, count)




                # 开始爬取具体每一项！！！

                specific_item_html = rq.get(item_url)
                specific_item_web = specific_item_html.content.decode('utf-8', 'ignore')
                # 正文信息
                specific_item_text = re.findall(
                    '<div class="body-main main-wrap v-4-2">([\s\S]*?)<div class="footer-wrap v-4-2">',
                    specific_item_web).__getitem__(0)
                # 右侧信息
                specific_item_text_summary = re.findall(
                    '<div class="sk-event-summary-box">([\s\S]*?)<div class="new-event4-1-box event-weixin-box">',
                    specific_item_web).__getitem__(0)

                pattern = re.compile('<span class="title-desc">(.*?)</span>', re.S)
                pattern1 = re.compile('<h3 class="title">.*?浏览量.*?<spanclass ="title-desc" > (.* ?) < / span > ' +
                                      '.*?<h3 class="title">.*?类型.*?<span class ="title-desc" > (.* ?) < / span > ' +
                                      '.*?<h3 class="title">.*?报名费.*?<span class ="title-desc" > (\d+)元 < / span > ' +
                                      '.*?<h3 class="title">.*?级别.*?<span class ="title-desc" > \n * (.* ?) < / span > ' +
                                      '.*?<h3 class="title">.*?参赛对象.*?<span class ="title-desc" > \n * (.* ?)\n * < / span > ' +
                                      '.*?<li class="new-event4-1-info-item clearfix">.*?class="info - content">(.*?)</div>'
                                      '.*?info-content" > (. *?) < / div >'
                                      '.* ?info - content">(.*?)</div>.*?info-content" > (. *?) < / div >'
                                      '.* ? < / li > ' + '.*?<span class="flitem - prize">(.*?)</span>'
                                                         '.*?<span class="flitem - prize">(.*?)</span>'
                                                         '.*?<span class="flitem - prize">(.*?)</span>'
                                                         '.*?<span class="flitem - prize">(.*?)</span>'
                                                         '.*?<span class="flitem - prize">(.*?)</span>'
                                                         '.*?<span class="flitem - prize">(.*?)</span>',
                                      re.S)
                pattern2 = re.compile('<span class="fl item-prize">(.*?)</span>', re.S)
                content = re.findall(pattern1, specific_item_web.__getitem__(0))
                print(content)
                for item in content:
                    browse = int(item[0].strip())
                    category = item[1]
                    price = item[2]
                    leval = item[3].strip()
                    target = item[4].strip()
                    sponser = item[5] + ' , ' + item[6]
                    register = item[7].strip().split('&nbsp;至&nbsp;')
                    over = item[8].strip().split('&nbsp;至&nbsp;')
                    begin = register[0] + '-' + register[1]
                    finish = over[0] + '-' + over[1]
                    prize = item[9] + item[10] + item[11] + item[12] + item[13]
                    contest_category = item[14]



                    # 如果数据库没有相应的URL，保存每一项具体的到数据库
                    '''
                    if not specific_items.find_one({'sp_item_url': item_url}):
                        specific_items.update({'sp_item_url': item_url},
                                              {'$set': {'sp_item_url': item_url,
                                                        'sp_item_title': item_title,
                                                        "specific_item_imgurl": specific_item_imgurl,
                                                        "specific_item_publisher": specific_item_publisher,
                                                        "specific_item_type": specific_item_type,
                                                        "specific_item_money": specific_item_money,
                                                        "specific_item_rank": specific_item_rank,
                                                        "specific_item_Participants": specific_item_Participants,
                                                        "specific_item_time_signup": specific_item_time_signup,
                                                        "specific_item_time_play": specific_item_time_play,
                                                        "specific_item_category": specific_item_category,
                                                        "specific_item_content": specific_item_content}},
                                              upsert=True)
                    items.update({'item_url': item_url},
                                 {'$set': {'item_url': item_url, 'item_title': item_title, "isCrawled": "yes"}},
                                 upsert=True)
                    '''

pool = Pool(1, main)  # 多线程爬取，4是线程数
time.sleep(60)
while tasks.count() > 0:
    print "tasks.count()>0"
    time.sleep(60)

pool.terminate()
