#! -*- coding:utf-8 -*-
__author__ = 'storm'
'''
抓取https://www.saikr.com/vse/？，每一项具体内容
'''

import requests as rq
import re
import time
import datetime
from multiprocessing.dummy import Pool
import pymongo  # 使用数据库负责存取
import urllib.parse  # 用来对URL进行解码

tasks = pymongo.MongoClient().saikr_com_vs2.tasks  # 分页链接
items = pymongo.MongoClient().saikr_com_vs2.items  # 每一项链接
specific_items = pymongo.MongoClient().saikr_com_vs2.specific_items  # 存放每一条具体结果
specific_items_error = pymongo.MongoClient().saikr_com_vs2.specific_items_error  # 存放爬取失败url

tasks.create_index([('url', 'hashed')])  # 建立索引，保证查询速度
items.create_index([('item_url', 'hashed')])
specific_items.create_index([('sp_item_url', 'hashed')])
specific_items_error.create_index([('error_url', 'hashed')])


def main():
    while True:
        if not items.find_one({"isCrawled": "no"}):
            print('已经爬取完毕')
            break

        url = items.find_one({"isCrawled": "no"})['item_url']  # 取出一个还未爬取过的url
        title = items.find_one({"isCrawled": "no"})['item_title']  # 得到标题
        print("取出的URL:")
        print(url)
        try:
            sess = rq.get(url)
            html = sess.content.decode('utf-8', 'ignore')  # 本页面的html
            # 正文信息
            specific_item_text = re.findall(
                '<div class="body-main main-wrap v-4-2">([\s\S]*?)<div class="footer-wrap v-4-2">',
                html).__getitem__(0)
            # 右侧信息
            specific_item_text_summary = re.findall(
                '<div class="sk-event-summary-box">([\s\S]*?)<div class="new-event4-1-box event-weixin-box">',
                html).__getitem__(0)

            # 1.得到图片路径
            specific_item_img_zz = u'<img[^>]+class=[^>]+>'
            specific_item_img = re.findall(specific_item_img_zz, specific_item_text).__getitem__(0)
            specific_item_imgurl_zz = u'src="(https://.*?)"'
            specific_item_imgurl = re.findall(specific_item_imgurl_zz, specific_item_img).__getitem__(0)
            # 2.得到竞赛信息!!!
            specific_item_content = re.findall(
                '<div class="event4-1-detail-text-box text-body clearfix">([\s\S]*?)<div class="event4-1-detail-box v-4-9">',
                html).__getitem__(0)
            # 3.得到发布者
            specific_item_publisher_zz = u'<dd class="item-desc" title="(.*?)">'
            specific_item_publisher = re.findall(specific_item_publisher_zz,
                                                 specific_item_text_summary).__getitem__(0)
            # 4.得到竞赛类别
            specific_item_category_zz = u'<div class="info-content clearfix">[^>]+<span class="fl item-prize">(.*?)</span>'
            try:
                specific_item_category = re.findall(specific_item_category_zz,
                                                    specific_item_text_summary).__getitem__(1)
            except:
                specific_item_category = re.findall(specific_item_category_zz,
                                                    specific_item_text_summary).__getitem__(0)

            # print(specific_item_imgurl)
            # # print(specific_item_content)
            # print(specific_item_publisher)
            # print(specific_item_category)

            # 5.得到浏览量
            pattern_browse = re.compile('<h3 class="title">.*?浏览量.*?<span class="title-desc">(.*?)</span>', re.S)
            browse = re.findall(pattern_browse, html)
            specific_item_browse = browse[0].strip()
            # 6.得到类型
            pattern_type = re.compile('<h3 class="title">.*?类型.*?<span class="title-desc">(.*?)</span>', re.S)
            type = re.findall(pattern_type, html)
            specific_item_type = type[0].strip()
            # 7.得到报名费
            pattern_price = re.compile('<h3 class="title">.*?报名费.*?<span class="title-desc">(.*?)</span>', re.S)
            price = re.findall(pattern_price, html)
            if len(price) > 1:
                specific_item_price = price[1].strip()
            else:
                specific_item_price = price[0].strip()

            # 8.得到级别
            pattern_leval = re.compile('<h3 class="title">.*?级别.*?<span class="title-desc">\n*(.*?)</span>', re.S)
            leval = re.findall(pattern_leval, html)
            specific_item_leval = leval[0].strip()
            # 9.得到参赛对象
            pattern_target = re.compile('<h3 class="title">.*?参赛对象.*?<span class="title-desc">\n*(.*?)\n*</span>', re.S)
            target = re.findall(pattern_target, html)
            if len(target) > 1:
                specific_item_target = target[1].strip()
            else:
                specific_item_target = target[0].strip()

            # 如果数据库没有相应的URL，保存每一项具体的到数据库
            if not specific_items.find_one({'sp_item_url': url}):
                specific_items.update({'sp_item_url': url},
                                      {'$set': {'sp_item_url': url,
                                                'sp_item_title': title,
                                                "specific_item_imgurl": specific_item_imgurl,
                                                "specific_item_publisher": specific_item_publisher,
                                                "specific_item_type": specific_item_type,
                                                "specific_item_browse": specific_item_browse,
                                                "specific_item_price": specific_item_price,
                                                "specific_item_leval": specific_item_leval,
                                                "specific_item_category": specific_item_category,
                                                "specific_item_target": specific_item_target,
                                                "specific_item_content": specific_item_content}},
                                      upsert=True)
                # 设置本条为已爬取
                items.update({'item_url': url},
                             {'$set': {'item_url': url, 'item_title': title, "isCrawled": "yes"}},
                             upsert=True)
                print('items更新:' + url + '\n')
        except:
            # 发生错误
            # 设置本条为已爬取
            items.update({'item_url': url},
                         {'$set': {'item_url': url, 'item_title': title, "isCrawled": "yes"}},
                         upsert=True)
            # 记录错误的url
            specific_items_error.update({'error_url': url}, {'$set': {'error_url': url, "error_title": title}},
                                       upsert=True)


pool = Pool(1, main)  # 多线程爬取，4是线程数
time.sleep(60)
while tasks.count() > 0:
    print("tasks.count()>0")
    time.sleep(60)

pool.terminate()
