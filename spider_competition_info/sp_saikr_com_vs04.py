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
import urllib.parse  # 用来对URL进行解码

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


def main():
    global count

    while True:
        url = tasks.find_one({"isCrawled": "no"})['url']  # 取出一个还未爬取过的url
        print("取出的URL:")
        print(url)
        tasks.update({'url': url}, {'$set': {"isCrawled": "yes"}}, upsert=True)

        sess = rq.get(url)
        web = sess.content.decode('utf-8', 'ignore')

        urls = re.findall(u'href="(/vs\?page.*?)"', web)  # 查找所有站内链接

        for u in urls:
            try:
                u = urllib.parse.unquote(str(u)).decode('utf-8')
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
                # 得到图片路径
                specific_item_img_zz = u'<img[^>]+class=[^>]+>'
                specific_item_img = re.findall(specific_item_img_zz, specific_item_text).__getitem__(0)
                specific_item_imgurl_zz = u'src="(https://.*?)"'
                specific_item_imgurl = re.findall(specific_item_imgurl_zz, specific_item_img).__getitem__(0)
                # 得到竞赛信息!!!
                specific_item_content = re.findall(
                    '<div class="event4-1-detail-text-box text-body clearfix">([\s\S]*?)<div class="event4-1-detail-box v-4-9">',
                    specific_item_web).__getitem__(0)
                # 得到发布者
                specific_item_publisher_zz = u'<dd class="item-desc" title="(.*?)">'
                specific_item_publisher = re.findall(specific_item_publisher_zz,
                                                     specific_item_text_summary).__getitem__(0)
                # 得到类型
                specific_item_type_zz = u'类型<span class="title-desc">(.*?)</span>'
                specific_item_type = re.findall(specific_item_type_zz, specific_item_text_summary).__getitem__(0)
                # 得到报名费
                specific_item_money_zz = u'报名费<span class="title-desc">(.*?)</span>'
                specific_item_money = re.findall(specific_item_money_zz, specific_item_text_summary).__getitem__(0)
                # 得到级别
                specific_item_rank_zz = u'级别<span class="title-desc">[^>]+</span>'
                specific_item_rank = re.findall(specific_item_rank_zz, specific_item_text_summary)
                # 得到参赛对象、报名时间、比赛时间
                specific_item_participants_zz = u'<li class="new-event4-1-info-item clearfix">[^>]+<div class="info-content">[^>]+</div>'
                specific_item_ParticipantsTime = re.findall(specific_item_participants_zz, specific_item_text_summary)
                specific_item_participants_zz02 = u'<div class="info-content">[^>]+</div>'
                specific_item_Participants = re.findall(specific_item_participants_zz02,
                                                        specific_item_ParticipantsTime.__getitem__(0))
                specific_item_time_signup = re.findall(specific_item_participants_zz02,
                                                       specific_item_ParticipantsTime.__getitem__(1))
                specific_item_time_play = re.findall(specific_item_participants_zz02,
                                                     specific_item_ParticipantsTime.__getitem__(2))
                # 得到竞赛类别
                specific_item_category_zz = u'<div class="info-content clearfix">[^>]+<span class="fl item-prize">(.*?)</span>'
                try:
                    specific_item_category = re.findall(specific_item_category_zz,
                                                        specific_item_text_summary).__getitem__(1)
                except:
                    specific_item_category = re.findall(specific_item_category_zz,
                                                        specific_item_text_summary).__getitem__(0)

                print(specific_item_imgurl)
                # print(specific_item_content)
                print(specific_item_publisher)
                print(specific_item_type)
                print(specific_item_money)
                print(specific_item_rank)
                print(specific_item_ParticipantsTime)
                print(specific_item_Participants)
                print(specific_item_time_signup)
                print(specific_item_time_play)
                print(specific_item_category)
                print("")
                # 如果数据库没有相应的URL，保存每一项具体的到数据库
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


pool = Pool(1, main)  # 多线程爬取，4是线程数
time.sleep(60)
while tasks.count() > 0:
    print("tasks.count()>0")
    time.sleep(60)

pool.terminate()
